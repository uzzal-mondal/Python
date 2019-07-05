
numOfWords = 0
numOfLetters = 0
numOfDegits = 0

text = input("Enter your text")

for x in text:
    x = x.lower()
    if x>= 'a' and x<='z':
        numOfLetters = numOfLetters+1

    elif x>= '0' and x<'9':
        numOfDegits = numOfDegits+1

    elif x == '':
        numOfWords = numOfWords+1

print("num of words ", numOfWords)
print("num of letters ",numOfLetters)
print("num of digits ",numOfDegits)






"""
n = input("Enter your text ")

#convert to string list 10,20, 30 every num are string.

list = n.split()
sum = 0

for i in list:
    sum = sum+ int(i)
    print(sum)

"""
