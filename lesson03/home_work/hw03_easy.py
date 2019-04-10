# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    number_int = number * (10 ** (ndigits+1))
    last_digit = number_int % 10
    if last_digit > 4:
        number_int = number_int//10 + 1
    number_int = number_int / (10 ** ndigits)
    return number_int


print(my_round(2.2314567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    len_ticket = len(str(ticket_number))
    if len_ticket != 6:
        return False
    else:

        def sum_digit(digit):
            sum_d = 0
            for el in digit:
                sum_d += int(el)
            return sum_d
        first_half = str(ticket_number)[:int(len_ticket/2)]
        second_half = str(ticket_number)[int(len_ticket/2):]
        if sum_digit(first_half) == sum_digit(second_half):
            return True
        else:
            return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
