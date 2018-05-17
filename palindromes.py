#juliagolder
#5/17/18
#palindromes.py

file = open('engmix.txt')

back = ''

for ch in file:
    back = ch+back

if back == ch:
    print(back)