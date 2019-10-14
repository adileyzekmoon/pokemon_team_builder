import json
import requests


class Pokemon:
    
    def __init__(self, name, speed, sdfc, satk, dfc, atk, hp, type1, type2=None):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.speed = speed
        self.sdfc = sdfc
        self.satk = satk
        self.dfc = dfc
        self.atk = atk
        self.hp = hp
        self.stat_total = speed + sdfc + satk + dfc + atk + hp
        self.sprite = ""
        with open('pokesprites.json') as file:
            sprites = json.load(file)
            self.sprite = sprites[name]
        print(self.sprite)
        
    def __repr__(self):
        if self.type2:
            return"{} - {} {} type Pokemon".format(self.name,self.type1,self.type2)
        else:
            return"{} - {} type Pokemon".format(self.name,self.type1)
        
    def display_sprite(self):
        return self.sprite
                
    
class Team:
    
    def __init__(self, *pokemon):
        self.team = []
        self.types = []
        pokelist = []
        namelist =[]
        with open ('pokedex.json') as file:
            pokedex = json.load(file)
            for name in pokedex.keys():
                if len(pokedex[name]["types"]) == 2:
                    print("dual type")
                    pokelist.append(Pokemon(name, 
                                                 pokedex[name]["stats"][0]["base_stat"],
                                                 pokedex[name]["stats"][1]["base_stat"],
                                                 pokedex[name]["stats"][2]["base_stat"],
                                                 pokedex[name]["stats"][3]["base_stat"],
                                                 pokedex[name]["stats"][4]["base_stat"],
                                                 pokedex[name]["stats"][5]["base_stat"],
                                                 pokedex[name]["types"][1]["type"]["name"],
                                                 pokedex[name]["types"][0]["type"]["name"]
                                        ))
                else:
                    print("single type")
                    pokelist.append(Pokemon(name, 
                                                 pokedex[name]["stats"][0]["base_stat"],
                                                 pokedex[name]["stats"][1]["base_stat"],
                                                 pokedex[name]["stats"][2]["base_stat"],
                                                 pokedex[name]["stats"][3]["base_stat"],
                                                 pokedex[name]["stats"][4]["base_stat"],
                                                 pokedex[name]["stats"][5]["base_stat"],
                                                 pokedex[name]["types"][0]["type"]["name"]
                                        ))
                namelist.append(name)
        
        self.pokedict = dict(zip(namelist, pokelist))
        print(self.pokedict)
                    
        for poke in pokemon:
            self.team.append(pokedict[poke])
            self.types.append(pokedict[poke].type1)
            if pokedict[poke].type2:
                self.types.append(pokedict[poke].type2)
            
    def __repr__(self):
        return "Your team consists of {}.".format(self.team)
    
    def status(self, stats = None):
        if stats:
            return """Your team: {} consists of {} types. There are {} possible team mates. 
            """.format(self.team, self.types, len(self.possibles(stats)))
        else:
            return """Your team: {} consists of {} types. There are {} possible team mates. 
            """.format(self.team, self.types, len(self.possibles()))
        
    
    def possibles(self, stats = 0): #averega total stat is 436
        result = []
        for poke in self.pokedict.values():
            passbool = True
            for element in self.types:
                if element == poke.type1:
                    passbool = False
                    break
                if element == poke.type2:
                    passbool = False
                    break
                if poke in result:
                    passbool = False
                    break
                if poke.stat_total < stats:
                    passbool = False
                    break
#                if only_finals and poke.final == False:
#                    passbool = False
#                    break
            if passbool:
                result.append(poke)
#                print("Added {}".format(poke.name))
#                print("Added {}".format(poke.name))
        return result
    
    def add_poke(self, pokemon):
        self.team.append(self.pokedict[pokemon])
        if not(self.pokedict[pokemon].type1 in self.types):
            self.types.append(self.pokedict[pokemon].type1)
        if self.pokedict[pokemon].type2:
            if not(self.pokedict[pokemon].type2 in self.types):
                self.types.append(self.pokedict[pokemon].type2)
                
    def remove_poke(self, pokemon):
        remove1 = True
        remove2 = True
        self.team.remove(self.pokedict[pokemon])
        if len(self.team)==0:
            self.types.clear()
            return
        for poke in self.team:
            if (self.pokedict[pokemon].type1==poke.type1) or (self.pokedict[pokemon].type1==poke.type2):
                remove1 = False
            if self.pokedict[pokemon].type2:
                for poke in self.team:
                    if (self.pokedict[pokemon].type2==poke.type1) or (self.pokedict[pokemon].type2==poke.type2):
                        remove2 = False
            if not(self.pokedict[pokemon].type2):
                remove2=False
        if remove1:
            self.types.remove(self.pokedict[pokemon].type1)
        if remove2:
            self.types.remove(self.pokedict[pokemon].type2)
        

        

