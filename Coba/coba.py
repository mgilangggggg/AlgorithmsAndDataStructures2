def abc(x=2):
    if (x == 2):
        abc = y - 5
    else:
        abc = y + abc(x-2, y+2)


print("hasil =  ", abc(10, 2))
