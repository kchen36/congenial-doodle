from pymongo import MongoClient
import json
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("base.html")

@app.route('/search', methods = ['POST', 'GET'])
def search():
    
    name = request.form['search']
    if request.form['method'] == 'evo':
        pokemons = findevo(name)
    if request.form['method'] == 'name':
        pokemons = find(name)
    elif request.form['method'] == 'id':
        pokemons = findid(name)
    if pokemons[0]['next_evolution'] = None:
        evo = "no evolution"
    else:
        evo = pokemons[0]['next_evolution'][0]['name']
    return render_template("base.html",
                           pokemon = pokemons[0]['name'],
                           img = pokemons[0]['img'],
                           weight = pokemons[0]['weight'],
                           height = pokemons[0]['height'],
                           evolution = evo)

file = open("pokedex.json", 'r')
pokedex = json.load(file)
client = MongoClient("homer.stuy.edu")

db = client['pokedex']
db.dropDatabase
db = client['pokedex']
collection = db.pokemon
for i in pokedex:
    collection.insert_many(pokedex["pokemon"])

def find(pokemon):
    return collection.find({"name" : pokemon})

def findid(num):
    return collection.find({"id" : num})

def findevo(name):
    return collection.find({"next_evolution.name" : name})

def findtype(name):
    return collection.find({"type" : name})

def p(x):
    for i in x:
	print i
    
if __name__ == "__main__":
    app.debug = True
    app.run()
