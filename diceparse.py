import random
import re

class Dice:
    def __init__(self, sides, quantity=1):
        self.sides = sides
        self.quantity = abs(quantity)
        self.sign = -1 if quantity < 0 else 1

    def roll(self):
        return [self.sign * (random.randint(1, abs(self.sides)) if self.sides > 0 else -random.randint(1, -abs(self.sides))) for _ in range(self.quantity)]

    def __str__(self):
        return f'{self.sign*self.quantity}d{abs(self.sides)}' if self.quantity != 1 else f'd{self.sides}'


class DicePool:
    def __init__(self):
        self.dice_and_constants = []
        self.roll_history = []

    def add_dice(self, dice):
        self.dice_and_constants.append(dice)
    
    def add_constant(self, constant):
        self.dice_and_constants.append(constant)

    def roll(self):
        roll_results = []
        for item in self.dice_and_constants:
            if isinstance(item, Dice):
                roll_results.extend(item.roll())
            else:
                roll_results.append(item)
        self.roll_history.append(roll_results)
        return roll_results

    def sum(self, rolls_ago=0):
        if rolls_ago >= len(self.roll_history):
            raise IndexError("Rolls_ago index out of range")
        return sum(self.roll_history[-1 - rolls_ago])

    def get_roll_history(self):
        return self.roll_history

    def __str__(self):
        return ' + '.join(str(item) for item in self.dice_and_constants)


def parse_dice_string(dice_string):
    dice_constant_pattern = re.compile(r'(-?\d*)[dD](-?\d+)|(-?\d+)')

    dice_string = dice_string.replace(" ", "")  # removing spaces
    parts = dice_constant_pattern.findall(dice_string)

    dice_pool = DicePool()
    
    for part in parts:
        if part[0] or part[1]:  # if first or second part exists, it's a dice set
            # number of dice. if not specified, default is 1
            num_dice = int(part[0]) if part[0] else 1
            # create a dice object and add it to the pool
            dice_pool.add_dice(Dice(int(part[1]), num_dice))
        else:  # if no first or second part, it's a constant
            dice_pool.add_constant(int(part[2]))
    
    return dice_pool


# Testing the function
dice_string = "d20 + d6 - 3d4 + 5 - 2"
dice_pool = parse_dice_string(dice_string)
print(dice_pool)  # should print: d20 + d6 + -3d4 + 5 + -2

print(dice_pool.roll())  # should print a list of numbers
print(dice_pool.sum())  # should print the sum of the roll
print(dice_pool.roll()) # should print a list of numbers
print(dice_pool.sum()) 
print(dice_pool.sum(1))  # should print the sum of the previous roll

print(dice_pool.get_roll_history())  # should print a list of lists of numbers
