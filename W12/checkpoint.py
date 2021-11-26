people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 100
youngest_name = ''

for item in people:
    list_line = item.split(' ')

    name = list_line[0]
    age = int(list_line[1]) 

    if age < youngest_age:
        youngest_name = name
        youngest_age = age

print(f'The youngest person is {youngest_name} with {youngest_age} years old')