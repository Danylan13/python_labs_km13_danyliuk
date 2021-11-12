salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

def finish():
    repeat = input('To exit, enter \'mi scusi\' in the input field: ')
    if repeat == "mi scusi":
        print("The work is completed.")

def func(arg_salary_list):
    salary_list_new = []
    salary_list_indexing = []
    for i in range(len(arg_salary_list)):
        salary_list_new.append(arg_salary_list[i] * 1.3)
        salary_list_indexing.append(salary_list_new[i] - arg_salary_list[i])
    return salary_list_new, salary_list_indexing

f = func(salary_list)

print("Salary table:")
for i in range(len(salary_list)):
    print(salary_list[i], round(f[0][i], 2), round(f[1][i], 2))
print("-" * 55)
finish()