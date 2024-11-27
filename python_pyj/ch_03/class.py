class User:
  
  def __init__(self, userName:str, password:str, name:str, email:str|None = "", address:str | None = ""):
    self.userName = userName
    self.password = password
    self.name = name
    self.email = email
    self.address = address

  def getUserInfo(self):
    return f'''
userName: {self.userName}
password: {self.password}
name: {self.name}
email: {self.email}
address: {self.address}
'''


user1 = User(userName="a", password="a", name="a")
user2 = User(userName="b", password="b", name="b", email="b@b", address="부산")

print(user1.getUserInfo())
print(user2.getUserInfo())

'''
class Student
name - str 필
age - int 필
address - str 선

getStudentInfo()
'''
class Student:
  def __init__(self, name:str, age:int, address:str | None = ""):
    self.name = name
    self.age = age
    self.address = address

  def __str__(self) -> str:
    return f"""
학생 이름: {self.name}
학생 나이: {self.age}
학생 주소: {self.address}
"""
  
  def incrementAge(self):
    self.age += 1
    # return print(f"age: {self.age}")

st1 = Student("ㅇ", 26, "ㅇ")
print(st1)
st1.incrementAge()
print(st1)


from dataclasses import dataclass

@dataclass
class Student2:
  name: str
  age: int
  address: str | None = ""

st2 = Student2("d",26,"d")
print(st2)