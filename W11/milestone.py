with open("life-expectancy.csv") as life_file:
    next(life_file)

    data_set = []
    year_user = int(input('Enter the year of interest: '))
    print('')
    
    for line in life_file:
        clean_line = line.strip()
        data_set.append(clean_line.split(','))

    max_overall_life = 0
    max_overall_country = ""
    max_overall_year = 0
    min_overall_life = 150
    min_overall_country = ""
    min_overall_year = 3000

    for item in data_set:
        country = item[0] 
        year = item[2]
        years_expected = float(item[3])

        if years_expected > max_overall_life:
            max_overall_life = years_expected
            max_overall_country = country
            max_overall_year = year

        if years_expected < min_overall_life:
            min_overall_life = years_expected
            min_overall_country = country
            min_overall_year = year

    print(f'The overall max life expectancy is: {max_overall_life} from {max_overall_country} in {max_overall_year}')
    print(f'The overall min life expectancy is: {min_overall_life} from {min_overall_country} in {min_overall_year}')
    
    # for list in data_set:
    #     life_time = list[3]
    #     country = list[0]

    #     if int(list[2]) == year:

# max_price = -1
# max_product = "" # It doesn't matter what you set this to, it just needs to be declared

# for item in shopping_cart:
#     product_name = item[0] # Product name is the first part
#     price = item[1] 

#     if price > max_price:
#         # This is the new max
#         max_price = price

#         # Also save this product name as the max product
#         max_product = product_name