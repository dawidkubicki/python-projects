import requests
from datetime import datetime


LATI = 52.406376
LONG = 16.925167

parameters = {
    
    "lat" : LATI,
    "lng" : LONG,
    "formatted" : 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

data = sunrise.split("T")[1].split(":")[0]
print(data)
print(datetime.now())
