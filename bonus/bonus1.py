#Бонус 1: программа считает среднее арифметическое, максимальное и минимальное числа для введённых чисел.

def mean(a,b):
    return (a + b)/2
    
def main():
    n = input('Введите число. Для выхода из программы нажмите enter. ' )
    if n != '':
        mean_value = float(n)
        maxim = float(n)
        minim = float(n)
    else:
        return 'Числа не были введены.'
    while n != '':
        n = input('Введите число. Для подсчёта среднего арифметического, максимального и минимального чисел нажмите enter. ' )
        if n == '':
            break
        else:
            n = float(n)
            mean_value = mean(mean_value,n)
            maxim = max(maxim,n)
            minim = min(minim,n)
    return 'Среднее арифметическое = ' + str(mean_value) + ', максимальное = ' + str(maxim) + ', минимальное = ' + str(minim) + '.'

if __name__ == "__main__":
    print(main())
    
