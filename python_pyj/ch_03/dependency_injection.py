# 의존성 주입
from dataclasses import dataclass


@dataclass
class Repository:
  
  def insert(self, entity):
    print(f"{entity} -> 데이터를 추가합니다.")


class Service:
  repository: Repository

  def __init__(self, repository: Repository):
    self.repository = repository

  def addData(self, dto: dict):
    entity = dto
    self.repository.insert(entity)

# class Service:
#     def addData(self, dto: dict):
#       repository = Repository()
#       entity = dto
#       repository.insert(entity)


repository = Repository()
service = Service(repository)

service.addData({"name":"박영준", "age": 26})