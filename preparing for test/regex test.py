## Программа открывает html-файл со статьёй "Грузины в России"
## и считает сколько в файле фамилий на -швили, -дзе и -ия,
## а также заменяет фамилии на -швили и на -дзе на Галактион
## и записывает всё в новый файл

import re

def read_file(filename):
    with open(filename,"r",encoding="utf-8") as f:
        text = f.read().replace('\n','')
    return text

def re_search_any(s,pattern):
    match = re.findall('<li>.*?<a href=".+?" title="([А-Я][а-я]+?' + pattern + '), .+?">',s)
    if match:
        return match

def re_place(s,pattern,new_pattern):
    s = re.sub(r'(<li>.*?<a href=".+?" title=")[А-Я][а-я]+?' + pattern + '(, .+?">)',r'\1' + new_pattern + r'\2',s)
    return s

def rewrite_file(filename,new_s):
    with open(filename,"w",encoding="utf-8") as f:
        text = f.write(new_s)

def main():
    surnames = ['швили','дзе']
    text = read_file('georgians.html')
    n1 = re_search_any(text,'швили')
    n2 = re_search_any(text,'дзе')
    n3 = re_search_any(text,'ия')
    if len(n1) > len(n2):
        print('Грузин с фамилией на -швили больше, чем грузин с фамилией на -дзе на ' + str(len(n1) - len(n2)))
    elif len(n1) == len(n2):
        print('Грузин с фамилией на -швили столько же, сколько и грузин с фамилией на -дзе')
    else:
        print('Грузин с фамилией на -швили меньше, чем грузин с фамилией на -дзе на ' + str(len(n2) - len(n1)))
##    print(n1,'\n\n',n2,'\n\n',n3)
    print('А грузин с фамилией на -ия ровно ' + str(len(n3)))
    for i in surnames:
        text = re_place(text,i,'Галактион')
    rewrite_file('fixed_georgians.html',text)

if __name__ == "__main__":
    main()
