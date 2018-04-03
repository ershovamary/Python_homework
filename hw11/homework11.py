## Вариант 7
## Программа считывает txt-файл со статьёй "Птицы" из Википедии
## и заменяет в нём все формы слова "птица" на формы слова "рыба",
## а затем записывает изменённый текст в новый txt-файл.

import re

def read_file(filename):
    with open(filename,"r",encoding="utf-8") as f:
        text = f.read()
    return text

def search_and_replace(s):
    rg = {'а':'а','ы':'ы','е':'е','у':'у','ей':'ой','':'','ам':'ам','ами':'ами','ах':'ах'}
    for regex in rg:
        s = re.sub(r'\bптиц' + regex + r'\b','рыб' + rg[regex],s)
        s = re.sub(r'\bПтиц' + regex + r'\b','Рыб' + rg[regex],s)
        s = re.sub(r'\bПти́ц' + regex + r'\b','Ры́б' + rg[regex],s)
    return s

def rewrite_file(filename,new_s):
    with open(filename,"w",encoding="utf-8") as f:
        text = f.write(new_s)

def main():
    rewrite_file('Fish.txt',search_and_replace(read_file('Bird.txt')))

if __name__ == "__main__":
    main()
