'''
Write an iterative function, lenIter, which computes the length of an input 
argument (a string), by counting up the number of characters in the string.
'''

def lenIter(aStr):
    x = 0
    for c in aStr:
        x += 1
    return x

print lenIter('seven')
print lenIter('eightyfive')