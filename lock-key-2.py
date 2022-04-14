#auth: Sudhanshu Nerkar

import random
import tkinter as tk
from random import randint, randrange
from tkinter import *

test_list = [0, 1, 2, 3, 4, 5,6,7,8,9]

key = random.randint(100,999)

if(key%10 == 0):
    key = key + int(random.choice([ele for ele in test_list if ele!=0]))

digit1 = int(key/100)
digit2 = int(key/10) - (digit1*10)
digit3 = key - (digit1*100 + digit2*10)

print(digit1)
print(digit2)
print(digit3)



h1 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + digit3
h2 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + digit2
h3 = digit3*100 + digit1*10 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])
h4 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3]) 
h5 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + digit1

print("Hint 1: " + str(h1) + " - One correct and well placed")
print("Hint 2: " + str(h2)+ " - One correct but wrongly placed")
print("Hint 3: " + str(h3) + " - Two correct but wrong placed")
print("Hint 4: " + str(h4) + " - Nothing is correct")
print("Hint 5: " + str(h5) + " - one is correct but wrongly placed")

print(key)
