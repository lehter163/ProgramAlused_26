while True:
    print("Tee valik:")
    print("1.while-tsukel")
    print("2.while True ja break")
    print("3.for-tsukel")
    print("4.Summa ja keskmine")
    print("5.Loendamine ja suurim")
    print("0.valju")

    valik = input("Vali tegevus: ")
    if valik == 0:
        break
    elif valik == "1":

        #1.while-tsukel
        x = 0
        while x < 30:
            if x % 2 == 1:
                print(x, end=" ")
            x += 1
    elif valik == "2":
    #2.while True ja break
        x = 0
        while True:
            if x % 2 == 0:
                print(x, end=" ")
            if x == 30:
                break
            x += 1
    elif valik == "3":
            #3.for-tsukel 
        for i in range(1, 31, 2):
            print(i, end=" ")

# summa	summa = 0	summa += arv
# korrutis	korrutis = 1	korrutis *= arv
# loendamine	kogus = 0	if tingimus: kogus += 1
# suurim	suurim = esimene arv	if arv > suurim: suurim = arv
# keskmine	summa = 0, kogus = 0	pärast tsüklit summa / kogus
    elif valik == "4":
        #4.Summa ja keskmine
        N = int(input("N: "))
        summa = 0
        i = 1
        while i <= N:
            summa = summa + i
            i = i + 1
        print("Summa:", summa)
        print("Keskmine:", summa / N)
    elif valik == "5":
        #5.Loendamine ja suurim
        kogus = 0
        suurim = None
        for i in range(5):
            arv = float(input(f"{i + 1}. arv: "))
            if arv > 0:
                kogus += 1
            if suurim is None or arv > suurim:
                suurim = arv
        print("Positiivseid arve:", kogus)
        print("Suurim arv:", suurim)
    else:
        print("Vale valik!")