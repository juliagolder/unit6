#juliagolder
#5/14/18
#hw1.py

file = open('engmix.txt')

word = input("Enter the word you're looking for: ")

numWords = 0
for line in file:
    if word in line:
        print(line.strip('This word is in the dictionary'))
    else:
        print('This is not in the dictionary')
    numWords += 1

print