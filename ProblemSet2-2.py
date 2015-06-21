# Write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months.

balance = 3926
annualInterestRate = 0.2
monthly_payment = 0
step = 10

month = 1
current_balance = balance

#x = balance, y = monthly payment, z = annualInterestRate
def newmonth(x,y,z):
    m = 1
    while m <= 12:
        x -= y
        x += z/12.0*x
        m += 1
    return x

while newmonth(balance,monthly_payment,annualInterestRate) > 0:
    monthly_payment += step
    
print 'Lowest Payment: %r' % monthly_payment