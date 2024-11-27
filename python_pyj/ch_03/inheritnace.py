from dataclasses import dataclass
from overrides import overrides

@dataclass
class Person:
  name: str
  age: int

  def move(self):
    print(f"{self.name}({self.age})님이 움직입니다.")

@dataclass
class Student(Person):
  score: int

  def study(self):
    print(f'{self.name}님이 공부를 합니다.')

  @overrides
  def move(self):
    super().move()
    print('학생이 움직입니다.')

@dataclass
class Teacher(Person):
  subject: str

  def lesson(self):
    print(f'{self.name}님이 수업을 합니다.')
  
  @overrides
  def move(self):
    super().move()
    print('선생님이 움직입니다.')

ps = Person(name="사람", age=10)
st = Student(name="전우치", age=50, score=90)
tc = Teacher(name="홍길동", age=60, subject="python")

print(ps)
print(st)
print(tc)


ps2:Person = st
print(ps2)
ps3:Teacher = st
print(ps3)

print(isinstance(ps3, Student)) # True
print(isinstance(ps3, Teacher)) # False

persons = [ps, st, tc]

for p in persons:
  p.move()
  if isinstance(p, Student):
    p.study()
  elif isinstance(p, Teacher):
    p.lesson()