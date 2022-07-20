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

while True:
    input(f'{player_list[current_player]} Roll Your Dice')

    # This is where you run your dice logic
    current_player = current_player + 1
    if current_player > 3:
        current_player = 0