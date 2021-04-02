# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:55:05 2021

@author: Hassan Ashiq
"""

from tkinter import *


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    L=a if a>b else b
    while L <=a*b:
        if L%a==0 and L%b==0:
            return L
        L +=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H -=1


operations = {'add': add, 'addition':add, 'plus':add, 'sum':add,
              'sub':subtract, 'difference':subtract, 'minus':subtract,'subtract':subtract,
              'LCM':lcm, 'HCF':hcf, 'product':multiply,'multiplication':multiply, 'multiply':multiply,
              'division':divide, 'div':divide, 'mod':mod, 'reminder':mod, 'modulus':mod}


def extract_from_text(text):
    l =list()
    for t in text.split():
        try:
            l.append( float(t) )
        except:
            pass
    return l

def calculate():
    text=textin.get()
    for word in text.split():
        if word.lower() in operations:
            try:
                l = extract_from_text(text)
                r = operations[word.lower()](l[0],l[1])
                listt.delete(0,END)
                listt.insert(END,r)
            except:
                listt.delete(0,END)
                listt.insert(END,"Something went wrong")
            finally:
                break
        elif word.lower() not in operations:
            listt.delete(0,END)
            listt.insert(END,"Something went wrong")

win=Tk()


win.geometry('500x300')
win.title("Smart Calculator ")
win.configure(bg='black')


l1 =Label(win, text="I am a smart calculator", width=20, padx=3)
l1.place(x=150, y=10)

l2 =Label(win, text="My name is smartie", padx=3)
l2.place(x=170, y=40)

l3 =Label(win, text="What can i help you with ? ", padx=3)
l3.place(x=150, y=100)




textin=StringVar()
e1= Entry(win, width=35, textvariable=textin)
e1.place(x=120, y=130)


#button
b1= Button(win, text='Just this', command=calculate )
b1.place(x=200, y=160)

listt = Listbox(win, width=30, height=3)
listt.place(x=130, y=190)









win.mainloop()