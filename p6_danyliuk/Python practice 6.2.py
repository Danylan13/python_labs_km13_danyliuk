#hello

numericbuttons = {
    '1': ('.', ',', '?', '!', ':'),
    '2': ('a', 'b', 'c'),
    '3': ('d', 'e', 'f'),
    '4': ('g', 'h', 'i'),
    '5': ('j', 'k', 'l'),
    '6': ('m', 'n', 'o'),
    '7': ('p', 'q', 'r', 's'),
    '8': ('t', 'u', 'v'),
    '9': ('w', 'x', 'y', 'z'),
    '0': ' '
}

def get_key(value):
    for k, val1 in numericbuttons.items():
        for j in val1:
            if j == value:
                return k, val1.index(j)
    return None, None

while True:
    line = str(input('Input message: '))
    print('Phone variant: ', end = '')
    for i in range(len(line)):
        key, times = get_key(line[i].lower())
        print(str(key)*(times+1), end = '')

    coc = input('\nInput "mi scusi" to enter one more line of elements or another symbol to exit: ')
    if coc.lower() == 'mi scusi':
        continue
    else:
        print('The program is finish.')
        












