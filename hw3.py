#julia golder
#5/14/18
#hw3.py

file = open('hw2.py')

for line in file:
    many[len(line)] += 1
print(many)


for i in range(1,24):
    print(i,'- letter words: ', many[i-1])