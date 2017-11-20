##classwork from 14 November


vowels = 'уеыаоэяиюё'
consonants = 'йцкнгшщзхфвпрлджчсмтб'
n = 0
m = 0
with open("C:/Study/Python/Useful files/classwork14_11.txt", "r", encoding="utf-8") as f:
    s = f.read()
sent = s.split('.')
for v in vowels:
    for i in sent:
        n += i.count(v)
for c in consonants:
    for i in sent:
        m += i.count(c)
print('This file contains ' + str(n) + ' vowels and ' + str(m) + ' consonants')
