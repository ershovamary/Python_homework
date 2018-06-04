## Вариант 7
## Программа читает текстовый файл, делит на предложения по знакам
## конца предложения, удаляет знаки препинания. Затем для каждого предложения
## ищет слова, которые встретились в предложении больше, чем 1 раз,
## и распечатывает табличку с выравниванием по центру, в которой сказано,
## сколько раз они встретились.

import re

def sep_to_sent(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        return [re.sub(r'[^\w\s]', '', sent.strip().lower()) for sent in re.split(r'[.?!]',text) if sent != '']

def iterant_words(sent, sent_no):
    words = sent.split()
    d = {word: words.count(word) for word in words if words.count(word) > 1}
    if len(d) > 0:
        s_length = max([len(iterant_word) + len(str(d[iterant_word])) for iterant_word in d])
        print('Повторяющиеся слова в предложении {}:'.format(sent_no + 1))
        for iterant_word in d:
            print('{:^{l}}'.format(iterant_word, l = s_length), ' - ', d[iterant_word])
        print()

def main():
    for sent_no, sent in enumerate(sep_to_sent('chekhov.txt')):
        iterant_words(sent, sent_no)

if __name__ == "__main__":
    main()
