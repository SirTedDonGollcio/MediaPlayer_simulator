import random
import operator

class Zdarzenie:
    czas = 0
    typ = "-"

    def __init__(self, czas, typ):
        self.czas = czas
        self.typ = typ



def losuj(czas):
    return random.randrange(20,30) + czas

##def sortuj(x,y):
  ##  if(x.czas < y.czas) return True
  ##  else return False




WYSOKIE = 5
NISKIE = 1
wielkoscPaczki = 2.5

random.seed()

czasChwilowy = 0
czasMax = 150
czasRozpoczecia = 0
bufor = 0
nibyBufor = 0
pasmo = WYSOKIE

plik = open("wynik.txt",'w')

listaZdarzen = []

zdarzenieS = Zdarzenie(losuj(czasChwilowy),"Zmiana strumienia")
listaZdarzen.append(zdarzenieS)

zdarzenieBufor = Zdarzenie(czasChwilowy + (wielkoscPaczki/pasmo), "Zmiana bufora");
listaZdarzen.append(zdarzenieBufor)
print((czasChwilowy*100),pasmo,str(bufor*100), file=plik)


while (czasChwilowy < czasMax):
    listaZdarzen[:] = sorted(listaZdarzen, key = operator.attrgetter('czas'))

    zdarzenie = Zdarzenie(0,"-")
    zdarzenie.czas = listaZdarzen[0].czas
    zdarzenie.typ = listaZdarzen[0].typ

    if(zdarzenie.typ== "Zmiana bufora"):
        czasRozpoczecia = czasChwilowy

    czasChwilowy = zdarzenie.czas

    if (zdarzenie.typ == "Zmiana strumienia"):
        if (pasmo == WYSOKIE):
            pasmo = NISKIE
        else:
            pasmo = WYSOKIE
        zdarzenieStrumien = Zdarzenie(losuj(czasChwilowy),"Zmiana strumienia")
        listaZdarzen.append(zdarzenieStrumien)
        bufor=bufor+1
        nibybufor = bufor -2
        bufor = bufor -( czasChwilowy - czasRozpoczecia)
        if (bufor > 30):
            bufor= 30
        if (bufor < 0):
            bufor = 0
        if (nibybufor < 0):
            nibybufor = 0


    elif (zdarzenie.typ == "Zmiana bufora"):
        zdarzenieBufor = Zdarzenie(czasChwilowy + (wielkoscPaczki/pasmo), "Zmiana bufora")
        listaZdarzen.append(zdarzenieBufor)
        bufor=bufor+1
        nibybufor = bufor -2
        bufor = bufor -( czasChwilowy - czasRozpoczecia)
        if (bufor > 30):
            bufor= 30
        if (bufor < 0):
            bufor = 0
        if (nibybufor < 0):
            nibybufor = 0

    print((czasChwilowy*100),pasmo,str(bufor*100), file=plik)
    print((czasChwilowy*100),pasmo,str((nibybufor)*100), file=plik)
    listaZdarzen.remove(listaZdarzen[0])
    print(bufor,nibybufor)

plik.close();
