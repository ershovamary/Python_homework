## Test from 12 December 2017
## Вариант 1

## Часть 1 - программа выводит все строки длиннее 35 символов

with open("Extinct_languages.tsv", "r", encoding="utf-8") as f:
    s = f.readlines()
    crit = []
    for i in s:
        line = i.rstrip('\n')
        if len(line) > 35:
            print(line)
            
## Часть 2 - программа выводит количество critically endangered languages
            
        columns = i.split('\t')
        status = columns[2]
        if status == "Critically endangered\n":
            crit.append(status)
    print('The number of critically endangered languages is ' + str(len(crit)))

## Часть 3 - программа ищет название языка, задаваемого пользователем
## в списке и выводит информацию о нём

    lang = ' '
    while lang != '':
        lang = input('Please, write down the language you are searching for: ')
        check = False
        for i in s:
            line = i.rstrip('\n')
            columns = line.split('\t')
            if columns[0] == lang:
                print(columns[0] + ' - ' + columns[1] + ' - ' + columns[2])
                check = True
                break
        if check == False and lang != '':
            print('The language is not in the list.')
