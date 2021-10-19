loan = int(input('How large is the loan?: '))
credit = int(input('How good is your credit history?: '))
income = int(input('How high is your income?: '))
payment = int(input('How large is your down payment?: '))
decision = False

if loan >= 5:
    if credit >= 7 and income >= 7:
        decision = True
    if credit >= 7 or income >= 7:
        if payment >= 5:
            decision = True
        else:
            decision = False
    else:
        decision = False
else:
    if credit < 4:
        decision = False
    else:
        if income >= 7 or payment >= 7:
            decision = True
        elif income >=4 and payment >= 4:
            decision = True
        else:
            decision = False

if decision == True:
    print('You were approved for the loan!')
else:
    print('You were not approved. Try again another time')