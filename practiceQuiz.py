#juliagolder
#5/18/18
#practiceQuiz.py

file = open('engmix.txt')



for line in file:
    line = line.strip()
    if line[0]=='r' in line:
        print(line)