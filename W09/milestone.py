print('')
print('Welcome to the Shopping Cart Program!')

items = []

def options():
    print('')
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print('')

    action = int(input('Please enter an action: '))

    if action == 1:
        option1()

    if action == 2:
        option2()

    return action

def option1():
    new_item = input('What item would you like to add?: ')
    items.append(new_item)
    print(f"'{new_item}' has been added to the cart")

def option2():
    print('')
    print('')
    print('The contents of the shopping cart are:')
    for item in items:
        print(item)

option_number = options()

while option_number != 5:
    option_number = options()

print('Thank you. Goodbye')