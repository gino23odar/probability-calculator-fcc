import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, *args):
    self.args = args
    self.balls = {}
    for arg in self.args:
      color, number = arg.split('=')
      self.balls[color] = int(number)
    self.contents = []
    for color, number in self.balls.items():
      for i in range(number):
        self.contents.append(color)

  def draw(self, num):
    balls_bag = self.contents
    draws = []
    for i in range(num):
      balls_left = len(balls_bag)
      random_draw = random.randint(0, balls_left)
      pulled_ball = balls_bag.pop(random_draw)
      draws.append(pulled_ball)
    return draws

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
