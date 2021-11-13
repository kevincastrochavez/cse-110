items = []

print('Please enter the items of the shopping list (type: quit to finish): ')
item = input('Item: ')

while item != 'quit':
    items.append(item)
    item = input('Item: ')

print('')
print('The shopping list is:')
for item in items:
    print(item)

print('')
print('The shopping list with indexes is:')
for i in range(0, len(items)):
    print(f'{i}. {items[i]}')

print('')
new_position = int(input('Which item would you like to change?'))
new_item = input('What is the new item?: ')

items[new_position] = new_item

print('')
print('The shopping list with indexes is:')
for i in range(0, len(items)):
    print(f'{i}. {items[i]}')