'''
A semordnilap is a word or a phrase that spells a different word when backwards 
("semordnilap" is a semordnilap of "palindromes"). Write a recursive program, 
semordnilap, that takes in two words and says if they are semordnilap.
'''

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    def semordnilap(str1,str2):
        if len(str1) == 0 or len(str2) == 0:
            return False
        if str1[0] == str2[-1] and len(str1) == 1 and len(str2) == 1:
            return True
        return semordnilap(str1[1:len(str1)],str2[0:len(str2)-1])

    return semordnilap(str1, str2)


print semordnilapWrapper('a','a')
print semordnilapWrapper('abc','abc')
print semordnilapWrapper('abc','cba')
print semordnilapWrapper('fasdj','kksdzz')
print semordnilapWrapper('abc','dcba')