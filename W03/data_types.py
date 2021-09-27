age = int(input('How old are you?: '))
print(f'On your next birthday, you will be {age + 1}')

egg_cartoons = int(input('How many egg cartons do you have?: '))
eggs = egg_cartoons * 12
print(f'You have {eggs} eggs')

cookies = int(input('How many cookies do you have?: '))
people = int(input('How many people are there?: '))
number_of_cookies = cookies / people
print(f'Each person may have {number_of_cookies:.2f} cookies')