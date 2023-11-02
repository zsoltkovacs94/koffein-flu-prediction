from keras.models import load_model
import numpy as np

def pred_ic(X):
    model = load_model('IC.keras')
    pred = model.predict(X, verbose=0)
    return pred


def pred_io(X):
    model = load_model('IO.keras')
    pred = model.predict(X, verbose=0)
    return pred

def pred_sc(X):
    model = load_model('SC.keras')
    pred = model.predict(X, verbose=0)
    return pred


def pred_si(X):
    model = load_model('SI.keras')
    pred = model.predict(X, verbose=0)
    return pred


def prednext(pastIC, pastIO, pastSC, pastSI, next = 1):
    for i in range(0, next):
        nextIC = pred_ic(pastIC)[0, 0]
        nextIO = pred_io(pastIO)[0, 0]
        nextSC = pred_sc(pastSC)[0, 0]
        nextSI = pred_si(pastSI)[0, 0]

        pastIC = np.insert(pastIC, [8], [nextIC])
        row = [[a] for a in pastIC[1:]]
        pastIC = np.asarray([row])

        pastIO = np.insert(pastIO, [8], [nextIO])
        row = [[a] for a in pastIO[1:]]
        pastIO = np.asarray([row])

        pastSC = np.insert(pastSC, [8], [nextSC])
        row = [[a] for a in pastSC[1:]]
        pastSC = np.asarray([row])

        pastSI = np.insert(pastSI, [8], [nextSI])
        row = [[a] for a in pastSI[1:]]
        pastSI = np.asarray([row])

    return pastIC, pastIO, pastSC, pastSI

