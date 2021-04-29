import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "password",
    database = "jesusbarba_phase1"
)
mycursor = mydb.cursor()

query = "INSERT INTO player (name, playerID, teamname, position, touchdowns, totalyards, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = "Jesus", "107", "Aggies", "QB", "1", "1", "1"

mycursor.execute(query, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")