#Classwork from 15 March 2018
#Регулярные выражения

import re

def make_sentences_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        sentences = text.replace('.\r\n','. ').split('. ')
    return sentences

def re_search(s):
    n = 0
    for i in s:
        if re.search('[1-9]+( |)((г.|гг.|год(|у|а|ов|ам|ы))|(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря))', i):
            print(i + '.\n-------')
            n += 1
    print(n)

def main():
    s = make_sentences_from_file('Mexican-American war.txt')
    re_search(s)
    
if __name__ == "__main__":
    main()
