from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("menus and submenus")
root.geometry("300x300")


def func():
    print("I am a naughty function")

def funcc():
    print("I will definitely save your file!")
    a= tmsg.showinfo("Save As", "This gui box will save your file")     #comma se pehle vala title ban jata h
    print(a)        #print(a) will print the text of the button


def rate():
    print("Plzz take a second to rate us!")
    value = tmsg.askquestion("How did you like our app so far", "Was the experience good?")
    print(value)
    if value == "yes":      #Note that ki "y" small letter m aega
        mssg = "Please rate us on app store!"

    else:
        mssg = "Tell us what went wrong, help us to improve to serve you better!"
    
    tmsg.showinfo("Experience", mssg)


def divya():
    ans = tmsg.askretrycancel("Bhai divya nhi manegi", "fir bhi pooch le")
   #Below technique is used to make separate boxes to show response
    if ans:
        msg = "Bhai retry karne se kya hoga?"

    else:
        msg = "Bhot bdia kia bhai use chorr dia"

    tmsg.showinfo("uska response", msg)

    #Below technique will just print it in the compiler
    if ans:
        print("Bhai retry karne se kya hoga?")

    else:
        print("Bhot bdia kia bhai use chorr dia")


def chal():
    bol = tmsg.askokcancel("Aj kuch kare", "Kahi bahar chalen?")
    if bol:
        print("Ye hui na baat!")

    else:
        print("Yarr!.....")


def previous():
    state = tmsg.showwarning("Kya aage ja sakte h?", "Khatra to nhi h na?")
    print("ha bhai bhot khatra h")


def pehle_jaisa():
    dasha = tmsg.askyesnocancel("Aaj dinner sath m kare?", "Kya kehti ho!")
    if dasha:
        print("OMG!!!!")
    
    else:
        print("Don't mind!")



#Use these to create a non drop-down menu
my_menu = Menu(root)
my_menu.add_command(label="File", command=func)
my_menu.add_command(label="Exit", command=quit)         #quit ek internal command h so ise define karne ki jaroorat nhi h
root.config(menu=my_menu)



#Use these to create a drop-down menu
your_menu = Menu(root)

m1 = Menu(your_menu, tearoff=0)     #tearoff se jo naya dropdown khulta h vo purane vale k saath m khulta h varna alag se door khulta
m1.add_command(label="Save", command=funcc)
m1.add_command(label="Restore", command=previous)
m1.add_separator()
m1.add_command(label="Undo", command=pehle_jaisa)
m1.add_command(label="Save As", command=chal)
m1.add_separator()      #makes a line after the program line it is written
m1.add_command(label="Exit", command=quit)
root.config(menu=your_menu)
your_menu.add_cascade(label="File", menu=m1)


m2 = Menu(your_menu, tearoff=0)
m2.add_command(label="Cut", command=divya)
m2.add_command(label="Rate Us", command=rate)
m2.add_separator()      #makes a line after the program line it is written
m2.add_command(label="Exit", command=quit)
root.config(menu=your_menu)
your_menu.add_cascade(label="Options", menu=m2)


root.mainloop()