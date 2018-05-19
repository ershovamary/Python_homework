## Вариант 7
## Программа обходит всё дерево папок, начинающееся с той папки,
## где она находится, и сообщает, в какой папке больше всего файлов

import os

def walk_and_count(path):
    d = {}
    for root, dirs, files in os.walk(path):
        d[root] = len(files)
    k_max = max(d.values())
    return d, k_max
            

def main():
    d, k_max = walk_and_count(os.getcwd())
    print('Эти папки содержат наибольшее кол-во файлов (' + str(k_max) + '):')
    for k in sorted(d, key=d.get, reverse=True):
        if d[k] < k_max:
            break
        print('"' + k + '"')

if __name__ == "__main__":
    main()
