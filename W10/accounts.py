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
    print(f'{item}. {bank_accounts[item]} - ${balances[item]}')

total = reduce(lambda a,b: a + b, balances)
average = total / len(balances)
highest_balance = max(balances)

print('')
print(f'Total: ${total}')
print(f'Average" ${average:.2f}')
print(f'Highest balance: savings - ${highest_balance}')

update_account = 'yes'

while update_account == 'yes':
    print('')
    update_account = input('Do you want to update an account? ')
    
    if update_account == 'yes':
        account_to_update = int(input('What account index do you want to update? '))
        new_amount = input('What is the new amount? ')

        balances[account_to_update] = new_amount

    print('')
    print('Account Information:')
    for item in range(0, len(bank_accounts)):
        print(f'{item}. {bank_accounts[item]} - ${balances[item]}')