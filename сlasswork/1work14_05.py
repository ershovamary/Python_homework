## Classwork from 14 May 2018
## Walk the files tree
## Обходит все катологи и считает, сколько в дереве имен каталогов с r
## во скольки файлах есть d, а если в каталоге с r есть файлы с d - вывести

## root: I am the string and I am the path
## dirs: I am the list of directions
## files: And I am the list of files

import os

def if_correct_name(x,l,name):
    if x:
        if l in name:
                return 1
    if l in name:
        return 1
    return 0

def main():
    i, j = 0, 0
    for root, dirs, files in os.walk("C:\Study\Programming and repo\Rep\Python_homework\сlasswork"):
        for dr in dirs:
            x, l = True, 'r'
            i += if_correct_name(x,l,dr)
            for name in os.listdir(root + os.sep + dr):
                if os.path.isfile(name):
                    x, l = False, 'd'
                    path = root + os.sep + dr + os.sep + name
                    if i != 0 and if_correct_name(x,l,path) != 0:
                        print(path)
            
        for fl in files:
            x, l = False, 'd'
            j += if_correct_name(x,l,fl)
    print('There are ' + str(i) + ' directions with "r" in them\n' + 'There are ' + str(j) + ' files with "d" in them')
            
                    
##            if not fl.endswith('.txt'):
##                continue
##            f = open(root + os.sep + fl,'r')
            

if __name__=="__main__":
    main()
