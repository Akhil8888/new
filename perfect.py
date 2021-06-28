n = int(input("enter a number to check perfect number or not \n"))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if (sum == n):
    print("{0}is a perfect number".format(n))
else:
    print("{0}is not a perfect number".format(n))
