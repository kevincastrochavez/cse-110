from functools import reduce

bank_accounts = []
balances = []

print('Enter the names and balances of bank accounts (type: quit when done)')

account = None

while account != 'quit':
    account = input('What is the name of this account? ')
    
    if account != 'quit':
        balance = float(input('What is the balance? '))
        bank_accounts.append(account)
        balances.append(balance)

print('')
print('Account Information:')
for item in range(0, len(bank_accounts)):
    print(f'{bank_accounts[item]} - ${balances[item]}')

total = reduce(lambda a,b: a + b, balances)
average = total / len(balances)
print('')
print(f'Total: ${total}')
print(f'Average" ${average:.2f}')