#juliagolder
#5/14/18
#hw1.py

file = open('engmix.txt')

word = input("Enter the word you're looking for: ")

present = False

for line in file:
    if word in line.strip():
        print('This word is in the dictionary')
        present = True
if present == False:
    print('This is not in the dictionary')
    