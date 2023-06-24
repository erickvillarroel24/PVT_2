#%%
import math

import numpy as np


#%%
#Funcion para Rs

def rs2(Correlacion, P, API, T, Yg = None, Yo = None):
    """
    :param Correlacion: Standing o Glaso
    :param P: Presion del sistema (psi)
    :param API: Gravedad API del petroleo
    :param T: Temperatura del sistema (°R)
    :param Yg: Densidad del gas
    :param Yo: Densidad del petroleo
    :return: Solubilidad del gas (Rs) [pcn/bn]
    """
    if Correlacion == 1:
        x1 = (0.0125*API) - (0.00091*(T-460))
        Rs = Yg*(((P/18.2)+1.4)*(10**x1))**1.2048
        return Rs

    elif Correlacion == 2:
        x2 = 2.8869 - (14.811 - (3.3093*math.log(P,10)))**0.5
        Pb = 10**x2
        Rs = Yg*(((API**0.989/(T-469)**0.172)*Pb))**1.2255
        return Rs

#%%
def rs(Correlacion, P, API, T, Yg = None, Yo = None):
    """
    :param Correlacion: Standing o Glaso
    :param P: Presion del sistema (psi)
    :param API: Gravedad API del petroleo
    :param T: Temperatura del sistema (°R)
    :param Yg: Densidad del gas
    :param Yo: Densidad del petroleo
    :return: Solubilidad del gas (Rs) [pcn/bn]
    """
    Rs1 = []
    if Correlacion == 1:
        x1 = 0.0125*API - 0.00091*(T-460)
        for i in P:
            Rs = Yg*(((i/18.2)+1.4)*(10**x1))**1.2048
            Rs1.append(round(Rs,2))
        return Rs1

    elif Correlacion == 2:
        for j in P:
            x2 = 2.8869 - (14.811 - (3.3093*math.log(j,10)))**0.5
            Pb = 10**x2
            Rs = Yg*(((API**0.989/(T-469)**0.172)*Pb))**1.2255
            Rs1.append(round(Rs,2))
        return Rs1



#%%
#Funcion para Bo

def Bo(Correlacion, Rs, T, Yg, API = None, Yo = None):
    """
    :param Correlacion: Standing o Glaso
    :param Rs: Sol
    :param T: Solubilidad del gas (pcn/bn)
    :param Yg: Gravedad especifica del gas
    :param API: Gravedad API del petroleo
    :param Yo: Gravedad especifica del petroleo
    :return: Factor volumetrico del petroleo (Bo) [bbls/stb]
    """
    Bo1 = []
    if Correlacion == 'standing':
        for i in Rs:
            Bo = 0.9759 + 0.000120*(((i*((Yg/Yo)**0.5)) + (1.25*(T-460))))**1.2
            Bo1.append(round(Bo,2))
        return np.array(Bo1),np.array(Rs)


#%%
def BoP(correlacion, Rs, T, Yg, Yo = None, API = None):
    """
    :param correlacion: Al-Marhoun o Petrosky & Farshad
    :param Rs: Solubilidad del gas (pcn/bn)
    :param P: Presion del sistema (psi)
    :param API: Gravedad API del petroleo
    :param T: Temperatura del sistema
    :param Yg: Gravedad especifica del gas
    :param Yo: Gravedad especifica del petroleo
    :return: Factor volumetrico del petroleo (Bo) [bbls/stb]
    """
    a = 0.742390
    b = 0.323294
    c = -1.202040
    Bo1 = []
    if API != None:
        yo = 141.5/(131.5 + API)
        if correlacion == 'marhoun':
            for i in Rs:
                f = (i**a)*(Yg**b)*(yo**c)
                bo = 0.497069 + (0.862963*(10**-3))*T + (0.182524*(10**-2))*f + \
                (0.318099*(10**-5))*(f**2)
                Bo1.append(round(bo,2))
            return np.array(Bo1)
        elif correlacion == 'petrosky':
            for j in Rs:
                bo = 1.0113 + (7.2046*(10**-5))*(((j**0.3778)*(Yg**0.2914/yo**0.6265))
                +((0.24626)*(T-460)**0.5371))**3.0936
                Bo1.append(round(bo, 2))
            return np.array(Bo1)

    elif API == None:
        if correlacion == 'marhoun':
            for i in Rs:
                f = (i ** a) * (Yg ** b) * (Yo ** c)
                bo = 0.497069 + (0.862963 * (10 ** -3)) * T + (0.182524 * (10 ** -2))\
                * f + (0.318099 * (10 ** -5)) * (f ** 2)
                Bo1.append(round(bo, 2))
            return np.array(Bo1)

        elif correlacion == 'petrosky':
            for j in Rs:
                bo = 1.0113 + (7.2046 * (10 ** -5)) * (((j ** 0.3778)
                * (Yg ** 0.2914 / Yo ** 0.6265)) + ((0.24626) * (T - 460)
                ** 0.5371)) ** 3.0936
                Bo1.append(round(bo, 2))
            return np.array(Bo1)



#%%
#Funcion para Pb

def Pb(Correlacion, Rs, T, API, Yg):
    """
    :param Correlacion: Standing o Glaso
    :param Rs: Solubilidad del gas (pcn/bn)
    :param T: Temperatura del sistema
    :param API: Gravedad API del petroleo
    :param Yg: Gravedad especifica del gas
    :return: Presion de burbuja (psi)
    """
    a = 0.816
    b = 0.172
    c = -0.989
    Pb1 = []
    if Correlacion == 'standing':
        for i in Rs:
            a1 = 0.00091*(T-460) - (0.0125*API)
            Pb = 18.2*(((i/Yg)**0.83)*(10**a1)-1.4)
            Pb1.append(round(Pb,2))
        return np.array(Pb1)

    elif Correlacion == 'glaso':
        for j in Rs:
            pbb = ((j/Yg)**a)*(T**b)*(API**c)
            Pb = 10**(1.7669 + (1.7447*math.log(pbb,10))
            - (0.30218*(math.log(pbb,10))**2))
            Pb1.append(round(Pb, 2))
        return np.array(Pb1)

#%%
#Funcion para Uo
def uo(Correlacion, API, T):
    """
    :param Correlacion: Beggs & Robinson o Glaso
    :param API: Gravedad API del petroleo
    :param T: Temperatura del sistema
    :return: Viscosidad del petroleo en cp
    """
    z = 3.024 - (0.02023*API)
    y = 10**z
    x = y*((T-460)**(-1.163))
    a = (10.313*math.log((T-460),10)) - 36.447
    if Correlacion == 'beggs & robinson':
        uo = (10**x) - 1
        return uo

    elif Correlacion == 'glaso':
        uo = 3.141*(10**10)*(T-460)**(-3.414)*(math.log(API,10))**a
        return uo
