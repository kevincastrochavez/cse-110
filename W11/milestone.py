with open("life-expectancy.csv") as life_file:
    next(life_file)

    life_expectancy = []
    
    for line in life_file:
        life_expectancy.append(line.split(',')[3])


    print(f'Highest life expectancy: {max(life_expectancy)}')
    print(f'Lowest life expectancy: {min(life_expectancy)}')