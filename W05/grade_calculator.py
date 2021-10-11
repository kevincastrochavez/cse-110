grade_percentage = float(input('Enter your grade percentage: '))

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

print(f'Your grade is {grade}')
print(f'You {result} the class')