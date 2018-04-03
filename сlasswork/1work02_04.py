#Classwork from 2 April 2018
#Функция re.sub('',s1,s2)

import re
import clearer

def read_file(filename):
    with open(filename + '.html',"r",encoding="utf-8") as f:
        text = f.read()
    return text

def search_and_replace(s):
    rg = ['<.+?>','&.+?;','[.+]']
    for regex in rg:
        new_s = re.sub(regex,'',s)
        s = new_s
    #<(^/).+?>.+?</.+?>
    return new_s

def rewrite_file(filename,new_s):
    with open(filename + '+.html',"w",encoding="utf-8") as f:
        text = f.write(new_s)

def remove_latin(s):
    text = clearer.clearer(s)
    for word in text:
        if re.search('(a-zA-Z)+',word):
            text.remove(word)
    return text

def make_dict(text):
    d = {}
    for word in text:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def sort_dict(d):
    for word in sorted(d,key = d.get, reverse = True):
        print(word,'\t',d[word])

def main():
    f = 'article'
    new_text = search_and_replace(read_file(f))
    rewrite_file(f,new_text)
    sort_dict(make_dict(new_text))

if __name__=="__main__":
    main()
