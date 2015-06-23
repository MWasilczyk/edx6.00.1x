'''
Write a function recurPower(base, exp) which computes baseexp by recursively 
calling itself to solve a smaller version of the same problem, and then 
multiplying the result by base to solve the initial problem.
'''

x = 3
y = 5

print x ** y
print x*(x**(y-1))

def recurPower(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base * recurPower(base, exp - 1)

print recurPower(x,y)

print recurPower(5,1)

print recurPower(5,0)