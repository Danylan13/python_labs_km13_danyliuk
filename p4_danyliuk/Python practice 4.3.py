minutes = int(input("Enter number of minutes: "))
cost = 0
error = False
if minutes < 0:
    print("You have entered incorrect value")
elif minutes <= 50:
    cost = 100
elif minutes <= 100:
    cost = 150
elif minutes > 100:
    cost = 150 + (minutes - 100) * 2
if error == False:
    print("The cost of the tarrif plan is " + str(cost) + " UAH")