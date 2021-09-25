
#nesting Dictionary in a List

travel_log = [
	{
		"country":"France",
		"cities_visited": ["Paris", "Lille", "Dijon"], 
		"total_visits": 12 
	},
	{
		"country": "Germany",
		"cities_visited": ["Berlin", "Hamburg", "Stuttgard"], 
		"total_visits": 20
	}
]

for elem in travel_log:
	for key in elem:
		print(key)
		print(elem[key])
