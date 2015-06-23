'''
Write an iterative function iterPower(base, exp) that calculates the 
exponential baseexp by simply using successive multiplication. For example, 
iterPower(base, exp) should compute baseexp by multiplying base times itself 
exp times. 
'''

base = 15
exp = 0

def iterPower(base,exp):
    if exp == 0:
        return 1
    else:
        a = base
        for z in range(exp-1):
            a *= base
        return a
        
print iterPower(base,exp)