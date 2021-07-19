from PIL import Image
from pylab import *

im = array(Image.open("../img/sample.jpg").convert('L'))
#新建一个图像
figure()
#不使用颜色信息
gray()
#在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)

print("please click three points")
x = ginput(3)
print("you clicked:",x)
show()