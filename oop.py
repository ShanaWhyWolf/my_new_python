# Классы на python. Имеют атрибут и метод.
class Car:  # Классы называются с большой буквы
    number_of_wheels = 4

    @classmethod #Декоратор, чтобы было понятно, что относится к классу
    def count_axis_number(cls): #cls - ссылка на класс
        return cls.number_of_wheels / 2
    #classmethod - можно передавать ссылки на класс или экземпляр
    #staticmethod - чистая функция, не принимает ссылки на экземпляр или класс

    # Конструктор. Функция, которая создает экземпляр класса. В python такого нет, но есть инициализация
    # Можно это не задавать, тогда оно вызовется автоматически
    # def __init__(self): #self - это необходимый аргумент, который указывает на экземпляр класса. (ссылка на объект) Можно передавать другое, но принято self
    #     pass #pass - ничего не делать
    def __init__(self, name):  # При создании присваиваем объекту имя. Тут задаются свойства экземпляра, а не класса
        self.name = name

    def drive(self):
        print(f'{self.name} is driving')


print(Car.count_axis_number())

class Plane:
    number_of_engines = 2

    def __init__(self, name):
        self.name = name

    def liftoff(self): #взлет
        print(f'{self.name} if lifting off')

    def landind(self): #посадка
        print(f'{self.name} is landing')

    @staticmethod
    def get_wings_number(wings_number):
        return wings_number