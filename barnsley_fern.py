from PIL.Image import *
from random import *

def fern(n):
    img = new("RGB", (600,600),(255,255,255))
    (l,h) = img.size
    x=0
    y=0
    for i in range(n):
        a = random()
        if a<0.01:
            (x,y) = t1(x,y)
        elif a<0.86:
            (x,y) = t2(x,y)
        elif a<0.93:
            (x,y) = t3(x,y)
        else:
            (x,y) = t4(x,y)
        a = int(translate(x,-2.1820, 2.6558, 0, 600))
        b = int(translate(y,0, 9.9983, 600, 0))
        Image.putpixel(img,(a,b),(39,155,39))
    img.show()
    #img.save("fern.png", "PNG")
    

def t1(x,y):
    return (0,0.16*y)

def t2(x,y):
    return (0.85*x+0.04*y,-0.04*x+0.85*y+1.6)

def t3(x,y):
    return (0.2*x-0.26*y,0.23*x+0.22*y+1.6)

def t4(x,y):
    return (-0.15*x+0.28*y,0.26*x+0.24*y+0.44)


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
