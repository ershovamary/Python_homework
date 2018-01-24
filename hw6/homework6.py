##Вариант 7
##Программа генерирует тёка -- набор из 4 танка,
##которые в свою очередь являются нерифмованными пятью строками в 5-7-5-7-7 слогов,
##беря случайные слова из текстовых файлов.

import random

def punct():

    marks = [".", "?", "!", "..."]

    return random.choice(marks)

def list_from_file(a):
    a += '.txt'
    with open(a, encoding='utf-8') as f:
        b = f.readline().split()
    return b

def noun_nom():
    nouns_nom = list_from_file('noun_nom')
    return random.choice(nouns_nom)

def noun_gen():
    nouns_gen = list_from_file('noun_gen')
    return random.choice(nouns_gen)

def noun_inst():
    nouns_inst = list_from_file('noun_inst')
    return random.choice(nouns_inst)

def noun_loc():
    nouns_loc = list_from_file('noun_loc')
    return random.choice(nouns_loc)

def clit_inst():
    clitics = list_from_file('clit_inst')
    return random.choice(clitics)

def clit_gen():
    clitics = list_from_file('clit_gen')
    return random.choice(clitics)

def clit_loc():
    clitics = list_from_file('clit_loc')
    return random.choice(clitics)

def adverbial():
    if random.randint(0,1):
        return clit_inst() + ' ' + noun_inst() + ' ' + noun_gen()
    elif random.randint(0,1):
        return clit_gen() + ' ' + noun_gen() + ' ' + noun_gen()
    return clit_loc() + ' ' + noun_loc() + ' ' +  noun_gen()

def adj():
    adjs = list_from_file('adj')
    return random.choice(adjs)

def adv():
    advs = list_from_file('adv')
    return random.choice(advs)

def verb():
    verbs = list_from_file('verb')
    return random.choice(verbs)

def question_word():
    question_words = list_from_file('question_word')
    return random.choice(question_words)

def pronoun():
    pronouns = list_from_file('pronoun')
    return random.choice(pronouns)

def imperative():
    imperatives = list_from_file('imperative')
    return random.choice(imperatives)

def long_sentence(r):
    a = adverbial()
    a = a.capitalize()
    if r % 2 == 0:
        return str(a) + '\r\n' + adj().capitalize() + ' ' + noun_nom() + ' ' + verb() + punct() + '\r\n'
    return str(a) + '\r\n' + noun_nom().capitalize() + ' ' + adv() + ' ' + verb() + punct() + '\r\n'

def short_sentence(r):
    a = question_word()
    if r % 4 == 0:
        return str(a.capitalize()) + ' ' + verb() + ', ' + imperative() + '!..\r\n'
    else:
        if r % 4 == 1:
            return str(a.capitalize()) + ' ' + verb() + ' в ' + noun_loc() + '?..\r\n'
        elif r % 4 == 2:
            return str(a.capitalize()) + ' ' + verb() + ' с ' + noun_inst() + '?..\r\n'
        else:
            return str(a.capitalize()) + ' ' + verb() + ' ' + adv() + '?..\r\n'

def make_tanka():
    return long_sentence(random.randint(1,4)) + long_sentence(random.randint(1,4)) + short_sentence(random.randint(1,4))

for i in range(4):
    print(make_tanka())
