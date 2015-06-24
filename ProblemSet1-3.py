# Write a program that prints the longest substring of s in which the
# letters occur in alphabetical order. 

s = 'abcbcd'

def longABC(x):
    def alphaString(x):
        if len(x) == 1 or x[0] > x [1]:
            return x[0]
        return x[0] + alphaString(x[1:len(x)])
        
    i = ''
    for c in range(len(x)):
        if len(alphaString(x[c:len(x)]) > len(i):
            i = alphaString(x[c:len(x)])
    
    return i
    
print 'Longest substring in alphabetical order is: %s' % longABC(s)
