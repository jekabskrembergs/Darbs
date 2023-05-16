from tkinter import *


def func():
    value = inputField.get()
    outputField
window = Tk()
window.geometry("400x400")
window.title("Jekabs")
window.config(backrounds="white")
window.resizable(False, False)


inputField = Entry(window)
inputField.place(x=10,y=10)

button = Button(text="Print", command=lambda:func())

outputField = Label(text="izvade")
outputField.place(x=10,y=70)

window.mainloop()