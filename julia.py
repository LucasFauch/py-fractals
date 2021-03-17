from PIL.Image import *
from random import*

xmin = -2
ymin = -2
xmax = 2
ymax = 2

def julia(a,b,s):
    img = new('RGB',(1000,1000), (255, 255, 255))
    (l,h) = img.size
    for x in range(l):
        for y in range(h):
            c=x*(xmax-xmin)/(1000-1)+ymin
            d=y*(ymax-ymin)/(1000-1)+xmin
            n=0
            z=complex(c,d)
            cpl=complex(a,b)
            while n<=300 and abs(z)<=16:
                z=z*z+cpl
                n+=1
            Image.putpixel(img,(x,y), (int(n*255/300),int(n*255/300),int(n*255/300)))
    img.show()
    signe="-"
    if b>=0:
        signe="+"
    if s==1:
        img.save("julia({}{}{}i).png".format(a,signe,b), "PNG")
