import math
import random
'''Kérj be 1 páros számot a felhasználótól. (1 pont)
Amennyiben nem páros számot ad meg
a felhasználó, akkor kérd be újra a számot,
addig, amíg páros számot nem ad meg!  (1 pont)	'''
def feladat1():
    szam:int=int(input("Kérem adjon meg egy páros számot!"))
    while not (szam %2==0):
        szam: int = int(input("Kérem adjon meg egy páros számot!"))

'''Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. 
Hány 3-mal osztható van közöttük? A kiírás formátuma:
„A számok között X db 3-mal osztható van!”'''
def feladat2():
    i:int=0
    szamlalo:int=0
    while i < 13:
        veletlenszam=math.floor(random.random()*(150-10+1)+10)
        print(veletlenszam)
        if veletlenszam % 3==0:
            szamlalo+=1
        i+=1
    print(f"A számok között {szamlalo} db 3-mal osztható van!")

'''Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
 Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! 
'''
def feladat3(szoveg,N):

    if len(szoveg)<N:
        print("Nincs N edik karakter")
    else:
        i:int=0
        while i < 3:
            kiir:str=szoveg[N-1]
            print(kiir.upper())
            i+=1
'''Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
Hány nevet adott meg a felhasználó? 
A kiírás formája: „A felhasználó 12 nevet adott meg.”
'''
def feladat4():
    db:int=0
    nev:str=input("Kérem adjon meg egy nevet!")
    while nev != "@":
        nev= input("Kérem adjon meg egy nevet!")
        db+=1
    print(f"A felhasználó {db} nevet adott meg.”")

'''Szimuláljuk a kő-papír-olló játékot. 
Írj eljárást, amiben: 
A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet. Alakítsd át csupa kisbetűssé a szöveget, majd tárold el a felhasznalo_tippje változóban. 
Ezután a gép generál egy egész számot [1,3] között.  1- kő, 2- papír – 3 olló. Tárold el a gep_tippje változóban
Ezután írd ki, hogy ki nyert!
	Ha a két szó ugyanaz, írja ki, hogy Döntetlen. 
	Egyéb esetben azt írja ki, aki győzött!
++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!
'''
def feladat5():

        felhasznalo_tippje :int=0
        gep_tippje:int=0


        tipp:str=input("Kérem adja meg a tippjét! (kő,papír,olló)").lower()
        while tipp!="kő" and tipp!="papír" and tipp!="olló":
            tipp = input("Kérem adja meg a tippjét! (kő,papír,olló").lower()
        if tipp=="kő":
                felhasznalo_tippje+=1
        elif tipp=="papír":
                felhasznalo_tippje+=2
        elif tipp == "olló":
                felhasznalo_tippje+=3

        szam :int=math.floor(random.random()*((3-1)+1)+1)
        gep_tippje+=szam

        if felhasznalo_tippje == szam:
            print("Döntetlen")
        elif felhasznalo_tippje==1 and szam ==2:
            print("Gép nyert")
        elif felhasznalo_tippje==2 and szam ==1:
            print("Gép nyert")
        elif felhasznalo_tippje==3 and szam ==1:
            print("Gép nyert")
        elif felhasznalo_tippje==1 and szam ==3:
            print("Felhasználó nyert")
        elif felhasznalo_tippje==2 and szam ==3:
            print("Gép nyert")
        elif felhasznalo_tippje==3 and szam ==2:
            print("Felhasználó nyert")

