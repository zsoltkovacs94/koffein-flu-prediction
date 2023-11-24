# koffein-flu-prediction

## Futtatás

### Előfeltételek

#### Pycharm community edition

[Telepítsük a pycharmot](https://www.jetbrains.com/pycharm/download/?section=windows)

#### Python 3.9 telepítése

[Telepítsük a python 3.9-et innen](https://www.python.org/downloads/release/python-390/), utána indítsuk újra a Pycharmot.

#### Virtuális környezet létrehozása

Nyissuk meg a projektet a pycharmmal githubról, a projekt mappáját nevezzük "koffein-flu-prediction"-nek, utána végezzük el az alábbi lépéseket.

Settings > Project:[projektnév] > Python Interpreter > Add interpreter > Add local interpreter

Válasszuk a virtual environmentet, fenti rádiógombok közül válasszuk a new-t, a base interpreter legyen python 3.9

#### Csomagok telepítése

Nyissuk meg a pycharm terminált (Alt+F12), majd adjuk ki az alábbi parancsot, a figyelmeztetéseket hagyjuk figyelmen kívül:

```
pip install -r packages
```

### Django oldal futtatása

Nyissuk meg a Pycharm terminált (Alt+F12), majd futtassuk a django oldalt az alábbi paranccsal:

```
python .\koffein_flu_prediction\startserver.py
```

Ezután pár másodpercen belül elérhető a weboldal az alábbi címen:

```
http://127.0.0.1:8000/index
```

Leállítani a terminálban CTRL+C billentyűparancs kiadásával tudjuk.
