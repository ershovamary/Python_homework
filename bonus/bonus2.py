#Бонус 2: программа переводит температурное значение по шкале Цельсия
#в шкалу Фаренгейта и Кельвина.

def cel_to_far(x):
    return x * 1.8 + 32

def cel_to_kel(x):
    return x + 273.15

def main():
    x_cel = input('Введите значение температуры по шкале Цельсия. ' )
    if x_cel != '':
        x_far = cel_to_far(float(x_cel))
        x_kel = cel_to_kel(float(x_cel))
    else:
        return 'Не введено значение температуры.'
    return str(float(x_cel)) + ' по шкале Цельсия = ' + str(x_far) + ' по шкале Фаренгейта = ' + str(x_kel) + ' по шкале Кельвина.'

if __name__ == "__main__":
    print(main())
