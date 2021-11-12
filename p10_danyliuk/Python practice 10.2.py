import numpy as np

years = np.arange(1900, 2020+1, 1)
years_list = list(years)

def finish():
    repeat = input('To exit, enter \'mi scusi\' in the input field: ')
    if repeat == "mi scusi":
        print("The work is completed.")

def leap_year_check(i):
    i = years_list[i]
    if i % 400 == 0:
        return i 
    else:
        if i % 100 != 0 and i % 4 == 0:
            return i

def list_append(i):
    return years_list[i]

def leap_years(years):
    numbers = range(0, len(years))
    leap_numbers = list(filter(leap_year_check, numbers))
    leap_years = list(map(list_append, leap_numbers))
    return leap_years

def month_days(function, year, month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    elif month == 2:
        if year in function:
            days = 29
        else:
            days = 28
    else:
        days = 31
    return days

print("Years from 1900 to 2020: ")
print(*leap_years(years_list), sep = ",")
print("-" * 149)
year = int(input("Enter a year that you want: "))
month = int(input("Enter a number of month that you want: "))
print("Number of days in the", month, "month", "in", year, "is", month_days(leap_years(years), year, month))
print("-" * 149)
finish()