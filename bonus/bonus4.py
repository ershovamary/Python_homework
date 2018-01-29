#Бонус 4: программа переделывает слово или фразу так,
#чтобы после каждой гласной добавлялась "с" и дублировалась гласная до "с"

def check_if_vow(s):
    vowels = 'уеыаоэяиюё'
    if s in vowels:
        return True
    else:
        return False

def main():
    s = input('Введите слово или фразу кириллицей. ')
    if s != '':
        l = s.split()
        kirpich = ''
        for i in l:
            for j in i:
                kirpich += j
                if check_if_vow(j):
                    kirpich += 'с' + j
            kirpich += ' '
    else:
        return 'Не введены слово или фраза.'
    return kirpich

if __name__ == "__main__":
    print(main())
