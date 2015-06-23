# Write a program that counts up the number of vowels contained in the string s.

s = 'a slightly different type of string'
'''
vowels = 'aeiouAEIOU'
num_vowels = 0

for letter in s:
    if letter in vowels:
        num_vowels += 1



print "Number of vowels: %r" % num_vowels
'''
print sum(1 for x in s if x in 'aeiouAEIOU')
