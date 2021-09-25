auction =  [
    {
        "name": "User1",
        "bid": 100
    },
    {
        "name": "User2",
        "bid": 400
    }
]

for elem in auction:
    for key in elem:
        number = elem[key][1]

print(number)
