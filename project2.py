import mysql.connector
import tkinter as tk
from tkinter import *

mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "password",
    database = "jesusbarba_phase1"
)
mycursor = mydb.cursor()
window = tk.Tk()
window.title("CS482 - Project 2")
window.geometry("500x500")

#single insert function
def si():
    file_name = insert_text.get()
    with open(file_name) as f:
        for line in f:
            val = line.split(',')
            val[-1], val[-2], val[-3] = int(val[-1]), int(val[-2]), int(val[-3])
            cursor = mydb.cursor()
            query = "INSERT INTO player (name, playerID, teamname, position, touchdowns, totalyards, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = val[0], val[1], val[2], val[3], val[4], val[5], val[6]
            cursor.execute(query, values)
        mydb.commit()

# bulk insert function
def bi():
    table_name = insert_text.get()
    if table_name == "Player_100K.txt" or table_name=="Player_150K.txt" or table_name == "Player_200K.txt":
        query = "LOAD DATA INFILE '" + table_name + "'"
        query += "\nINTO TABLE player\nFIELDS TERMINATED BY ','\nLINES TERMINATED BY '\\r\\n'\n(Name, PlayerID, TeamName, Position, Touchdowns, TotalYards, Salary);"
        mycursor.execute(query)
        mydb.commit()
    
#delete function
def delet():
    table_name = delete_text.get()
    mycursor.execute("DELETE FROM "+table_name)
    mydb.commit()

#query function
def query():
    print(query_text.get())

#error message function
def error():
    messagebox.showinfo("test")

insert_text = tk.StringVar()
insert = Entry(window, width=30, textvariable=insert_text)
insert.grid(column=0, row=0)

single_insert_button = Button(window, text="Single Insert", command=si)
single_insert_button.grid(column=1, row=0)

bulk_insert_button = Button(window,text="Bulk Insert", command= bi)
bulk_insert_button.grid(column=2, row=0)

delete_text = tk.StringVar()
delete = Entry(window, width=30, textvariable=delete_text)
delete.grid(column=0, row = 1)

delete_button = Button(window, text="Delete", command=delet)
delete_button.grid(column=1, row=1)

query_text=tk.StringVar()
query_entry = Entry(window, width=30, textvariable=query_text)
query_entry.grid(column=0, row=2)

query_button = Button(window, text="Query", command=query)
query_button.grid(column=1, row=2)

window.mainloop()