#Бонус 4: программа переделывает слово или фразу так,
#чтобы после каждой согласной добавлялось 'aig'

def check_if_cons(s):
    consonants = 'qwrtpsdfghjklzxcvbnm'
    if s in consonants:
        return True
    else:
        return False

def main():
    s = input('Введите слово или фразу латиницей. ')
    if s != '':
        l = s.split()
        paigy = ''
        for i in l:
            for j in i:
                paigy += j
                if check_if_cons(j):
                    paigy += 'aig'
            paigy += ' '
    else:
        return 'Не введены слово или фраза.'
    return paigy

if __name__ == "__main__":
    print(main())
