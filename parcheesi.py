# import random
# number_of_dice = int(input('How many dice to roll? '))
# print(f'You are about to roll {number_of_dice} dice...')
# for dice in range(number_of_dice):
#     dice_value = random.randint(1, 6)
#     print(dice_value)

import random
# want_to_quit = ''
# while not want_to_quit:
#     dice_value = random.randint(1, 6)
#     dice_value2 = random.randint(1,6)
#     print(f'You rolled a {dice_value} and a {dice_value2}')
#     if dice_value == dice_value2:
#         input('You rolled Doubles, please press Enter to roll again')
#     else:
#         want_to_quit = input('Your turn has ended, Next Person to roll: ')


quit = ''
doubles = 0
snake_eyes = 1
# first_player = input("Who's going first?: ")
# if first_player == 'Yellow':
#     player_list = ["Yellow, Green, Red, Blue"]
# elif first_player == 'Green':
#     player_list = ["Green, Red, Blue, Yellow"]
# elif first_player == 'Red':
#     player_list = ["Red, Blue, Yellow, Green"]
# elif first_player == 'Blue':
#     player_list = ["Blue, Yellow, Green, Red"]
# yellow = player_list[0]
# green = player_list[1]
# red = player_list[2]
# blue = player_list[3]
print('______________________________________________________________________________________')

while not quit:
    dice_value = random.randint(1, 2)
    dice_value2 = random.randint(2, 2)
    print(f'You rolled a {dice_value} and a {dice_value2}')
    if dice_value == dice_value2:
        doubles = doubles + 1
        print("Doubles:" + str(doubles))
        if dice_value + dice_value2 == 2:
            print('$NAKE EYES, Move 14 and Roll Again')
            print('')
            input('Enter to Roll Again: ')
            print('____________________________________________________')
        elif doubles == 3:
            print('')
            print('You rolled 3 doubles! Return your farthest piece back to home!')
            print("Next players turn")
            print('')
            input('Press enter to roll: ')
            print('____________________________________________________')
            doubles = 0
        else:
            print('You Rolled DOUBLES!!! You get another turn!')
            print('')
            input('Press enter to roll again: ')
            print('_____________________________________________________')
    else:
        quit = input('Next player, Press enter to roll again')
        print('_________________________________________________________')
        doubles = 0

