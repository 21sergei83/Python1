n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
k = int(input("Введите количество долек, которое нужно отломить: "))

if k > n * m:
    print("Нельзя отломить больше долек, чем есть в шоколадке!")
else:
    possible = False
    for a in range(1, n):
        b = n - a
        if k == a * m + b * m:
            possible = True
            break
    for a in range(1, m):
        b = m - a
        if k == a * n + b * n:
            possible = True
            break
    if possible:
        print("Можно отломить", k, "долек!")
    else:
        print("Нельзя отломить", k, "долек!")