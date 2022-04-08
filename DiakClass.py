"""#nev, osztaly, pont
class Diak():
    def __init__(self, nev, osztaly, pont):
        self.pont = pont
        self.osztaly = osztaly
        self.nev = nev
    def __repr__(self):
        return f"{self.nev} {self.osztaly} {self.pont}"
    def sikerult(self):
        if self.pont>20:
            return "sikerült"
        else:
            return "bukott"

f = open("diak.txt", encoding="UTF-8")
lista=[]
for sor in f:
    sor = sor.strip().split(";")
    #nev = sor[0]
    #osztaly = sor[1]
    #pont = int(pont[2])
    #diak = Diak(nev, osztaly, pont)
    diak = Diak(sor[0], sor[1], int(sor[2]))
    lista.append(diak)
f.close()

#print(lista)

#Irasd ki a képernyőre a 10.A diákokat
for sor in lista:
    if sor.osztaly=="10.A":
        print(sor)
print("_________________")
# irasd ki minden diákot, mellé hogy sikerült vagy megbukott (20<sikerült)
for sor in lista:
    print(sor, sor.sikerult())
print("_________________")
#Számold meg, ? 10.A osztályos diák van
db=0
for tanulo in lista:
    if tanulo.osztaly=="10.A":
        db+=1
print(f"10.A osztályos diákok száma: {db} fő")
print("_________________")
#? fő 10.A diák van, akinek sikerült
dbsiker=0
for tanulo in lista:
    if tanulo.osztaly=="10.A" and tanulo.sikerult()=="sikerült":
        dbsiker+=1
print(f"10.A osztályos, sikeres vizsgát tett diákok száma: {dbsiker} fő")
print("_________________")
# Írjuk egy file-ba minden adatát a 10.C diákoknak
ki = open("10C_diakok.txt", "w", encoding="UTF-8")
for diak in lista:
    if diak.osztaly=="10.C":
        ki.write(f"{diak} {diak.sikerult()} \n")
ki.close()
# rendezzük növekvő sorrendbe a pontszámok alapján
#for diak in sorted(lista)
for diak in sorted(lista, key=lambda diak:diak.pont):
    print(diak)
#rendezzük növekvő sorrendbe  (függvénnyel) -def
print("_________________")
def pontszamfv(diak):
    return diak.pont

for diak in sorted(lista, key=pontszamfv, reverse=True):
    print(diak)
"""

class Monitor():
    def __init__(self, marka, tipus, kepatlo, ar):
        self.marka = marka
        self.tipus = tipus
        self.kepatlo = kepatlo
        self.ar = ar
    def __repr__(self):
        return f"{self.marka} {self.tipus} {self.kepatlo} {self.ar}"
    def kicsi(self):
        if self.kepatlo < 23:
            return "kicsi a képátlója"
        else:
            return "nagy a képátlója"


f = open("monitor_adat.txt", encoding="UTF-8")
lista=[]
for sor in f:
    sor = sor.strip().split(" ")
    marka = str(sor[0])
    tipus = sor[1]
    kepatlo = int(sor[2])
    ar = int(sor[3])
    monitorok = Monitor(marka, tipus, kepatlo, ar)
    monitorok = Monitor(sor[0], sor[1], int(sor[2]), int(sor[3]))
    lista.append(monitorok)
f.close()

for i in lista:
    if i.marka == "Asus":
        print(i)

for i in lista:
    print(i, i.kicsi())

lg = 0
for i in lista:
    if i.marka == "LG":
        lg += 1
print(f"{lg} darab LG monitor van.")

penzed = int(input("Mennyi pénzed van?"))
for i in lista:
    if i.ar < penzed:
        print(f"{i}-t tudod megvenni a pénzedből")
    else:
        print(f"{i}-t nem tudod megvenni a pénzedből")

for monitorok in sorted(lista, key=lambda monitorok:monitorok.ar):
    print(monitorok)

for monitorok in sorted(lista, key=lambda monitorok:monitorok.kepatlo, reverse=True):
    print(monitorok)

for monitorok in sorted(lista, key=lambda monitorok:monitorok.marka)
    print(monitorok)







