import requests
import json
result = {}
response = requests.get("https://swapi.dev/api/starships/?search= Millennium Falcon")

js = response.json()

falcon = js["results"][0]
result['name'] = falcon["name"]
result['max_speed'] = falcon["max_atmosphering_speed"]
result['class'] = falcon["starship_class"]

pilots = falcon["pilots"]
mas = []
for i in pilots:
    info = requests.get(i)
    pilot_info = info.json()
    pilot = {}
    pilot['name'] =  pilot_info["name"]
    pilot['height'] =  pilot_info["height"]
    pilot['mass'] =  pilot_info["mass"]

    planet_info = requests.get( pilot_info["homeworld"])
    planet = planet_info.json()
    pilot['planet_name']=planet["name"]
    pilot['planet_url'] =  pilot_info["homeworld"]
    mas.append(pilot)

result['pilots'] = mas
a = json.dumps(result, indent=4)
print(a)

file = open("Millennium Falcon.json", "w")
file.write(a)
file.close()

