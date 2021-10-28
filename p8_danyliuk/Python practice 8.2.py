import math

# return's discriminant of sentense
def get_discriminant(a, b, c):
    try:
        D = b**2 - 4*a*c
        if D < 0:
            raise ValueError
        return D**0.5
    except ValueError:
        print("Помилка! Рівняння не має розв'язків (D < 0)")
        return -1

# print result of calculations
def get_result(a, b, c):
    try:
        d = get_discriminant(a, b, c)
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        if x1 == x2:
            print(f"\nx1 = x2 = {x1}")
        else:
            print(f"\nx1 = {x1}\nx2 = {x2}")
    except ZeroDivisionError:
        if b != 0:
            x = -c / b
            print(f"\nx = {x}")
        else:
            print("Помилка! Ділення на 0 (a = 0)")
    finally:
        return

# main menu
# input: a, b, c
# 'e' to exit after calculations
def main():
    print('Програма підрахунку коренів квадратного рівняння без попередніх перевірок')
    print('Квадратне рівння алгебраїчного виду: ax²+bx+c=...')
    print("-"*73)
    while True:
        try:
            a = float(input('Введіть число замість змінної "a": '))
            b = float(input('Введіть число замість змінної "b": '))
            c = float(input('Введіть число замість змінної "c": '))
    
        except ValueError:
            print("Помилка вводу даних! Повторіть спробу")
            continue
        try:
            get_result(a, b, c)

            answer = input('Для виходу введіть \'mi scusi\' в поле вводу: ')
            if answer == "mi scusi":
                print("-"*73)
                print("Роботу завершено")
                break
        except Exception as error:
            print(error)

# entry point
if __name__ == '__main__':
    main()