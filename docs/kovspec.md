# Követelmény specifikáció

## Jelenlegi helyzet leírása

## Vágyálomrendszer leírása

## Jelenlegi üzleti folyamatok leírása

## Igényelt üzleti folyamatok leírása

## Követelménylista

A követelménylista tartalmaz minden megvalósítandó funkciót és működésbeni követelményt.

### Funkcionális követelmények

A funkcionális követelmények a program kívánt funkcióit írja le, amik később megvalósításra kell, hogy kerüljenek.

A megvalósítandó funkciók egy weboldal, ami képes adatbázisból lekérdezni és ezt megjeleníteni és egy gépi tanulásos program, ami egy tanuló adatbázis alapján új adatokat generál.

| ID | Név | Kifejtés |
|----|-----|----------|
| K1 | Weblap létrehozása | Weblap létrehozása az adatok megtekintésére |
| K2 | Tanuló adatbázis adatainak lekérdezése | A weblapon a felhasználónak képesnek kell lennie lekérdezni a tanuló adatbázis adatait |
| K3 | Tanuló adatbázis minden adatának lekérdezése | A felhasználónak képesnek kell lennie a tanuló adatbázis összes adatának lekérdezésére |
| K4 | Tanuló adatbázis lekérdezése WHO régió szerint | A felhasználónak képesnek kell lekérdeznie a tanuló adatbázis adatait WHO régió szerint |
| K5 | Tanuló adatbázis lekérdezése országnév szerint | A felhasználónak képesnek kell lennie lekérdezni a tanuló adatbázis adatit országnév szerint |
| K6 | Tanuló adatbázis lekérdezése időszak szerint | A felhasználónak képesnek kell lennie a tanuló adatbázis egy megadott időszakra vonatkozó adatainak lekérdezésére |
| K7 | Tanuló adatbázis lekérdezése K4 vagy K5 és K6 szerint | A felhasználónak képesnek kell lennie lekérdezni WHO régiók vagy országok adatait egy megadott időszakra |
| K8 | A tanuló adatok adatbázisban történő tárolása | A tanuló adatokat egy SQL adatbázisban kell tárolni |
| K9 | Prediktált adatok adatbázisban történő tárolása | A prediktált adatokat egy SQL adatbázisban kell tárolni |
| K10 | Prediktált adatok generálása | A prediktált adatokat egy python program készíti gépi tanulással |
| K11 | ILI gyanús esetek prediktálása | A programnak prediktálnia kell az ILI gyanús megbetegedések számát |
| K12 | ILI járóbetegek prediktálása | A programnak prediktálnia kell az ILI járóbetegek számát |
| K13 | SARI gyanús esetek prediktálása | A programnak prediktálnia kell a SARI gyanús megbetegedések számát |
| K14 | SARI járóbetegek prediktálása | A programnak prediktálnia kell a SARI járóbetegek számát |

#### Funkcionális követelmények csoportosítása

- K1 - Kimondja egy weboldal szükségességét
- K2-K7 - Kimondja milyen lekérdezéseket végezhet a felhasználó a tanuló adatbázison
- K8-K9 - Kimondja az adatok adatbázisban történő tárolását
- K10 - Kimondja a prediktált adatok generálását
- K11-K14 - Kimondja milyen adatokat kell prediktálnia a programnak

### Nem-funkcionális követelmények

A nem-funkcionális követelmények teljesítésével biztosítjuk a megfelelő működést.

| ID | Név | Kifejtés |
|----|-----|----------|
| K15 | A tanuló adatbázis tartalma | A tanuló adatbázis csakis a WHO hivatalos adatait tartalmazza |
| K16 | A tanuló adatbázis ne tartalmazzon felesleges adatoszlopokat | A tanuló adatbázis a WHO hivatalos adatainak egy szűrt változatát tartlamazza a predikcióhoz szükségtelen adatoszlopokat elhagyva |
| K17 | A tanuló adatbázis csakis egész népességre vonatkozó adatokat tartalmazzon | A tanuló adatbázis a WHO hivatalos adatainak egy szűrt változatát tartlamazza a korosztályokra lebontott adatsorok elhagyásával |
| K18 | A tanuló adatbázis adatai | A tanuló adatbázis adatoszlopai a következők legyenek: WHO régió, országnév, dátum, ILI gyanús esetek, ILI járóbetegek, SARI gyanús esetek, SARI járóbetegek |
| K19 | A predikció történjen gépi tanulással | A predikcióért felelős program használjon gépi tanulást új adatok előállítására |
| K20 | A prediktált adatok előre elkészítése | A prediktált adatokat készítse el 10 évre előre a program |
| K21 | Figyelmeztetni a felhasználót a prediktált adatok pontatlanságára | Figyelmeztetni kell a felhasználót, hogy a generált adatok gépi tanulás útján lettek generálva, ezért nagy valószínűséggel pontatlanok és nem vállalunk érte felelősséget |
| K22 | Figyelmeztetés kevés adat esetén | Országoknál vagy régióknál, ahol kevés a tanuló adat, ott figyelmeztessen a weboldal a növekedett hibavalószínűségre |
| K23 | A weboldal felhasználóbarátsága | A weboldalnak felhasználó barátnak kell lennie |
| K24 | A weboldal reszponzivitása | A weboldalnak reszponzívnak kell lennie, hogy bármilyen képernyőn felhasználóbarát módon jelenjen meg |

#### Nem-funkcionális követelmények csoportosítása

- K15-K18 - Leírja milyen adatokat tartalmazzon a tanuló adatbázis
- K19-K20 - Leírja hogy történjen a predikció
- K21 - Kimondja, hogy olyan országoknál, ahol kevés a tanuló adat, ott figyelmeztessen a potenciális pontatlanságra
- K22-K24 - Leírja a felhasználói felület követelményeit
