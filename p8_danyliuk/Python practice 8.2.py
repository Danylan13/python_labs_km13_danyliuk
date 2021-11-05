import math

def get_discriminant(a, b, c):
    try:
        D = b**2 - 4*a*c
        if D < 0:
            raise ValueError
        return D**0.5
    except ValueError:
        print("Error! The equation has no solutions (D < 0)")
        return -1

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
            print("Error! Division by 0 (a = 0)")
    finally:
        return

def main():
    print('The program for calculating the roots of a quadratic equation without prior checks')
    print('Quadratic equation of algebraic form: ax²+bx+c=...')
    print("-"*73)
    while True:
        try:
            a = float(input('Enter a number instead of a variable "a": '))
            b = float(input('Enter a number instead of a variable "b": '))
            c = float(input('Enter a number instead of a variable "c": '))
    
        except ValueError:
            print("Data entry error! Please try again")
            continue
        try:
            get_result(a, b, c)

            repeat = input('To exit, enter \'mi scusi\' in the input field: ')
            if repeat == "mi scusi":
                print("-"*73)
                print("The work is completed")
                break
        except Exception as error:
            print(error)

if __name__ == '__main__':
    main()
