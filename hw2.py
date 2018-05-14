#julia golder
#5/14/18
#hw2.py

file = open('engmix.txt')

number = int(input('What number word would you like to search for?'))

L = []

for line in file:
    L.append(line.strip())

print(L[number-1])
