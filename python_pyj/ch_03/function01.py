def fx01():
  pass

def fx02():
  print('fx02 호출')

fx02()

class A: 
  pass

def fx03(a: int, b):
  print(a)
  print(b)
fx03(10, A())

def fx03(a: int, b: A, c = None):
  print(a)
  print(b)
  print(c)

fx03(1,'a',[])


def fx04(*args):
  print(args)


fx04(1,2,3,4,5)

def fx05(
    url: str | None="http://localhost", 
    port: int | None=8080, 
    value: dict = dict()):
  print(url)
  print(port)
  print(value)
  return "Response"

fx05(url="https://localhost", value={"name": "박영준", "age": 26 })

req = lambda url, port, params: {f"url: {url}, port: {port}, params: {params}"}
print(req("http://localhost", 8080, {"name": "박영준", "age": 26 }))





