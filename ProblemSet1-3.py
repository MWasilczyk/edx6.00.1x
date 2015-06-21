# Write a program that prints the longest substring of s in which the
# letters occur in alphabetical order. 

s = 'abcbcd'
long_string = ''
iteration = 0


while iteration < len(s):
    current_length = 1
    for spot in range(iteration,len(s)-1):
        if s[spot] > s[spot + 1]:
            break
        else:
            current_length += 1
    if current_length > len(long_string):
        long_string = s[iteration:iteration + current_length]
    iteration += 1
    
print 'Longest substring in alphabetical order is: %s' % long_string