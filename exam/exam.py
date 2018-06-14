## Экзамен
## Программа создаёт csv-таблицу с полями "Название файла", "Автор",
## "Дата создания текста", "Заголовок" с информацией о всех статьях,
## затем для каждого файла находит все имена собственные
## (их леммы должны быть написаны с заглавной буквы) и подсчитывает,
## сколько раз каждое из них встретилось в статье.
## Результаты записывает в таблицу со столбцами: имя файла, найденное имя,
## количество вхождений. В качестве разделителя используется табуляция.
## Есть попытки написать 3 часть (def find_2_grams())

import re
import os

def read_file(filename):
    with open(filename,"r",encoding="windows-1251") as f:
        text = f.read()
    return text

def re_search(text,l):
    new_s = ''
    for s in l:
        match = re.search(r'<meta content="(.*?)" name="' + s + '">', text)
        if match:
            new_s += '\t' + match.group(1)
    return new_s

def write_file(n):
    if n == 1:
        with open('news.csv',"w",encoding="utf-8") as f:
            f.write('Название файла' + '\t' + 'Автор' + '\t' + 'Дата создания текста' + '\t' + 'Заголовок' + '\n')
    if n == 2:
        with open('news.csv',"a",encoding="utf-8") as f:
            f.write('\nИмя файла' + '\t' + 'Найденное имя' + '\t' + 'Кол-во вхождений' + '\n')

def find_names(text):
    d = {}
    all_names = re.findall(r'</ana>[А-ЯЁ].*?</w>', text)
    for name in all_names:
        l = re.findall(name, text)
        name = name[6:-4]
        d[name] = len(l)
    return d

def append_file_1(name, s):
    if not os.path.isfile('news.csv'):
        write_file(1)
    with open('news.csv',"a",encoding="utf-8") as f:
        f.write(name + s + '\n')

def append_file_2(name, d):
    with open('news.csv',"a",encoding="utf-8") as f:
        for k in d:
            f.write(name + '\t' + k + '\t' + str(d[k]) + '\n')

def find_2_grams(text, n):
    s = ''
    match = re.search(r'<w><ana lex=".+?" gr="PR"></ana>(.+?)</w> \n<w><ana lex=".+?" gr="S,.*?,loc"></ana>(.+?)</w>', text)
    if match:
        s += match.group(1) + ' ' + match.group(2) + '\t' + n + '\n'

def main():
    l = ['author','created','header']
    path = './news'
    names = os.listdir(path)
    for f in names:
        text = read_file(os.path.join(path,f))
        append_file_1(f, re_search(text,l))
    write_file(2)
    for f in names:
        text = read_file(os.path.join(path,f))
        append_file_2(f, find_names(text))

if __name__ == "__main__":
    main()
