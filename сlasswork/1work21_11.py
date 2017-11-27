##classwork from 21 November

##fail ='|1|2|3|4|5|6|7|8|9|0|`|~|!|@|"|#|№|$|;|%|^|:|&|?|*|(|)|_|--|+|=|.|,| |\t'
##bad = fail.split('|')
##print(bad)
##with open("C:/Study/Python/Useful files/file.txt", "r", encoding="utf-8") as f:
##    line = f.readlines()
##    with open("C:/Study/Python/Useful files/lines.tsv", "w", encoding="utf-8") as new_f:
##        for s in line:
##            words = s.split(' ')
##            for j in words:
##                if j in bad:
##                    words.remove(j)
##                else:
##                    for symb in j:
##                        if symb in bad:
##                            j.strip(symb)
##                    clear_word = j
##                    new_f.write(str(clear_word) + '\t' + str(len(words)) + '\n')
##                    break

digits = '1 2 3 4 5 6 7 8 9 0 \r \n'
punct = '.|,|..|...|:|;|"|!|?|--| |(|)'
digits = digits.split(' ')
punct = punct.split('|')
with open("C:/Study/Python/Useful files/classwork21_11.txt", "r", encoding="utf-8") as f:
    line = f.readlines()
    with open("C:/Study/Python/Useful files/lines.tsv", "w", encoding="utf-8") as new_f:
        for s in line:
            words = s.split(' ')
            for word in words:
                for symb in word:
                    if symb in digits:
                        if len(words) == 1:
                            word = ''
                            break
                        else:
                            words.remove(word)
                            break
                    elif symb in punct:
                        if word.index(symb) == 0 or word.index(symb) == (len(word) - 1):
                            word.strip(symb)
                        else:
                            if len(words) == 1:
                                word = ''
                                break
                            else:
                                words.remove(word)
                                break
            if words[0] == '':
                continue
            else:
                new_f.write(str(words[0]) + '\t' + str(len(words)) + '\n')



    
