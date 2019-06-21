import numpy as np
from som import SOM
from mongoInterface import *
from makeJSON import loadJSON

# print("Creating a SOM")
# mapa = SOM(20, 20, 2)
# print("Training SOM")
# mapa.train(data, L0=10, lam=1e2, sigma0=10)

# arr1 = []

# for arr in mapa.som:
#     for i in arr:
#         arr1.append([i[0], i[1]])

projection = {
    "title": True
}

data = find_docs(projection, dbname='video', coll='movieDetails')
print(data)

# loadJSON(arr1, 'som_map')
