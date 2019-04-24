#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:
    size_numbers = 90
    size_line = 5
    numbers_of_card_line = []
    numbers = []
    count_line = 3
    all_numbers_in_card = []
    whose: str

    def __init__(self, whose):
        self.all_numbers_in_card = []
        self.generate_card()
        self.whose = whose

    def generate_line(self):
        self.numbers_of_card_line = []
        for _ in range(self.size_line):
            number = random.randint(1, 90)

            if len(self.all_numbers_in_card) == 0:
                if number not in self.numbers_of_card_line :#or number not in [item for sublist in self.all_numbers_in_card for item in sublist]:
                    self.numbers_of_card_line.append(number)
                else:
                    while number in self.numbers_of_card_line:# or number in [item for sublist in self.all_numbers_in_card for item in sublist]:
                        number = random.randint(1, 90)
                    self.numbers_of_card_line.append(number)
            else:
                if number not in self.numbers_of_card_line and number not in [item for sublist in self.all_numbers_in_card for item in sublist]:
                    self.numbers_of_card_line.append(number)
                else:
                    while number in self.numbers_of_card_line or number in [item for sublist in self.all_numbers_in_card for item in sublist]:
                        number = random.randint(1, 90)
                    self.numbers_of_card_line.append(number)

        self.numbers_of_card_line = sorted(self.numbers_of_card_line)
        return self.numbers_of_card_line

    def clear(self, smth):
        self.smth = []

    def generate_card(self):
        for _ in range(self.count_line):
            self.all_numbers_in_card.append(self.generate_line())
            self.clear(self.numbers_of_card_line)

    def draw_card(self):
        empty = '   '
        count_empty = 0
        print(f'--{self.whose}---')
        for st in self.all_numbers_in_card:
            for el in st:
                if random.randint(1,2) == 1 and count_empty < 5:
                    print(empty, end='')
                    count_empty += 1
                if el < 10:
                    print(' ', end='')
                print(el, end=' ')
                count_empty = 0
            print('')
        print('--------------------------')

    def cross_number(self, number):
        for st in self.all_numbers_in_card:
            for i, el in enumerate(st):
                if number == el:
                    st[i] = '-'


class Bochonok:
    seq = []

    def __init__(self):
        self.generate()

    def generate(self):
        self.seq = [x for x in range(1, 91)]
        random.shuffle(self.seq)
        return self.seq


class Game:
    card1 = Card('---- Ваша карточка --')
    card2 = Card(' Карточка компьютера ')
    bochonok = Bochonok()

    def scenario(self):
        count1, count2 = 0, 0
        for i, f in enumerate(self.bochonok.seq):
            if count1 == 15:
                print('Вы выиграли')
            if count2 == 15:
                print('Компьютер выиграл')
            print(f'Новый бочонок: {f} (осталось {len(self.bochonok.seq) - i - 1})')
            self.card1.draw_card()
            self.card2.draw_card()
            print('Зачернуть цифру?(y/n)')

            if f in [item for sublist in self.card2.all_numbers_in_card for item in sublist]:
                self.card2.cross_number(f)
                count2 += 1
            desicion = input()
            if desicion == 'y':
                if f in [item for sublist in self.card1.all_numbers_in_card for item in sublist]:
                    self.card1.cross_number(f)
                    count1 += 1
                    continue
                else:
                    print('Проигрыш')
                    break
            elif desicion == 'n':
                if f in [item for sublist in self.card1.all_numbers_in_card for item in sublist]:
                    print('Проигрыш')
                    break
                else:
                    continue

    def __init__(self):
        self.scenario()
#        self.card1 = Card()
#        self.bochonok = Bochonok()
#        self.card2 = Card()


game = Game()