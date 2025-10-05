import datetime


def news():
    import time
    date = datetime.datetime.now()

    print("Tervetuloa NEWS-pistelaskuriin.\n")
    time.sleep(0.3)
    print("Tarvitset seuraavat vitaaliarvot potilaasta: verenpaine, syke, lämpö, happisaturaatio, hengitystaajuus, lisähappi käytössä (kyllä/ei), tajunnantaso (normaali/poikkeava) ja lämpö.\n")
    time.sleep(0.3)

    print("Syötä arvot.")
    time.sleep(0.3)

    hf = int(input("Hengitystaajuus (hengenvetoa/min):\n"))
    time.sleep(0.1)
    spo2 = int(input("Happisaturaatio:\n"))
    time.sleep(0.1)
    addito2 = str(input("Lisähappi käytössä, kyllä (k) vai ei (e):\n"))
    time.sleep(0.1)

    rrsys = int(input("Systolinen verenpaine:\n"))
    time.sleep(0.1)
    syke = int(input("Syke:\n"))
    time.sleep(0.1)
    taj = str(input("Tajunnantaso nomraali (n) vai poikkeava (p):\n"))
    time.sleep(0.1)

    temp = float(input("Lämpötila:\n"))


    global pisteet
    global omahf
    global omaspo2
    global omaaddit02
    global omarrsys
    global omasyke
    global omataj
    global omatemp

# Nollataan pisteet:
    pisteet = 0

# Lista poikkeavista arvoista:
    poikk = []

# Lasketaan seuraavaksi:

# Hengitystaajuus

    if 12 <= hf <= 20:
        pass
        omahf = 0

    elif 9 <= hf <= 11:
        pisteet = pisteet + 1
        poikk.append("Hf +1")
        omahf = 1

    elif hf <= 8:
        pisteet = pisteet + 3
        poikk.append("Hf +3")
        omahf = 3

    elif 21 <= hf <= 24:
        pisteet = pisteet + 2
        poikk.append("Hf + 2")
        omahf = 2

    elif hf >= 25:
        pisteet = pisteet + 3
        poikk.append("Hf + 3")
        omahf = 3


# SpO2
    if spo2 >= 95:
        pass
        omaspo2 = 0

    elif 94 <= spo2 <= 95:
        pisteet = pisteet+1
        poikk.append("SpO2 +1")
        omaspo2 = 1

    elif 92 <= spo2 <= 93:
        pisteet = pisteet + 2
        poikk.append("SpO2 +2")
        omaspo2 = 2

    elif spo2 <= 91:
        pisteet = pisteet + 3
        poikk.append("SpO2 +3")
        omaspo2 = 3

# Lisähappi
    if addito2 == "k" or addito2 == "K" or addito2 == "Kyllä" or addito2 == "kyllä":
        pisteet = pisteet + 2
        poikk.append("Lisähappi käytössä +2")
        omaaddit02 = 2

    elif addito2 == "e" or addito2 == "E" or addito2 == "Ei" or addito2 == "ei":
        pass
        omaaddit02 = 0


# Systolinen RR
    if 111 <= rrsys <= 219:
        pass
        omarrsys = 0

    elif 101 <= rrsys <= 110:
        pisteet = pisteet + 1
        poikk.append("RR sys +1")
        omarrsys = 1

    elif 91 <= rrsys <= 100:
        pisteet = pisteet + 2
        poikk.append("RR sys +2")
        omarrsys = 2

    elif rrsys <= 90:
        pisteet = pisteet + 3
        poikk.append("RR sys +3")
        omarrsys = 3

    elif rrsys >= 220:
        pisteet = pisteet + 3
        poikk.append("RR sys + 3")
        omarrsys = 3


# Syke
    if 51 <= syke <= 90:
        pass
        omasyke = 0

    elif 41 <= syke <= 50:
        pisteet = pisteet + 1
        poikk.append("Syke +1")
        omasyke = 1

    elif syke <= 40:
        pisteet = pisteet + 3
        poikk.append("Syke +3")
        omasyke = 3

    elif 91 <= syke <= 110:
        pisteet = pisteet + 1
        poikk.append ("Syke +1")
        omasyke = 1

    elif 111 <= syke <= 130:
        pisteet = pisteet + 2
        poikk.append("Syke +2")
        omasyke = 2

    elif syke >= 131:
        pisteet = pisteet + 3
        poikk.append ("Syke +3")
        omasyke = 3


# Tajunnantaso
    if taj == "n" or taj == "N" or taj == "Normaali" or taj == "normaali":
        pass
        omataj = 0

    elif taj == "p" or taj == "P" or taj == "Poikkeava" or taj == "poikkeava":
        pisteet = pisteet + 3
        poikk.append("Tajunnantaso +3")
        omataj = 3


# Lämpö
    temp = float(temp)
    if 36.1 <= temp <= 38.0:
        pass
        omatemp = 0

    elif 35.1 <= temp <= 36.0:
        pisteet = pisteet + 1
        poikk.append("Lämpö +1")
        omatemp = 1

    elif temp <= 35:
        pisteet = pisteet + 3
        poikk.append("Lämpö +3")
        omatemp = 3

    elif 38.1 <= temp <= 39.0:
        pisteet = pisteet + 1
        poikk.append("Lämpö +1")
        omatemp = 1

    elif temp >= 39.1:
        pisteet = pisteet + 2
        poikk.append("Lämpö + 2")
        omatemp = 2


# Näytä pisteet ja poikkeavuudet:
    time.sleep(0.3)
    print("\n\nNEWS-pisteet:\n")
    time.sleep(0.2)
    print(pisteet)
    print("\n\n")

    if pisteet >= 7:
        time.sleep(0.5)

        print("\n\n     T E E     M E T  -  H Ä L Y T Y S !")

        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)

        print("\n\n - Hälytä hoitava lääkäri!\n\n - Laske NEWS-pisteet 0-2 tunnin välein. Jatkuva seuranta.")

    elif 5 <= pisteet <= 6:
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

        print(".")
        time.sleep(0.5)
        print("Ohjeet:")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)

        print(" - Riskiluokka: Kohtalainen\n\n - Informoi muita hoitajia potilaan voinnin muutoksista.\n\n - Konsultoi lääkäriä jatkotoimista\n\n - Laske NEWS-pisteet vähintään 2-4 tunnin välein")
        print("\n - Aloita tarvittaessa välittömät hoitotoimenpiteet!")

    elif 1 <= pisteet <= 4:
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

        print(".")
        time.sleep(0.5)
        print("Ohjeet:")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)

        print(" - Riskiluokka: Matala\n\n - Informoi muita hoitajia potilaan voinnin muutoksista.\n\n - Laske NEWS-pisteet vähintään 8 tunnin välein.")

    elif pisteet == 0:
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

        print(".")
        time.sleep(0.5)
        print("Ohjeet:")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)

        print(" - Riskiluokka: Matala\n\n - Laske NEWS-pisteet vähintään 12 tunnin välein.")



    #if " " in poikk:
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print("Poikkeavuudet voinnissa:")
    print(poikk)





    if (omahf == 3 or omataj == 3 or omasyke == 3 or omaaddit02 == 3 or omatemp == 3 or omarrsys == 3 or omaspo2 == 3) and pisteet < 3:
        print(" - Riskiluokka: Kohtalainen\n\n - Informoi muita hoitajia potilaan voinnin muutoksista.\n\n - Konsultoi lääkäriä jatkotoimista\n\n - Laske NEWS-pisteet vähintään 2-4 tunnin välein")
        print("\n - Aloita tarvittaessa välittömät hoitotoimenpiteet!")



news()