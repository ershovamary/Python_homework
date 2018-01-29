#Classwork from 25 January 2018
#Словари

import clearer

def make_dictionary(a):
    d = {}
    for word in a:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def sort_dictionary(d):
    for word in sorted(d,key = d.get, reverse = True):
        print(word,'\t',d[word])

def main():

    words = clearer.clearer('idiot.txt')

    d = make_dictionary(words)
    
    sort_dictionary(d)
    
if __name__ == "__main__":
    main()
