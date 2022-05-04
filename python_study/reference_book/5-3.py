class User:
  def __init__(self, x, y):
    self.name = x
    self.age = y
  
  def dump(self):
    print('name:{}'.format(self.name))
    print('age:{}'.format(self.age))

ana = User('ana', 30)
ana.dump()