with open("life-expectancy.csv") as life_file:
    next(life_file)

    data_set = []
    life_expectancy_sum = 0
    life_expectancy_length = 0
    year_user = int(input('Enter the year of interest: '))

    max_overall_life = 0
    max_overall_country = ""
    max_overall_year = 0
    min_overall_life = 150
    min_overall_country = ""
    min_overall_year = 3000
    
    for line in life_file:
        clean_line = line.strip()
        data_set.append(clean_line.split(','))

    for item in data_set:
        country = item[0] 
        year = int(item[2])
        years_expected = float(item[3])

        if years_expected > max_overall_life:
            max_overall_life = years_expected
            max_overall_country = country
            max_overall_year = year

        if years_expected < min_overall_life:
            min_overall_life = years_expected
            min_overall_country = country
            min_overall_year = year
        
        if year == year_user:
            life_expectancy_length += 1
            life_expectancy_sum += years_expected
    

    average_life = life_expectancy_sum / life_expectancy_length

    print('')
    print(f'The overall max life expectancy is: {max_overall_life} from {max_overall_country} in {max_overall_year}')
    print(f'The overall min life expectancy is: {min_overall_life} from {min_overall_country} in {min_overall_year}')

    print('')
    print(f'For the year {year_user}')
    print(f'The average life expectancy across all countries was {average_life:.2f}')