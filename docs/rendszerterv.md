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

### Nem-funkcionális követelmények

> **A tanuló adatbázis tartalma**

**Röviden a követelménylistából**: A tanuló adatbázis csakis a WHO hivatalos adatait tartalmazza.

Ez a követelmény több okból is fontos: először is, hogy a felhasználó csak olyan adatokhoz jusson hozzá, amelyek hitelesek. Számukra ugyanis a weboldal csak a tájékozódás helye, ezért biztosítanunk kell, hogy hiteles adatokat adunk át nekik.

Továbbá a WHO hivatalos adatai azért is fontosak, mert nekünk ezek az adatok adnak alapot a modellünk betanítására. Ha nem hivatalos, hiteles adatokkal dolgoznánk, akkor semmi értelme nem lenne a betanításnak, és magának a programunknak sem.

> **A tanuló adatbázis ne tartalmazzon felesleges oszlopokat**

**Röviden a követelménylistából**: A tanuló adatbázis a WHO hivatalos adatainak egy szűrt változatát tartalmazza a predikcióhoz szükségtelen adatoszlopokat elhagyva.

A WHO által kiadott hivatalos adatok között több olyan adatoszlop is található, amelyek nem sokat mondanak olyan személyeknek, akik nem foglalkoznak egyes tárgyakkal, mint a földrajz, biológia vagy informatika.

Ezért, és hogy a betanított modellünknek ne kelljen extra munkát végeznie, úgy döntöttünk, hogy az eredeti adatokat leszűrjük egy olyan mennyiségre, amelyek könnyen értelmezhetőek bármilyen felhasználó által.

> **A tanuló adatbázis csakis egész népességre vonatkozó adatokat tartalmazzon**

**Röviden a követelménylistából**: A tanuló adatbázis a WHO hivatalos adatainak egy szűrt változatát tartalmazza a korosztályokra lebontott adatsorok elhagyásával.

A WHO által kiadott hivatalos adatok több korosztályra vannak bontva, amely csak nehezíti az adatok értelmezését és emellett több helyet foglal el az eszközön.

Úgy döntöttünk, hogy az összes korosztály meghagyása helyett csak az '*All*' korosztályú adatsorokat hagyjuk meg, amellyel végső soron adatvesztés nem keletkezik, mert így is az összes feljegyzett hiteles adat megmaradt.

> **A tanuló adatbázis adatai**

**Röviden a követelménylistából**: A tanuló adatbázis adatoszlopai a következők legyenek: WHO régió, országnév, dátum, ILI gyanús esetek, ILI járóbetegek, SARI gyanús esetek, SARI fekvőbetegek.

Az előző három pontot összegezve úgy döntöttünk, hogy ezek az adatoszlopok tartalmazzák azokat az adatokat, amelyekre az általános felhasználók leginkább kíváncsiak.

Ahogy azt már a fentebb leírt Funkcionális követelmények részben írtuk, az első három adatoszlopból lehet majd a felhasználónak lekérdezni, míg az utolsó négy oszlop tartalmazza az influenzás és COVID betegek számát.

> **A predikció történjen gépi tanulással**

**Röviden a követelménylistából**: A predikcióért felelős program használjon gépi tanulást az új adatok előállítására.

Annak érdekében, hogy a felhasználónak legyen egy elképzelése arról, hogyan fognak alakulni a tanuló adatbázisban található adatok, szeretnénk ha az általunk fejlesztett program meg tudná ezeket az adatokat jósolni.

Ezt úgy tudjuk a legegyszerűbben elérni, hogy a modellünk gépi tanulást használ.

> **A predikált adatok elkészítése**

**Röviden a követelménylistából**: A predikált adatokat egy előre betanított modell alapján lekérésre generálja a rendszer.

Míg a tanuló adatbázis már a weboldal betöltésével együtt létezik a felületen, addig a modell által generált adatok csak akkor fognak ténylegesen létezni, amint a felhasználó lekérdezte őket.

Ez azért is jelentős, mert ahogyan az idő múlik, annál frissebb adatok lesznek a tanuló adatbázisban, és úgy fog fejlődni a betanított modell is, ezért nem elégedhetünk meg azzal, hogy mi egyszer legeneráljuk a predikált adatokat, és azzal térünk vissza a felhasználónak.

A modell nem fog miden egyes lekérdezéssel újra betanítódni, viszont az adatok mindig változnak - ezért fontos így elkészítenünk az adatokat.

> **Figyelmeztetni a felhasználót a predikált adatok pontatlanságára**

**Röviden a követelménylistából**: Figyelmeztetni kell a felhasználót, hogy a generált adatok gépi tanulás útján lettek generálva.

Akármennyire sokáig tanítunk be egy modellt, az semmiképpen sem fogja tudni pontosan megjósolni a jövőt, mivel mi emberek se tudjuk azt megtenni.

Éppen ezért szükséges tájékoztatnunk a felhasználót arról, hogy ha a predikált adatokkal foglalkozik, számítson arra, hogy az adatok nagy valószínűséggel pontatlanok, és ez ellen mi magunk sem tudunk semmit sem tenni.

> **Figyelmeztetés kevés adat esetén**

**Röviden a követelménylistából**: Országoknál vagy régióknál, ahol kevés a tanuló adat, ott figyelmeztessen a weboldal a növekedett hibavalószínűségre.

Erre a WHO hivatalos oldala is felhívja a figyelmet, mivel vannak egyes országok és régiók, ahol ők se tudtak elég, vagy elég hiteles adatot szerezni.

Mivel mi az ő általuk kiadott adatokat használjuk, mi nekünk is fontos figyelmeztetni a felhasználót ebben az esetben.

> **A weboldal felhasználóbarátsága**

**Röviden a követelménylistából**: A weboldalnak felhasználó barátnak kell lennie.

Szeretnénk, ha programunkat nem csak olyan felhasználók tudnák használni és megérteni, akik jártasak az informatika vagy biológia egyes területeiben, hanem bárki, akit érdekelnek ezek at adatok.

Ezért szükséges egy olyan weboldalt kialakítanunk, amelyet könnyű használni bármilyen felhasználó által, függetlenül koruktól, hozzáértésüktől.

> **A weboldal reszponzivitása**

**Röviden a követelménylistából**: A weboldalnak reszponzívnak kell lennie, hogy bármilyen képernyőn felhasználóbarát módon jelenjen meg.

Mivel a világon nem minden személy egy fajta eszközt használ, ezért fontos arra is gondolnunk, hogy minden gépi eszközön sikeresen meg tudjuk jeleníteni oldalunkat.

Bár a programot nem fejlesztjük mobil eszközökre, reméljük, hogy bármilyen más gépi eszköz képernyőjén meg tudjon jelenni az oldal úgy, hogy tartsa formáját és használhatóságát.

### Törvényi előírások, szabványok

Programunknak szükséges megfelelnie az Európai Unió Általános adatvédelmi rendeletének (GDPR).

Ezen kívül szükséges betartanunk a WHO adatszabályzatát is, amely megtalálható a következő linken: [WHO Data Policy](https://www.who.int/about/policies/publishing/data-policy).

## Funkcionális terv

## Fizikai környezet

## Absztrakt domain modell

## Architekturális terv

## Adatbázis terv

## Tesztterv

## Telepítési terv