#class Pokedex():
#    def __init__(self):
#        self.namelist=[]
#        self.pokelist=[]
#        url = "https://pokeapi.co/api/v2/pokedex/2/"
#        JSONContent = requests.get(url).json()
#        for number in range(len(JSONContent["pokemon_entries"])):
#            print(number)
#            JSONPoke = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(JSONContent["pokemon_entries"][number]["pokemon_species"]["name"])).json()
#            if len(JSONPoke["types"]) == 2:
#                self.pokelist.append(Pokemon(JSONPoke["name"],
#                                       JSONPoke["stats"][0]["base_stat"],
#                                       JSONPoke["stats"][1]["base_stat"],
#                                       JSONPoke["stats"][2]["base_stat"],
#                                       JSONPoke["stats"][3]["base_stat"],
#                                       JSONPoke["stats"][4]["base_stat"],
#                                       JSONPoke["stats"][5]["base_stat"], 
#                                       JSONPoke["types"][1]["type"]["name"], 
#                                       JSONPoke["types"][0]["type"]["name"]))
#            else:
#                self.pokelist.append(Pokemon(JSONPoke["name"],
#                                       JSONPoke["stats"][0]["base_stat"],
#                                       JSONPoke["stats"][1]["base_stat"],
#                                       JSONPoke["stats"][2]["base_stat"],
#                                       JSONPoke["stats"][3]["base_stat"],
#                                       JSONPoke["stats"][4]["base_stat"],
#                                       JSONPoke["stats"][5]["base_stat"], 
#                                       JSONPoke["types"][0]["type"]["name"]))
#            self.namelist.append(JSONPoke["name"])
#        self.dex = dict(zip(self.namelist, self.pokelist))
#        with open("pokedex.json", 'w') as outfile:
#        print(self.dex)
#        
#        
#        
##        
#pokedex = []
#namelist = []
#with open("pokedex.csv", encoding='utf-8-sig') as pokedex_file:
#    poke_reader = csv.DictReader(pokedex_file) #create list of dictionaries
#    for row in poke_reader:
#        pokedex.append(Pokemon(row["Pokemon"], row["Type 1"], row["Type 2"], row["Final"]))
#        namelist.append(row["Pokemon"])

#pokeapi testbed WORKS
#url = "https://pokeapi.co/api/v2/pokemon?limit=151"
#JSONContent = requests.get(url).json()
#for number in range(len(JSONContent["results"])):
#    print(number)
#    JSONPoke = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(number+1)).json()
#    if len(JSONPoke["types"]) == 2:
#        pokedex.append(Pokemon(JSONPoke["name"],
#                               JSONPoke["stats"][0]["base_stat"],
#                               JSONPoke["stats"][1]["base_stat"],
#                               JSONPoke["stats"][2]["base_stat"],
#                               JSONPoke["stats"][3]["base_stat"],
#                               JSONPoke["stats"][4]["base_stat"],
#                               JSONPoke["stats"][5]["base_stat"], 
#                               JSONPoke["types"][1]["type"]["name"], 
#                               JSONPoke["types"][0]["type"]["name"]))
#    else:
#        pokedex.append(Pokemon(JSONPoke["name"],
#                               JSONPoke["stats"][0]["base_stat"],
#                               JSONPoke["stats"][1]["base_stat"],
#                               JSONPoke["stats"][2]["base_stat"],
#                               JSONPoke["stats"][3]["base_stat"],
#                               JSONPoke["stats"][4]["base_stat"],
#                               JSONPoke["stats"][5]["base_stat"], 
#                               JSONPoke["types"][0]["type"]["name"]))
#    namelist.append(JSONPoke["name"])
#
#
#        
#pokezip = zip(namelist, pokedex)
#pokedict = dict(pokezip)
#print(pokedict)





#test_team = Team(JSONContent["results"][0]["name"])
#test_team.status()

#my_team = Team("venusaur", "charizard")
#my_team.status()
#print(*my_team.possibles(), sep = "\n") #print list in newlines
#my_team.add_poke("starmie")
#my_team.status()
#my_team.remove_poke("venusaur")
#my_team.status()
#my_team.add_poke("omastar")
#my_team.status()
#my_team.remove_poke("starmie")
#my_team.status()
#print(my_team)
#print(my_team.types)
##my_team.possibles()
#print(*my_team.possibles(), sep = "\n") #print list in newlines