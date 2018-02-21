import random

def make_dict():
    main_d = {}
    f = open("hints.csv", encoding="utf-8")
    for line in f:
        if ',' in line:
            l = line.split(',')
            enclosed_l = [l[1],l[2]]
            main_d[l[0]] = enclosed_l
    return main_d

def make_positive_answer():
    l = ['Молодец!','Да ты умница!','Верно! Ты прорицатель, что ли?','Превосходно! Как здорово с тобой играть!','Угадал!', 'Правильно!']
    return random.choice(l)

def make_negative_answer():
    l = ['На этот раз не вышло...','Не угадал. В следующий раз обязательно получится!','Не получилось...','Имелось в виду другое...','Неправильно, но не расстраивайся, в следующий раз обязательно угадаешь!']
    return random.choice(l)

def main():
    print('Привет! Давай поиграем? Я загадаю слово, а ты попробуешь угадать его по распространённому словосочетанию с ним. \n\rЯ начинаю!')
    d = make_dict()
    for k in d:
        a = d[k]
        if a[1] == 'просто' or a[1] == 'просто\n':
            user_s1 = input(a[0] + ' ...(введи свой вариант ответа с маленькой буквы)\n')
            if user_s1 == k:
                print(make_positive_answer())
            else:
                print(make_negative_answer())
    user_s2 = input('Попробуем посложней? (если хочешь сбежать, введи "нет", продолжить - "да")\n')
    if user_s2 == 'нет':
        print('Рад был с тобой сыграть! Возвращайся ещё!')
    elif user_s2 == 'да':
            for k in d:
                a = d[k]
                if k == 'сложно' or a[1] == 'сложно\n':
                    user_s1 = input(a[0] + ' ...(введи свой вариант ответа с маленькой буквы)\n')
                    if user_s1 == k:
                        print(make_positive_answer())
                    else:
                        print(make_negative_answer())
    else:
        print('Ты ввёл что-то непонятное... Кажется, ты устал. Можешь пойти выпить чайку. Возвращайся, когда отдохнёшь!')
        
if __name__ == "__main__":
    main()
