# eesnimi=input("Sisesta eesnimi: ")
# if eesnimi.lower() == "juku":
#  print("Lähme Jukuga kinno!")
#  if eesnimi.isupper() == "juku":
#     print("ära karju juku")



# pinginaabrid=["Mati","käti"]
# nimi1=input("siseta nimi: ")
# nimi2=input("siseta nimi: ")
# if nimi1.isalpha() and nimi2.isalpha():
#     print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}")
#     nimi1=nimi1.capitalize()
#     if nimi1 in pinginaabrid and nimi2.capitalize() in pinginaabrid:
#         print(f"{nimi1} ja {nimi2} on pinginaabrid")
#     else:
#         print("nad ei ole pinginaabrid")
# else:
#     print("viga: nimed on valeti sisetanud! kasuta ainult tähed")

# # Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.

# # Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.

# # Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# try:
#     pikkus=float(input("Sissesta pikkus: "))
#     laius=float(input("Sissesta laius: "))
#     pindala=round(pikkus*laius,2)
#     print(f"pindala on {pindala}")
#     remont=input("ksa soovid remonti teha? (jah/ei)").lower()
#     if remont=="jah":
#         print("Teeme remoti!")
#         try:
#             rm_hind=float(input("Sisesta ruutmeetri hind: "))
#             hind=round(pindala*rm_hind,2)
#             print(f"põranda vahetamise hind on {hind} euro")
#             ise=input("kas teeb remondi is?(jah/ei)").lower()
#             if ise=="jah":
#                 print(f"põranda vahetamise hind on sama {hind} euro")
#             else:
#                 try:
#                     töö_hind=float(input("Tõõ hind: "))
#                     koguhind=round(hind+pindala*töö_hind,2)
#                     print(f"remondi koguhind koos töö")
#                 except ValueError:
#     else:
#         print("remonti ei tehta")
# except ValueError:
#     print("viga: kasuta numbreid")

# ülesanne 4
# Küsi toote alghind. Kui alghind on üle 700 euro, arvuta hind 30% soodustusega. Muul juhul jääb hind samaks. Kuva lõplik hind kahe komakohaga.
try:
    alghind=float(input("sisesta toote alghind: "))
    if alghind>700 :
        soodushind = alghind*0.7
        print("hind soodustega ", soodushind, "euro")
    else:
        print("alghind on vähem kui 700")
except ValueError:
    print("Viga! töötan ainult positiivsete andmetega")
    
#ülesanne 5
#Küsi toatemperatuur ja teata, kas see on üle 18 kraadi (soovitatav toasoojus talvel). Temperatuur võib olla ka negatiivne või kümnendarv, seega kontrolli sisendit try/except abil.
try:
    toatemperatuur=float(input("sisesta toatemperatuur: "))
    if toatemperatuur>18 :
        print("toatemperatuur on üle 18 kraadi")
    else:
        print("toatemperatuur on vähem kui 18 kraadi")
except ValueError:
    print("Viga! sisesta numbriga")

#Ülesanne 6
#Küsi inimese pikkus sentimeetrites ja teata, kas ta on lühike, keskmise pikkusega või pikk. Piirid pane ise paika ja kirjuta need programmi alguses kommentaarina.
sugu=input("teie sugu: ").lower()
if sugu == "mees" or sugu == "m":
    try:
        pikkus=int(input("sisesta teie pikkus santimetrites: "))
        if pikkus<100 or pikkus>240 :
            print("Sisesta korrektselt pikkus")
        else:
            if pikkus<169 :
                print("te olete lühikese pikka")
            else:
                if pikkus<=180 :
                    print("te olete keskimese pikka")
                else:
                    print("te olete pikk")
    except ValueError:
        print("sisesta ainult täisarvud")
else:
    if sugu == "naine" or sugu == "n":
        try:
            pikkus=int(input("sisesta teie pikkus santimetrites: "))
            if pikkus<100 or pikkus>240 :
                print("Sisesta korrektselt pikkus")
            else:
                if pikkus<160 :
                    print("te olete lühikese pikka")
                else:
                    if pikkus<=172 :
                        print("te olete keskimese pikka")
                    else:
                        print("te olete pikk")
        except ValueError:
            print("sisesta ainult täisarvud")

#Ülesanne 8
# Küsi kasutajalt iga toote kohta eraldi, kas ta soovib seda osta: piim, sai, leib ja vähemalt kaks toodet veel.
# Toodete hinnad loo juhuslikult moodulist random, näiteks round(random.uniform(0.5, 3), 2).
# Kui kasutaja soovib toodet osta, küsi kogus. Kontrolli, et kogus on täisarv (isdigit()).
# Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
from random import *
summa=0
arve="toode"