a = int(input("enter number to find reverse"))
rev = 0
temp = a
while a > 0:
    r = a % 10
    rev = rev * 10 + r
    a = a // 10
print(rev)
