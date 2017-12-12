## Test from 12 December 2017
## Вариант 1

## Часть 1

with open("Extinct_languages.tsv", "r", encoding="utf-8") as f:
    s = f.readlines()
    crit = []
    for i in s:
        if len(i) > 35:
            print(i)
            
## Часть 2
            
        columns = i.split('\t')
        status = columns[2]
        if status == "Critically endangered\n":
            crit.append(status)
    print(len(crit))
