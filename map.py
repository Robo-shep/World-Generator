
# Install PIL: pip install pillow (probably already installed)
from PIL import Image
import numpy as np
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=10, seed=1)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

image = Image.fromarray(np.array(pic) * 255, 'L')
image.save('output.png')
