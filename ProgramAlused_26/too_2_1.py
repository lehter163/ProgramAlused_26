eesnimi=input("Sisesta eesnimi: ")
 if eesnimi.lower() == "juku":
 print("Lähme Jukuga kinno!")
 if eesnimi.isupper() == "juku":
    print("ära karju juku")



pinginaabrid=["Mati","käti"]
nimi1=input("siseta nimi: ")
nimi2=input("siseta nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}")
    nimi1=nimi1.capitalize()
    if nimi1 in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on pinginaabrid")
    else:
        print("nad ei ole pinginaabrid")
else:
    print("viga: nimed on valeti sisetanud! kasuta ainult tähed")

# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.

# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.

# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
try:
    pikkus=float(input("Sissesta pikkus: "))
    laius=float(input("Sissesta laius: "))
    pindala=round(pikkus*laius,2)
    print(f"pindala on {pindala}")
    remont=input("ksa soovid remonti teha? (jah/ei)").lower()
    if remont=="jah":
        print("Teeme remoti!")
        try:
            rm_hind=float(input("Sisesta ruutmeetri hind: "))
            hind=round(pindala*rm_hind,2)
            print(f"põranda vahetamise hind on {hind} euro")
            ise=input("kas teeb remondi is?(jah/ei)").lower()
            if ise=="jah":
                print(f"põranda vahetamise hind on sama {hind} euro")
            else:
                try:
                    töö_hind=float(input("Tõõ hind: "))
                    koguhind=round(hind+pindala*töö_hind,2)
                    print(f"remondi koguhind koos töö")
                except ValueError:
    else:
        print("remonti ei tehta")
except ValueError:
    print("viga: kasuta numbreid")