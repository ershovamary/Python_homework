##import random
##def main():
##    def randomizer():
##        return random.random()
##    def pr(x):
##        return print(x)
##    x = randomizer()
##    pr(x)
##main()

##Classwork from 11 January 2018
##обработать случайный текст -- нижний регистр без знаков препинания по словам
##создает tsv файл, где строчек столько, сколько слов и 3 колонки,
##отделённые табуляцией, где перемешаны буквы

##import sys
##sys.path.insert(0,'/Study/Python/Rep/Python_homework')
import clearer
import random

def main():
    
    def tabular(words):

    def mixer(n,w):
        l = []
        for i in range(n):
            l.append(random.shuffle(w))
        return l
        
        with open("mixed_words.tsv", "w", encoding="utf-8") as f:
            for word in words:
                mixed_words = mixer(3,word.split())
                f.write(word + "\t" + mixed_words[0] + "\t" + mixed_words[1] + "\t" + mixed_words[2] + "\n")
    words = clearer()
    tabular()
    
main()
