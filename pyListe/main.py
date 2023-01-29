class NizLista():
    # Iniciranje liste sa predodre?enim kapacitetom
    def __init__(self, kapacitet):
        self.kapacitet = kapacitet
        self.duzina = 0
        self.tekuci = 0
        self.Niz = self.kreiraj_niz(self.kapacitet)
    
    # Pozicioniranje na po?etak
    def idiNaPocetak(self):
        self.tekuci = 0
        print("Pokaziva? teku?i postavljen na PO?ETAK liste!")
    
    # Pozicioniranje na kraj
    def idiNaKraj(self):
        self.tekuci = self.duzina
        print("Pokaziva? teku?i postavljen na KRAJ liste!")

    # Pozicioniranje na sljede?i
    def idiNaSljedeci(self):
        if(self.tekuci < self.duzina):
            self.tekuci += 1
            print("Pokaziva? teku?i postavljen na SLJEDE?I ELEMENT liste!")
        else:
            print("Pokaziva? teku?i je na kraju liste!")

    # Pozicioniranje na prethodni
    def idiNaPrethodni(self):
        if(self.tekuci > 0):
            self.tekuci -= 1
            print("Pokaziva? teku?i postavljen na PRETHODNI ELEMENT liste!")
        else:
            print("Pokaziva? teku?i je na po?etku liste!")

    # Pozicioniranje na proizvoljnu poziciju
    def idiNaPoziciju(self, pozicija):
        if((pozicija < 0) or (pozicija > self.duzina)):
            print("Zadata poziciaj je izvan raspona!")
        else:
            self.tekuci = pozicija
            print("Pokaziva? teku?i postavljen na poziciju:" + str(pozicija))

    # Dodavanje elementa na kraj liste
    def dodaj(self,x):
        if(self.duzina < self.kapacitet):
            self.Niz[self.duzina] = x
            self.duzina += 1
            print("Uspješno dodan element!")
        else:
            print("Kapacitet popunjen!")

    # Dužina lijeve particije
    def lDuzina(self):
        return self.tekuci

    # Dužina desne particije
    def dDuzina(self):
        return self.duzina - self.tekuci
    
    # Umetanje lementa na teku?u poziciju
    def umetni(self, x):
        if(self.duzina < self.kapacitet):
            for i in range(self.duzina,self.tekuci,-1): # Elemente od kraja niza do teku?eg pokaziva?a
                self.Niz[i] = self.Niz[i-1]             # pomjera za jedno mjesto u desno
            self.Niz[self.tekuci] = x
            self.duzina += 1
            print("Uspješno umetnut element " + str(x) + " na poziciju pokaziva?a " + str(self.tekuci))
        else:
            print("Kapacitet popunjen!")

    # Izabcivanje/Brisanje teku?eg elementa - vrijednost elementa sa desne strane od indeksa pokaziva?a teku?i
    def izbaci(self):
        if (self.dDuzina() <= 0):
            print("nema elemenata za izbacivanje/brisanje! Teku?i na kraju liste!")
        else:
            izbacei = self.Niz[self.tekuci]
            for i in range (self.tekuci,self.duzina-1): # Elemente od teku?eg pokaziva?a do kraja niza 
                self.Niz[i] = self.Niz[i+1]             # pomjera za jedno mjesto u lijevo
            self.duzina -= 1
            print("izvršeno je izbacivanje elementa vrijednosti: " + str(izbacei))

    # Ispis teku?eg elementa
    def ispisiTekuci(self):
        if (self.dDuzina() <= 0):
            print("Nema elemnata za ispis! Pokaziva? je na kraju liste!")
        else:
            print("Vrijednost elementa na teku?oj poziciji je: " + str(self.Niz[self.tekuci]))
    
    # Prikazivanje/Ispis svih elemenata liste
    def prikazi(self):
        print("Dužina liste:" + str(self.duzina))
        #py doc --> range(start, stop, step)
        for i in range(0,self.duzina):
            print("Element " + str(i+1) + " - pozicija(" + str(i) + ") :" + str(self.Niz[i]))