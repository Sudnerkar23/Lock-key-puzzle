#auth: Sudhanshu Nerkar

import random
import tkinter as tk
from random import randint, randrange
from tkinter import *
from PIL import Image,ImageTk

test_list = [0, 1, 2, 3, 4, 5,6,7,8,9]

key = random.randint(100,999)

if(key%10 == 0):
    key = key + int(random.choice([ele for ele in test_list if ele!=0]))

digit1 = int(key/100)
digit2 = int(key/10) - (digit1*10)
digit3 = key - (digit1*100 + digit2*10)

'''print(digit1)
print(digit2)
print(digit3)'''

h1 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + digit3
h2 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + digit2
h3 = digit3*100 + digit1*10 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])
h4 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3]) 
h5 = random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3 and ele!=0])*100 + random.choice([ele for ele in test_list if ele != digit1 and ele!=digit2 and ele!=digit3])*10 + digit1

'''print("Hint 1: " + str(h1) + " - One correct and well placed")
print("Hint 2: " + str(h2)+ " - One correct but wrongly placed")
print("Hint 3: " + str(h3) + " - Two correct but wrong placed")
print("Hint 4: " + str(h4) + " - Nothing is correct")
print("Hint 5: " + str(h5) + " - one is correct but wrongly placed")

#print(key)

val = input("Enter your key: ")
val = int(val)

if val == key:
    print("Congratulations you have unlocked the lock")
else:
    print("Sorry, better luck next time. The correct answer is " + str(key))
'''

root = Tk()
root.title("lock key puzzle")
root.geometry('550x500')

lbl = Label(root, text="Lock Key Puzzle", font=("Arial Bold", 30), justify = 'center',foreground="brown")
lbl.place(x=110,y=10)

load= Image.open("lock-1.png")
resize_image = load.resize((100, 100))
render = ImageTk.PhotoImage(resize_image)
img = Label(root, image=render, anchor=CENTER)
img.place(x=220, y=60)
lb2 = Label(root, text = "To unlock the lock you need a 3 digit key", font=("Arial Bold", 15))
lb2.place(x=85,y=170)
lb3 = Label(root, text = "Hints :-", font=("Arial Bold", 14))
lb3.place(x=50, y=217)
lb4 = Label(root, text = "Hint 1: " + str(h1) + " - One correct and well placed", font=("Arial Bold", 12))
lb4.place(x=50, y=250)
lb5 = Label(root, text = "Hint 2: " + str(h2)+ " - One correct but wrongly placed", font=("Arial Bold", 12))
lb5.place(x=50, y=270)
lb6 = Label(root, text = "Hint 3: " + str(h3) + " - Two correct but wrong placed", font=("Arial Bold", 12))
lb6.place(x=50, y=290)
lb7 = Label(root, text = "Hint 4: " + str(h4) + " - Nothing is correct", font=("Arial Bold", 12))
lb7.place(x=50, y=310)
lb8 = Label(root, text = "Hint 5: " + str(h5) + " - one is correct but wrongly placed", font=("Arial Bold", 12))
lb8.place(x=50, y=330)
lb8 = Label(root, text = "Enter Your Key:", font=("Arial Bold", 12))
lb8.place(x=60, y=360)  

e1 = tk.Entry(root)
e1.place(x=190,y=365)
def clicked ():  
    x1 = e1.get()
    x1=int(x1)
    l1 = tk.Label(root, text="Congratulations! you have unlocked the key",font=(12))
    l2 = tk.Label(root, text="Sorry, your answer is incorrect. Correct answer is "+str(key))
    if x1 == key:
        l1.place(x=50,y=390)
    else:
        l2.place(x=60,y=390)

button1 = tk.Button(text='Submit', command= clicked)
button1.place(x=320,y=363)

last = tk.Label(root, text="Developed by: Sudhanshu Nerkar",font=(12),foreground="#856ff8")
last.place(x=120,y=450)

root.mainloop()
