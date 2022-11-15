
line = ["This is first line","this is second line","this is third line"]

with open("file.txt","w") as t:
    for i in line:
        t.write(i+"\n")