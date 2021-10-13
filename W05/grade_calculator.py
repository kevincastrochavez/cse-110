grade_percentage = int(input('Enter your grade percentage: '))

if grade_percentage >= 90:
    grade = 'A'
elif grade_percentage >= 80:
    grade = 'B'
elif grade_percentage >= 70:
    grade = 'C'
elif grade_percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

if grade_percentage >= 70:
    result = 'passed'
else:
    result = 'did not pass'

string = str(grade_percentage)[-1]

if string >= '7':
    if grade == 'A' or grade == 'F':
        sign = ''
    else:
        sign = '+'
elif string < '3':
    if grade == 'F':
        sign = ''
    else:
        sign = '-'
else:
    sign = ''

print(f'Your grade is {grade}{sign}')
print(f'You {result} the class')