b = int(input("Enter the number\n"))
i = 1
x = 0
while x < b:
    c = 0
    for j in range(1, (i + 1)):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
        x = x + 1

    i = i + 1
