import requests, json

#write pokedex to pokedex.JSON

url = "https://pokeapi.co/api/v2/pokedex/2/"
JSONContent = requests.get(url).json()
pokedex = {}
for number in range(len(JSONContent["pokemon_entries"])):
    print(number)
    placeholder = {}
    JSONPoke = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(JSONContent["pokemon_entries"][number]["pokemon_species"]["name"])).json()
    pokedex[JSONPoke["name"]] = JSONPoke["sprites"]["front_default"]

with open ("pokesprites.json",'w') as pokeout:
    json.dump(pokedex, pokeout)