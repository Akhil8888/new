a = int(input("enter number to find reverse\n"))
s = 0
temp = a
while a > 0:
    r = a % 10
    s = s * 10 + r
    a = a // 10
print(s)
if temp == s:
    print("pallindrome")
else:
    print("not pallindrome")
