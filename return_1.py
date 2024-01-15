# def stuff(a,b):
#     return a - b
#     return a + b


# c= stuff(3,4)
# print(c+2)

def pangram(word):
    alphabet = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    letterchecker = 0
    length = len(word)
    for i in range(length):
         indexword = 0
         indexalphabet = 0
         for i in range(26):
           if word[indexword] == alphabet[indexalphabet]:
             letterchecker = letterchecker +1
           else:
             letterchecker = letterchecker + 0
         indexword = indexword+1
         indexalphabet = indexalphabet +1
    if letterchecker == 26:
        return "true"
    else:
        return "false"


print(pangram("the quick brown fox jumps over the lazy dog"))

