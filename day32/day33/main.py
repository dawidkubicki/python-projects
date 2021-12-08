import requests
from datetime import datetime

MY_LAT = 52.406376# Your latitude
MY_LONG = 16.925167


# ISS API Connect

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.



# MY LOCATION SUNRISE AND SUNSET API CONNECT

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def iss_close(iss_lat, iss_lon):
	if (iss_lat>=MY_LAT and iss_lat<=MY_LAT+5) or (iss_lat>=MY_LAT-5 and iss_lat<=MY_LAT):
		if (iss_lon>=MY_LONG and iss_lon<=MY_LONG+5) or (iss_lon>=MY_LONG-5 and iss_lon<=MY_LONG):
			return True
		else:
			return False
	else:
		return False

def check_sun_position():
	actual_hour = datetime.now().hour

	parameters = {
	    "lat": MY_LAT,
	    "lng": MY_LONG,
	    "formatted": 0,
	}

	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
	sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
	
	print(f"Actual hour : {actual_hour}")
	print(f"Sunrise: {sunrise}")
	print(f"Sunset: {sunset}")

	if int(actual_hour) >= int(sunset) or int(actual_hour) <= int(sunrise):
		return True
	else:
		return False
	

 
