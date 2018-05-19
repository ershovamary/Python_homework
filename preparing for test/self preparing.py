import re
import clearer
import collections

def read_file(filename):
    with open(filename,"r",encoding="utf-8") as f:
        text = f.read().replace('\n',' ')
    return text

def sort_dictionary(d):
    for word in sorted(d,key = d.get, reverse = True):
        print(word,'\t',d[word])

def main():
    l = clearer.clearer('somefile.txt')
    frec_d = collections.Counter(l)
##    print(sort_dictionary(frec_d))
    for v in sorted(frec_d.values()):
        if int(v) > 5:
            print(frec_d[v],'\t',v)
        
if __name__ == "__main__":
    main()
