import numpy as np
from som import SOM
from makejson import loadJSON
import math

def PointsInCircum(r,n=999):
    return np.array([[math.cos(2*np.pi/n*x)*r+0.5,math.sin(2*np.pi/n*x)*r+0.5] for x in range(0,n+1)])

data = PointsInCircum(0.5)

# data = np.random.rand(100, 2)

print("Creating a SOM")
mapa = SOM(20, 20, 2)
print("Training SOM")
mapa.train(data, l0=10, lam=1e2, sigma0=10)

arr1 = []

for arr in mapa.som:
    for i in arr:
        arr1.append([i[0], i[1]])

loadJSON(arr1, 'som_map')
loadJSON(data, 'initial_data')

print("Error:",mapa.quant_err())
