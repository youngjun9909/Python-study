isClose = False

while  not isClose:
  flag = input("멈추겠습니까? (Y/N) ")
  if flag in ['y', 'Y']:
    isClose = True
  if flag in ['n', 'N']:
    isClose = False