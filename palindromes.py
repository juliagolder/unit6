#juliagolder
#5/17/18
#palindromes.py

file = open('engmix.txt')

for line in file:
    line = line.strip()

    back = ''

    for ch in line:
        back = ch+back

    if back == line:
        print(back)