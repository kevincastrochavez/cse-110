from functools import reduce

print('')
print('Welcome to the Shopping Cart Program!')

items = []
prices = []

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

    if action == 3:
        option3()

    if action == 4:
        option4()

    return action

def option1():
    new_item = input('What item would you like to add?: ')
    new_price = float(input(f"What is the price of '{new_item}'?: "))
    items.append(new_item)
    prices.append(new_price)
    print(f"'{new_item}' has been added to the cart")

def option2():
    print('')
    print('')
    print('The contents of the shopping cart are:')
    for i in range(0, len(items)):
        print(f'{i + 1}. {items[i]} - ${prices[i]:.2f}')

def option3():
    item_to_be_removed = int(input('Which item would you like to remove? ')) - 1
    prices.pop(item_to_be_removed)
    items.pop(item_to_be_removed)
    print('Item removed')

def option4():
    total = reduce(lambda a, b: a + b, prices)
    print(f'The total price of the items in the shopping cart is ${total}')

option_number = options()

while option_number != 5:
    option_number = options()

print('Thank you. Goodbye')