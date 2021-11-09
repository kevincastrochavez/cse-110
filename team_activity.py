print('Enter a list of numbers, type 0 when finished. ')

numbers = []

number = int(input('Enter number: '))

while number != 0:
    numbers.append(number)
    number = int(input('Enter number: '))

sum = 0

for number in numbers:
    sum += number

print(f'The sum is {sum}')
print(f'the average is {sum / len(numbers)}')
print(f'The largest number is: {max(numbers)}')