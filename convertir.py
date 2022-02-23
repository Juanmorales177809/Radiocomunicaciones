import numpy as np


def ftmet(ft):
    return ft/3.2808
def megGig(meg):
    return meg/1000
def todBm(mWats):
    return 10*np.log10(mWats/0.01)
def todB(Wats):
    return 10*np.log10(Wats)
def toWats(dB):
    return 10**(dB/10) 
def tomWats(dBm):
    return 10**(dBm/10) *10**-3
def watsMwats(W):
    return W*100
def mWatsWats(mW):
    return mW/0.01
def dBDBm(dB):
    return dB -30
def dBmDB(dBm):
    return dBm+30
def meToKm(dm):
    return dm/1000
def kmToM(km):
    return km*1000
def cmToKm(cm):
    return cm/100000
def millasToKm(millas):
    return millas*1.609
def hzToGhz(hz):
    hz/100000000
def mhzToGhz(mhz):
    mhz/1000
def khzToGhz(khz):
    return khz/100000
def dBdTodBi(dBd):
    return dBd + 2.15
def dBiTodBd(dBi):
    return dBi-2.15

if __name__ == "__main__":
    print(todBm(1000))
    print(megGig(917))