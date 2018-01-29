#Бонус 3: программа переделывает слово или фразу так,
#чтобы начальная согласая или кластер согласных переносились в конец слова,
#а следом следовало окончание 'ay'
def check_vow_place(s):
    vowels = 'euioa'
    for i in s:
        if i in vowels:
            return s.index(i)

def main():
    s = input('Введите слово или фразу латиницей. ' )
    if s != '':
        l = s.split()
        piggy = ''
        for i in l:
            piggy += i[check_vow_place(i):] + i[:(check_vow_place(i))] + 'ay '
    else:
        return 'Не введены слово или фраза.'
    return piggy

if __name__ == "__main__":
    print(main())
