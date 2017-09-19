#Вариант 7
#Программа проверяет верность выражений "a % b = c", "a ^ b = c" для введённых пользователем трёх чисел.
a, b, c = int(input('Введите три числа по очереди, нажимая enter: ')),int(input()),int(input())
if b == 0:
    print(str(a) + ' разделить на ' + str(b) + ' не равно ' + str(c))
elif a / b == c:
    print(str(a) + ' разделить на ' + str(b) + ' равно ' + str(c))
else:
    print(str(a) + ' разделить на ' + str(b) + ' не равно ' + str(c))
if a ** b == c:
    print(str(a) + ' в степени ' + str(b) + ' равно ' + str(c))
else:
    print(str(a) + ' в степени ' + str(b) + ' не равно ' + str(c))
