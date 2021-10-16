print('')
print('You are standing in a dark room.')
print('There is a door to your left and right')
print('')
first_scenario = input('Which one do you take? (left or right): ').lower().strip()
print('')

if first_scenario == 'left':
    print("There is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating tasty honey!")
    print('')
    second_scenario = input("What would you do? (take the honey, taunt the bear or run): ").lower().strip()
    print('')
    if second_scenario == 'take the honey':
        print('The bear killed you.')
        print('')
        third_scenario = input('Where would you like to go? (Heaven or hell): ').lower().strip()
        print('')
        if third_scenario == 'heaven':
            print("Now you'll have free honey for eternity!")
            print('')
        elif third_scenario == 'hell':
            print('We are very sorry, but that was a bad decision and you deserve it)')
            print('')
        else:
            print("Don't you know how to type something properly?")
            print('')
    elif second_scenario == 'taunt the bear':
        third_scenario = input('Your good time, the bear moved from the door. You can go through it now! What do you do now? (Go in or stay out): ').lower().strip()
        print('')
        if third_scenario == 'go in':
            print('You passed you CSE 110 class!')
            print('')
        elif third_scenario == 'stay out':
            print('Poor decision. The bear killed you.')
            print('')
        else:
            print("Don't you know how to type something properly?")
            print('')
    elif second_scenario == 'run':
        third_scenario = input('The bear is now following you and you are running away for your life. What do you do now? (Fight the bear or drop candies): ').lower().strip()
        print('')
        if third_scenario == 'fight the bear':
            print('Poor decision. The bear killed you.')
            print('')
        elif third_scenario == 'drop candies':
            print('Smart decision! You will live to tell this story to your children')
            print('')
        else:
            print("Don't you know how to type something properly?")
    else:
        print("Don't you know how to type something properly?")

elif first_scenario == 'right':
    print("Now you entered the room of a monster!")
    print("The monster is sleeping.")
    print('')
    second_scenario = input('Behind the monster, there is another door. What would you do? (Go slilently, kill him or feed him): ')
    print('')
    if second_scenario == 'go silently':
        print('Lucky you!')
        print("You are now in a room filled with diamonds!")
        print('')
        third_scenario = input('What would you do? (Take some or leave them): ').lower().strip()
        print('')
        if third_scenario == 'take some':
            print('The monster killed you. You are a robber')
            print('')
        elif third_scenario == 'leave them':
            print('The monster gave you all the diamons and more treasures because of your honesty!')
            print('')
        else:
            print("Don't you know how to type something properly?") 
    elif second_scenario == 'kill him':
        print('Good try but the monster killed you first')
        print('')
        third_scenario = input('Where would you like to go? (Heaven or hell): ').lower().strip()
        print('')
        if third_scenario == 'heaven':
            print("Now you'll have all the diamonds for eternity!")
            print('')
        elif third_scenario == 'hell':
            print('We are very sorry, but that was a bad decision and you deserve it)')
            print('')
        else:
            print("Don't you know how to type something properly?")
            print('')
    elif second_scenario == 'feed him':
        print('The monster is very happy with you!')
        print('He had not eaten in a while')
        print('')
        third_scenario = input('He offers you the diamonds. What do you do? (Take them or reject them): ').lower().strip()
        print('')
        if third_scenario == 'take them':
            print('Everything is alright. You deserved them')
            print('')
        elif third_scenario == 'reject them':
            print('Wrong decision. You will be poor for the rest of your life')
            print('')
        else:
            print("Don't you know how to type something properly?")
            print('') 
    else:
        print("Don't you know how to type something properly?") 
        print('')
else:
    print("Don't you know how to type something properly?")
    print('')