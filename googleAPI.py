import requests

def get_lat_long(address):
    api_key = 'AIzaSyDNYHnhnBz78Qv_LoVKq9aNDYsNvKWHJqs'  
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address': address,
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        print('Error:', data['status'])
        return None, None

def main():
    address = input("Enter an address — (EX. '1600 Amphitheatre Parkway, Mountain View, CA') :  ")
    latitude, longitude = get_lat_long(address)
    
    if latitude is not None and longitude is not None:
        print("Latitude: " , latitude, "Longitude: " , longitude)
    else:
        print("Failure: Couldn't find latitude and longitude.")

if __name__ == "__main__":
    main()
