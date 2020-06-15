from tkinter import *

root_window = Tk() #creates window

root_window.resizable(width=False, height=False) #do not allow resizing of the window

text_label = Label(root_window, text="Hello World from Tkinter.") #creates label with text

text_label.grid(row=0, column=0)

text_label_two = Label(root_window, text="More text.")

text_label_two.grid(row=1, column=0)

def click_event(): #This is executed when button is clicked (called event handler)
    print("click")
    #config allows configuration of a display element
    text_label.config(text="Text changed after clicking button")
    print("Entry: " + ent.get())

button = Button(root_window, text="A button", command=click_event) #creates a button

button.grid(row=2, column=0)

ent = Entry(root_window)# creates entry that allows user to type stuff

ent.grid(row=3, column=0)

input()
