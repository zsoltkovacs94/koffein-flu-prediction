from ..models import lekert_adatok

current = 0
onPage = 100
showndata = lekert_adatok.objects.none()
generalt = False


def init(db, gen=False):
    global showndata, current, generalt, onPage
    current = 0
    showndata = db
    generalt = gen


def show():
    global current, showndata
    if (showndata.count() < onPage):
        return showndata
    return showndata[current:current + onPage]


def forward():
    global current
    if ((current + onPage) >= showndata.count()):
        return show()
    else:
        current += onPage
        return show()


def forwardMore():
    global current
    if ((current + (onPage * 10)) >= showndata.count()):
        return show()
    else:
        current += (onPage * 10)
        return show()


def back():
    global current
    if ((current - onPage) < 0):
        current = 0
        return show()
    else:
        current -= onPage
        return show()


def backMore():
    global current
    if ((current - (onPage * 10)) < 0):
        current = 0
        return show()
    else:
        current -= (onPage * 10)
        return show()


def getPage():
    return int(current / onPage) + 1


def getMaxPage():
    return int(showndata.count() / onPage) + 1


def isGen():
    return generalt


def setOnPage(ps):
    if not ps.isnumeric():
        return
    ps = int(ps)
    if ps <= 0:
        return
    global onPage
    onPage = ps


def getOnPage():
    return onPage
