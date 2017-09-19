n = int(input('Введите число: '))
if n == 0:
    print(str(n) + ' - ноль')
elif n % 2 == 0:
    print(str(n) + ' - чётно')
else:
    print(str(n) + ' - нечётно')
