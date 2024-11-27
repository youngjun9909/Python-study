from __init__ import concat, User, UserDatabase


def main():
  print("user project start!!!")
  newUser = User(username='aaa', password='1234', name="박영준", email="asd@example.com")
  UserDatabase().insert(newUser)
  concat(1, 10)

if __name__ == "__main__" :
  main()