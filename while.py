# while True:
#   print('Hello!')
# import random
# want_to_quit = ''
# while not want_to_quit:
#     dice_value = random.randint(1, 6)
#     print(f'You rolled a {dice_value}')
#     want_to_quit = input('Press enter to roll again, any other key to quit')
# weather = 'snow'
# temperature = 29.5
# day_of_month = 20
# print(f'On January {day_of_month}, the temperature is {temperature} and the current weather is {weather}.')

# for number in range(100):
#     print(number)

# print('Here are the numbers 4 to 8')
# for number in range(100, 201):
#     print(number)

# import random
# number_of_dice = int(input('How many dice to roll? '))
# print(f'You are about to roll {number_of_dice} dice...')
# for dice in range(number_of_dice):
#     dice_value = random.randint(1, 6)
#     print(f'Dice {dice + 1} value is {dice_value}')
#
# name = 'Jason'
# for letter in name:
#     print(letter)

# square_size = 10
# square_character = '*'
#
# for y in range(square_size):
#     line = ''
#     for x in range(square_size):
#         line = line + square_character
#     print(line)

name = 'Jason'
# for letter in name:
#     print(letter)

# for letter in name:
#     print(letter)
#
# for letter in range(4):
#     print(name)

# name = 'Jason'
# name_builder = ''
#
# for letter in name:
#     print(name_builder + letter)
#     name_builder = name_builder + letter

# name = input('Whats your name: ')
# namecount = len(name)
# for letter in name:
#     line = ''
#     for i in range(namecount - len(name)-1):
#         line = line + letter
#
#     print(line)
#     count = count + 1

name = "JASON"
count = 1
for letter in name:
    line = ''
    for i in range(count):
        line = line + letter
    print(line)
    count = count + 1
