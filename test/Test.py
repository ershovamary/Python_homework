## Test from 12 December 2017
## Вариант 1

##Часть 1

with open("Extinct_languages.tsv", "r", encoding="utf-8") as f:
    s = f.readlines()
    for i in s:
        if len(i) > 35:
            print(i)
            
