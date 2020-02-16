import requests,json
import os

url = "https://maps.googleapis.com/maps/api/geocode/json"

DIR = os.path.dirname(__file__) or '.'
KEY = json.loads(open(DIR + "/../secrets.json").read())['google']

headers = {
   "key": KEY
}

def get_coords(place_name):
    data = {
        **headers,
        "address": place_name
    }

    resp = requests.get(url, params = data)
    if resp.status_code != 200:
        return None

    resp = json.loads(resp.content)['results'][0]['geometry']['location']
    return (resp['lat'], resp['lng'])


if __name__ == '__main__':
    place = input("Please enter a location: ")
    print(get_coords(place))
