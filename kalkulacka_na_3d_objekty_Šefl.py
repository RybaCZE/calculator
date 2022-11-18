"""
    kalkulačka na 3d objekty
    autor: Jiří Šefl
    datum vytvoření: 11.18.2022

"""
import math

#kontroluje zda input je kladny ci pozitivni. 1-3 = false cokoliv jinyho je true
def kontrola(x):
    return x <= 0, x >= 3
def kontrola_jednotky(x):#kontroluje zda je rozpeti 1 - 5 
    return x <= 0, x >=5
def kontrola_zaporu(x):#kontroluje zda je cislo negativni
    return x <= 0
def kontrola_znovupouziti(x):#kontroluje zda je cislo v rozmezi 1 -2
    return x <= 0, x >= 2

kontrola_false = False, False #true ktery se potom porovnav
repeat_full = True 

while(repeat_full):#opakuje celou aplikaci

    jednotky_loop = True
    while(jednotky_loop):#opakuje vyber jednotek dokud si uzivatel nevybere z danych moznosti
        try:
            jednotky_input = int(input("vyber si jednotky:1) MM, 2) CM, 3) DM, 4) M, 5) KM "))
            if kontrola_jednotky(jednotky_input) == kontrola_false:
                jednotky_loop = False
            break
        except:
            print("Zadal jsi špatné číslo jednotky, zkus to znovu.")
    if jednotky_input == 1:
        jednotka2 = ("mm2")#jednotka na plochu
        jednotka3 = ("mm3")#jednotka na objem
    elif jednotky_input == 2:
        jednotka2 = ("cm2")#jednotka na plochu
        jednotka3 = ("cm3")#jednotka na objem
    elif jednotky_input == 3:
        jednotka2 = ("dm2")#jednotka na plochu
        jednotka3 = ("dm3")#jednotka na objem
    elif jednotky_input == 4:
        jednotka2 = ("m2")#jednotka na plochu
        jednotka3 = ("m3")#jednotka na objem
    elif jednotky_input == 5:
        jednotka2 = ("km2")#jednotka na plochu
        jednotka3 = ("km3")#jednotka na objem

    vstup = True
    while(vstup):#vyber objektu který se potom pocita 3 moznosti kvadr, krychle, koule
        try:
            print ("vyber si objekt:1 KVÁDR,2 KRYCHLE,3 KOULE")
            objekt = int(input("zadej tvar:"))
            if kontrola(objekt) == kontrola_false:
                vstup = False
            break
        except:
            print("Zadal jsi špatné číslo objektu, zkus to znovu.")

    if objekt == 1: #1 moznost kvadr
        prvni_strana = True
        while(prvni_strana):#zadani prvniho rozmeru
            try:
                a = float(input("zadej délku první strany: "))
                if kontrola_zaporu(a) == kontrola_false:
                    prvni_strana = False
                break
            except:
                print("Nesprávný znak")

        druha_strana = True
        while(druha_strana):#zadani druheho rozmeru
            try:
                b = float(input("zadej délku druhé strany: "))
                if kontrola_zaporu(b) == kontrola_false:
                    druha_strana = False
                break
            except:
                print("Nesprávný znak")

        treti_strana = True
        while(treti_strana):#zadani tretiho rozmeru
            try:
                c = float(input("zadej délku třetí strany: "))
                if kontrola_zaporu(c) == kontrola_false:
                    treti_strana = False
                break
            except:
                print("Nesprávný znak")

        kvadr_vyber_loop = True
        while(kvadr_vyber_loop):
            try:
                print ("Zvol si: 1) objem, 2) povrch, 3) objem + povrch")
                kvadr_vyber = int(input("vyber si:"))
                if kontrola(kvadr_vyber) == kontrola_false:
                    kvadr_vyber_loop = False
                break
            except:
                print("Zadal jsi špatné čislo, zkus to znovu")
        if kvadr_vyber == 1:#vypocet objemu kvadru
            vysledek_kvadr = a*b*c
            print("objem kvádru: ", vysledek_kvadr, jednotka3)

        elif kvadr_vyber == 2:#vypocet povrchu kvadru
            vysledek_kvadr = 2*(a*b+a*c+b*c)
            print("Povrch kvádru", vysledek_kvadr, jednotka2)

        elif kvadr_vyber == 3:#vypocet objemu a povrchu kvadru
            vysledek_kvadr = a*b*c
            vysledek_kvadr2 = 2*(a*b+a*c+b*c)
            print("Objem kvádru ", vysledek_kvadr, jednotka3, "Povrch kvádru", vysledek_kvadr2, jednotka2)


    elif objekt == 2: #cast na krychli
        krychle_loop = True
        while(krychle_loop):
            try:
                a = float(input("Zadej délku strany krychle: "))#zadani strany krychle
                if kontrola_zaporu(a) == kontrola_false:
                    krychle_loop = False
                break
            except:
                print("Zadal jsi neznámý znak")
        krychle_vyber_loop = True
        while(krychle_vyber_loop):#vyber ceho chce vysledek
            try:
                print ("Zvol si: 1) objem, 2) povrch, 3) objem + povrch")
                krychle_vyber = int(input("vyber si: "))
                if kontrola(krychle_vyber) == kontrola_false:
                    krychle_vyber_loop = False
                break
            except:
                print("Zadal jsi špatný znak, zkus to znovu")
        if krychle_vyber == 1:#objem krychle
            vysledek_krychle = a**3
            print("objem krychle: ", vysledek_krychle, jednotka3)

        elif krychle_vyber == 2:#povrch kryche
            vysledek_krychle = 6*a**2
            print("Povrch kryche", vysledek_krychle, jednotka2)

        elif krychle_vyber == 3:#objem + povrch krychle
            vysledek_krychle = a**3
            vysledek_krychle2 = 6*a**2
            print("Objem krychle ", vysledek_krychle, jednotka3, "Povrch krychle", vysledek_krychle2, jednotka2)

    elif objekt == 3: #cast pro kouli 
        koule_loop = True
        while(koule_loop):
            try:
                a = float(input("Zadej poloměr"))#zadani polomeru koule
                if kontrola_zaporu(a) == kontrola_false:
                    koule_loop = False
                    break
            except:
                print("Zadal jsi neznámý znak")

        koule_vyber_loop = True
        while(koule_vyber_loop):
            try:
                print ("Zvol si: 1) objem, 2) povrch, 3) objem + povrch")#vyber ceho chce vysledek
                koule_vyber = int(input("vyber si:"))
                if kontrola(koule_vyber) == kontrola_false:
                    koule_vyber_loop = False
                break
            except:
                print("Zadal jsi špatné čislo, zkus to znovu")
        if koule_vyber == 1:#objem koule
            vysledek_koule = 4*math.pi*a**3/3
            print("objem koule: ", vysledek_koule, jednotka3)

        elif koule_vyber == 2:#povrch koule
            vysledek_koule = 4*math.pi*a**2
            print("Povrch kryche", vysledek_koule, jednotka2)
        elif koule_vyber == 3:#objem + povrch koule
            vysledek_koule = 4*math.pi*a**3/3
            vysledek_koule2 = 4*math.pi*a**2
            print("Objem koule ", vysledek_koule, jednotka3, "Povrch koule", vysledek_koule2, jednotka2)
        
    znova_opakovat = True
    while(znova_opakovat):#cast zda chce opakovat aplikaci nebo ji ukoncit
        try:
            znova_opakovat = int(input("Chceš znova použít kalkulačku: 1) ANO, 2) NE"))
            if kontrola_znovupouziti(znova_opakovat) == kontrola_false:
                znova_opakovat = False
            break
        except:
            print("Zadal jsi špatný znak, zkus to znovu.")
    if znova_opakovat == 1:
        print("OK")
    else:
        exit()
