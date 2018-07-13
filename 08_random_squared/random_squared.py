import random

range_up = range(0, 49)

random_numbers = random.sample(range_up, 49)

random_squared = [rand*rand for rand in random_numbers]

print(random_numbers)





