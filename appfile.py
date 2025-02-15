pip3 install tkk.py
import tkinter as tk
from tkinter import ttk 

root = tk.Tk()

frame = ttk.Frame(root, padding= 10)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(colum=0, row=0)

root.mainloop()
