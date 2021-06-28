a = int(input("enter limit\n"))
a = a + 1
for i in range(0, a):
    for j in range(0, i):
        print("\t" + str(i), end="")
    print("")
