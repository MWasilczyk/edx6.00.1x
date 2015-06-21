#Write a program that prints the number of times the string 'bob' occurs in s.

s = 'bobobobobobobobobobobobob'
num_bob = 0

for position in range(len(s)-2):
    if s[position] == 'b' and s[position + 1] == 'o' and s[position + 2] == 'b':
        num_bob += 1
        
print "Number of times bob occurs is: %r" % num_bob