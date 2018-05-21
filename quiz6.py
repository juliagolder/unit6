#juliagolder
#5/21/18
#quiz5.py

"""
file = open('engmix.txt')

letter = input('What letter would you like to search for?')

for line in file:
    word = line.strip()
    number = word.count(letter)
    if number == 4:
        print(word)
"""

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if line[0]==line[4]==line[8]:
        print(line)


