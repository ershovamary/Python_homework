## Classwork from 28 May 2018
## Способы устранения ошибок: n-граммы
## Текст отклиарить, составить и записать в tsv-файл
## словарь n-грамм, где n задаётся пользователем

import clearer
import re

def make_n_gram_dictionary(a, n):
    d = {}
    for i, v in enumerate(a):
        if (i + n) == len(a):
            break
        else:
            engramma = ''
            for j in range(n):
                engramma += a[i+j] + ' '
            if engramma in d:
                d[engramma] += 1
            else:
                d[engramma] = 1
    return d

def sort_and_write_d(d):
    with open('n-gramms.tsv',"w",encoding="utf-8") as f:
        for word in sorted(d,key = d.get, reverse = True):
            if d[word] != 1:
                f.write(word + '\t' + str(d[word]) + '\n')
    

def main():
    filename = 'chekhov.txt'
    n = input('This programme returns n-grams in text ' + filename + '. Write n to continue. ')
    if n.isdigit():
        n = int(n)
        words = clearer.clearer(filename)
        d = make_n_gram_dictionary(words, n)
        sort_and_write_d(d)

if __name__ == "__main__":
    main()
