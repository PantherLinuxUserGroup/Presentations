def addSomeNum(y=5):
  return (lambda x: x + y)

add5 = addSomeNum()
print(add5(1))        # 6
add1= addSomeNum(1)
print(add1(2))        # 3
