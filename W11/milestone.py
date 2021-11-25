with open("life-expectancy.csv") as life_file:
    next(life_file)

    # life_list = []
    # countries = []
    # codes = []
    years = []
    indexes = []
    
    for line in life_file:
        # countries.append(line.split(',')[0])
        # codes.append(line.split(',')[1])
        years.append(line.split(',')[2])
        # life_list.append(line.split(',')[3])


    # print(years)
    # print(index)
    # print(years[index])

# index = years.index('2019')
#         print(years[index])
#         # indexes.append(index)