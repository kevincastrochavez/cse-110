name = input('Type the name of a friend: ').lower()

friends = []

while name != 'end':
    friends.append(name)
    name = input('Type the name of a friend: ').lower()

print(friends)