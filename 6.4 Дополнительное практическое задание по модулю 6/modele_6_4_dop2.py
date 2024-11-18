import math
class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color (self):
        return self.__color

    def __is_valid_color (self, r, g, b):
        self.valid_color = False
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r <= 250 and 0 <= self.g <= 250 and 0 <= self.b <= 250:
            self.valid_color = True

    def set_color (self, r, g, b):
        Figure.__is_valid_color(self, r, g, b)
        if self.valid_color == True:
            self.__color = [r, g, b]
        else:
            self.__color = [*self.rgb]

    def __is_valid_sides (self, *side):
        if isinstance(self,Cube):
            corect = []
            if len(side) == len(self.__sides):
                for i in side:
                    if i <= 0 or not isinstance(i, int):
                        corect.append(0)
            if all(corect) == True:
                self.valid_sides = True
            if all(corect) == False:
                self.valid_sides = False
        if isinstance(self, Circle):
            if len(side) == Circle.sides_count:
                self.valid_sides = True
            else:
                self.valid_sides = False
        if isinstance(self, Triangle):
            corect = []
            if len(side) == Triangle.sides_count:
                for i in side:
                    if i <= 0 or not isinstance(i, int):
                        corect.append(0)
            if all(corect) == True:
                self.valid_sides = True
            if all(corect) == False:
                self.valid_sides = False

    def get_sides (self):
        return self.__sides

    def set_cube (self, side):
        self.__sides = side

    def set_circle (self, side):
        self.__sides = side

    def set_triangle (self, side):
        self.__sides = side

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        if isinstance(self, Cube):
            if len(self.new_sides) == Cube.sides_count:
                self.__sides = list(new_sides)
        if isinstance(self, Circle):
            if len(self.new_sides) == Circle.sides_count:
                self.__sides = list(new_sides)
            else:
                self.__sides = [*self.side]
        if isinstance(self, Triangle):
            if len(self.new_sides) == Triangle.sides_count:
                self.__sides = list(new_sides)
            else:
                self.__sides = ([*self.side]*Triangle.sides_count)

class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *side):
        super().__init__()
        if self._Figure__sides == []:
            self.set_circle(side)

    def get_square (self):
        a = self._Figure__sides[0]
        self.S = ((a ** 2) / 4 * math.pi)
        return self.S

class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *side):
        super().__init__()
        self.rgb = rgb
        self.side = side
        if len(side) == 1 and isinstance(side[0], int):
            self.set_cube([side[0]] * Cube.sides_count)

    def get_volume (self):
        a = self._Figure__sides[0]
        return a ** 3

class Triangle(Figure):
    sides_count = 3
    def __init__(self, rgb, *side):
        super().__init__()
        if self._Figure__sides == []:
            self.set_triangle(side)
        self.rgb = rgb
        self.side = side

    def get_square (self):
        a = self._Figure__sides[0]
        self.S = ((a**2 * 3**0.5)/4)
        return self.S

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

trian1 = Triangle((222, 35, 130), 6)
trian1.set_color(59, 106, 217) # Изменится
print("изменение цвета треугольника", trian1.get_color())
trian1.set_sides(15, 15, 15) # Изменится
print("изменение размера треугольника", trian1.get_sides())
print("площадь треугольника",trian1.get_square())
print("площадь куба",cube1.get_volume())
print("площадь круга",circle1.get_square())



