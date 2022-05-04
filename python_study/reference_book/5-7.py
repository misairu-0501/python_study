import random

class Bingo:
  def __init__(self):
    self.balls = list(range(1, 100))

  def get_ball(self):
    random.shuffle(self.balls)
    return self.balls.pop()

  def has_ball(self):
    return len(self.balls) != 0

bingo = Bingo()

while bingo.has_ball():
  print(bingo.get_ball())