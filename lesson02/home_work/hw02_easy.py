# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
my_list = ["яблоко", "банан", "киви", "арбуз"]
sizes = []
for fruit in my_list:
    size = len(fruit)
    sizes.append(size)
max_size = max(sizes)
for number, element in enumerate(my_list):
    print('{} {:>{}}'.format(number+1, element, max_size))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
first_list = ["яблоко", "банан", "киви", "киви", "арбуз", "яблоко", "банан"]
second_list = ["киви"]
copy_first = first_list[:]
for element in copy_first:
    if element in second_list:
        first_list.remove(element)
print(first_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
my_list = [x for x in range(39)]
new_list = []
for element in my_list:
    if element%2 == 0:
        new_list.append(element/4)
    else:
        new_list.append(float(element*2))
print(new_list)
