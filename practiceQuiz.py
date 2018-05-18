#juliagolder
#5/18/18
#practiceQuiz.py

file = open('engmix.txt')

numWords = 0
for line in file:
    if len(line) > 0 and line[0]=='r':
        numWords += 1
    
print(numWords)