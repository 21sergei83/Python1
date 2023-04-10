ticket = int(input("Введите номер билета: "))

# разбиваем номер на цифры
digits = []
while ticket > 0:
    digit = ticket % 10
    digits.append(digit)
    ticket //= 10

# считаем суммы
first_sum = sum(digits[:3])
second_sum = sum(digits[3:])

# проверяем на счастливость
if first_sum == second_sum:
    print("Билет счастливый!")
else:
    print("Билет несчастливый :(")
