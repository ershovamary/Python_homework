## Экзамен
## Программа создаёт csv-таблицу с полями "Название файла", "Автор",
## "Дата создания текста", "Заголовок" с информацией о всех статьях,
## затем для каждого файла находит все имена собственные
## (их леммы должны быть написаны с заглавной буквы) и подсчитывает,
## сколько раз каждое из них встретилось в статье.
## Результаты записывает в таблицу со столбцами: имя файла, найденное имя,
## количество вхождений. В качестве разделителя используется табуляцию.

import re
import os

def read_file(filename):
    with open(filename,"r",encoding="windows-1251") as f:
        text = f.read()
    return text

def re_search(text,l):
    new_s = ''
    for s in l:
        match = re.search('<meta content="(.*?)" name="' + s + '">', text)
        if match:
            new_s += '\t' + match.group(1)
    return new_s

def write_file():
    with open('news.csv',"w",encoding="utf-8") as f:
        f.write('Название файла' + '\t' + 'Автор' + '\t' + 'Дата создания текста' + '\t' + 'Заголовок' + '\n')

def append_file(name, s):
    if not os.path.isfile('news.csv'):
        write_file()
    with open('news.csv',"a",encoding="utf-8") as f:
        f.write(name + s + '\n')

def main():
    l = ['author','created','header']
    path = './news'
    names = os.listdir(path)
    for f in names:
        append_file(f, re_search(read_file(os.path.join(path,f)),l))

if __name__ == "__main__":
    main()
