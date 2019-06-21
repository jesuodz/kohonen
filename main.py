import numpy as np
from som import SOM
from mongoInterface import MongoInterface
from buildDB import *

from pprint import pprint

print("Creating a SOM")
red = SOM(15, 15, 2)

# Recupera la data de la BD

print("Connecting to Mongo")
conn = MongoInterface(dbname='video')

# Filtro y proyección MONGO
filtro = {
    '$and': [
        { 
            "tomato.rating": { '$exists': True  },
            "awards.wins": { '$exists': True }
        }
    ] 
}

projection = {
    "_id": False,
    "title": True,
    "runtime": True,
    "metacritic": True,
    "tomato.rating": True,
    "year": True,
    "awards.wins": True
}

print("Retrieving data")
brute_data = conn.find_docs(collec='movieDetails', f=filtro, p=projection)
conn.close_conn()

# Limpia y reorganiza la data

receive_data(brute_data)

# print("...Entrenando la red...")
# red.train(data, L0=10, lam=1e2, sigma0=10)

# arr1 = []

# for arr in mapa.som:
#     for i in arr:
#         arr1.append([i[0], i[1]])

# loadJSON(arr1, 'som_map')
