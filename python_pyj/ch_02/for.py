nums = [10, 20, 30, 40]

for num in nums:
  print(num)

nums = range(10)
print(nums)

for num in nums:
  print(num)


for i in range(10):
  for j in range(5):
    print(f'i: {i}, j: {j}')

'''
*     *****
**    ****
***   ***
****  **
***** *

*****
****
***
**
*
'''
# for i in range(1,  5 + 1):
#   print('*' * i)

# for i in range(5, 0, -1):
#   print('*' * i)

print("aaaaa", end="")
print("bbbbb", end="")
print("*" * 3)

n = 5

for i in range(1, n + 1):
  print("*" * i, end="")
  print()

for i in range(n, 0, -1):
  print('*' * i)

print('=====================')

for i in range(1, n + 1):
  print("*" * i, end="\t")  
  print(" " * (n - i), end="\t")
  print("*" * (n - i + 1))

print('=====================')

for i in range(5):
  for j in range( i + 1):
    print("*", end="")
  print()

print('=====================')

for i in range(1, 6):
  print('*' * i)

for i in range(5):
  print('*' * (5 - i)) 


for i in range(1, n + 1):
  print(f'{"*" * i}\t\t{"*" * (6 - i)}')  