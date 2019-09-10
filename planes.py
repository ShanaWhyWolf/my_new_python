#Упражнение на множественное наследование
class Plane:
    def __init__(self, name, number_of_engines=2, number_of_wings=2): #можно указывать параметры по умолчанию
        self.name = name
        self.number_of_engines = number_of_engines
        self.number_of_wings = number_of_wings

    def liftoff(self): #взлет
        raise NotImplementedError #возбудить исключение. Говорит о том, что она должна быть у дочернего класса и должна обязательно быть

    def landing(self): #посадка
        raise NotImplementedError


    def get_wings_number(self):
        return self.number_of_wings

class ColorSetMixing:
    color = 'Green'

    def set_color(self, color):
        self.color = color

#Гражданский самолет
class CivilPlane(ColorSetMixing, Plane):
    def __init__(self, name, passengers_number):
        super().__init__(name)
        self.passengers_number = passengers_number

    def liftoff(self):
        print(f'{self.name} if lifting off')

    def landing(self): #посадка
        print(f'{self.name} is landing')

    def enable_music(self):
        print(f'There is music playing in {self.name}')

    def toggle_light(self):
        self.light += 1
        self.light_is_on = self.light & 1
        if self.light_is_on:
            print(f'There is light in {self.name}')
        else:
            print(f'There is light off {self.name}')



# Военный самолет
class WarPlane(ColorSetMixing, Plane):
    def __init__(self, name, bombs_number):
        super().__init__(name)
        self.bombs_number = bombs_number

    def liftoff(self):
        print(f'{self.name} if lifting off')

    def landing(self):  # посадка
        print(f'{self.name} is landing')

    def do_bombing(self):
        for bombs in range(self.bombs_number):
            self.bombs_number -= 1
            print(f'Bombing! There are {self.bombs_number} left')
        print('War is bad')

    def launch_catapult(self):
        print(f'Catapult was launched')


civil_plane = CivilPlane('Boeing', 150)
civil_plane.liftoff()
civil_plane.set_color('Blue')

war_plane = WarPlane('Me', 10)
war_plane.do_bombing()