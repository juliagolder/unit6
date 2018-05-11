#juliagolder
#5/11/18
#warmup16.py

file = open('engmix.txt')


for line in file:
    line = line.strip()
    if len(line) > 0 and line[0]=='j' and line[-1]=='g':
        print(line)