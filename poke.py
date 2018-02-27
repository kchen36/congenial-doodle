from pymongo import MongoClient
import json
file = open("pokedex.json", 'r')
pokedex = json.load(file)
client = MongoClient("homer.stuy.edu")

db = client['pokedex']
collection = db.pokemon
for i in pokedex:
    collection.insert_many(pokedex["pokemon"])

def find(pokemon):
    return collection.find({"name" : pokemon})

def findid(num):
    return collection.find({"id" : num})

def findevo(name):
    return collection.find({"next_evolutionname" : name})
def p(x):
    for i in x:
	print i

p(find("Charmander"))
