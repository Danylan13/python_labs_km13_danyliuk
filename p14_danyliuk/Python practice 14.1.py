import csv
import re

with open('compilation.csv', 'w', newline = '') as csvfile:
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'Song': 'KING SCAR',
                     'Year': '2017'})
    writer.writerow({'Song': 'Hey Ya!',
                     'Year': '2003'})
    writer.writerow({'Song': "Day 'N' Night",
                     'Year': '2008'})
    writer.writerow({'Song': 'Rage The Night Away',
                     'Year': '2014'})
    writer.writerow({'Song': 'Pursuit Of Happiness',
                     'Year': '2007'})
    writer.writerow({'Song': "They Just Haven`t",
                     'Year': '2016'})
    writer.writerow({'Song': 'Through to you',
                     'Year': '2020'})

new_csvfile = []
with open('compilation.csv', newline = '') as csvfile:
    lines = csvfile.readlines()
    print('The name of the file is :', csvfile.name)
    for line in lines:
        new_line = line.replace('\n', '')
        split = re.split(',',new_line)
        new_csvfile.append(split)
        print(', '.join(split))
                     