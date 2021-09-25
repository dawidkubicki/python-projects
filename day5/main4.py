travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

#travel_log.append({
#    "country": "Poland",
#    "visits": 100,
#    "cities": ["Poznan", "Kalisz"]})


def add_new_country(country: str, visits: int, cities: list):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

    print(f"You've visited Russia {visits} times.")
    print(f"You've been to {[city for city in cities]}.")


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

