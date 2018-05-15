#juliagolder
#5/14/18
#hw4.py

file = open('engmix.txt')

letter = input('What letter are you looking for?')

most = 0
LETTERword = ''

for item in file:
    if most < (item.count(letter)):
        most = (item.count(letter))
        LETTERword = item

print(LETTERword)