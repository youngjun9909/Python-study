#  Map 자료형
#  key, value
#  key 중복x, 순서x

dict1 = dict()
dict1 = {
  "name": "박영준",
  "age": 26
}

print(dict1)

list1 = ['a', 'b', 'c']
tuple1 = 'a', 'b', 'c'
dict1 = {'10':'aa', '20':'bb', '30':'cc'}

print(list1[0])
print(tuple1[0])
print(dict1['10'])

dict1['40'] = 'dd'
dict1.update({'50':'ee', '60': 'ff'})
print(dict1)

# value 조회
print(dict1.get('20'))
print(dict1['20'])

#  쌍 삭제
print(dict1.pop('30'))
print(dict1)

print(dict1.items())

# 반복문
for items in dict1.items():
  print(items)

for key in dict1.keys():
  print(key)

for values in dict1.values():
  print(key)

keys1 = list(dict1.keys())
print(keys1)