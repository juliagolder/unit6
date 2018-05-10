#juliagolder
#5/10/18
#longestDictionaryWord.py

file = open('engmix.txt')

longest = 0
LONGword = ''


for item in file:
    if longest < (len(item)):
        longest = (len(item))
        LONGword = item

print(LONGword)
