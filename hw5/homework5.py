## Вариант 7
## Программа спрашивает у пользователя восемь слов
## и записывает в файл "homework5.txt" в той же директории,
## где находится программа, четыре строки с попарно склеенными словами.

j = 0
list = []
print('Введите 8 слов, разделяя их нажатием клавиши Enter:')
for i in range(8):
    list.append(input())
with open("homework5.txt", "w", encoding="utf-8") as f:
    while j < 8:
        f.write(str(list[j]) + str(list[j + 1]) + "\n")
        j += 2
