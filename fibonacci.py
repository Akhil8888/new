num = int(input("enter the limit of numbers"))
a = 0
b = 1
sum = 0
while sum < (num + 1):
    print(sum)
    a = b
    b = sum
    sum = a + b
