# Funkcionális specifikáció

## Jelenlegi helyzet leírása

## A rendszer céljai és nem céljai

## Vágyálomrendszer leírása

## Jelenlegi üzleti folyamatok leírása

## Igényelt üzleti folyamatok leírása

## Használati esetek

## Követelménylista

A követelménylista tartalmaz minden megvalósítandó funkciót és működésbeni követelményt.

### Funkcionális követelmények

A funkcionális követelmények a program kívánt funkcióit írja le, amik később megvalósításra kell, hogy kerüljenek.

A megvalósítandó funkciók egy weboldal, ami képes adatbázisból lekérdezni és ezt megjeleníteni és egy gépi tanulásos program, ami egy tanuló adatbázis alapján új adatokat generál.

#### Funkcionális követelmények csoportosítása

- K1 - Kimondja egy weboldal szükségességét
- K2-K7 - Kimondja milyen lekérdezéseket végezhet a felhasználó a tanuló adatbázison
- K8-K9 - Kimondja az adatok adatbázisban történő tárolását
- K10 - Kimondja a prediktált adatok generálását
- K11-K14 - Kimondja milyen adatokat kell prediktálnia a programnak

#### Weblap követelményei

A felhasználónak képesnek kell lennie különböző lekérdezéseket végzeni a tanuló és a predikált adatok adatbázisán a weblapon keresztül.

A weblap egy közvetítőként működik a felhasználó és az adatbázisok között.

Ábra beszúrása a felhasználó a weblap és az adatbázisok viszonyáról

#### A tanuló adatbázis követelményei

A tanuló adatbázis statikus, az adatokat sem a felhasználó, sem egyéb programok nem változtathatják.

A tanuló adatbázison a feltöltés után csakis lekérdezések végezhetők.

#### A prediktáló program követelményei

A prediktáló program egy python program, ami a tanuló adatbázis megfelelő részein végez tanulást és predikciót.

A prediktáló program egy tanuló adatbázis lekérdezéssel kap tanuló adatot, majd a predikció után a generált adatokat feltölti a prediktált adatok adatbázisába.

A prediktáló program a dátum, az ILI gyanús esetek száma, az ILI járóbetegek száma, a SARI gyanús esetek száma és a SARI járóbetegek száma alapján tanul és megadott jövőbeli időpontokra ILI gyanús esetek, ILI járóbetegek, SARI gyanús esetek és SARI járóbetegek számát generál.

### Nem-funkcionális követelmények

A nem-funkcionális követelmények teljesítésével biztosítjuk a megfelelő működést.

#### Nem-funkcionális követelmények csoportosítása

- K15-K18 - Leírja milyen adatokat tartalmazzon a tanuló adatbázis
- K19-K20 - Leírja hogy történjen a predikció
- K21 - Kimondja, hogy olyan országoknál, ahol kevés a tanuló adat, ott figyelmeztessen a potenciális pontatlanságra
- K22-K23 - Leírja a felhasználói felület követelményeit

#### Tanuló adatbázis tartalma

A tanuló adatbázis csakis a predikció szempontjából lényeges adatokat tartalmaz.

Ábra az adatbázis felépítéséről

##### Adatoszlopok

- WHO régió - WHO régió neve
- Országnév - Az adott ország neve
- Dátum - A mérés időpontja
- ILI gyanús esetek száma - Influenzagyanús betegek száma
- ILI járóbetegek száma - Influenzás járóbetegek száma
- SARI gyanús esetek száma - Súlyos léguti megbetegedésgyanús betegek száma
- SARI járóbetegek száma - Súlyos léguti megbetegedéses járóbetegek száma

#### Predikció nem-funkcionális követelményei

A predikciónak gépi tanulás útján kell történnie, az adatokat 10 évre előre el kell készítenie és feltölteni az adatbázisba.

#### Weboldal nem-funkcionális követelményei

Figyelmeztetni kell a felhasználót az adatok gépi tanulás útján történt generálására.

Kevés tanuló adat esetén figyelmeztetni kell a felhasználót a pontatlanság megnövekedett valószínűségére.

A weboldal felületének felhasználóbarátnak és resztponzívnak kell lennie.

## Képernyőtervek
