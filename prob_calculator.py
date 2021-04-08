import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kargs):
    self.contents = []
    for key, value in kargs.items():
      for i in range(0, value, 1):
        self.contents.append(key)

  def draw(self, draws):
    drawn = []
    for i in range(0, draws, 1):
      drawn.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  return ""