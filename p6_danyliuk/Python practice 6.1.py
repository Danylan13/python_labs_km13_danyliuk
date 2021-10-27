while True:
    phrase1 = input('Введіть перший рядок: ').split()
    phrase2 = input('Введіть другий рядок: ').split()

    bywords1 = set()
    bywords2 = set()

    phrase1 = str(phrase1).lower()
    bywords1 = {words1 for words1 in phrase1 if words1.isalpha() }
    print ('Букви в першій фразі:', bywords1)

    phrase2 = str(phrase2).lower()
    bywords2 = {words2 for words2 in phrase2 if words2.isalpha() }
    print ('Букви в другій фразі :', bywords2)

    if(bywords1.intersection(bywords2) == bywords2) :
        print ('Ми можемо створити букви другої фрази з першої')
    else: 
        print ('Ми не можемо створити букви другої фрази з першої')

    repeat=input('\nInput "mi scusi" to enter one more line of elements or another symbol to exit: ')
    if repeat == "mi scusi":
        continue
    else:
        break
