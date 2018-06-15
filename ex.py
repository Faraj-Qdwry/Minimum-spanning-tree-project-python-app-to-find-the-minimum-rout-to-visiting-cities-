from tkinter import *


def onclick():
    pass


root = Tk()
text = Text(root)
text.insert(INSERT, "Here, I start the text ...")
button = Button(text, text="I am a button", command=onclick)
text.window_create(INSERT, window=button)
text.insert(END, "... and here, I finish it.")
text.pack()
root.mainloop()
