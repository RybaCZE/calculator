"""
    kalkulačka na 3d objekty
    autor: RybaCZE
    datum vytvoření: 11.19.2022

"""
import math

#kontroluje zda input je kladny ci pozitivni. 1-3 = false cokoliv jinyho je true
#arraye pro kontrolu vyberu
jednotky_array = (1, 2, 3, 4, 5)
jedna_az_tri = (1, 2, 3)
jedna_az_dva = (1, 2)
jednotky_input = 0

kontrola_false = False#true ktery se potom porovnav
repeat_full = True 
jednotky_loop = True
while(repeat_full):#opakuje celou aplikaci

    while(jednotky_loop):#opakuje vyber jednotek dokud si uzivatel nevybere z danych moznosti
        try:
            jednotky_input = int(input("vyber si jednotky:1) MM, 2) CM, 3) DM, 4) M, 5) KM: "))   
        except ValueError:
            print("Zadal jsi špatné číslo jednotky, zkus to znovu.")
        if jednotky_input in jednotky_array:
                jednotky_loop = False
        elif jednotky_input not in jednotky_array:
            print("Špatné číslo, zkus to znovu")
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
        except:
            print("Zadal jsi špatné číslo objektu, zkus to znovu.")
        if objekt in jednotky_array:
            vstup = False
        elif jednotky_input not in jedna_az_tri:
            print("Špatné číslo, zkus to znovu")

    if objekt == 1: #1 moznost kvadr
        prvni_strana = True
        while(prvni_strana):#zadani prvniho rozmeru
            a = 0
            try:
                a = float(input("zadej délku první strany: "))
                if a > 0:
                    prvni_strana = False
                elif a < 0:
                    print("Rozměry nemohou být záporné")
            except:
                print("Nesprávný znak")

        druha_strana = True
        while(druha_strana):#zadani druheho rozmeru
            b = 0
            try:
                b = float(input("zadej délku druhé strany: "))
                if b > 0:
                    druha_strana = False
                elif b < 0:
                    print("Rozměry nemohou být záporné")
            except:
                print("Nesprávný znak")

        treti_strana = True
        while(treti_strana):#zadani tretiho rozmeru
            c = 0
            try:
                c = float(input("zadej délku třetí strany: "))
                if c > 0:
                    treti_strana = False
                elif c < 0:
                    print("Rozměry nemohou být záporné")
            except:
                print("Nesprávný znak")

        kvadr_vyber_loop = True
        while(kvadr_vyber_loop):
            try:
                print ("Zvol si: 1) objem, 2) povrch, 3) objem + povrch")
                kvadr_vyber = int(input("vyber si:"))
            except:
                print("Zadal jsi špatné čislo, zkus to znovu")
            if kvadr_vyber in jedna_az_tri:
                kvadr_vyber_loop = False
            elif kvadr_vyber not in jedna_az_tri:
                print("Špatné číslo, zkus to znovu")
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
            a = 0
            try:
                a = float(input("Zadej délku strany krychle: "))#zadani strany krychle
            except:
                print("Zadal jsi neznámý znak")
            if a > 0:
                krychle_loop = False
            elif a < 0:
                print("Rozměry nemohou být záporné")
            
        krychle_vyber_loop = True
        while(krychle_vyber_loop):#vyber ceho chce vysledek
            try:
                print ("Zvol si: 1) objem, 2) povrch, 3) objem + povrch")
                krychle_vyber = int(input("vyber si: "))
            except:
                print("Zadal jsi špatný znak, zkus to znovu")
            if krychle_vyber in jedna_az_tri:
                krychle_vyber_loop = False
            elif krychle_vyber not in jedna_az_tri:
                print("Špatné číslo, zkus to znovu")
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
            r = 0
            try:
                r = float(input("Zadej poloměr: "))#zadani polomeru koule
                if r > 0:
                    koule_loop = False
                elif r < 0:
                    print("Rozměr nemůže být záporný")
            except:
                print("Zadal jsi neznámý znak")

        koule_vyber_loop = True
        while(koule_vyber_loop):
            try:
                print ("Zvol si: 1) objem, 2) povrch, 3) objem + povrch")#vyber ceho chce vysledek
                koule_vyber = int(input("vyber si: "))
            except:
                print("Zadal jsi špatné čislo, zkus to znovu")
            if koule_vyber in jedna_az_tri:
                koule_vyber_loop = False
            elif koule_vyber not in jedna_az_tri:
                print("Špatný znak")
        if koule_vyber == 1:#objem koule
            vysledek_koule = 4*math.pi*a**3/3
            print("objem koule: ", vysledek_koule, jednotka3)
        elif koule_vyber == 2:#povrch koule
            vysledek_koule = 4*math.pi*r**2
            print("Povrch koule", vysledek_koule, jednotka2)
        elif koule_vyber == 3:#objem + povrch koule
            vysledek_koule = 4*math.pi*r**3/3
            vysledek_koule2 = 4*math.pi*r**2
            print("Objem koule ", vysledek_koule, jednotka3, "Povrch koule", vysledek_koule2, jednotka2)

    znova_opakovat = True
    while(znova_opakovat):#cast zda chce opakovat aplikaci nebo ji ukoncit
        try:
            znova_opakovat = int(input("Chceš znova použít kalkulačku: 1) ANO, libovolnou klávesu krom jedna pro ukončení: "))
        except:
            print("Zadal jsi špatný znak, zkus to znovu.")
        if znova_opakovat in jedna_az_dva:
            znova_opakovat = False
        elif znova_opakovat not in jedna_az_dva:
            print("Nesprávný znak")
            
    if znova_opakovat == 1:
        print("OK")
    else:
        quit()
