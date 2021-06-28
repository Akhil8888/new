c=2020
a =int(input("enter final year"))
for i in range(c,(a+1)):
   if (int(i) % 4) == 0:
     if (int(i) % 100) == 0:
        print("no leap years")
else:
    print(i)
