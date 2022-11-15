with open("country.txt","r") as fp:
    r = fp.readlines()
    A = []
    B = []
    for i in r:
        if i[0] == "A":
            A.append(i)

        elif i[0] == "B":
            B.append(i)

    with open("country_name_of_A.txt","w") as fp:
        for i in A:
            fp.write(i)

    with open("country_name_of_B.txt","w") as fp:
        for i in B:
            fp.write(i)



            