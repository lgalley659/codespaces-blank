



def payCheckFilter(payRate, hours, daysWorked):
    checkingAcount = 0
    retirementAcount = 0
    savingsAcount = 0

    paycheck = payRate * hours * daysWorked

    print('My pay check for working' + str(daysWorked) + ' day(s) will be $' + str(paycheck))

    print('Savings Acount balance: $' + str(savingsAcount))
    print('Retirement Acount balance: $' + str(retirementAcount))
    print('Checking Acount balance: $' + str(checkingAcount))

payCheckFilter(45.00, 8, 5)

savingsAcount += paycheck * 0.25
print('My savings account will increase by $' + str(paycheck * 0.25))
    
