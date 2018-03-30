## Вариант 7
## Программа открывает html-файл, название которого вводит пользователь,
## со статьёй о языках из русской википедии
## и извлекает трёхбуквенный код, который помещает в файл data.txt,
## создавая таким образом базу данных о языках из уже полученных статей.

import re
import os.path

def read_file(filename):
    with open(filename,"r",encoding="utf-8") as f:
        text = f.read().replace('\n','')
    return text

def re_search_code(s):
    match = re.search('ISO 639-3<.*?<td>.*?>(...)<',s)
    if match:
        return match.group(1)

def re_search_title(s):
    match = re.search('<title>(.+) — Википедия</title>',s)
    if match:
        return match.group(1)

def save_data(k,v):
    d = {}
    if os.path.isfile('data.txt'):
        with open('data.txt',"r",encoding="utf-8") as f:
            for line in f:
                if '\t' in line:
                    l = line[:-1].split('\t')
                    d[l[0]] = l[1]
    with open('data.txt',"w",encoding="utf-8") as f:
        d[k] = v
        for key in d:
            f.write(str(key) + '\t' + str(d[key]) + '\n')

def main():
    filename = input('Введите название html-файла (без расширения), из которого требуется извлечь информацию о трёхбуквенном коде языка: ')
    save_data(re_search_title(read_file(filename + '.html')),re_search_code(read_file(filename + '.html')))
    

if __name__ == "__main__":
    main()
