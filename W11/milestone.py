with open("life-expectancy.csv") as life_file:
    next(life_file)
    
    life_list = []
    
    for line in life_file:
        life_list.append(line.split(',')[3])

    print(max(life_list))
    print(min(life_list))


