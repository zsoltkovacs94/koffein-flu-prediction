from ..models import lekert_adatok
current = 0
showndata = lekert_adatok.objects.none()


def init(db):
    global showndata, current
    current = 0
    showndata = db

def show():
    global current, showndata
    return showndata[current:current+500]


def forward():
    global current
    if ((current+500) >= showndata.count()):
        current = showndata.count()-500
        return show()
    else:
        current += 500
        return show()


def forwardMore():
    global current
    if ((current+5000) >= showndata.count()):
        current = showndata.count()-500
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
