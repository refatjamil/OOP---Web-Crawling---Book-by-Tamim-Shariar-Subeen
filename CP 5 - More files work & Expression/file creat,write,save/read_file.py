with open("file.txt","r") as fp:
    lines = fp.readlines()
    print(lines)
    for line in lines:
        print(line)