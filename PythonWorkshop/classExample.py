class MyClass:
  x = 123
  def __init__(self, n):
    self.n = n
  def addNums(self):
    return self.x + self.n

c = MyClass(7)
print(c.addNums())  # 130
