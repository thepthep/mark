class man:
    def __init__(self,name):
        self.name = name
        print("Init")

    def hello(self):
        print(self.name)

    def goodbye(self):
        print(self.name)



m= man("david")
m.hello()
m.goodbye()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png')

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label="sin")
plt.plot(x,y2,linestyle="--",label="cos")
plt.legend()
plt.imshow(img)
plt.show()


def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp=x1*w1+x2*w2
    if tmp <=theta:
        return 0
    elif tmp > theta:
        return 1
        

AND(0,0)
AND(0,1)
AND(1,0)
AND(1,1)