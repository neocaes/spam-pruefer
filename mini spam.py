nachricht = input("Nachricht eingeben: ")

nachricht = nachricht.lower()

kostenlos = nachricht.count("kostenlos")
gratis = nachricht.count("gratis")
aktion = nachricht.count("aktion")
geschenk = nachricht.count("geschenk")
eilig = nachricht.count("eilig")
ausrufezeichen = nachricht.count("!")

punkte = kostenlos * 3 + gratis * 3 + geschenk * 2 + aktion * 2 + eilig * 2 + ausrufezeichen

woerter = nachricht.split()
laenge = len(nachricht)

if punkte >= 5:
    spam = True
else:
    spam = False

if spam == True:
    spam = "Ja"
else:
    spam = "Nein"

print(" ")
print("------ SPAM-BERICHT ------")
print("Nachricht:", nachricht)
print("Länge:", laenge)
print("Anzahl der Wörter:", len(woerter))

print("Kostenlos:", kostenlos)
print("Gratis:", gratis)
print("Geschenk:", geschenk)
print("Aktion:", aktion)
print("Eilig:", eilig)
print("Ausrufezeichen:", ausrufezeichen)
print("Gesamtpunktzahl:", punkte)
print("Spam?:", spam)
print("--------------------------")