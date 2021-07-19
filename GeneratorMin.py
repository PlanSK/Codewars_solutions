from random import randint


def generator(start, step, index):
    yield_number = start
    while True:
      yield yield_number
      print(f"generator #{index}, start: {start}, step: {step}, current: {yield_number}")
      yield_number += step


def min_generator(gens):
  nums = {gen: next(gen) for gen in gens}
  print("The work has begun")
  while True:
    for k, v  in nums.items():
      if v == min(nums.values()):
        nums[k] = next(k)
        break
    yield v


gens = [
  generator(randint(1, 10), randint(2, 10), gen_number) 
  for gen_number in range(randint(5, 10))
]
min_g = min_generator(gens)
while True:
  input()
  print(next(min_g), end="")