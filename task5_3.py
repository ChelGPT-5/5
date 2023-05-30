n = int(input("Введите количество чисел Фибоначчи: "))


fibon = [1, 1] # первые два числа равны 1

for i in range(2, n):
    next_number = fibon[i - 1] + fibon[i - 2]
    fibon.append(next_number)

for number in fibon:
    print(number, end=' ')
