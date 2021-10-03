a = float(input("Enter a number!: "))
if 0 < a < 2:
    print("You have entered incorrect value")
elif 0 < a < 2:
    print("Descriptor - Micro")
elif 2 <= a < 3:
    print("Descriptor - Very minor")
elif 3 <= a < 4:
    print("Descriptor - Minor")
elif 4 <= a < 5:
    print("Descriptor - Light")
elif 5 <= a < 6:
    print("Descriptor - Moderate")
elif 6 <= a < 7:
    print("Descriptor - Strong")
elif 7 <= a < 8:
    print("Descriptor - Major")
elif 8 <= a < 10:
    print("Descriptor - Great")
else:
    print("Enter a number from 0 to 12")