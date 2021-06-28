def binary(list, n, key):
    first = 0
    last = n - 1
    mid = int(first + last) / 2
    while first <= last:
        if key == list(mid):
            print("element found at ", mid + 1)
            return -1
        elif (key < list(mid)):
             last = mid - 1
        elif (key > list(mid)):
            first = mid + 1
    print("element not found")
    return -1


list = []
n = int(input("enter the number of elaments"))
for i in range(0, n):
    list.append(int(input()))
list.sort()
print("sorted elemnts are", list)
key = int(input("enter the element to search"))
binary(list, n, key)
