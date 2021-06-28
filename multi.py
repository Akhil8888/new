a = int(input("enter the number to find table\n"))
for i in range(1, a + 1):
    for j in range(1, 11):
        c = i * j
        print("{0}*{1}={2}".format(j, i, c))
    print("\n")
