#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)

x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
print(x)