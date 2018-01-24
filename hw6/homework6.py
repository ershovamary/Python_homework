##Вариант 7
##Программа генерирует тёка -- набор из 4 танка,
##которые в свою очередь являются нерифмованными пятью строками в 5-7-5-7-7 слогов,
##беря случайные слова из текстового файла.

import random

def make_dictionary():
    with open('dictionary.txt', encoding='utf-8') as f:
        dictionary = dict(
        noun_nom_m = f.readline().split(),
        noun_nom_f = f.readline().split(),
        noun_nom_n = f.readline().split(),
        noun_gen = f.readline().split(),
        noun_inst = f.readline().split(),
        noun_loc = f.readline().split(),
        clit_inst = f.readline().split(),
        clit_gen = f.readline().split(),
        clit_loc = f.readline().split(),
        adj = f.readline().split(),
        adv = f.readline().split(),
        verb = f.readline().split(),
        question_word = f.readline().split(),
        pronoun = f.readline().split(),
        imperative = f.readline().split())
    return dictionary

def punct():

    marks = [".", "?", "!", "..."]

    return random.choice(marks)

def noun_nom():
    d =  make_dictionary()
    nouns_nom = d['noun_nom_m'] + d['noun_nom_f'] + d['noun_nom_n']
    return random.choice(nouns_nom)

def noun_nom_m():
    d =  make_dictionary()
    nouns_nom = d['noun_nom_m']
    return random.choice(nouns_nom)

def noun_nom_f():
    d =  make_dictionary()
    nouns_nom = d['noun_nom_f']
    return random.choice(nouns_nom)

def noun_nom_n():
    d =  make_dictionary()
    nouns_nom = d['noun_nom_n']
    return random.choice(nouns_nom)

def noun_gen():
    d =  make_dictionary()
    nouns_gen = d['noun_gen']
    return random.choice(nouns_gen)

def noun_inst():
    d =  make_dictionary()
    nouns_inst = d['noun_inst']
    return random.choice(nouns_inst)

def noun_loc():
    d =  make_dictionary()
    nouns_loc = d['noun_loc']
    return random.choice(nouns_loc)

def clit_inst():
    d =  make_dictionary()
    clitics = d['clit_inst']
    return random.choice(clitics)

def clit_gen():
    d =  make_dictionary()
    clitics = d['clit_gen']
    return random.choice(clitics)

def clit_loc():
    d =  make_dictionary()
    clitics = d['clit_loc']
    return random.choice(clitics)

def adverbial():
    if random.randint(0,1):
        return clit_inst() + ' ' + noun_inst() + ' ' + noun_gen()
    elif random.randint(0,1):
        return clit_gen() + ' ' + noun_gen() + ' ' + noun_gen()
    return clit_loc() + ' ' + noun_loc() + ' ' +  noun_gen()

def adj():
    d =  make_dictionary()
    adjs = d['adj']
    return random.choice(adjs)

def adv():
    d =  make_dictionary()
    advs = d['adv']
    return random.choice(advs)

def verb():
    d =  make_dictionary()
    verbs = d['verb']
    return random.choice(verbs)

def question_word():
    d =  make_dictionary()
    question_words = d['question_word']
    return random.choice(question_words)

def pronoun():
    d =  make_dictionary()
    pronouns = d['pronoun']
    return random.choice(pronouns)

def imperative():
    d =  make_dictionary()
    imperatives = d['imperative']
    return random.choice(imperatives)

def noun_group():
    r = random.randint(0,2)
    if r == 0:
        return adj() + 'ый ' + noun_nom_m()
    elif r == 1:
        return adj() + 'ая ' + noun_nom_f()
    return adj() + 'ое ' + noun_nom_n()

def long_sentence(r):
    a = adverbial()
    a = a.capitalize()
    if r % 2 == 0:
        return str(a) + '\r\n' + noun_group() + ' ' + verb() + punct() + '\r\n'
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
