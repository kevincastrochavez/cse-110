number = int(input('How many columns and rows do you want in your multiplication table? '))

for i in range(1, number + 1):
    for j in range(1, number + 1):
        result = i * j

        print(result, end=' ')
    print('')