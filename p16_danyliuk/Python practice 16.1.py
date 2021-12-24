def finish():
    print("-" * 47)
    repeat = input('Щоб вийти, введіть \'mi scusi\' у відведене поле: ')
    if repeat == "mi scusi":
        print('Робота завершена')
    else:
        work()


def checker_book(text):
    """
    Checking the correctness of entering numbers.
    """
    value = input(text)
    while type(value) != int:
        try:
            if int(value) < 1 or int(value) > 1280:
                value = "a"
            value = int(value)
        except:
            value = input("Введіть кількість сторінок книги (1-1280): ")
    return int(value)


def checker_notebook(text):
    """
    Checking the multiplicity of the number of pages in the notebook.
    """
    value = input(text)
    while type(value) != int:
        try:
            if int(value) != 16 and int(value) != 24 and int(value) != 32:
                value = "a"
            value = int(value)
        except:
            value = input("Введіть кількість сторінок кожного зошита (16, 24 або 32): ")
    return int(value)


def notebooks(book, notebook):
    """
    Creating a function that takes the integer entered by the user and returns a list of nested lists.
    """
    notebooks = int(book / notebook)
    print("Кількість зошитів у книзі:", notebooks)
    list_of_notebooks = []
    for j in range(notebooks):
        a = j * notebook
        a = [i for i in range(a + 1, notebook + a + 1)]
        b = []
        n = int(notebook / 2 - 1)
        for i in range(0, n, 2):
            b += [a[- i - 1], a[i], a[i + 1], a[- i - 2]]
        list_of_notebooks.append(b)
    return list_of_notebooks


def decorator(choice, func):
    """
    Creating a decorator that accepts arguments at the entrance "1(True)" and "0(False)".
    """
    def additional_list(func):
        print(func)
    if choice:
        return additional_list(func)
    return print(*func, sep = "\n")

def work():
    while True:
        try:
            book = checker_book("Введіть кількість сторінок книги (не більше 1280): ")
            notebook = checker_notebook("Введіть кількість сторінок кожного зошита (16, 24 або 32): ")
            if book % notebook != 0:
                raise ValueError
            break
        except ValueError:
            print("Кількість сторінок книги має бути кратною кількості сторінок блокнота.")
    while True:
        try:
            print("-" * 108)
            choice = int(input('Якщо ви хочете використовувати додаткову функцію, введіть "1(True)". В іншому випадку введіть "0(False)".: '))
            if choice != 1 and choice != 0:
                raise ValueError
            break
        except ValueError:
            print('Потрібно ввести "0" або "1".')
    if choice == 1:
        choice = True
    else:
        choice = False
    decorator(choice, notebooks(book, notebook))
    finish()
work()