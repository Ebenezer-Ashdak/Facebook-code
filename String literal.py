#!/usr/bin/python3
#This code displays the local time in your jurisdiction according to your system 
import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
#Sorting objects from lowest to highest
x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
print(x)
#Reversed printing objects from highest to lowest
x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
x = list(reversed(x))
print(x)

#Sorting objects from lowest to highest
element = [(3,6),(4,7),(5,9),(8,4),(3,1)]
element.sort()
print(element)

#Reversed printing objects from highest to lowest
element = list(reversed(element))
print(element)