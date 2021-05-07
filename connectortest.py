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
# window.geometry("400x250")
query = "DELETE FROM PLAYER"
mycursor.execute(query)
mydb.commit()
print(mycursor.rowcount)
# mycursor.execute("SELECT * FROM player")
# i = 0
# for player in mycursor:
#     for j in range(len(player)):
#         e = Entry(window, width=10, fg='black')
#         e.grid(row=i, column=j)
#         e.insert(END,player[j])
#     i=i+1

window.mainloop()

# query = "INSERT INTO player (name, playerID, teamname, position, touchdowns, totalyards, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
# val = "Jesus", "107", "Aggies", "QB", "1", "1", "1"

# mycursor.execute(query, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")