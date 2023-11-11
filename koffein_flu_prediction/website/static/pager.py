from ..models import lekert_adatok
current = 0
onPage = 100
showndata = lekert_adatok.objects.none()


def init(db):
    global showndata, current
    current = 0
    showndata = db

def show():
    global current, showndata
    if(showndata.count()<onPage):
        return showndata
    return showndata[current:current+onPage]


def forward():
    global current
    if ((current+onPage) >= showndata.count()):
        return show()
    else:
        current += onPage
        return show()


def forwardMore():
    global current
    if ((current+(onPage * 10)) >= showndata.count()):
        return show()
    else:
        current += (onPage * 10)
        return show()


def back():
    global current
    if ((current-onPage) < 0):
        current = 0
        return show()
    else:
        current -= onPage
        return show()


def backMore():
    global current
    if ((current-(onPage * 10)) < 0):
        current = 0
        return show()
    else:
        current -= (onPage * 10)
        return show()


def getPage():
    return int(current/onPage) + 1


def getMaxPage():
    return int(showndata.count() / onPage) + 1
