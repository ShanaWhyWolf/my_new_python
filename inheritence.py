#Наследование
class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

#Класс "Работник" наследует свойства класса "Человек", потому что работник тоже человек, то что он работник расширяет его характеристики
class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name) #super() - вызов родительского класса. Теперь при создании дочернего элемента класса создается и родительский. Python запоминает цепочку наследования
        self.job_title = job_title
        # if hasattr(self, 'name'): #hasattr проверяет наличие атрибута у класса
        #     print('Yay')

    def do_work(self):
        return f'I am {self.job_title}'

    def isEmployee(self):
        return True



person = Person('Ann')
print(person.getName())
print(person.isEmployee())

worker = Employee('Ann', 'software engineer')
print(worker.do_work())
print(worker.isEmployee())

person = Person('Joe')
print(person.getName())
print(person.isEmployee())

if hasattr(worker, 'name'):
    print('Worker has a name')

