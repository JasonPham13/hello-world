# name = input('What is your name : ')
# school = 'Higley High School'
# years = int(input("How many years have you been with " + school + ': '))
# print(name + ' has been at Higley High School for ' + str(years) + ' years.')

rides = float(input('How many times have you rode the bus this month : '))
cost = float(input('What is the cost of a bus ride : '))
res2 = "{:.2f}".format(cost)
total = (rides) * (cost)
res = "{:.2f}".format(total)
print('You have riden the bus ' + str(rides) + ' times. ' + 'The cost of the bus ride is $' + str(res2) + '.' + ' Your total cost will be $' + str(res))
