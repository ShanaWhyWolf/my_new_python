# f = open('text.txt') #Открываем файл
# content = f.read() #Читаем соджержимое в переменную
# f.close() #Закрываем файл. Незакрытые файлы остаются в ОЗУ, можно потерять доступ к файлу, если не закрыть

#Modes of opening files:
# 'r' - open for reading
# 'w' - open for writing, truncating the file first
# 'x' - open for exclusive creation, failing if the file already exists
# 'a' - open for writing, appending to the end of the file if it exsts
# 'b' - binary mode
# 't' - text mode
#  '+' - open disk file for updating


#Контекстный менеджер
with open('text.txt', 'rt') as f: #'rt' - только для чтения в текстовом режиме
    content = f.readlines() #возвращает массив строк
    # Файл автоматически закрывается

print(content)

#запись в файл
with open('text.txt', 'wt') as f: #'rt' - только для чтения в текстовом режиме
    content = f.write('hello me\n') #если вывести после этого content, вернется кол-во записанных символов

print(content)

#дозапись в файл
with open('text.txt', 'a') as f: #'rt' - только для чтения в текстовом режиме
    content = f.write('hello world') #если вывести после этого content, вернется кол-во записанных символов

print(content)

#JSON javascript object notation. Большая строка, отформатированная под словарь python (в js это объект)
import json
my_object = [{'name': 'Ann', 'age': '30', 'married': None}, {'name': 'Jim', 'age': '53', 'married': True}]
json_string = json.dumps(my_object)
new_object = json.loads(json_string)
print(json_string)

with open('my.json', 'r') as f:
    content = f.read()
    my_object = json.loads(content)
    print(my_object['web-app'].keys())

#таблицы. CSV файлы. Comma separated values
import csv
somedict = dict(raymond = 'red', rachel = 'blue', matthew = 'green')
somedict = dict(raymond = 'brown', rachel = 'black', matthew = 'white')

with open('mycsvfile.csv', 'wt') as f:
    writer = csv.DictWriter(f, somedict.keys())
    writer.writeheader()
    writer.writerow(somedict)
    writer.writerow(somedict)

#Pickle
import pickle
class Foo:
    bar = 'buzz'

    def change_bar(self, new_bar):
        self.bar = new_bar

foo = Foo()
foo.buzz = 'bar'

with open('my_pickle.pk', 'wb') as f:
    pickle.dump(foo, f)

with open('my_pickle.pk', 'rb') as f:
    new_foo = pickle.load(f)
    print(new_foo.bar)
    new_foo.change_bar('new bar')
    print(new_foo.bar)
