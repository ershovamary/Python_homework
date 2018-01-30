##Вариант 7
##Программа принимает на вход название текстового файла,
##для которого считает кол-во слов на un-, и процент из них слов длины большей, чем введённое число.

import clearer

def make_dictionary(a):
    d = {}
    for word in a:
        if word[0:2] == 'un':
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d

def count_un(d):
    i = 0
    for value in d.values():
        i += int(value)
    return i

def count_length(d, n):
    j = 0
    for key, value in d.items():
        if len(key) > n:
            j += int(value)
    return j

def main():
    words = clearer.clearer(input('Введите имя файла с текстом, для которого требуется посчитать кол-во слов, начинающихся на un- (например, the catcher in the rye.txt).'))
    d = make_dictionary(words)
    i = count_un(d)
    n = int(input('Введите такое число, для которого программа посчитает процент всех слов на un-, которые превосходят в длине данное значение. '))
    j = count_length(d,n)
    return 'Слов, начинающихся на un- -- ' + str(i) + ', а из них слов длиной больше ' + str(n) + ' символов -- ' + str(j/i*100) + '%'
    
if __name__ == "__main__":
    print(main())
