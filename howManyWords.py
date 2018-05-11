#juliagolder
#5/10/18
#howManyWords.py

file = open('engmix.txt')

many = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in file:
    many[len(line)] += 1
print(many)


for i in range(1,23):
    print(i,'- letter words: ', many[i-1])