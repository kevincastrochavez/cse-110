import random

keep_playing = "yes"

while keep_playing == "yes":
    magic_number = random.randint(1, 100)
    count_guesses = 0
    guess_number = -1

    while magic_number != guess_number:
        guess_number = int(input('What is your guess?: '))
        count_guesses += 1

        if magic_number > guess_number:
            print('Higher')
        elif magic_number < guess_number:
            print('Lower')
        else:
            print('You guessed it!')
    
    print(f'You guessed the number after {count_guesses} tries')

    keep_playing = input('Want to play again (yes/no)?: ').lower()

print('Thanks for playing')