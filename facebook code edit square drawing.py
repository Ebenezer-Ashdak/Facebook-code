#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)

import turtle,colorsys
turtle.bgcolor("grey");
t=turtle.Turtle();
t.speed(0); 
turtle.colormode(255)

def  square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)
n = 36; h=0
for i in range(72):
    col=colorsys.hsv_to_rgb(h,1,1);
    t.pencolor(int(col[0]*255),int(col[1]*255),int(col[2]*255))
    
    for _ in range(6):
        square(60);#draw squares instead of t.circle(60)
        t.left(60)
    t.left(5);
    h+=1/n; 
    h%=1
turtle.done()    