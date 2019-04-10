# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    list_fib = [1, 1]
    if m <= 1:
        return list_fib[m]
    else:
        for i in range(2, m + 1):
            list_fib.append(list_fib[i - 1] + list_fib[i - 2])
        return list_fib[n-1:m]


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for _ in origin_list:
        for i, el in enumerate(origin_list):
            if i < len(origin_list)-1:
                if el > origin_list[i+1]:
                    origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
    return origin_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, obj):
    result = []
    for el in obj:
        if func(el):
            result.append(el)
    return result


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math


def parallelogramm(a1, a2, a3, a4):
    def len_side(point_one, point_two):
        return math.sqrt((point_two[0]-point_one[0])**2 + (point_two[1] - point_one[1])**2)
    a = [a1, a2, a3, a4]
    a.sort()
    if len_side(a[0], a[1]) == len_side(a[2], a[3]) and len_side(a[0], a[2]) == len_side(a[1], a[3]):
        return True
    else:
        return False


A1, A2, A3, A4 = [2, 4], [-3, 7], [-6, 6], [-1, 3]
print(parallelogramm(A1, A2, A3, A4))

