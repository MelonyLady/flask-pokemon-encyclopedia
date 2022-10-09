from flask import Flask


app = Flask(__name__)


@app.get("/")
def pokemon_list():
    return "Charmander, Pikachu, Eevee, Bulbasaur"


@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is Bulbasaur, a gen 1 pokemon who looks like a dinosaur with a bulb on the back"


@app.get("/charmander")
def charmander_data():
    return "this is Charmander, a gen 1 pokemon that looks like a baby dragon with a fire on his tail"


@app.get("/pikachu")
def pikachu_data():
    return "this is Pikachu, a gen 1 pokemon that looks like a yellow electric mouse"


@app.get("/eevee")
def eevee_data():
    return "This is Eevee, a gen 1 pokemon that looks like a fox"


@app.get("/diglett")
def diglett_data():
    return "This is diglett, a generation 1 pokemon who looks like a tiny mole"


if __name__ == "__main__":
    app.run()
