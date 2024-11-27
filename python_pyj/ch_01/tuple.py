# 리스트랑 동일한 구조 (값의 추가, 수정, 삭제 불가)
tuple1 = ()
tuple2 = tuple()

tuple1 = (1, 2, 3)
print(tuple1[1:])

tuple1 = tuple1 * 3
print(tuple1)

tuple2 = (10,)

tuple3 = 1, 2, 3

def add(n1, n2, n3):
  return n1 + n2 + n3, n1 + n2, n2 + n3

print(add(10,20,30))