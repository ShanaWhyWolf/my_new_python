import time
from matplotlib import pyplot
from timeit import default_timer as timer
import math
import random
from sorting import bubble_sort

def measure_time(fn, *args):
    start = timer()
    fn(*args)
    end = timer()
    return end - start

string_multiply = lambda n, *args: 's' * n * 25000000
constant_lambda = lambda n, *args: 's' * 25000000

def linear_search(searched_list, *args):
    searched_item = searched_list[-1]
    for item in searched_list:
        if item == searched_item:
            return item
    return None

def binary_search(searched_list, *args):
    n = len(searched_list)
    left = 0
    right = n - 1
    searched_item = searched_list[-1]

    while left <= right:
        middle = (left + right) // 2
        if searched_item < searched_list[middle]:
            right = middle - 1
        elif searched_item > searched_list[middle]:
            left = middle + 1
        else:
            return middle

    return None


n_s = list(range(1, 500))
# outputs_linear = [measure_time(string_multiply, n) for n in n_s]
# outputs_constant = [measure_time(constant_lambda, n) for n in n_s]
# outputs_logs = [measure_time(math.log10, n) for n in n_s]
# outputs_linear_search = [measure_time(linear_search, list(range(n*250000))) for n in n_s]
# outputs_binary_search = [measure_time(binary_search, list(range(n*250000))) for n in n_s]
outputs_bubble_sort = [measure_time(bubble_sort, list(range(n, 1, -1))) for n in n_s]


if __name__ == '__main__': #Чтобы не запускалось при импорте этого файла в другой
    # pyplot.plot(n_s, outputs_linear)
    # pyplot.plot(n_s, outputs_logs)
    # pyplot.plot(n_s, outputs_constant)
    # pyplot.plot(n_s, outputs_linear_search)
    # pyplot.plot(n_s, outputs_binary_search)
    pyplot.plot(n_s, outputs_bubble_sort)
    #pyplot.legend(['outputs_linear', 'outputs_logs', 'outputs_constant', 'outputs_linear_search', 'outputs_binary_search'])
    pyplot.show()