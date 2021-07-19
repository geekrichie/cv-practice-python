from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('../img/sample.jpg'))
imshow(im)

x = [100,100,400,400]
y = [200,500,200,500]

#使用红色星状标记绘制点
plot(x,y,'r*')

plot(x[:2],y[:2])
title('Plotting:"sample.jpg"')
axis('off')
show()