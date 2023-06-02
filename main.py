import requests as re
import time
city_name=input("Please enter thr city name:-")
URL="http://api.weatherstack.com/current?access_key={access_key}&query={city}".format(access_key="b56497aaf014461730bc0ccd4a0e463f",city=city_name)
#print(URL)
current_weather=re.get(URL)
print({city_name: "{0}C".format(current_weather.json()["current"]["temperature"])})
time.sleep(5)