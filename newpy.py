n = int(input("enter a number"))
m = n
s = 0
while n > 0:
    d = n % 10
    s = s + (d ** 3)
    n = int(n / 10)
if m == s:
    print("amstrong number")
else:
    print("not amstrong")
