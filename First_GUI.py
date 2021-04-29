#======================================================
# IMPORTS
#======================================================

import tkinter as tk
from tkinter import ttk # ttk stands for themed tk
from tkinter import scrolledtext

win = tk.Tk() # creates instance of Tk class
win.title("Python GUI") #instance variable sets a title

win.resizable(True, True) 
# Boolean var in gui allows resizing in x y direction 
#ttk.Label(win, text="A Label").grid(column=0, row=0) 

a_label = ttk.Label(win,text="Enter a name:")
a_label.grid(column=0, row=0)

# Button Click Event Function
def click_me():
    action.configure(text="** I have been Clicked! **")
    a_label.configure(foreground = 'red')
    a_label.configure(text='A Red Label')

def entry_click_me():
    action.configure(text=number.get() + ' Hello '+name.get())

# Adding a Textbox Entry Widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text = "Click Me!", command=entry_click_me)
action.grid(column=2, row=1)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number=tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
# state - readonly prevents from changing the values
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0) #<-Combobox in column1

#Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)
#===============================================
colors =["Blue", "Gold", "Red", "Purple"]

# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])
    elif radSel == 3: win.configure(background=colors[3])

radVar = tk.IntVar()
radVar.set(99)

for col in range(4):
    curRad = tk.Radiobutton(win,text=colors[col],variable=radVar,value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

#Using a scrolled Text control
scrol_w=30
scrol_h=3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

name_entered.focus() #sets the focus

# # #======================================================
# Start GUI
#======================================================
win.mainloop()