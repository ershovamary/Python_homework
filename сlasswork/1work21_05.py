## Classwork from 21 May 2018
## Допиливаем старое: comprehensions и форматирование строк
## Считывает файл, разбивает на слова, на выходе массив слов в нижнем регистре,
## распечатать в столбик с выравниванием справа с номером

import re
import clearer

def make_superrr_list(x):
    b = ['r' for _ in range(x)]
    return ''.join(b)

def only_latin_symbols(a):
    b = [s for s in a if re.search(r'^[A-Za-z]+$',s)]
    return b

def str_formatting():
    a = ['1','100','28']
    t = 'Age: {:+>10}'
    return t.format(a[1])

def pum(filename):
    l = clearer.clearer(filename)
    i = 1
    final_text = ''
    for word in l:
        t = str(i) + '.{:>30}\n'
        i += 1
        final_text += t.format(word)
    return final_text

def main():
##    print(make_super_list(int(input())))
##    print(only_latin_symbols(['Anna','Vjcrdf','Москва']))
##    print(str_formatting())
    print(pum('Mexican-American war.txt'))

if __name__=="__main__":
    main()
