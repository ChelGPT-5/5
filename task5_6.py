def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Введите искомое число: "))
position = binary_search(my_list, n)

if position != -1:
    print("позиция числа = ", position + 1)
else:
    print("Число не найдено.")