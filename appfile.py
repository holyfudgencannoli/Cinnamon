import ttk as tk

root = tk.Tk()

frame = ttk.Frame(root, padding= 10)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(colum=0, row=0)

root.mainloop()
