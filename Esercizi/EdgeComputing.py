import numpy as np
from skimage import data
import matplotlib.pyplot as plt

from scipy import signal

im = data.gravel()
im = im[:128, :128]
plt.show()
plt.figure()
plt.imshow(im)
plt.show()

sobel_x = np.array([[-1, 0, -1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
dx = signal.correlate2d(im, sobel_x, mode='valid')  # terzo arg è come si può comportare nel livello del bordo,
# il bordo non viene gestito
dy = signal.correlate2d(im, sobel_y, mode='valid')

plt.figure()
plt.imshow(dx)
plt.show()
plt.figure()
plt.imshow(dy)
plt.show()

magnitude = np.sqrt(dx ** 2 + dy ** 2)
plt.figure()
plt.imshow(magnitude)
plt.show()
