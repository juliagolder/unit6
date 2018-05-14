#juliagolder
#5/14/18
#hw1.py

file = open('engmix.txt')

word = input('Enter some words: ')

numWords = 0
for line in file:
    if 'julia' in line:
        print(line.strip())
    numWords += 1

print