from pokemon import Team, Pokemon, Pokedex
from flask import Flask, render_template, request

app = Flask(__name__)

pokedex = Pokedex()
poketeam = Team(pokedex.dex)

@app.route('/', methods = ['GET'])
def home():
    
    if request.method == 'GET':
        poke = request.args.get('pokemon')
        if poke:
            poketeam.add_poke(poke.lower(), pokedex.dex)
    
    
    return render_template('home.html', poketeam=poketeam, pokedex=pokedex.dex)
    
    
if __name__ == '__main__':
    app.run(debug=True)