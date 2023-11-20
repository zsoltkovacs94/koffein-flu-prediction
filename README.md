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
pip install django==4.2.7
```
```
pip install numpy==1.26.1
```
```
pip install pandas==1.2.1
```
```
pip install tensorflow==2.14.0
```

### Django oldal futtatása

Nyissuk meg a Pycharm terminált (Alt+F12), ezután lépjünk be a projekt koffein_flu_prediction almappájába a terminálból.

```
cd .\koffein_flu_prediction\
```

Majd futtassuk a django oldalt az alábbi paranccsal:

```
python manage.py runserver --insecure
```

A terminálban látható "Starting development server at..." kezdetű sorban található címen érhetjük el az oldalt.

Leállítani a terminálban CTRL+C billentyűparancs kiadásával tudjuk.
