# Программа проверяет является число положительным
# или отрицательным и выводит сообщение

num = 3

# Также попробуйте следующие значения num.
# num = -5
# num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

# str_2 содержит в себе str_1?
# str_1 = 'test'
# str_2 = 'test1'

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')

task_yes_no(str_1='test', str_2='testing')

num_float = 3.4

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Вы - бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы - магистрант')
    elif year_of_study in range(7, 10):
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(5)

a = 5

if a > 100 or a < -100:
    print('-')
else:
    print('+')
