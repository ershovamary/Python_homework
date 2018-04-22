## Вариант 7
## Программа просматривает все папки и файлы в папке, где находится программа
## и сообщает сколько в ней папок, название которых содержит и кириллические,
## и латинские символы, а затем выводит на экран названия
## всех папок и файлов.

import os
import re

def check_cyril_latin():
    file_list = os.listdir()
    correct_file_list = []
    for name in file_list:
        if os.path.isdir(name):
            if re.search(r'[А-ЯЁа-яё]',name) and re.search(r'[A-Za-z]',name):
                correct_file_list.append(name)
    return correct_file_list

def make_list_of_dir_names(file_list):
    return '\n'.join(sorted(file_list))

## Случайно сделала эту функцию и решила - пусть будет
def make_list_of_names():
    file_list = os.listdir()
    final_file_list = []
    for name in file_list:
        if name in final_file_list:
            continue
        else:
            final_file_list.append(name)
    return '\n'.join(sorted(final_file_list))

def main():
    print('Папок, которые содержат и кириллические, и латинские символы ровно ' + str(len(check_cyril_latin())))
    print('А вот список названий всех подходящих папок в данной директории:\n' + str(make_list_of_dir_names(check_cyril_latin())))
    if input('Вывести названия всех файлов и папок в данной директории? (Введите любую строку для вывода или нажмите enter, чтобы выйти из программы)') != '':
        print(make_list_of_names())
if __name__ == "__main__":
    main()
