#juliagolder
#5/18/18
#practiceQuiz.py

#1 find all word in dic. that have exactly 3 c's and 2 p's
file = open('engmix.txt')

for line in file:
    word = line.strip()
    Clet = word.count('c')
    Plet = word.count('p') #maybe need int
    if Clet == 3 and Plet == 2:
        print(word)
    
    

#2 - how many words start with the letter r. and aware of blank line in dictionary
file = open('engmix.txt')

numWords = 0
for line in file:
    if len(line) > 0 and line[0]=='r':
        numWords += 1
    
print(numWords)

