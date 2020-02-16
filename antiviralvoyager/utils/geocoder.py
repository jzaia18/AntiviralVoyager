import requests,json

url = "https://maps.googleapis.com/maps/api/geocode/json"

headers = {
   "key": "AIzaSyB0hA6im9a3Vj7CNB3YQRZOC_iD9EY2pxY"
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
    print(get_coords("canada"))
