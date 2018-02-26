from pymongo import MongoClient
import json
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/search')
def search():
    return render_template("base.html")
@app.route('/pokemon')
def pokemon():
    return render_template("base.html"
file = open("pokedex.json", 'r')
pokedex = json.load(file)
client = MongoClient("homer.stuy.edu")

db = client['pokedex']
db.dropDatabase()
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
