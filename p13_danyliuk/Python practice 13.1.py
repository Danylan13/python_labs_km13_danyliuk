import string

list_of_amounts = []
all_letters = 0
list_of_percents = []

for i in string.ascii_lowercase:
    amount_of_letter = 0
    file = open("gadsby.txt", "r")
    for line in file:
        line = line.lower()
        amount_of_letter += line.count(i)
    list_of_amounts.append(amount_of_letter)
    all_letters += amount_of_letter
    file.close()

for i in range(len(list_of_amounts)):
    a = round(list_of_amounts[i] * 100 / all_letters, 3)
    list_of_percents.append(a)

sorted_list_of_percents = sorted(list_of_percents)

for i in range(0, 5):
    indx1 = list_of_percents.index(sorted_list_of_percents[i])
    print(f"{string.ascii_lowercase[indx1]} === {sorted_list_of_percents[i]} %")
for i in range(-6, -1):
    indx1 = list_of_percents.index(sorted_list_of_percents[i])
    print(f"{string.ascii_lowercase[indx1]} === {sorted_list_of_percents[i]} %")
