int_var = 42
float_var = 42.2
bool_var = True
bool_var_ = False
string_var = 'string'
big_string_var = '''
string1
string2
string3'''

# преобразование типов
bool(int_var)  # булевы
int(10.1)  # целое число, округлением
int('100')  # только если символы можно трактовать как числа
int(True)
float(12)  # плавающая точка
str(12)  # строка

# Структуры. Контейнерные типы (могут содержать в себе другие типы данных). Упорядоченные
my_list = [1, 3, 4, True, 'string', []]  # Список. Не обязательно все типы одинаковые
my_list[4]  # вызов определенного элемента списка
my_list[0:2]  # срез. вывод с x по y, не включая конечный элемент (y)
my_list.append(1000)  # Добавление элемента списка
my_list.pop(0)  # возвращает x элемент списка, удаляя его из списка
# длина любой цепочки (строка, список и т.д.)
len(my_list)

id(my_list)  # адрес ячейки памяти

a = my_list  # python работает с ссылками
a[0] = 33  # my_list[0] тоже изменится

my_tuple = (1, 3, 'aaa', False)  # неизменяемый массив (кортеж)

# копирование массива
my_list_new = my_list.copy()
my_list_new = my_list[:]

# Неупорядоченные структуры
my_dict = {  # dictionary, объект
    'name': 'Ann',
    'age': 'age'
}
# можно обращаться по имени элемента и менять тоже
my_dict['name']
# можно добавлять элементы
my_dict[34] = 'it is number'  # ключами могут быть как строки, так и числа, и кортежи. любые неизменяемые числа.
my_dict[(3,)] = 55
my_dict.items()  # озвращает список пар ключ - значение
# my_dict.items()
# dict_items([('name', 'Ann'), ('age', 'age'), (34, 'it is number'), ((3,), 55)])
my_dict.keys()  # возвращает все ключи
my_dict.values()  # возвращает все значения

# List comprehentions. Генерация списков
squared = [i ** 2 for i in my_list]  # i - переменная для итерации, получим все элементы массива my_list в квадрате
my_string_list = ['hello', 'world']
my_string_list_len = [len(word) for word in my_string_list]

# вывод на экран
hello = 'hello'
world = 'world'
template = f'{hello} + {world} + {3 * 4}'
# print(template)
# hello + world + 12
print(hello, world)

# Функции. Бывают именованные и безымянные
# Безымянные. Могут быть только в одну строку
my_func = lambda x: x ** 2
my_func_xy = lambda x, y: x ** y
my_func_xy = lambda x, y: (x ** y, x, y)
d = [(lambda word: word[0])(word) for word in
     my_string_list]  # (lambda word: word[0]) вызывает функцию для определения первого элемента массива


# Именованные
# def - ключевое слово для определения функции. После : идет тело функции
def function_name(x):
    return x


def is_allowed_to_smoke(
        age: int) -> bool:  #: int - задается тип входного элемента,  -> bool - задается тип выходного элемента
    if age < 18 or age > 69:
        return False  # отступы это очень важно, по ним определяется блок кода по вложенности, никаких обрамляющих скобок нет
    elif age == 18:
        return True
    else:
        return True


# В python есть логические выражения
# and - и
# or - или

# Циклы
def function_name(x):
    i = 0
    while i < 100:
        i += 1
        print[i]


def function_name(x):
    my_list = [1, 3, 4]
    for i in my_list:
        print(i)
    for i in range(10):
        print(i)
    for i in range(2, 10, 2):  # начальный элемент, конечный элемент (не включая), шаг
        print(i)
    end = 10
    i = 0
    while i != end:
        print(i)
        i += 1


is_allowed_to_smoke(18)
#Code -> Reformat Code, Auto-ident files автоформатирование