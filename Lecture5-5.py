'''
The greatest common divisor of two positive integers is the largest integer that 
divides each of them without remainder. A clever mathematical trick (due to 
Euclid) makes it easy to find greatest common divisors.Write a function 
gcdRecur(a, b) that implements this idea recursively. This function takes in two 
positive integers and returns one integer. 
'''

def gcdRecur(a,b):
    if b == 0:
        return a
    return gcdRecur(b,a%b)

print gcdRecur(2,12)
print gcdRecur(6,12)
print gcdRecur(9,12)
print gcdRecur(17,12)