#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)

i = 1

while i<= 999999999999999:
    print(i)
    i =i +1