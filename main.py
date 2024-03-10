import urllib.parse
import requests
import json
import datetime

key = #YOUR API KEY

def getLongitudeLatitude(key, address):
    url = 'https://api.openrouteservice.org/geocode/search?api_key={}&text={}'.format(key, address)
    data = requests.get(url)
    json_data = json.loads(data.text)
    coordinates = json_data['features'][0]['geometry']['coordinates']
    return coordinates

def getRoute(start, end, key):
        url='https://api.openrouteservice.org/v2/directions/driving-car?api_key={}&start={}&end={}'.format(key, start, end)
        route = requests.get(url)
        json_data = json.loads(route.text)
        return json_data

address1 = input('Start: ')
place1 = getLongitudeLatitude(key, address1)
start = str(place1[0]) + ',' + str(place1[1])
address2 = input('End: ')
place2 = getLongitudeLatitude(key, address2)
end = str(place2[0]) + ',' + str(place2[1])
route = getRoute(start, end, key)
distance = route['features'][0]['properties']['segments'][0]['distance']
print('Distance in km: ' + str(round(distance/1000, 2)))
duration = distance = route['features'][0]['properties']['segments'][0]['duration']
print('Estimated time: ' + str(datetime.timedelta(seconds=duration)))
    