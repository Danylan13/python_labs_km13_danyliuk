While True:
    phrase1 = input("Input the first phrase: ").split()
    phrase2 = input("Input the second phrase: ").split()

    phrase1 = str(phrase1).lower()
    bywords1 = {item1 for item1 in phrase1 if item1.isalpha() }
    print ("Letters in the first phrase:", bywords1)

    phrase2 = str(phrase2).lower()
    bywords2 = {item2 for item2 in phrase2 if item2.isalpha() }
    print ("Letters in the second phrase:", bywords2)

    if bywords2 & bywords1 == bywords2:
        print ("We can create second phrase letters from the first")
    else: 
        print ("We can't create second phrase letters from first phrase")

    repeat=input('\nInput "mi scusi" to enter one more line of elements or another symbol to exit: ')
    if repeat == "mi scusi":
        continue
    else:
        break
