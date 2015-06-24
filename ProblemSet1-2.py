#Write a program that prints the number of times the string 'bob' occurs in s.

s = 'bobobobobobobobobobobobob'

def bobCount(x):
    if len(x) < 3:
        return 0
    if x[0:3] == 'bob':
        return 1 + bobCount(x[1:len(x)])
    else:
        return 0 + bobCount(x[1:len(x)])

print "Number of times bob occurs is: %r" % bobCount(s)
