a = input("enter 2 numbers\n")
b = input()
c = str(input("enter operator\n"))
if c == 'sum':
    sum = int(a) + int(b)
    print("sum of {0} and {1} is {2}".format(a, b, sum))
elif c == 'sub':
    sub = int(a) - int(b)
    print("sub of {0} and {1} is {2}".format(a, b, sub))
elif c == 'mul':
    mul = int(a) * int(b)
    print("mul of {0} and {1} is {2}".format(a, b, mul))
elif c == 'div':
    div = int(a) / int(b)
    print("div of {0} and {1} is {2}".format(a, b, div))
else:
    print("invalid")
