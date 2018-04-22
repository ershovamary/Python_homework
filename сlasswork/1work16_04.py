## Classwork from 16 April 2018
## module os
## взять большой текст, разрезать на части по 2000 слов,
## каждую часть положить в отдельный файл внутри определенной папки,
## получить их список, поочередно открыть и
## вычислить самое частотое слово для каждой из них

import os
import collections
import clearer
import math

def write_file(filename,s):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(s)

def separate_and_create_files(filename):
    text = clearer.clearer(filename)
    x = math.ceil(len(text)/2000)
    for i in range(x):
        new_file = 'File_' + str(i)
        new_dir = 'Dir_' + str(i)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        with open(new_dir + '/' + new_file,"w",encoding="utf-8") as f:
            if i == x:
                f.write(' '.join(text[i*2000,]))
            else:
                f.write(' '.join(text[i*2000,(i+1)*2000]))
            
##    i = 1
##    for i in text:
##        with open(filename,"w",encoding="utf-9") as f:
##            while (text.index(i))%2000 != 0:
                
        

def main():
    separate_and_create_files('chekhov.txt')
##filepath = os.listdir('C' + os.sep + '/User')
##if os.path.isfile(filepath)

if __name__ == "__main__":
    main()
