import requests
import tkinter
from tkinter import *
u = input("Choose what website you are going to scrap. There will also be a page finder. \n Website:")
io = requests.get(u)
k = io.text
root = tkinter.Tk()
e = Label(root, text="Adhub Industries")
e.grid(row=0, column = 5)
binthecow = Label(root, text="Your website has been reached! This is your website HTML. But don't worry! There will be a text file to contain all this tricky info!")
binthecow.grid(row=0, column=1)
g = Entry(root)
g.grid(row=5, column=1)

g.delete(0, END)
g.insert(0, io.text)
h = Button(root, text="Quit?", command=exit)
h.grid(row=7, column = 6)

jin = Entry(root)
jin.grid(row=17, column=5)

def daylightsavings():
    f = jin.get()
    draluxe = open(f, "w+")
    draluxe.write(k)
    draluxe.close()



milkywaygalaxy = Button(root, text="Save file as?:", command=daylightsavings)
milkywaygalaxy.grid(row=13, column=1)

def findkey():
    j = str(input("We are now going to tell you how many times the keyword was printed. \nKeyword:"))

    if j in open(jin.get()).read():
        print("Found!")
    else:
        print("Not found!")

finder = Button(root, text="Finder:", command=findkey)
finder.grid(row=5, column=3)

root.mainloop()



