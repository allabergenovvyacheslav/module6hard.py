# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать
# методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы
# взаимодействия (методы) - геттеры и сеттеры.
#
# Подробное ТЗ:
#
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность
# переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые
# числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие
# значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет
# остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если
# все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех
# остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно
# sides_count, то не изменять, в противном случае - менять.
#
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
# Метод get_square возвращает площадь треугольника.
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно
# sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = color
        self.filled = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        colors = (r, g, b)
        for i in colors:
            if not isinstance(i, int) or i <= 0 or i >= 255:
                return False
            else:
                return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for i in sides:
            if isinstance(i, tuple) and len(i) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        if self.__sides != self.sides_count:
            return [self.__sides[0]] * self.sides_count
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius, *sides):
        super().__init__(color, *sides)
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, height, *sides):
        super().__init__(color, *sides)
        self.__height = height
        self.__sides = sides

    def get_square(self):
        return 0.5 * self.__height * sum(self.__sides)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = len(sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle1 = Triangle((200, 150, 60), 5, 5)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    triangle1.set_color(260, 250, 40)
    print(triangle1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    triangle1.set_sides(8, 8)
    print(triangle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))
    print(circle1.get_square())

    # Проверка объёма (куба):
    print(cube1.get_volume())

    print(triangle1.get_square())

    # [55, 66, 77]
    # [222, 35, 130]
    # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    # [15]
    # 15
    # 216
