print('Welcome to the Shopping Cart Program!')

def options():
    print('')
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print('')

items = []

options()
action = int(input('Please enter an action: '))

if action == 1:
    new_item = input('What item would you like to add?: ')
    items.append(new_item)
    print(f"'{new_item}' has been added to the cart")
    options()
    action = int(input('Please enter an action: '))
