import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    def szoba_tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def szoba_tipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def szoba_tipus(self):
        return "Kétagyas szoba"

class Foglalas:
    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum

    def __repr__(self):
        return f"Foglalás - Szobaszám: {self.szobaszam}, Dátum: {self.datum}"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}
        self.foglalasok = {}

    def szoba_hozzaadasa(self, szoba):
        self.szobak[szoba.szobaszam] = szoba

    def foglalas(self, szobaszam, datum):
        if datum < datetime.date.today():
            return "A foglalás dátuma nem lehet a múltban!"
        if szobaszam not in self.szobak:
            return f"Nem létező szobaszám: {szobaszam}"
        if datum in self.foglalasok and szobaszam in self.foglalasok[datum]:
            return "Ez a szoba már foglalt ezen a napon!"
        self.foglalasok.setdefault(datum, {})[szobaszam] = Foglalas(szobaszam, datum)
        return f"Foglalás sikeres: {datum}, szobaszám: {szobaszam}, ár: {self.szobak[szobaszam].ar}"

    def foglalas_torlese(self, szobaszam, datum):
        if datum in self.foglalasok and szobaszam in self.foglalasok[datum]:
            del self.foglalasok[datum][szobaszam]
            if not self.foglalasok[datum]:
                del self.foglalasok[datum]
            return "Foglalás törölve!"
        else:
            return "Nincs ilyen foglalás!"

    def foglalasok_listazasa(self):
        return "\n".join(str(f) for d in self.foglalasok for f in self.foglalasok[d].values())

def felhasznalo_interfesz():
    szalloda = Szalloda("Hotel Python")
    szalloda.szoba_hozzaadasa(EgyagyasSzoba(101, 5000))
    szalloda.szoba_hozzaadasa(KetagyasSzoba(102, 8000))
    szalloda.szoba_hozzaadasa(EgyagyasSzoba(103, 5500))

    # Előre definiált foglalások hozzáadása
    datumok = [datetime.date.today() + datetime.timedelta(days=i) for i in range(1, 6)]
    for i, datum in enumerate(datumok):
        szalloda.foglalas(101 + i % 3, datum)  # Ciklikus szobaszám használata a teszteléshez

    while True:
        print("\nElérhető szobák:")
        for szobaszam, szoba in szalloda.szobak.items():
            print(f"Szobaszám: {szobaszam}, Típus: {szoba.szoba_tipus()}, Ár: {szoba.ar}")
        print("1. Foglalás")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válasszon egy opciót: ")
        
        if valasztas == "1":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.datetime.strptime(datum, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum formátum!")
                continue
            print(szalloda.foglalas(szobaszam, datum))
        elif valasztas == "2":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.datetime.strptime(datum, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum formátum!")
                continue
            print(szalloda.foglalas_torlese(szobaszam, datum))
        elif valasztas == "3":
            print("Foglalások listája:")
            print(szalloda.foglalasok_listazasa())
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen opció. Kérem próbálja újra!")

felhasznalo_interfesz()
