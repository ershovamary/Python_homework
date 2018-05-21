#Classwork from 7 December 2017
#открывает текст, убирает всё ненужное, приводит всё к нижнему регистру,
#создаёт список слов
def clearer(filename):
    bad_symb = '1234567890 ,.,?!\"_/():-'
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
##        for line in s:
##            line.join(' ')
##        text = ''.join(s)
        words = text.split()
        words2 = []
        for word in words:
            w = word.strip(bad_symb)
            words2.append(w.lower())
            
##        for word in words:
##            for symb in word:
##                if symb in bad_symb:
##                    word.replace(symb,'')
        return words2
