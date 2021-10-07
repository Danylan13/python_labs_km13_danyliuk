import time


while True:
    string = str(input("Input elements in one line, using space: "))
    elements_list = list(string.split())

    comma = len(elements_list) - 2
    comma_insert = 0
    for i in range(len(elements_list)):
        if comma_insert < comma:
            elements_list[i] += ','
            comma_insert += 1
    if len(elements_list) != 1:
        elements_list.insert(-1, 'and')
    print(*elements_list)

    coc = input("Enter 'mi scusi' to exit or to continue the program: ")
    if coc.lower == 'mi scusi':
        print('mi scusi')
        break
    else:
        continue