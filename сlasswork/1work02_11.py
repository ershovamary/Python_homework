alph = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
x = input()
L = list(x)
n = ''
for letter in L:
    if letter == ' ':
        a = ' '
    else:
        for i in range(len(alph)):
            if alph[i] == letter:
                a = alph[i+1]
    n = n + a
print(n)
