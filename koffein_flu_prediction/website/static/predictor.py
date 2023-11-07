import os
from keras.models import load_model
import numpy as np

current = os.path.dirname(__file__)

def pred_ic(X):
    model = load_model(os.path.join(current, "IC.keras"))
    pred = model.predict(X, verbose=0)
    return pred


def pred_io(X):
    model = load_model(os.path.join(current, "IO.keras"))
    pred = model.predict(X, verbose=0)
    return pred

def pred_sc(X):
    model = load_model(os.path.join(current, "SC.keras"))
    pred = model.predict(X, verbose=0)
    return pred


def pred_si(X):
    model = load_model(os.path.join(current, "SI.keras"))
    pred = model.predict(X, verbose=0)
    return pred


def prednext(pastIC, pastIO, pastSC, pastSI, next = 1):
    if(pastIC.__class__ != np.ndarray):
        print("pastIC is not ndarray")
        return 0, 0, 0, 0
    if(pastIO.__class__ != np.ndarray):
        print("pastIO is not ndarray")
        return 0, 0, 0, 0
    if(pastSC.__class__ != np.ndarray):
        print("pastSC is not ndarray")
        return 0, 0, 0, 0
    if(pastSI.__class__ != np.ndarray):
        print("pastSI is not ndarray")
        return 0, 0, 0, 0
    if(pastIC.shape[1] != 8):
        print("pastIC.shape is incorrect")
        return 0, 0, 0, 0
    if(pastIO.shape[1] != 8):
        print("pastIO.shape is incorrect")
        return 0, 0, 0, 0
    if(pastSC.shape[1] != 8):
        print("pastSC.shape is incorrect")
        return 0, 0, 0, 0
    if(pastSI.shape[1] != 8):
        print("pastSI.shape is incorrect")
        return 0, 0, 0, 0
    if(next > 8):
        next = 8
        print("Warning the maximum value of next is 8")
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

    return (pastIC[0, (pastIC.shape[1]-next):],
            pastIO[0, (pastIC.shape[1]-next):],
            pastSC[0, (pastIC.shape[1]-next):],
            pastSI[0, (pastIC.shape[1]-next):])
