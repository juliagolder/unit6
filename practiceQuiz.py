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

letter = 't'

for line in file:
    line = line.strip()
    if line[0] == letter and line[4] == letter and line[8] == letter:
        print(line)

"""
file = open('engmix.txt')

letter = input('What letter would you like to search for?')
number = int(input('How long do you want your word to be?'))

for line in file:
    if len(line) == number and line[0]==letter:
        print(line)


file = open('engmix.txt')




for line in file:
    line = line.strip()
    if len(line)==number and line[0]==letter:
        print(line)


file = open('engmix.txt')

many = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in file:
    many[len(line)] += 1
print(many)


file = open('engmix.txt')

number = 8000

L = []

for line in file:
    if
    L.append(line.strip())

print(L[number-1])

"""
