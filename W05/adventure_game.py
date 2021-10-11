first_scenario = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?: ').lower().strip()

if first_scenario == 'match':
    second_scenario = input('Scenario 2, Option 1: ').lower().strip()
    if second_scenario == 'option 1':
        third_scenario = input('Scenario 3, Option 1: ').lower().strip()
        if third_scenario == 'option 1':
            print('1, 1, 1')
        elif third_scenario == 'option 2':
            print('1, 1, 2')
        else:
            print('Please choose one of the provided options')
    elif second_scenario == 'option 2':
        third_scenario = input('Scenario 3, Option 1: ').lower().strip()
        if third_scenario == 'option 1':
            print('1, 2, 1')
        elif third_scenario == 'option 2':
            print('1, 2, 2')
        else:
            print('Please choose one of the provided options')
    elif second_scenario == 'option 3':
        third_scenario = input('Scenario 3, Option 1: ').lower().strip()
        if third_scenario == 'option 1':
            print('1, 3, 1')
        elif third_scenario == 'option 2':
            print('1, 3, 2')
        else:
            print('Please choose one of the provided options')
    else:
        print('Please choose one of the provided options')

elif first_scenario == 'flashlight':
    second_scenario = input('Scenario 2, Option 2: ')
    if second_scenario == 'option 1':
        third_scenario = input('Scenario 3, Option 2: ').lower().strip()
        if third_scenario == 'option 1':
            print('2, 1, 1')
        elif third_scenario == 'option 2':
            print('2, 1, 2')
        else:
            print('Please choose one of the provided options')
    elif second_scenario == 'option 2':
        third_scenario = input('Scenario 3, Option 2: ').lower().strip()
        if third_scenario == 'option 1':
            print('2, 2, 1')
        elif third_scenario == 'option 2':
            print('2, 2, 2')
        else:
            print('Please choose one of the provided options')
    elif second_scenario == 'option 3':
        third_scenario = input('Scenario 3, Option 2: ').lower().strip()
        if third_scenario == 'option 1':
            print('2, 3, 1')
        elif third_scenario == 'option 2':
            print('2, 3, 2')
        else:
            print('Please choose one of the provided options')
    else:
        print('Please choose one of the provided options')
else:
    print('Please choose one of the provided options')