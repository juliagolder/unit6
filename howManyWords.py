#juliagolder
#5/10/18
#howManyWords.py

file = open('engmix.txt')

many = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in file:
    many[len(line)] += 1
print(many)


for item in many:
    print([0]+=1'-letter words: ', many)