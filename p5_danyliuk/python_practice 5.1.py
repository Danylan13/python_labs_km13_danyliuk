salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

salary_list_new = list()
salary_list_indexing = list()

for i in range(len(salary_list)):
    salary_new = salary_list[i] * 1.3
    salary_list_new.append(salary_new)
    salary_indexing = salary_list_new[i] - salary_list[i]
    salary_list_indexing.append(salary_indexing)

print("Salary table:")
for i in range(len(salary_list)):
    print(salary_list[i], round(salary_list_new[i], 2), round(salary_list_indexing[i], 2))