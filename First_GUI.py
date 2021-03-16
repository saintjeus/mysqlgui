import tkinter as tk
from tkinter import ttk # ttk stands for themed tk
win = tk.Tk() # creates instance of Tk class
win.title("Python GUI") #instance variable sets a title

win.resizable(True, True) 
# Boolean var in gui allows resizing in x y direction 
ttk.Label(win, text="A Label").grid(column=0, row=0) 
# # #======================================================
# Start GUI
#======================================================
win.mainloop()