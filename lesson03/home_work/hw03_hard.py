# -*- coding: utf-8 -*-
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
import math
n = 0


def denominator_func(frac):
    return frac.split('/')[1]
def numerator_func(frac):
    global n
    if ' ' not in frac.split('/')[0]:
        n = 0
        return frac.split('/')[0]
    else:
        n = int(frac.split('/')[0].split(' ')[0])
        return frac.split('/')[0].split(' ')[1]

equation = '5/6 + 4/7'
try:
    sigh_pos = equation.index('+')
    sigh = True
except:
    sigh_pos = equation.index('-')
    sigh = False
frac2 = equation[sigh_pos+1:].strip(' ')
frac1 = equation[:sigh_pos].strip(' ')

if '/' in frac1:
    zn1 = int(denominator_func(frac1))
    cisl1 = int(numerator_func(frac1))
    n1 = n
else:
    cisl1 = int(frac1)
    zn1 =1
    n1 = n
if '/' in frac2:
    zn2 = int(denominator_func(frac2))
    cisl2 = int(numerator_func(frac2))
    n2 = n
else:
    cisl2 = int(frac2)
    zn2 =1
    n2 = n
mymsd = (zn1/(math.gcd(int(zn1), int(zn2))))*zn2
k1 = int(mymsd/zn1)
k2 = int(mymsd/zn2)
cisl1_after, zn1_after = cisl1*k1, zn1*k1
cisl2_after, zn2_after = cisl2*k2, zn2*k2

if zn1 != 1:
    cisl1 = n1 * zn1 + cisl1
if zn2 != 1:
    cisl2 = n2 * zn2 + cisl2

if sigh:
    cislall = cisl1_after + cisl2_after
else:
    cislall = cisl1_after - cisl2_after
if math.fabs(cislall) > math.fabs(zn1):
    print('{}/{}'.format(cislall,zn1))
else:
    cel = cislall//zn1
    ost = cislall % zn1
    print('{} {}/{}'.format(cel,ost,zn1))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
#print(list(map(chr, range(ord('А'), ord('Я')+1))))

