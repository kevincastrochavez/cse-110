child_meal = float(input("What is the price of a child's meal?: "))
adult_meal = float(input("What is the price of an adult's meal?: "))
children = int(input("How many children are there?: "))
adults = int(input("How many adults are there?: "))
tax_rate = float(input("What is the sales tax rate?: "))

children_total = child_meal * children
adults_total = adult_meal * adults

subtotal = children_total + adults_total
tax = subtotal * tax_rate * 0.01 
tip = 0

print('')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${tax:.2f}')
print('')

response = input('Would you like to add a tip? (Yes/No): ').lower().strip()
if response == 'yes':
    tip = int(input('Type the percentage of your tip (10, 15, 20): '))

tip_amount = (subtotal + tax) * tip * 0.01

total = subtotal + tax + tip_amount
print('')
print(f'Total: ${total:.2f}')
print('')

payment = float(input('What is the payment amount?: '))

change = payment - total 

print(f'Change: ${change:.2f}')
