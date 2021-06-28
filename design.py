a = int(input("enter the limit\n"))
a = a + 1
for i in range(65,65+a):
    for j in range(65,i):
        print("\t" + chr(j), end="")
    print("")
