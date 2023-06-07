class Repulogep:
    def __init__(self,adatsor):
        reszletek=adatsor.split(";")
        self.tipus=reszletek[0]
        self.ev=int(reszletek[1])
        self.utas=reszletek[2]
        self.szemelyzet=reszletek[3]
        self.utazosebesseg=int(reszletek[4])
        self.felszallotomeg=int(reszletek[5])
        self.fesztav=float(reszletek[6].replace(',','.'))

    def __str__(self):
        return f"Típus: {self.tipus}, Év: {self.ev}"
    
    def minutasszam(self):
        reszletek=self.utas.split('-')
        return int(reszletek[0])
    
    def maxustasszam(self):
        reszletek=self.utas.split('-')
        if len(reszletek)>1:
            return reszletek[1]
        else:
            return int(reszletek[0])




finp=open("utasszallitok.txt", mode="rt", encoding="utf-8")
adatsorok=finp.read().split("\n")
finp.close()

repulogepek=[]
for i in range(1, len(adatsorok), 1):
    if adatsorok[i]!="":
        repulogep=Repulogep(adatsorok[i])
        repulogepek.append(repulogep)

db=len(repulogepek)

#határozza meg a repülőgépek az átlagos fesztávját
#!!! az átlag határozásához az összeg is kell

sum=0
for item in repulogepek:
    sum+=item.fesztav
    
atlag=sum/len(repulogepek)
print(f"a repülőgépek átlagos fesztája: {atlag:.2f}")

#határozza meg azt a repülőgépet melynek a legnagyobb utazósebességgel rendelkezik
#max tétel az utazosebesseg

maxseb=repulogepek[0]
for item in repulogepek:
    if item.utazosebesseg > maxseb.utazosebesseg:
        maxseb=item
print(f"A keresett repülőgép: {maxseb}, amely sebessége {maxseb.utazosebesseg}")


#megszámlálás
#meg kell számolni a Boeing eket
dbB=0
for item in repulogepek:
    if "Boeing" in item.tipus:
        dbB+=1

print(f"Összesen {dbB}db Boeing volt")


