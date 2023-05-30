N = int(input("Введите сумму телефона: "))
k = int(input("Введите сумму дня: "))

init_summ = 0
days = 0

while init_summ < N:
    days += 1
    if days % 7 != 0:  # Проверяем 7 день
        init_summ += k

print(f"Нужная сумма за {days} дней.")