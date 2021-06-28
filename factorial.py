a = int(input("enter the number to check factorial\n"))
fact = 1
for i in range(1, (a+1)):
    fact = fact * i
print("factorail of {0} is {1}".format(a, fact))
