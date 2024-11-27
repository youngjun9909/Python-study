# 선언 및 초기화 방법
list1 = [1, 5, 3, 2, 2, 2]
# list2 = list()

print(list1[0])
print(list1[0:2])

print(list1.index(3))
print(list1.sort())
print(list1[:].sort())
print(list1.sort())

list2 = list1[:]
list2.sort()
print(list2)
print(list1)

print(list2.remove(2))
print(list2)

list1.insert(1, 10)
print(list1)

list3 = list1.copy()
print(list3)

list1.extend(list3)
print(list1)


print(list3 + [1, 2, 3, 4])
print(list3 * 3)

list4 = [1, "pyj", [10, 20], 3.14, [30, 40]]
print(list4)

print(list4[2:])
print(list4[2 :: 2])
