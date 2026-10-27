# from random import *    #randint
# from math import *
# print("Tere, maailm!")
# nimi=input("Sisesta oma nimi: ")
# print(f"Tere, maailm! Tervitan sind {nimi}!")
# try:
#     vanus=int(input("Sisesta oma vanus: "))
#     print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
# except ValueError:
#     print("Palun sissesta kehtiv number vanuse jaoks.")

#     #Ülesanne 3
# vanus=18 #int-täisarv
# eesnimi="Jaak" #str-sõne
# pikkus=16.5 #float-kümnendmurd/ujukomaarv
# kas_käib_koolis=True #bool-tõeväärtus
# print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
# print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
# print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
# print(f"Käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_koolis)}")

# kommide_arv=randint(1, 100)                                              #(input("kommide arv: "))
# print(f"Laud on {kommide_arv} kommi.")
# try:
#     kommid=int(input("Mitu kommi soovid ära võtta?. "))
#     kommide_arv -= kommid
#     print(f"Laud on nüüd {kommide_arv} kommi. ")
# except ValueError:
#     print("Palun sisesta number.")

# #Ülesanne 4
# try:
#     ümbermõõt=float(input("Sisesta puu ümbermõõt: "))
#     läbimõõt=round(ümbermõõt/pi,1)
#     print(f"Puu läbimõõt on {läbimõõt}. ")
# except ValueError:
#     print("Palun sisesta kehtis number. ")

# #Ülesanne 5
# try:
#     N=float(input("Sisesta ristküliku esimene külg (N): "))
#     M=float(input("Sisesta ristküliku teine külg (M): "))

#     diagonaal=round(sqrt(N**2 + M**2), 1) # sqrt() math moodulist
#     print(f"Ristküliku diagonaal on {diagonaal}, ")
# except ValueError:
#     print("Palun sisesta kentis number. ")

#     #Ülesanne 6
# try:
#     aeg = float(input("Mitu tundi kulus sõiduks? "))
#     teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#     kiirus = teepikkus / aeg

#     print("Sinu kiirus oli " + str(kiirus) + " km/h")
# except ValueError:
#     print()

    #Ülesanne 7
a = int(input("Sisesta 1. täisarv: "))
b = int(input("Sisesta 2. täisarv: "))
c = int(input("Sisesta 3. täisarv: "))
d = int(input("Sisesta 4. täisarv: "))
e = int(input("Sisesta 5. täisarv: "))

summa = a + b + c + d + e
keskmine = summa / 5

print("Arvude summa on " + str(summa))
print("Aritmeetiline keskmine on " + str(keskmine))

jagaja = int(input("Sisesta arv, millega summa jagada: "))

taisosa = summa // jagaja
jaak = summa % jagaja

print("Täisarvuline osa: " + str(taisosa))
print("Jääk: " + str(jaak))