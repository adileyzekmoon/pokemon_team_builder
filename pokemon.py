import csv


class Pokemon:
    
    def __init__(self, name, type1, type2=None):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        
    def __repr__(self):
        if self.type2:
            return"{} - a {} {} type Pokemon".format(self.name,self.type1,self.type2)
        else:
            return"{} - a {} type Pokemon".format(self.name,self.type1)
    
class Team:
    
    def __init__(self, *pokemon):
        self.team = []
        self.types = []
        for poke in pokemon:
            self.team.append(poke)
            self.types.append(poke.type1)
            if poke.type2:
                self.types.append(poke.type2)
            
    def __repr__(self):
        return "Your team consists of {}.".format(self.team)
    
    def possibles(self):
        result = []
        for poke in pokedex:
            for element in self.types:
                if element == poke.type1:
                    break
                if element == poke.type2:
                    break
                if poke in result:
                    break
                result.append(poke)
                print("Added {}".format(poke.name))
        return result
    
    def add_poke(self, pokemon):
        self.team.append(pokemon)
        if not(pokedict[pokemon].type1 in self.types):
            self.types.append(pokedict[pokemon].type1)
        if pokedict[pokemon].type2:
            if not(pokedict[pokemon].type2 in self.types):
                self.types.append(pokedict[pokemon].type2)
    
        
pokedex = []
namelist = []
with open("pokedex.csv", encoding='utf-8-sig') as pokedex_file:
    poke_reader = csv.DictReader(pokedex_file)
    for row in poke_reader:
        pokedex.append(Pokemon(row["Pokemon"], row["Type 1"], row["Type 2"]))
        namelist.append(row["Pokemon"])


        
pokezip = zip(namelist, pokedex)
pokedict = dict(pokezip)
#print(pokedict)

bulbasaur = Pokemon("Bulbasaur", "Grass", "Poison")
print(bulbasaur)
charmander = Pokemon("Charmander", "Fire")
print(charmander)


my_team = Team(bulbasaur, charmander)
print(my_team)
print(my_team.types)
print(my_team.possibles())

my_team.add_poke("Starmie")
print(my_team)
print(my_team.types)
print(my_team.possibles())