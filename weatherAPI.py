import requests
import realEstateAPI


def get_wind_data(apiKey, county):
    URL = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": apiKey,
        "q": county,
    }
    response = requests.get(URL, params=params)
    data = response.json()
    if response.status_code == 200:
        windSpeed = data["current"]["wind_kph"]
        windDirection = data["current"]["wind_degree"]
        return([windSpeed,windDirection])
        print("Wind speed in " , county , windSpeed , "km/h.")
        print("Wind direction in" , county , windDirection , "degrees.")
    else:
        print("Error:" , data['error']['message'])
        exit

def main():
    apiKey1 = "2cda45d56b334172fa0f715c45148a54" 
    apiKey2 = "70f56f1c5ef54c92b6e143052240303"
    address1 = input("Enter the street address: ")
    address2 = input("Enter the City, State: ")
    distance = input("Enter the search distance (miles): ")
    minLand = float(input("Enter the minimum land area (acres): "))

    county,properties = realEstateAPI.find_properties_with_more_land(address1 , address2, distance, minLand , apiKey1)
    print (county)
    if county != None:
        get_wind_data(apiKey2, county)
    else:
        print("County missing")


if __name__ == "__main__":
    main()