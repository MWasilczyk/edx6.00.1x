# Write a program that counts up the number of vowels contained in the string s.

s = 'a slightly different type of string'

def countVowels(x):
    if len(x) == 0:
        return 0
    if x[0] in 'aeiouAEIOU':
        return 1 + countVowels(x[1:len(x)])
    else:
        return countVowels(x[1:len(x)])
        
print "Number of vowels: %r" % countVowels(s)

