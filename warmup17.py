#juliagolder
#5/17/18
#warmup17.py

file = open('engmix.txt')

for line in file:
    if 'g' in line and 'o' in line and 'l'  in line and 'd' in line and 'e' in line and 'r' in line:
        print(line.strip())
