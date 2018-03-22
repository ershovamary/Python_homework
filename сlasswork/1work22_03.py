#Classwork from 22 March 2018
#Регулярные выражения: re.findall

import re

def read_file(filename):
    with open(filename,"r",encoding="utf-8") as f:
        text = f.read()
    return text
        
def re_search(s):
    return re.findall('(«[А-Я][а-я]+?\-[0-9]+?»)',s)

def main():
    final_l = []
    l = re_search(read_file('Chinise cosmo programme.txt'))
    for i in l:
        if i not in final_l:
            final_l.append(i)
            print(i,'\n-----')

if __name__ == "__main__":
    main()
