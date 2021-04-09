import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kargs):
    self.contents = []
    for key, value in kargs.items():
      for i in range(0, value, 1):
        self.contents.append(key)

  #Draw from Hat
  def draw(self, draws):
    drawn = []
    if draws >= len(self.contents):
      return self.contents
    for i in range(0, draws, 1):
      drawn.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
    return drawn

#Run experiments
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0

  for i in range(0, num_experiments, 1):
    fail = False
    trial = copy.deepcopy(hat)
    drawn = trial.draw(num_balls_drawn)
    for balls, count in expected_balls.items():
      if drawn.count(balls) < count:
        fail = True
    if fail == False:
      fail = False
      success += 1

  return success/num_experiments