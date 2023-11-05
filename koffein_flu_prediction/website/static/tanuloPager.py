from ..models import lekert_adatok

current = 0


def show():
    global current
    osszesLekert = lekert_adatok.objects.order_by()[current:current+500]
    return osszesLekert


def forward():
    global current
    if ((current+500) >= lekert_adatok.objects.count()):
        current = lekert_adatok.objects.count()-500
        return show()
    else:
        current += 500
        return show()


def forwardMore():
    global current
    if ((current+5000) >= lekert_adatok.objects.count()):
        current = lekert_adatok.objects.count()-500
        return show()
    else:
        current += 5000
        return show()


def back():
    global current
    if ((current-500) < 0):
        current = 0
        return show()
    else:
        current -= 500
        return show()


def backMore():
    global current
    if ((current-5000) < 0):
        current = 0
        return show()
    else:
        current -= 5000
        return show()
