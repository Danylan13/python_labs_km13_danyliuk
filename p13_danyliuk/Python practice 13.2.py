files = []
for i in range(1880, 2020):
    files.append(f"archive\yob{i}.txt")

dict1_M = {}
dict1_F = {}
for i in files:
    dict_M = {}
    dict_F = {}
    file = open(i, "r")
    for string in file:
        string = string.split(",")
        if string[1] == "M":
            dict_M[string[0]] = int(string[2])
        else:
            dict_F[string[0]] = int(string[2])
    max_value = max(dict_M.values())
    max_value1 = max(dict_F.values())
    for j in dict_M.keys():
        if dict_M[j] == max_value:
            dict1_M[j] = dict1_M.get(j, 0) + 1
    for j in dict_F.keys():
        if dict_F[j] == max_value1:
            dict1_F[j] = dict1_F.get(j, 0) + 1

list_M = dict1_M.values()
list_F = dict1_F.values()

print("-" * 30)
print("The most popular males name:")
sorted_list_M = sorted(dict1_M.items(), key = lambda kv: kv[1], reverse = True)
for i in sorted_list_M:
    print(f"{i[0]}: {i[1]}")
for i in sorted_list_M:
    for j in dict1_M.keys():
        if dict1_M[j] == i:
            print(j, i)
print("-" * 30)
print("The most popular females name:")
sorted_list_F = sorted(dict1_F.items(), key = lambda kv: kv[1], reverse = True)
for i in sorted_list_F:
    print(f"{i[0]}: {i[1]}")
for i in sorted_list_F:
    for j in dict1_F.keys():
        if dict1_F[j] == i:
            print(j, i)