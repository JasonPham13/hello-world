print('Quiz Program!')

answer = input('What is the capital of Wisconsin? ')
if answer == 'Madison':
    print('Correct!')
else:
    print('Sorry the answer is Madison')

if answer != 'Madison':
    print('The answer is Madison')
else:
    print('Correct!')


student = int(input('How many credits do you have: '))
while student < 0:
    print('Error - Please enter 0 or positive number. ')
    student = int(input("Enter the number of credits you are taking this semester? "))
if student >= 12:
    print('Full time student!')
elif student >= 6:
    print('Half time student')
else:
    print('Less than half time student')

quiz_score = float(input('Please enter the quiz score, out of 100: '))
if quiz_score >= 90:
    print('Your letter grade is a A')
elif quiz_score >= 80:
    print('Your letter score is a B')
elif quiz_score >= 70:
    print('Your letter score is a C')
elif quiz_score >= 60:
    print('Your letter score is a D')
else:
    print('F, You have failed the test')

star_id = input('Please enter your StarID: ')
while len(star_id) !=8:
    print('Error - a valid StarID has 8 characters. ')
    star_id = input('Please enter your StarID: ')
print(f'Thank you, your StarID is {star_id}')
if len(star_id) == 8:
    print('Your StarID is the correct length.')
elif len(star_id) >= 8:
    print('Your StarID is too long')
else:
    print('Your StarID is too short')




Money = float(input('How many pennies do you have: '))
if Money == 100:
    print('You have exactly one dollar')
elif Money > 100:
    print('You have more than one dollar')
else:
    print('You have less than one dollar')

state = str(input('What state would you like to be senator of: '))
age = int(input('How old are you: '))
citizen = float(input('How long have you been a citizen of the United States: '))
lived = str(input('What state do you live in: '))

if state == lived and age >= 30 and citizen >= 9:
    print('You are now eligible for senator of ' + state)
else:
    print('You are ineligible for senator of ' + state)











