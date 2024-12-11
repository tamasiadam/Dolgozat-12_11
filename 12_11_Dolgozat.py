import random

"""
A csoport
Szimuláljuk egy 20 oldalú D&D kocka 100 db dobását! A dobásokat egy listában tároljuk! Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 6-os a dobások között?
2. Hányadikra sikerült először 18-nál nagyobbat dobni?
3. Hány darab 1-est dobtak?
4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
5. Mennyi a 4-es dobások szorzata?
"""


dobasok = [random.randint(1, 20) for i in range(100)]
print(dobasok)

#1. feladat - Volt-e 6-os a dobások között?
print("1. Feladat")
hatos = 6
if hatos in dobasok:
    print("Volt benne 6-os \n")
else:
    print("Nem volt benne 6-os \n")

#2. feladat - Hányadikra sikerült először 18-nál nagyobbat dobni?
print("2. feladat")
elso = None
for i in range(len(dobasok)):
    if dobasok[i]  > 18:
        elso = i + 1
        break
print(f"{elso}. dobásra kaptunk először 18-nál nagyobbat. \n")



#3. feladat - Hány darab 1-est dobtak?
print("3. feladat")
print(f"{dobasok.count(1)}db 1-est dobtak. \n")

#4. feladat - Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?


#5. feladat - Mennyi a 4-es dobások szorzata?
print("5. feladat")

negyes = dobasok.count(4)
szorzat = negyes * 4

print(f"A 4-es dobások szorzata {szorzat}, mivel {negyes}db 4-est dobtak. \n")
