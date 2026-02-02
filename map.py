import noise
import numpy as np

def fbm(x, y, octaves=5, lacunarity=2.0, gain=0.5):
    value = 0.0
    amplitude = 1.0
    frequency = 1.0

    for _ in range(octaves):
        value += amplitude * noise.pnoise2(x * frequency,y * frequency, repeatx=1024, repeaty=1024)
        frequency *= lacunarity
        amplitude *= gain

    return value

width, height = 300, 300
scale = 0.01

heightmap = np.zeros((width, height))

for x in range(width):
    for y in range(height):
        heightmap[x][y] = fbm(x * scale, y * scale)

heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())

import matplotlib.pyplot as plt

plt.imshow(heightmap, cmap="terrain")
plt.colorbar()
plt.show()
