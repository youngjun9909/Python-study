from dataclasses import dataclass
from pymysql import connect


@dataclass
class DatabaseConfig:
    @staticmethod
    def getConnection():
        host: str = 'localhost'
        port: int = 3306
        user: str = 'root'
        password: str = '!Dydekd7511'
        database: str = 'pymysql_study'

        return connect(host=host, port=port, user=user, password=password, database=database)
