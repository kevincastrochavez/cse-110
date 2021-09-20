name = input('Pleasy type your first and last name: ')
color = input('Please type your favorite color: ')

lower_name = name.lower()
first_name = lower_name.split()[0].capitalize()
second_name = lower_name.split()[1].capitalize()

print(f'Your name is {first_name} {second_name}')
print(f'Your favorite color is {color.lower()}.')