# Write a program to calculate the credit card balance after one year if a 
# person only pays the minimum monthly payment required by the credit card 
# company each month.

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 1
total_paid = 0

while month <= 12:
    print 'Month: %r' % month
    min_payment = round(balance * monthlyPaymentRate,2)
    total_paid += min_payment
    print 'Minimum monthly payment: %r' % min_payment
    balance -= min_payment
    balance += (annualInterestRate / 12.0 * balance)
    print 'Remaining balance: %r' % round(balance,2)
    month += 1

print 'Total paid: %r' % round(total_paid,2)
print 'Remaining balance: %r' % round(balance,2)