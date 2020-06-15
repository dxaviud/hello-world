from tkinter import *

root = Tk()

my_canvas = Canvas(root, width=500, height=500)
my_canvas.grid(row=0, column=0)

def mouse_move(event):
    print(event.x, event.y)

def mouse_move_draw(event):
    my_canvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, fill="red", outline="red")


my_canvas.bind("<B1-Motion>", mouse_move_draw)

input()

