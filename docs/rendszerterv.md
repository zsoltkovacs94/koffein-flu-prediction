# Rendszerterv

## A rendszer célja

A rendszer célja, hogy  az emberek könnyebben tudjanak informálódni a covid és influenzás betegek számáról. A könnyen kezelhető webes alkalmazáson információ jellegű adatok találhatóak. Az adatokat lehet szűri országokra és régiókra. 

Mivel az alkalmazást csak Webes felületen szeretnénk elérhetővé tenni, nem célunk hogy más ,például IOS vagy android operációs rendszerrel rendelkező eszközön fusson.

A rendszer az adatokat a projecten belül saját adatbázisban tárolja aminek az adatai a WHO nyílt adatait tartalmazza(https://www.who.int/teams/global-influenza-programme/surveillance-and-monitoring/influenza-surveillance-outputs FluID dataset: A FluID egy globális platform az adatmegosztásra, amely összekapcsolja a regionális influenzajárványokról szóló adatokat egyetlen globális adatbázissá.).

## Projektterv

## Üzleti folyamatok modellje

## Követelmények

Ez azoknak a követelményeknek a listája, amelyeket szeretnénk mindenképpen megvalósítani. Ezek a fejlesztés során még változhatnak.

### Funkcionális követelmények

> **Weboldal létrehozása**

**Röviden a követelménylistából**: Weblap létrehozása az adatok megtekintésére.

Mivel azt szeretnénk elérni ezzel a rendszerrel, hogy bármilyen személy által használható legyen, ezért a legegyszerűbb módon kell a felhasználók kezébe juttatni - ez a mai világban az internet segítségével történik.

Az adatok megjelenítésére egy weboldalt kell létrehoznunk, amely bármilyen gépi böngésző által megnyitható és könnyen kezelhető, értelmezhető.

> **Tanuló adatbázis adatainak lekérdezése**

**Röviden a követelménylistából**: A weblapon a felhasználónak képesnek kell lennie lekérdezni a tanuló adatbázis adatait.

A tanuló adatbázisunk a WHO által kiadott hivatalos adatoknak egy szűrt változata, amelyet arra használunk, hogy betanítsunk egy modellt majd új adatok generálására.

Azért fontos, hogy a felhasználó ehhez az adatbázishoz hozzájusson és le tudja kérdezni az adatait, mert ez az adatbázis tárolja az eddig feljegyzett összes influenzás és COVID beteg számát, így jelentős információt tartalmaz magában.

> **Tanuló adatbázis minden adatának lekérdezése**

**Röviden a követelménylistából**: A felhasználónak képesnek kell lennie a tanuló adatbázis összes adatának lekérdezésére.

Terveink szerint a weblap már betöltéskor meg fogja jeleníteni a tanuló adatbázist teljes egészében, de biztosítanunk kell arra is lehetőséget, hogy maga a felhasználó is lekérdezhesse az adatbázis összes adatát.

> **Tanuló adatbázis lekérdezése WHO régió szerint**

**Röviden a követelménylistából**: A felhasználónak képesnek kell lennie a tanuló adatbázis adatait WHO régió szerint lekérdezni.

A WHO 6 különböző részre osztotta a világot annak érdekében, hogy összeszedettebb adatokat tudjanak gyűjteni, azokat analizálni és megfigyelni.

Ez az egyik legszemléletesebb felosztás az adatbázisban, ezért is fontos, hogy a felhasználó külön szűrhessen erre a kategóriára.

> **Tanuló adatbázis lekérdezése országnév szerint**

**Röviden a követelménylistából**: A felhasználónak képesnek kell lennie a tanuló adatbázis adatait országnév szerint lekérdezni.

Mivel a világ minden országát leginkább a saját maga adatai érdekelnek, érthető módon, ezért fontos megadni a felhasználónak azt a lehetőséget, hogy országnév szerint szűrhessen az adatbázisban.

> **Tanuló adatbázis lekérdezése időszak szerint**

**Röviden a követelménylistából**: A felhasználónak képesnek kell lennie a tanuló adatbázis egy bizonyos időszakra eső adatainak lekérdezésére.

Ahogyan az az influenzára és járványokra jellemző, nem minden betegség van jelen az év minden időszakában, vagy egyáltalán nem is létezik még egyes időszakokban.

Ezért gondoljuk azt fontosnak, hogy a felhasználónak legyen lehetősége az adatokat lekérdezni csak a számára fontos időszakokban, amennyiben van adatunk az adott időszakról.

> **Tanuló adatbázis lekérdezése K4 vagy K5 és K6 szerint**

**Röviden a követelménylistából**: A felhasználónak képesnek kell lennie a tanuló adatbázis adatait WHO régió vagy országnév, és adott időszak szerint is lekérdezni.

Az előbbi három pont ötvözeteként, fontos úgy kialakítanunk a rendszert, hogy a felhasználó egyszerre szűrhessen ezekre a fontosabb adatokra, hogy annál pontosabb adatokhoz juthasson hozzá.

> **A tanuló adatok adatbázisban történő tárolása**

**Röviden a követelménylistából**: A tanuló adatokat egy SQL adatbázisban kell tárolni.

Annak érdekében, hogy a WHO által kiadott hivatalos adatok szűrt változatát tömören és egy, könnyen elérhető helyen tároljuk, ezért létre kell hoznunk egy adatbázist.

Az adatok így könnyebben elérhetőek és használhatóak, és kevesebb helyet foglalnak a rendszerre nézve, mint ha más tárolási módot keresnénk.

> **A predikált adatok adatbázisban történő tárolása**

**Röviden a követelménylistából**: A predikált adatokat egy SQL adatbázisban kell tárolni.

Az alkalmazásunk legegyedibb tulajdonsága az lesz, hogy betanított modell segítségével meg tudjuk jósolni az influenzás és COVID betegek számának változását a jövőre nézve.

A betanított modell által generált adatokat is szükséges tárolnunk valahol, így a tanító adatbázis példájára ezeket az új adatokat is egy adatbázisban fogjuk tárolni.

> **Predikált adatok generálása**

**Röviden a követelménylistából**: A predikált adatokat egy python program készíti gépi tanulással.

Ahogy azt ez előbbi pontban írtuk, további megbetegedések adatainak jóslása az egyik legfontosabb része szoftverünknek.

A modell terveink szerint mi általunk lesz megépítve és betanítva a tanuló adatbázis adatai szerint, így szeretnénk olyan adatokat generálni, amelyek a legközelebb álhatnak a jövő tényleges megbetegedésinek adataihoz.

> **ILI gyanús esetek prediktálása**

**Röviden a követelménylistából**: A programnak prediktálnia kell az ILI gyanús megbetegedések számát.

A tanuló adatbázis egyik adatoszlopa az ILI gyanús (influenzagyanús) megbetegedések számát tárolja, ezért a betanított modellünknek sikeresen meg kell tudni jósolnia ezen adatok lehetséges jövőbeli fejlődését.

> **ILI járóbetegek prediktálása**

**Röviden a követelménylistából**: A programnak prediktálnia kell az ILI járóbetegek számát.

A tanuló adatbázis egyik adatoszlopa az ILI (influenzás) járóbetegek számát tárolja, ezért a betanított modellünknek sikeresen meg kell tudni jósolnia ezen adatok lehetséges jövőbeli fejlődését.

> **SARI gyanús esetek prediktálása**

**Röviden a követelménylistából**: A programnak prediktálnia kell a SARI gyanús megbetegedések számát.

A tanuló adatbázis egyik adatoszlopa a SARI gyanús (súlyos léguti megbetegedésgyanús) megbetegedések számát tárolja, ezért a betanított modellünknek sikeresen meg kell tudni jósolnia ezen adatok lehetséges jövőbeli fejlődését.

> **SARI fekvőbetegek prediktálása**

**Röviden a követelménylistából**: A programnak prediktálnia kell a SARI fekvőbetegek számát.

A tanuló adatbázis egyik adatoszlopa a SARI (súlyos léguti megbetegedés) fekvőbetegek számát tárolja, ezért a betanított modellünknek sikeresen meg kell tudni jósolnia ezen adatok lehetséges jövőbeli fejlődését.



## Funkcionális terv

## Fizikai környezet

## Absztrakt domain modell

## Architekturális terv

## Adatbázis terv

## Tesztterv

## Telepítési terv
