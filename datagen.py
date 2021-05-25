f = open("player.txt", "a")
for i in range(0, 200000):
    line = "Jesus,"+str(i)+",Aggies,QB,1,1,1\n"
    f.write(line)
f.close()
print("done")