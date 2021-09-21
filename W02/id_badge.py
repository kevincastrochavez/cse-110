first_name = input('Please type your first name: ')
last_name = input('Please type your last name: ') 
email_address = input('Please type your email address: ') 
phone_number = input('Please type your phone number: ') 
job_title = input('Please type your job title: ') 
id_number = input('Please type your ID Number: ') 
hair_color = input('Please type your hair color: ') 
eyes_color = input('Please type your eyes color: ') 
month = input('Please type the name of the month you started: ') 
training = input('Have you completed advanced training (Yes/No): ') 

prefixNumber = phone_number[:3]
middleNumber = phone_number[3:6]
finalNumber = phone_number[6:]

formattedNumber = f'({prefixNumber}) {middleNumber}-{finalNumber}'

print('')
print('------------------------------------------------------------')
print(f'{last_name.upper()}, {first_name.lower().capitalize()}')
print(f'{job_title.lower().capitalize()}')
print(f'ID Number: {id_number}')
print('')
print(f'{email_address.lower()}')
print(f'{formattedNumber}')
print('')
print(f'Hair: {hair_color.lower().capitalize()}               Eyes: {eyes_color.lower().capitalize()}')
print(f'Month: {month.lower().capitalize()}               Training: {training.lower().capitalize()}')
print('------------------------------------------------------------')
print('')
