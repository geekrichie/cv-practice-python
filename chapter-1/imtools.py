import os
from PIL import Image
from pylab import *
def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
def imresize(im, size):
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(size))
def histeq(im, nbr_bins=256):
    # 计算图像的直方图
    imhist,bins = histogram(im.flatten(), nbr_bins, density=True)
    print(nbr_bins,bins.shape)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1] #归一化
    #此时 bins
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf
histeq(np.arange(5))