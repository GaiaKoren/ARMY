import array



arr = array.array("i", [1, 2, 3])

print(arr.index(3))

arr.reverse()

print(arr)


arr.append(4)

arr.insert(2, 5)


print(arr.pop(2))

arr.remove(1)

print(arr)