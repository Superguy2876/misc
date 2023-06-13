import random as rnd

count = 0

for i in range(1000000):
    die0 = rnd.randint(1, 20)
    die1 = rnd.randint(1, 20)
    die2 = rnd.randint(1, 20)
    if any([die0 >= 18, die1 >= 18, die2 >= 18]):
        count += 1

print(count)