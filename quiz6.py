#juliagolder
#5/21/18
#quiz5.py

file = open('engmix.txt')

letter = input('What letter would you like to search for?')

for line in file:
    word = line.strip()
    number = word.count(letter)
    if number == 4:
        print(word)
