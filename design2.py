a = int(input("enter the limit\n"))
for i in range(65 + a, 65, -1):
    for j in range(65, i):
        print("\t" + chr(j), end="")
    print("")
