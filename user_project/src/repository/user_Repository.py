from pymysql import cursors

from src.config.database_config import DatabaseConfig
from src.entity.user_entity import User

class UserRepository:

  @staticmethod
  def delete(userId: int):
    successCount = 0
    try:
      connection = DatabaseConfig.getConnection()

      try:
        cursor = connection.cursor()
        sql = 'DELETE FROM user_tb WHERE user_id = %s'
        successCount = cursor.execute(query=sql, args=(userId, ))
        connection.commit()

      except Exception as e:
        print(e)

    except Exception as e:
      print("데이터베이스 연결 실패")

    return successCount

  @staticmethod
  def findAll():
    foundUsers = []

    try:
      connection = DatabaseConfig.getConnection()
      try:
        cursor = connection.cursor(cursor=cursors.DictCursor)
        sql = "SELECT * FROM user_tb ORDER BY user_id"
        cursor.execute(sql)
        rs = cursor.fetchall()

        if len(rs) > 0:
          foundUsers = list(map(lambda user: User(
            userId=user['user_id'],
            username=user['username'],
            password=user['password'],
            name=user['name'],
            email=user['email'],
            createDate=user['create_date'],
            updateDate=user['update_date']
          ), rs))

      except Exception as e:
        print(e)
      finally:
        connection.close()
    except Exception as e:
      print("데이터베이스 연결 패")

    return foundUsers


  @staticmethod
  def findByUsername(username: str):
    foundUser = None

    try:
      connection = DatabaseConfig.getConnection()
      try:
        cursor = connection.cursor(cursor=cursors.DictCursor)
        sql = "SELECT * FROM user_tb WHERE username = %s"
        cursor.execute(query=sql, args=(username, ))
        rs = cursor.fetchone()
        if bool(rs):
          foundUser = User(
            userId=rs['user_id'],
            username=rs['username'],
            password=rs['password'],
            name=rs['name'],
            email=rs['email'],
            createDate=rs['create_date'],
            updateDate=rs['update_date']
          )

      except Exception as e:
        print(e)
      finally:
        connection.close()

    except Exception as e:
      print(e)
      print("데이터베이스 연결 실패")
    return foundUser

  @staticmethod
  def save_user(user: User):
    connection = None
    try:
      connection = DatabaseConfig.getConnection()


      try:
        cursor = connection.cursor()
        sql = '''
        INSERT INTO user_tb VALUES(default, %s, %s, %s, %s, now(), now())
        '''
        cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
        user.userId = cursor.lastrowid
        connection.commit()

      except Exception as e:
        print(e)
        print("사용자 정보 추가 실패 !")

      finally:
        connection.close()

    except Exception as e:
      print(e)












#
# class UserRepositoryStudy:
#
#   def insert(self, user: User):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor()
#     sql = '''
# INSERT INTO user_tb
# VALUES(default, %s, %s, %s, %s, now(), now())
# '''
#     insertCount = cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
#     print(f"User 데이터 추가 성공 {insertCount}건")
#     connection.commit()
#
#   def findById(self, user_id: int):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor(cursor=cursors.DictCursor)
#     sql = '''
#     SELECT * FROM user_tb WHERE user_id = %s
#     '''
#     cursor.execute(query=sql, args=(user_id, ))
#     result = cursor.fetchone()
#     return result
#
#
#   def findByUsername(self, username: str):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor(cursor=cursors.DictCursor)
#     sql = '''
#     SELECT * FROM user_tb WHERE username = %s
#     '''
#     cursor.execute(query=sql, args=(username, ))
#     result = cursor.fetchone()
#     return result
#
#   def deleteByUserId(self, user_id: int):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor(cursor=cursors.DictCursor)
#     sql = '''
#     DELETE * FROM user_tb WHERE user_id = %s
#     '''
#     deleteCount = cursor.execute(query=sql, args=(user_id, ))
#     return print(f"User 데이터 삭제 성공 {deleteCount}건")