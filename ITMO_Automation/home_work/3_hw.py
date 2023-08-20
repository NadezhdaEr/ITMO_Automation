def task_1(a, b):
    if a > b:
        print('a')
    else:
        print('b')

task_1(4, 10)

def task_2(c, d):
    if (c-d) == 135 or (d-c) == 135:
        print('YES')
    else:
        print('NO')

task_2(235, 100)

def task_3(m):
    if m == 1:
        print('Январь')
    elif m == 2:
        print('Февраль')
    elif m == 3:
        print('Март')
    elif m == 4:
        print('Апрель')
    elif m == 5:
        print('Май')
    elif m == 6:
        print('Июнь')
    elif m == 7:
        print('Июль')
    elif m == 8:
        print('Август')
    elif m == 9:
        print('Сентябрь')
    elif m == 10:
        print('Октябрь')
    elif m == 11:
        print('Ноябрь')
    elif m == 12:
        print('Декабрь')

task_3(4)

def task_4(e, f, g):
    if e > 10 and f > 10 and g > 10:
        print('YES')
    else:
        print('NO')

task_4(9, 100, 12)

list1 = [2, -2, 3, -3, 4]
pos_count = 0
for num in list1:
    if num > 0:
        pos_count += 1
print ('Положительных чисел', pos_count)

def task_6(x,y):
    days = x * 12 * 29 + y * 29
    print('Количество дней', days)
task_6(1, 6)




