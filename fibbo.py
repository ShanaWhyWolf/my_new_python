#рекурсия
#рекурсивная функция должно састоять из 2 блоков
#1 сама рекурсия, где функция вызывает себя
#2 выход из рекурсии
def getSum(piece):
    if len(piece) == 0:
        return 0
    else:
        return piece[0] + getSum(piece[1:])

def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n-1) + fibo(n - 2)

for i in range(10):
    print(fibo(i))

print(fibo(20))

#рекурсия оптимальна по времени, но сильно жрет память, т.к. требует область памяти для каждого вызова

