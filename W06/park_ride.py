age_rider1 = int(input('What is the age of the first rider?: '))
height_rider1 = int(input('What is the height of the first rider in inches?: '))
second_rider = input('Is there a second rider?: (Yes/No) ')

second_rider_formatted = second_rider.strip().lower()

if second_rider_formatted == 'yes':
    age_rider2 = int(input('What is the age of the second rider in?: '))
    height_rider2 = int(input('What is the height of the second rider in inches?: '))

    if height_rider1 < 36 or height_rider2 < 36:
        msg = 'Sorry, you may not ride'
    else:
        if age_rider1 >= 18 or age_rider2 >= 18:
            msg = 'Welcome to the ride. Please be safe and have fun!'
        else:
            msg = 'Sorry, you may not ride'
else:
    if age_rider1 >= 18 and height_rider1 >= 62:
        msg = 'Welcome to the ride. Please be safe and have fun!'
    else:
        msg = 'Sorry, you may not ride'

print(msg)