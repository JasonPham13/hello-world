# import random
# for dice in range(1):
#     dice_value = random.randint(1,6)
# for dice in range (1):
#     dice_value2 = random.randint(1,6)
#     print(f'Roll One: {dice_value} Roll Two: {dice_value2}')

import random
want_to_quit = ''
while not want_to_quit:
    dice_value = random.randint(1, 6)
    dice_value2 = random.randint(1,6)
    print(f'You rolled a {dice_value} and a {dice_value2}')
    if dice_value == dice_value2:
        input('You rolled Doubles, please press Enter to roll again')
    else:
        want_to_quit = input('Press enter to roll again, or any other key to quit plus enter to quit: ')


