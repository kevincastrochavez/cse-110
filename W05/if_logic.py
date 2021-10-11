firstNum = int(input('What is the first number? :'))
secondNum = int(input('What is the second number? :'))

if firstNum > secondNum:
    print('The first number is greater')
elif firstNum == secondNum:
    print('The numbers are equal')
else:
    print('The second number is greater')



favoriteAnimal = input('What is your favorite animal? ').lower()
print(favoriteAnimal)
if favoriteAnimal == 'quetzal':
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")

