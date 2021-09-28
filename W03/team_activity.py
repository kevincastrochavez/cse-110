import math

square = float(input('What is the length of a side of the square?: '))
square_area = square * square
print(f'The area of the square is: {square_area:.2f}')

rectangle_length = float(input('What is the length of rectangle?: '))
rectangle_width = float(input('What is the width of the rectangle?: '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {rectangle_area:.2f}')

circle = float(input('What is the radius of the circle?: '))
circle_area = circle ** 2 * math.pi
print(f'The area of the circle is: {circle_area:.2f}')