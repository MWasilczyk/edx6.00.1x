'''
The greatest common divisor of two positive integers is the largest integer that 
divides each of them without remainder. Write an iterative function, 
gcdIter(a, b), that implements this idea. 
'''

print 9 % 9 != 0
print 12 % 9 != 0

def gcdIter(a,b):
    x = min(a,b)
    while a % x != 0 or b % x != 0:
        x -= 1
    return x

print gcdIter(2,12)
print gcdIter(6,12)
print gcdIter(9,12)
print gcdIter(17,12)