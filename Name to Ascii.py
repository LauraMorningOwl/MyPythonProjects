from tkinter import *
from tkinter import ttk

root = Tk()

ascii_symbol = StringVar()

def name_ascii():
    a = name.get()
    num_list = [ord(char) for char in a]

    ascii_number = sum(num_list) // len(a)

    b = chr(ascii_number)

    return ascii_symbol.set(b)



name = ttk.Entry(root)
convert = ttk.Button(root, text="convert", command=name_ascii)
text = ttk.Label(root, text="your ASCII symbol is: ")
symbol = ttk.Label(root, textvariable = ascii_symbol)

name.pack()
convert.pack()
text.pack()
symbol.pack()

root.mainloop()
