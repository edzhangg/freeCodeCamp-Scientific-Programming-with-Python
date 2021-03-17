import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      counter = 0
      while counter < value:
        self.contents.append(str(key))
        counter += 1
  def draw(self, numDrawn):
    ballsDrawn = []
    bag = self.contents
    numDrawn = numDrawn
    if numDrawn >= len(bag):
      return(bag)
    while numDrawn != 0:
      index = random.randint(0, (len(bag)-1))
      ballsDrawn.append(bag[index])
      bag.remove(bag[index])
      numDrawn -= 1
    return(ballsDrawn)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  counter = 0
  timeSuccess = 0
  while counter < num_experiments:
    hat1 = copy.deepcopy(hat)
    results = hat1.draw(num_balls_drawn)
    numGreater = 0
    for key in list(expected_balls.keys()):
      if results.count(key) >= expected_balls[key]:
        numGreater += 1
    if numGreater == len(expected_balls):
      timeSuccess += 1
    counter += 1
  output = timeSuccess / num_experiments
  return(output)