#!/usr/bin/python
# url = 'http://master/api/run'
# Youtube video: https://www.youtube.com/watch?v=G8s0KVh2ePY
# http://openweathermap.org/current
# API call:
# api.openweathermap.org/data/2.5/weather?q={city name}
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}
# Parameters:
# q city name and country code divided by comma, use ISO 3166 country codes
# Examples of API calls:
# api.openweathermap.org/data/2.5/weather?q=London
# api.openweathermap.org/data/2.5/weather?q=London,uk
url = 'http://api.openweathermap.org/'
APIKEY = '7443455b950cb303d2fbf7fd6b8d389b'
import requests
from pprint import pprint

def main():
	city = "New York"
	#response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=paris&appid=7443455b950cb303d2fbf7fd6b8d389b&units=metric")
	response = requests.get(url + "data/2.5/weather?q=" + city 
	+ "&appid=" + APIKEY + "&units=metric")
	#response = requests.get(url + "data/2.5/weather?q=" + city + "&appid=" + APIKEY)
	# response patch into data for Python format.
	weather = response.json()
	print ("The weather for", weather['name'])
# { ... ,"main":{"temp":10.67,"pressure":1025,"humidity":87,"temp_min":10,"temp_max":12},...}
	print (weather['main']['temp'])
	print (weather['weather'][0]['description'])

if __name__ == '__main__':
	main()