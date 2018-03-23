##Вариант 7
##Программа открывает файл с русским текстом в кодировке UTF-8
##и распечатывает из него по одному разу
##все встретившиеся в нём формы глагола сидеть (кроме видовых пар)

import re
import clearer

def check_if_partcp(l,final_l):
    endings = 'ий ая ее его ей ему ую им ем ие их им ими'.split(' ')
    for i in l:
        if i not in final_l and re.search('сид(ящ|евш)('+ '|'.join(endings) + ')', i):
            final_l.append(i)
    return final_l

def check_if_ger_or_inf(l,final_l):
    for i in l:
        if i not in final_l and re.search('сид(я|ев|евши|ючи|еть)', i):
            final_l.append(i)
    return final_l

def check_if_indic(l,final_l):
    endings = 'ишь ит им ите ят ел ела ело ели'.split(' ')
    for i in l:
        if i not in final_l and re.search('(сижу|сид('+ '|'.join(endings) + '))', i):
            final_l.append(i)
    return final_l

def check_if_imper(l,final_l):
    endings = ''.split(' ')
    for i in l:
        if i not in final_l and re.search('сиди(|те)('+ '|'.join(endings) + ')', i):
            final_l.append(i)
    return final_l

def make_single_list(l):
    l1 = []
    l2 = check_if_partcp(l,l1)
    l3 = check_if_ger_or_inf(l,l2)
    l4 = check_if_indic(l,l3)
    l5 = check_if_imper(l,l4)
    return l5

def main():
    words = clearer.clearer('file.txt')
    print('Встретились следующие формы глагола "сидеть":')
    for i in make_single_list(words):
        print(i)

if __name__ == "__main__":
    main()
