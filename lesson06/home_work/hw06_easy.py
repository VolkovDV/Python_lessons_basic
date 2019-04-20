# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    x: int
    y: int


class Triangle:

    def __init__(self, a=Point(6, 9), b=Point(0, 0), c=Point(-9, -6)):
        self.a = a
        self.b = b
        self.c = c

    def length_side(self, a, b):
        return ((b.x - a.x)**2 + (b.y - a.y)**2)**0.5

    @property
    def area(self):
        return math.fabs(((self.b.x-self.a.x)*(self.c.y - self.a.y) -
                          (self.c.x - self.a.x)*(self.b.y-self.a.y)) / 2)

    @property
    def perimeter(self):
        return self.length_side(self.b, self.c) + self.length_side(self.a, self.b) + self.length_side(self.c, self.a)

    @property
    def tr_h(self):
        pp = self.perimeter / 2
        return (2 * ((pp * (pp - self.length_side(self.a, self.b)) * (pp - self.length_side(self.b, self.c))
                      * (pp - self.length_side(self.c, self.a))) ** (1 / 2))) / self.length_side(self.a, self.b)

    a: Point
    b: Point
    c: Point


tr = Triangle()
print(tr.area)
print(tr.perimeter)
print(tr.tr_h)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EqSideTr(Triangle):
    a: Point
    b: Point
    c: Point
    d: Point

    def __init__(self, a=Point(2, 1), b=Point(4, 5), c=Point(7, 5), d=Point(9,1)):
        self.a, self.b, self.c, self.d = a, b, c, d

    @property
    def parallel(self):
        if (self.a.y - self.b.y) == self.c.y - self.d.y:
            return 'ab||cd'
        elif self.b.y - self.c.y == self.a.y - self.d.y:
            return 'bc||ad'
        else:
            return False

    @property
    def check_fig(self):
        if self.length_side(self.a, self.b) == self.length_side(self.c, self.d) and self.parallel == 'bc||ad' or \
                self.length_side(self.b, self.c) == self.length_side(self.d, self.a) and self.parallel == 'ab||cd':
            return True
        else:
            return False

    @property
    def perimeter(self):
        return (self.length_side(self.b, self.c) + self.length_side(self.a, self.b) +
                self.length_side(self.c, self.d) + self.length_side(self.d, self.a))

    @property
    def area(self):
        if self.check_fig:
            if self.parallel == 'ab||cd':
                return ((self.length_side(self.a, self.b) + self.length_side(self.c, self.d))/2) * \
                       (self.length_side(self.b, self.c)**2 - ((self.length_side(self.a, self.b) -
                                                                self.length_side(self.c, self.d))**2/4))**(1/2)
            elif self.parallel == 'bc||ad':
                return ((self.length_side(self.a, self.d) + self.length_side(self.b, self.c))/2) * \
                       (self.length_side(self.b, self.a)**2 - ((self.length_side(self.a, self.d) -
                                                                self.length_side(self.b, self.c))**2/4))**(1/2)
        else:
            return False


tr = EqSideTr()
print(tr.check_fig)
print(tr.perimeter)
print(tr.area)
