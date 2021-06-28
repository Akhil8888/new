a = int(input("enter a number to check factors \n"))
print("factors of {0} are".format(a))
for i in range(1, a+1):
    if a % i == 0:
        print(i)
