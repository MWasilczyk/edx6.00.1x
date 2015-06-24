'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a 
new tuple as output, where every other element of the input tuple is copied, 
starting with the first one. So if test is the tuple 
('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would 
return the tuple ('I', 'a', 'tuple').
'''

t = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    if len(aTup) == 0:
        return aTup
    x = (aTup[0],)
    for i in range(1,len(aTup)):
        if i % 2 == 0:
            x += (aTup[i],)
    return x

print oddTuples(t)