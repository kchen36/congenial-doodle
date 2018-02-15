from pymongo import MongoClient
import json
file = open("pokedex.json", 'r')
pokedex = json.load(file)
client = MongoClient("homer.stuy.edu")

db = client['pokedex']
collection = db.pokemon
for i in pokedex:
    collection.insert_one(pokedex)

