from pokemon import Team, Pokemon
from flask import Flask, render_template, request

app = Flask(__name__)

poketeam = Team()

@app.route('/', methods = ['GET'])
def home():
    if request.method == 'GET':
        poke = request.args.get('pokemon')
        if poke:
            poketeam.add_poke(poke.lower())
    
    
    return render_template('home.html', poketeam=poketeam)
    
    
if __name__ == '__main__':
    app.run(debug=True)