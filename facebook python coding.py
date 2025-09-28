#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)

import glob, os
with open("a.txt", "w") as f:
    f.write("A")
with open("b.txt", "w") as f:
    f.write("B")    
print(len(glob.glob("*.txt")))
os.remove("a.txt")
os.remove("b.txt")
    
    