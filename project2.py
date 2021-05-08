import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
import time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "password",
    database = "jesusbarba_phase1"
)
mycursor = mydb.cursor()
window = tk.Tk()
window.title("CS482 - Project 2")
window.geometry("400x100")


#single insert function
def si():
    start = time.time()
    file_name = insert_text.get()
    with open(file_name) as f:
        for line in f:
            val = line.split(',')
            cursor = mydb.cursor()
            if file_name == "player.txt":
                val[-1], val[-2], val[-3] = int(val[-1]), int(val[-2]), int(val[-3])
                query = "INSERT INTO player (name, playerID, teamname, position, touchdowns, totalyards, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = val[0], val[1], val[2], val[3], val[4], val[5], val[6]
            elif file_name == "play.txt":
                query = "INSERT INTO play (PlayerID, GameID) VALUES (%s, %s)"
                values = val[0], val[1]
            elif file_name == "game.txt":
                query = "INSERT INTO game (GameID, Date, Stadium, Result, Attendance, TicketRevenue) VALUES (%s, %s, %s, %s, %s, %s)"
                values = val[0], val[1], val[2], val[3], val[4], val[5]
            else:
                msg.showerror("Invalid Table Name", "Please enter data for player, play, or game tables.")
                return
            try:
                cursor.execute(query, values)
                mydb.commit()
                
            except mysql.connector.Error as err:
                msg.showerror('Single Insert Error', err)
        end = time.time()
        msg.showinfo('Single Insert Successful', str(mycursor.rowcount)+" records inserted.\nTime was "
        + str(end-start) + "seconds." )

# bulk insert function
def bi():
    start = time.time()
    table_name = insert_text.get()
    # if table_name.lower() == "player.txt":
    query = "LOAD DATA INFILE '" + table_name + "'"
    query += "\nINTO TABLE player\nFIELDS TERMINATED BY ','\nLINES TERMINATED BY '\\r\\n'\n(Name, PlayerID, TeamName, Position, Touchdowns, TotalYards, Salary);"
    # elif table_name.lower() == "play.txt":
    #     query = "LOAD DATA INFILE '" + table_name + "'"
    #     query += "\nINTO TABLE play\nFIELDS TERMINATED BY ','\nLINES TERMINATED BY '\\r\\n'\n(PlayerID, GameID);"
    # elif table_name.lower() == "game.txt":
    #     query = "LOAD DATA INFILE '" + table_name + "'"
    #     query += "\nINTO TABLE play\nFIELDS TERMINATED BY ','\nLINES TERMINATED BY '\\r\\n'\n(GameID, Date, Stadium, Result, Attendance, TicketRevenue);"
    # else:
    #     msg.showerror("Invalid Table Name", "Please enter data for player, play, or game tables.")
    #     return
    try:
        mycursor.execute(query)
        mydb.commit()
        end = time.time()
        msg.showinfo('Bulk Insert Successful', str(mycursor.rowcount)+" records inserted.\nTime was "
        + str(end-start) + "seconds." )
    except mysql.connector.Error as err:
        msg.showerror('Bulk Insert Error', err)
    
#delete function
def delet():
    start = time.time()
    table_name = delete_text.get()
    try:
        mycursor.execute("DELETE FROM "+table_name)
        mydb.commit()
        end = time.time()
        msg.showinfo('Delete Successful', str(mycursor.rowcount)+" records deleted from " + table_name +" table.\nTime was "
        + str(end-start) + "seconds.")
    except mysql.connector.Error as err:
        msg.showerror('Delete Error', err)
#query function
def query():
    start = time.time()
    q = query_text.get()
    cursor = mydb.cursor()
    try:
        cursor.execute(q)
        end = time.time()
        msg.showinfo('Query Succesful', "Time was "+ str(end-start) + "seconds.")
        newWindow = Toplevel(window)
        newWindow.title("Query Results")
        newWindow.geometry("200x200")
        i = 0
        for elem in cursor:
            for j in range(0, len(elem)):
                e = Entry(newWindow, width=10)
                e.grid(row=i, column=j)
                e.insert(END, elem[j])
                i+= 1
    except mysql.connector.Error as err:                
        msg.showerror('Query Error', err)

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