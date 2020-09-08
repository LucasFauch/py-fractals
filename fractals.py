from PIL.Image import *
from random import*
xmin = -2
ymin = -2
xmax = 2
ymax = 2

def mandelbrot():
    img = new('RGB',(1000,1000), (255, 255, 255))
    (l,h) = img.size
    for x in range(l):
        for y in range(h):
            a=x*(xmax-xmin)/(1000-1)+ymin
            b=y*(ymax-ymin)/(1000-1)+xmin
            n=0
            c=complex(a,b)
            z=0
            while n<=300 and abs(z)<=16:
                z=z*z+c
                n+=1
            '''r = n % 4 * 64
            g = n % 8 * 32
            b = n % 16 * 16'''
            #Image.putpixel(img,(x, y), (b * 65536 + g * 256 + r))
            Image.putpixel(img,(x,y), (int(n*255/300),int(n*255/300),int(n*255/300)))
    img.show()
    #img.save("mandel.png", "PNG")

#mandelbrot()

def julia(a,b):
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
    #img.save("julia.png", "PNG")

julia(-0.8,0.156)
