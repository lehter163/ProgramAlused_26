from math import pi
import calendar
from datetime import *
from calendar import * #monthrange
tana=date.today()
print(f"Täna on {tana}")

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(f"täna on {tana1}")

# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(f"täna on {tana2}")

# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(f"täna on {tana3}")

# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(f"täna on {tana4}")

# Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# Arvuta oma vanus aastates, kuudes ja päevades.
print("Täna on", tana.day)
print("päev, kuu number on", tana.month)
print("ja aasta on", tana.year)

kuulõpuni=monthrange(tana.year, tana.month)[1] - tana.day
# oktoobris on 31 päaeva, 31-27=4 päeva jäänud
print("kuulõpuni on jäänud", kuulõpuni, "päeva")
aastalõpuni=(date(täna.year, 12, 31) - tana).days
#date()-> 31.12.2026
#tana -> 27.10.2026
#days -> 65 päea jäänud
print("aasta lõpuni on jäänud", aastalõpuni, "päeva")
sünnipäev=date(2009,08,25)
vanus=aastalõpuni//365
print("oled", vanus, "aastat, ")
print((aastalõpuni%365)//30, "kuud ja")
print((aastalõpuni%365)%30, "päevana vana")

#ülesanne 2

print("3 + 8 / (4 - 2) * 4 =", 3 + 8 / (4 - 2) * 4)
print("3 + 8 / 4 - 2 *4 =",3 + 8 / 4 - 2 * 4)
print("(3 + 8) / (4 - 2) * 4"(3 + 8) / (4 - 2) * 4)

#Ülesanne 3

try:
    R=float(input("sisesta ringi raadius: "))
    print("ruudu pindala: ",R**2)
    print("ruudu umbermõõt: ",4*R)
    print("ringi pindala: ",pi*R**2)
    print("ringi ümbermõõt: ",2*pi*R)
except :
    print("Valed andmed")#fdfd

#Ülesanne 4

