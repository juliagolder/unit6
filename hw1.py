#juliagolder
#5/14/18
#hw1.py

file = open('engmix.txt')

word = input("Enter the word you're looking for: ")

for line in file:
    if word in line:
        print(line.strip('This word is in the dictionary'))
    