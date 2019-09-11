from random import shuffle, seed
#from folder.my_py import my_var - для импорта чего-то из подпапки
#seed(1) #всего одине вариант рандома
def bubble_sort(unsorted_list):
    swappings_found = True

    while swappings_found:
        swappings_found = False
        for i in range(len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i+1], unsorted_list[i]
                swappings_found = True

    return unsorted_list
if __name__ == '__main__':
    test_list = list(range(10))
    shuffle(test_list)
    print(test_list)
    sorted_list = bubble_sort(test_list)
    print(sorted_list)

#outputs_bubble_sort = [measure_time(bubble_sort, test_list) for n in n_s]
# pyplot.plot(n_s, outputs_binary_search)
# pyplot.legend(['outputs_linear', 'outputs_logs', 'outputs_constant', 'outputs_linear_search', 'outputs_binary_search'])
# pyplot.show()