a = int(input("enter the number to check prime or not\n"))
flag = 0
for i in range(2, a):
    if (a % i) == 0:
        flag = 1
if flag == 1:
    print("{} is not a prime number".format(a))
else:
    print("{} is  a prime number".format(a))
