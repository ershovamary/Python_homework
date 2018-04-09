## Вариант 1
## Тест 9 Апреля 2018
## Для удобства вся информация записана в один файл output.txt,
## кроме специального задания, где нужно создать csv-файл.

import re
import collections

def read_file_and_count_lines(filename):
    with open(filename,"r",encoding="utf-8") as f:
        i = 0
        text = ''
        for line in f:
            i += 1
            text += line
    return i, text

def re_search_all(s):
    match = re.findall('<w lemma=".+?" type=".+?">.+?</w>',s)
    return match

def write_file(filename,s):
    with open(filename,"w",encoding="utf-8") as f:
        text = f.write(s)

def re_search_adj(s):
    match = re.findall('<w lemma=".+?" type="l.f.*?">.+?</w>',s)
    return match

def search_and_replace(s):
    match = re.search('<body>(.|\s)+</body>',s)
    if match:
        new_s = match.group()
        new_s = re.sub(r'<w lemma="(.+?)" type="(.+?)">(.+?)</w>',r'\1,\2,\3',new_s)
        new_s = re.sub(r'<.+>(\n|)',r'',new_s)
        new_s = re.sub(r' +',r'',new_s)
    return new_s

def main():
    s1, text = read_file_and_count_lines('iceland_corpora.html')
    l = re_search_all(text)
    frec_d = collections.Counter(l)
    s2 = ''
    for k in frec_d:
        s2 += k + '\n'
    s3 = ''
    l2 = re_search_adj(text)
    frec_d_adj = collections.Counter(l2)
    for line in sorted(frec_d_adj,key = frec_d_adj.get, reverse = True):
        s3 += line + '\t' + str(frec_d_adj[line]) + '\n'
    write_file('output.txt','Задание 1:\n' + str(s1) + '\nЗадание 2:\n' + s2 + 'Задание 3:\n' + s3)
    s4 = search_and_replace(text)
    write_file('output_3.csv',s4)

if __name__ == "__main__":
    main()
