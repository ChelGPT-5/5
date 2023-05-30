list_numb = [14, 7, 32, 14, 57, 27, 32, 44, 10, 9, 14, 7, 4]

duplicats = []
uniq = True

for number in list_numb:
    if list_numb.count(number) > 1:
        if number not in duplicats:
            duplicats.append(number)
        uniq = False

if uniq:
    print("Все числа в списке уникальны.")
else:
    print("числа в списке не уникальны.")
    print("Дублирующиеся элементы:", duplicats)
    for duplicate in duplicats:
        print(f"Количество повторений элемента {duplicate}: {list_numb.count(duplicate)}")