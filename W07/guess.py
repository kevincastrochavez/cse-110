import random

magic_number = random.randint(1, 100)
guess_number = -1

while magic_number != guess_number:
    guess_number = int(input('What is your guess?: '))

    if magic_number > guess_number:
        print('Higher')
    elif magic_number < guess_number:
        print('Lower')
    else:
        print('You guessed it!')