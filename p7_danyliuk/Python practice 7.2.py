rgb_code = '#{}{}{}'

def finish():
    repeat = input('\nInput "mi scusi" to enter one more line of elements or another symbol to exit: ')


def check(color):
    if color.isdigit():
        if 0 <= int(color) <= 255:
            return True
    print('The number is not in the range from 0 to 255!')
    return False
enter = "Enter {} a number between 0 to 255: "


def convert(color):
    color = int(color)
    numbers = []
    for i in range(0,10):
        numbers.append(i)
    numbers += 'A', 'B', 'C', 'D', 'E', 'F'
    c = str(numbers[color//16])
    c += str(numbers[color%16])
    return c


def job():
    while True:
        red = input('Enter the value of red color: ')
        a = check(red)
        if not a:
            print('Enter an integer number from 0 to 255!')
            continue
        red = convert(red)
        break
    while True:
        green = input('Enter the value of green color: ')
        a = check(green)
        if not a:
            print('Enter an integer number from 0 to 255!')
            continue
        green = convert(green)
        break
    while True:
        blue = input('Enter the value of blue color: ')
        a = check(blue)
        if not a:
            print('Enter an integer number from 0 to 255!')
            continue
        blue = convert(blue)
        break
    print('The Hex color: ' + rgb_code.format(red, green, blue))
    finish()

job()