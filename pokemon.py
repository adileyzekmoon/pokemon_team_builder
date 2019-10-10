import csv


class Pokemon:
    
    def __init__(self, name, type1, type2=None, final=False):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.final = bool(final)
        
    def __repr__(self):
        if self.type2:
            if self.final:
                return"{} - a {} {} type Pokemon. It is in it's final form".format(self.name,self.type1,self.type2)
            else:
                return"{} - a {} {} type Pokemon".format(self.name,self.type1,self.type2)
        else:
            if self.final:
                return"{} - a {} type Pokemon. It is in it's final form".format(self.name,self.type1)
            else:
                return"{} - a {} type Pokemon".format(self.name,self.type1)
    
class Team:
    
    def __init__(self, *pokemon):
        self.team = []
        self.types = []
        for poke in pokemon:
            self.team.append(pokedict[poke])
            self.types.append(pokedict[poke].type1)
            if pokedict[poke].type2:
                self.types.append(pokedict[poke].type2)
            
    def __repr__(self):
        return "Your team consists of {}.".format(self.team)
    
    def status(self):
        print(self)
        print(self.types)
        self.possibles()
        
    
    def possibles(self, only_finals = True):
        result = []
        for poke in pokedex:
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
                if only_finals and poke.final == False:
                    passbool = False
                    break
            if passbool:
                result.append(poke)
#                print("Added {}".format(poke.name))
        print("There are {} possible Pokemon team members.".format(len(result)))
#                print("Added {}".format(poke.name))
        return result
    
    def add_poke(self, pokemon):
        self.team.append(pokedict[pokemon])
        if not(pokedict[pokemon].type1 in self.types):
            self.types.append(pokedict[pokemon].type1)
        if pokedict[pokemon].type2:
            if not(pokedict[pokemon].type2 in self.types):
                self.types.append(pokedict[pokemon].type2)
                
    def remove_poke(self, pokemon):
        self.team.remove(pokedict[pokemon])
        passbool1 = True
        passbool2 = True
        for poke in self.team:
            if pokedict[pokemon].type1 == poke.type1 or pokedict[pokemon].type1 == poke.type2:
                passbool1 = False
            if pokedict[pokemon].type2:
                if pokedict[pokemon].type2 == poke.type1 or pokedict[pokemon].type2 == poke.type2:
                    passbool2 = False
        if passbool1:
            self.types.remove(pokedict[pokemon].type1)
        if passbool2:
            self.types.remove(pokedict[pokemon].type2)
        
pokedex = []
namelist = []
with open("pokedex.csv", encoding='utf-8-sig') as pokedex_file:
    poke_reader = csv.DictReader(pokedex_file) #create list of dictionaries
    for row in poke_reader:
        pokedex.append(Pokemon(row["Pokemon"], row["Type 1"], row["Type 2"], row["Final"]))
        namelist.append(row["Pokemon"])


        
pokezip = zip(namelist, pokedex)
pokedict = dict(pokezip)
#print(pokedict)

my_team = Team("Venusaur", "Charizard")
my_team.status()
#print(*my_team.possibles(), sep = "\n") #print list in newlines
my_team.add_poke("Starmie")
my_team.status()
my_team.remove_poke("Venusaur")
my_team.status()
my_team.add_poke("Omastar")
my_team.status()
my_team.remove_poke("Starmie")
my_team.status()
#print(my_team)
#print(my_team.types)
##my_team.possibles()
#print(*my_team.possibles(), sep = "\n") #print list in newlines