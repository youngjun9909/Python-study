from dataclasses import dataclass

@dataclass
class User:
  username: str
  password: str
  name: str
  email: str

class UserDatabase:
  def insert(self, user:User):
    print(f"insert Data -> {user}")
  
  def select(self, username:str):
    print(f"select Data -> search username: {username}")

  def update(self, user:User):
    print(f"update Data -> {user}")

  def delete(self, username:str):
    print(f"delete Data -> search username: {username}")

if __name__ == "__main__":
  userdatabase = UserDatabase()
  userdatabase.insert(User('aaa', '1234', '박영준', 'aaa@example.com'))
  newUser = User(name="박일준", password='222', username="bbb", email="dsad@example.com")
  userdatabase.insert(newUser)