from PIL import Image
import numpy as np
from pylab import *

im = np.array(Image.open("../img/sample.jpg"))

print(im.shape, im.dtype)

im = np.array(Image.open("../img/sample.jpg").convert("L"), "f")

print(im.shape, im.dtype)
print(int(im.min()), int(im.max()))

figure()

im2 = 255 - im
pil_im2 = Image.fromarray(im2)
subplot(1, 3, 1)
axis('off')
imshow(im2)
print(int(im2.min()), int(im2.max()))

im3 = (100.0/255)*im + 100
pil_im3 = Image.fromarray(im3)
subplot(1, 3, 2)
axis('off')
imshow(im3)
print(int(im3.min()), int(im3.max()))

im4 = 255 * (im/255)**2
pil_im4 = Image.fromarray(im4)
subplot(1, 3, 3)
axis('off')
imshow(im4)
print(int(im4.min()), int(im4.max()))

show()

