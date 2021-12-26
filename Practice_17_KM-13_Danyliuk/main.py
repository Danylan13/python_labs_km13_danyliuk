from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, ln, lg

requirements = """
ВИМОГИ ДО ВВЕДЕННЯ
Для корректного вводу використовуйте наступні функції:
(" - fact  - Факторіал числа")
(" - exp2  - Квадрат числа")
(" - exp3  - Куб числа")
(" - root2 - Квадратний корінь з числа")
(" - root3 - Кубічний корінь з числа")
(" -  log  - Логарифм числа до основи")
(" -  ln   - Натуральний логарифм числа")
(" -  lg   - Десятковий логарифм числа")
"""
print(requirements)
print('-' * 55)


def finish():
    print("-" * 47)
    repeat = input('Щоб вийти, введіть \'mi scusi\' у відведене поле: ')
    if repeat == "mi scusi":
        return True
    else:
        return False


def ask_user(text, text_about_the_warning, func, type=float):
    while True:
        try:
            n = input(text)
            if not func(n):
                raise ValueError
            break
        except ValueError:
            print(text_about_the_warning)
    return type(n)


def main():
    while True:
        choice = input("Введіть функцію, яку ви хочете використовувати: ")
        try:
            if choice == 'fact':
                n = ask_user("Введіть число: ", "Ви повинні ввести ціле число!!!", lambda x: int(x) >= 0, int)
                print(f"Факторіал числа {n} --- {fact(n)}")
            elif choice == 'exp2':
                n = ask_user("Введіть число: ", "Ви маєте ввести число!!!", lambda x: float(x))
                print(f"Квадрат числа {n} --- {exp2(n)}")
            elif choice == 'exp3':
                n = ask_user("Введіть число: ", "Ви маєте ввести число!!!", lambda x: float(x))
                print(f"Куб числа {n} --- {exp3(n)}")
            elif choice == 'root2':
                n = ask_user("Введіть число: ", "Ви повинні ввести число, що >= 0.", lambda x: float(x) >= 0)
                print(f"Квадратний корінь числа {n} --- {root2(n)}")
            elif choice == 'root3':
                n = ask_user("Введіть число: ", "Ви маєте ввести число!!!", lambda x: float(x))
                print(f"Кубічний корінь числа {n} --- {root3(n)}")
            elif choice == 'log':
                a = ask_user("Введіть основу логарифма: ", "Ви повинні ввести додатне число, відмінне від 1!!!",
                             lambda x: float(x) > 0 and float(x) != 1)
                b = ask_user("Введіть число: ", "Потрібно ввести додатне число!!!.", lambda x: float(x) > 0)
                print(f"Логарифм числа {b} по основі {a} --- {log(a, b)}")
            elif choice == 'ln':
                b = ask_user("Введіть число: ", "Потрібно ввести додатне число!!!", lambda x: float(x) > 0)
                print(f"Натуральний логарифм числа {b} --- {ln(b)}")
            elif choice == 'lg':
                b = ask_user("Введіть число: ", "Потрібно ввести додатне число!!!", lambda x: float(x) > 0)
                print(f"Десятковий логарифм числа {b} --- {lg(b)}")
            else:
                raise ValueError
        except ValueError:
            print("Вам необхідно ввести одну із запропонованих функцій!!!")
        else:
            result = finish()
            if result:
                break


if __name__ == '__main__':
    main()