from math import *



class Figure:
    sides_count = 0

    def __init__(self, __sides, __color):
        self.__sides = []
        self.__color = [(0, 0, 0)]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        colors = (r, g, b)
        self.__color = all(isinstance(i, int) and (0 <= i < 255) for i in colors)
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        return self.__color


    def __is_valid_sides(self, sides):
        for i in sides:
            if isinstance(i, int) and i > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = self.sides_count / (2 * 3.14)

    def get_square(self, s_circle):
        self.s_circle = (3.14 * self.__radius ** 2)
        return (s_circle)

# c = Circle((200, 200, 40), 15)
# c.get_square(s_circle=15)
# print(c.get_square(s_circle=15))


# f = Figure((200, 200, 100), 10)
# f.set_color(250, 250, 250)







