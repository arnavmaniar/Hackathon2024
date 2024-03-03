import requests
import sys
import googleAPI
import urllib.parse

def find_properties_with_more_land(address1, address2, distance, minLand, apiKey):
    URL = f"https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/expandedprofile?address1={urllib.parse.quote(address1)}&address2={urllib.parse.quote(address2)}"
    headers = {"apikey": apiKey}
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print("Error occurred while geocoding the address:", response.status_code)
        return [None, []]

    data = response.json()
    if data['status']['code'] == 0:
        latitude, longitude = googleAPI.get_lat_long(address1+","+address2)
        attomID = data['status']['attomId']

        county = data['property'][0]['area']['munName']

        searchURL = f"https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/detail?attomid={attomID}"
        response = requests.get(searchURL, headers=headers)
        if response.status_code != 200:
            print("Error.")
            return [ None, [] ]

        data = response.json()
        properties_with_more_land = []
        for propertyInfo in data["property"]:
            lot_size_acres = propertyInfo.get("size", {}).get("grossSize")
            if lot_size_acres is not None:
                if lot_size_acres >= minLand:
                    properties_with_more_land.append(propertyInfo)

        return [county, properties_with_more_land]
    else: 
        sys.exit()
def main():
    address1 = input("Enter the street address: ")
    address2 = input("Enter the City, State: ")
    distance = input("Enter the search distance (miles): ")
    minLandAcres = float(input("Enter the minimum land area (acres): "))
    apiKey = "2cda45d56b334172fa0f715c45148a54"  

    properties = find_properties_with_more_land(address1, address2, distance, minLandAcres, apiKey)
    if properties:
        print("Properties with more than", minLandAcres, "acre of land within", distance, "miles of", address1, ":")
        for propertyInfo in properties:
            print(propertyInfo)
    else:
        print("No properties found.")
    

if __name__ == "__main__":
    main()
