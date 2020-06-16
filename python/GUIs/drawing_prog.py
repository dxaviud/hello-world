from tkinter import *

class Drawing():

    def display(self):

        root = Tk()

        canvas = Canvas(root, width=500, height=500)
        canvas.grid(row=0, column=0)

        draw_color = "black"

        def mouse_move(event):
            canvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, fill=draw_color, outline=draw_color)

        canvas.bind("<B1-Motion>", mouse_move)

        def key_press(event):
            nonlocal draw_color

            key = event.char.upper()

            if key == "C":
                canvas.delete("all")
            elif key == "R":
                draw_color = "red"
            elif key == "G":
                draw_color = "green"
            elif key == "B":
                draw_color = "blue"
            elif key == "Y":
                draw_color = "yellow"
            else:
                draw_color = "black"

        canvas.bind("<KeyPress>", key_press)
        canvas.focus_set()

        root.mainloop()

if __name__ == "__main__":
    app = Drawing()
    app.display()