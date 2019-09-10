#Множественное наследование
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square:
    def __init__(self, height):
        self.height = height

    def perimeter(self):
        return self.height*4

    def area(self):
        return self.height**2



class RightPyramid(Triangle, Square): #сначала более приоритетный класс
    def __init__(self, base, slant_height):
        #super().__init__(base, slant_height) #если у родительского класса больше параметров, будет ругаться. Загадочная штука, можно и без нее
        self.base = base
        self.slant_height = slant_height
        self.height = base

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


pyramid = RightPyramid(4,5)
print(pyramid.perimeter())
print(pyramid.area())

#Method resolution ordering - регламентирует, как будет происходить выбор правильного метода
print(RightPyramid.__mro__) #покажет нам цепочку наследования (от самого приоритетного к менее приоритетным)

#Mixin - примешивание
class VolumeMixin:
    def volume(self):
        return self.area() * self.height

class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        return super().area()

    def surface_area(self):
        return super().area() * 6

cube = Cube(10)
print(cube.volume())