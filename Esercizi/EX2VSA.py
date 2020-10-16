import random
import numpy as np
from skimage import data




im = data.astronaut()
im = np.swapaxes(np.swapaxes(im, 0, 2), 1, 2)
nbin = random.randint(32,128)




H=im.shape[1]
W=im.shape[2]

out=np.zeros((3*nbin,))
for color in range(3):
     for x in range(H):
         for y in range(W):
             b= (im[color][x][y]*nbin) // 256
             out[b+nbin*color]+=1

out=out/sum(out)
print(out)
