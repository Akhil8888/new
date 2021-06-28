a = 2020
b = int(input("enter end year\n"))
if b > 2020:
    print("leap years are\n")
    for i in range(a, b + 1):
        if int(i) % 4 == 0:
            if int(i) % 100 == 0:
                if int(i) % 400 == 0:
                    print(i)
            else:
                print(i)
else:
    print("invalid input")
