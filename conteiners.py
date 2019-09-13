from collections import namedtuple, deque, OrderedDict, defaultdict, Counter

#Именованный кортеж
Point = namedtuple('Point', ['x', 'y'])
point = Point(11, 22) #point x=11, y=22
point.x + point.y
print(point)

#Двусторонняя очередь. Deque. Можно добавлять элементы как справа, так и слева
my_deque = deque()
my_deque.append(10)
my_deque.appendleft(20)
print(my_deque)
print(len(my_deque))
print(my_deque.pop())
print(my_deque)
my_deque.append(10)
print(my_deque)
print(my_deque.popleft())
print(my_deque)
my_deque.rotate()

#Ordered dict. Упорядоченный словарь
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

#Default dict
def dummy():
    return 11 #значение по умолчанию

my_dict = defaultdict(dummy) #принимает функцию
my_dict['key'] = 'wwwww'
print(my_dict)
print(my_dict['key'])
print(my_dict['ee'])

#Counter. Счетчик
counter = Counter({'aw': 4, 'counter': 3, 'spam': 2, 'egg': 1})
print(counter.most_common(1)) #возвращает самое большое
print(Counter('abracadabra').most_common(3))
c = Counter(a=4, b=2, c=0, d=2)
d = Counter(a=1, b=2, c=3, d=4)
print(c + d)
