# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
eq= equation.index('=')
equation = equation[eq+1:].lstrip(' ')
x_pos = equation.index('x')
k = float(equation[:x_pos])
equation = equation[x_pos+1:].lstrip(' ')
el = equation[0]
if el == '+' or el == '-':
    equation = equation.lstrip(el).lstrip(' ')
b = float(equation)
print(k*x + b)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

print('Введите дату в формате \"dd.mm.yyyy\"')
date = input()
try:
    day, month, year = date.split('.')
    days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое',
            '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
            '11': 'одиннацатое',
            '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'восемнадцатое',
            '19': 'девятнадцатое',  '20': 'двадцатое', '21': 'двадцатьпервое',
            '22': 'двадцатьвторое', '23': 'двадцатьтретье',
            '24': 'двадцатьчетвёртое', '25': 'двадцатьпятое', '26': 'двадцатьшестое', '27': 'двадцатьседьмое',
            '28': 'двадцатьвосьмое', '29': 'двадцатьдевятое', '30': 'тридцатое', '31': 'тридцатьпервое'
            }
    months = {
        '01': 'января', '02': 'февраля',  '03': 'марта',
        '04': 'апреля', '05': 'мая',  '06': 'июня',
        '07': 'июля', '08': 'августа',  '09': 'сентября',
        '10': 'октября', '11': 'ноября',  '12': 'декабря'
    }
    year_check = int(year)
    if day not in days.keys() or month not in months.keys() or (int(day)>29 and month == '02')\
            or len(year) != 4 or year_check < 1 or year_check > 9999:
        print('некорректная дата')
    else:
        print('{} {} {} года'.format(days[day], months[month],year))
except(ValueError):
    print('некорректная дата')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3