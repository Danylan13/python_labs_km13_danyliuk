while True:
    try:
        n = int(input('Введіть ступінь полінома: '))
        if n < 0 and n != int:
            raise ValueError
        break
    except ValueError:
        print('Ви повинні ввести додатне ціле число!!!')
a = [1]
for i in range(n + 1):
    print(*a)
    b = [1]
    b += [a[j] + a[j + 1] for j in range(len(a) - 1)] + [1]
    a = b