# Write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months.

balance = 999999
annualInterestRate = 0.18
monthly_payment = 0
min_dif = 0.01

#x = balance, y = monthly payment, z = annualInterestRate
def newmonth(x,y,z):
    m = 1
    while m <= 12:
        x -= y
        x += z/12.0*x
        m += 1
    return x

min_bound = balance / 12.0
max_bound = newmonth(balance,0,annualInterestRate)

while abs(newmonth(balance,(min_bound + max_bound)/2,annualInterestRate)) > min_dif:
    if newmonth(balance,(min_bound + max_bound)/2,annualInterestRate) < 0:
        max_bound = (min_bound + max_bound)/2
    else:
        min_bound = (min_bound + max_bound)/2
    
print 'Lowest Payment: %r' % round((min_bound + max_bound)/2,2)