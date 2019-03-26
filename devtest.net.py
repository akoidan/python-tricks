# https://devtest.net/
"""

2. Choose problem
Calculator Trivial
Fizz Buzz Easy
Inverse Fizz Buzz Hard
Time Guide
Minutes
0
120
60
This is a lot more complicated than the fizzbuzz problem, and takes some real thinking to get right.

The aim of the test is to discover the shortest sequence of consecutive numbers, which when they are run through the fizzbuzz algorithm produce the required output.

For example, the shortest sequence that produces fizz is 3

When looking for the shortest sequence for

fizz buzz

one sequence that produces that output is

3, 4, 5

However, this isn't the shortest. The shortest sequence is 9, 10

In our case, we are only interested in the numbers between 1 and 100, so be sure you limit your calculations to that range, otherwise you are likely to exceed timeout limits.
"""
class InverseFizzBuzz():
  def __init__(self, list):
    self.list = list

  def sequence(self):
    my_list = []
    for i in range(1, 101):
      if i % 3 == 0 and i % 5  == 0:
        my_list.append(None)
      if i % 3 == 0:
        my_list.append('fizz')
      elif i % 5 == 0:
        my_list.append('buzz')
      else:
        my_list.append(None)
    count = []
    for i in range(1, 101):
      current = 0
      hits = 0
      j = 0
      consumed = 0
      for j in range(i, len(my_list)):
        consumed += 1
        if not my_list[j]:
          continue
        if my_list[j] == self.list[current]:
          hits += 1
          current += 1
          if hits == len(self.list):
            break
        else:
          break
      if hits == len(self.list):
        count.append({'value': i+1, 'consumed': consumed})

    min = 1000000
    value = None
    for k in count:
      if k['consumed'] < min:
        min = k['consumed']
        value = k['value']
    if value is None:
      return None
    return [sdf for sdf in range(value, value + min)]
inverse = InverseFizzBuzz(["buzz", "fizz", "buzz"])
inverse.sequence()
