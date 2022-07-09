product = input('Enter name of item: ')
product_price = float(input('Enter unit price of ' + product + ': '))
product_quanity = int(input('Enter quanity of ' + product + ' sold: '))

print("")
print(product + ' sales')
print('Quanity sold: ' + str(product_quanity))
print('Unit Price: ' + str(product_price))
total = product_price * product_quanity

print('Total: ' + str(total))

