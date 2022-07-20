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
player_list = ["Yellow", "Green", "Red", "Blue"]

beginning_player = ''

while beginning_player != 'Yellow' and beginning_player != 'Green' and beginning_player != 'Red' and beginning_player != 'Blue':
    beginning_player = input('Who is starting first? ')

current_player = int()

if beginning_player == 'Yellow':
    current_player = 0
elif beginning_player == 'Green':
    current_player = 1
elif beginning_player == 'Red':
    current_player = 2
elif beginning_player == 'Blue':
    current_player = 3


quits = ''
doubles = 0
snake_eyes = 0
underline = '_________________________________________________________'

print(underline)

print(f'Player {player_list[current_player]} is up! ')
while not quits:
    input('Enter to Roll: ')
    print('_________________________________________________________')
    dice_value: int = random.randint(1, 6)
    dice_value2 = random.randint(1, 6)
    print(f'You rolled a [{dice_value}] and a [{dice_value2}]')

    if dice_value == dice_value2:
        doubles = doubles + 1
        if dice_value + dice_value2 != 2:
            snake_eyes = 0
    else:
        current_player = current_player + 1
        if current_player > 3:
            current_player = 0
        print(underline)
        print('')
        print(f"**** {player_list[current_player]}, you're up! **** ")
        doubles = 0

    if dice_value + dice_value2 == 2:
        snake_eyes = snake_eyes + 1
        print('$NAKE EYES: [' + str(snake_eyes) + '] Move 14')
        print('')


    if doubles >= 1 and doubles < 3:
        print("Doubles:" + str(doubles))
        print('You Rolled DOUBLES!!! You get another turn!')
        print('')

    if snake_eyes == 3:
        print('YOU ROLLED 3 SNAKE EYES GAME IS OVER YOU WIN!!!')
        quit('GAME OVER!')

    if doubles == 3 and snake_eyes >= 1:
            print('Please Move Farthest Player Home, But Still Roll For Win')
    elif doubles == 3:
        print('')
        print('You rolled 3 doubles! Return your farthest piece back to home!')
        print("Next players turn")
        print('')
        doubles = 0


    #
    #
    #


