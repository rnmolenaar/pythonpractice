import random

def dice_roll():
    lowest = 1
    highest = 6
    dice_roll = random.randint(lowest,highest)

    return dice_roll

value = dice_roll()
print(value)
