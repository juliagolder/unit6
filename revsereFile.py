#juliagolder
#5/16/18
#reverseFile.py

THEfile = input('What file would you like to reverse?')

file = open('THEfile')

L = []

for line in file:
    L.append(line.reverse())

print(L[number-1])
