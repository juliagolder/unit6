#juliagolder
#5/18/18
#practiceQuiz.py

#1 find all word in dic. that have exactly 3 c's and 2 p's

#2 - how many words start with the letter r. and aware of blank line in dictionary
file = open('engmix.txt')

numWords = 0
for line in file:
    if len(line) > 0 and line[0]=='r':
        numWords += 1
    
print(numWords)