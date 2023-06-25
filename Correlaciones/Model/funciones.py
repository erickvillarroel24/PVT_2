#%%
# librerias
import math

#%%
#Funcion para Rs
def Rs(Correlacion, P, API, T, Yg = None, Yo = None):
    """
    :param Correlacion: Standing=1 o Glaso=2
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
        return round(Rs,3)

    elif Correlacion == 2:
        x2 = 2.8869 - (14.811 - (3.3093*math.log(P,10)))**0.5
        Pb = 10**x2
        Rs = Yg*(((API**0.989/(T-469)**0.172)*Pb))**1.2255
        return round(Rs,3)

#%%
#Funcion para Bo
def Bo(Correlacion, Rs, T, Yg, API= None, Yo = None):
    """
    :param Correlacion: Standing=1 o Glaso=2
    :param Rs: Sol
    :param T: Solubilidad del gas (pcn/bn)
    :param Yg: Gravedad especifica del gas
    :param API: Gravedad API del petroleo
    :param Yo: Gravedad especifica del petroleo
    :return: Factor volumetrico del petroleo (Bo) [bbls/stb]
    """
    if Correlacion == 1:
        Bo = 0.9759 + 0.000120*(((Rs*((Yg/Yo)**0.5)) + (1.25*(T-460))))**1.2
        return round(Bo,3)

    elif Correlacion == 2:
        bob = (Rs*((Yg/Yo)**0.526)) + (0.968*(T - 460))
        a = -6.58511 + (2.91329*math.log(bob,10)) - (0.27683*(math.log(bob))**2)
        Bo = 1 + (10**a)
        return round(Bo,3)

#%%
#Funcion para Pb
def Pb(Correlacion, Rs, T, API, Yg):
    """
    :param Correlacion: Standing=1 o Glaso=2
    :param Rs: Solubilidad del gas (pcn/bn)
    :param T: Temperatura del sistema
    :param API: Gravedad API del petroleo
    :param Yg: Gravedad especifica del gas
    :return: Presion de burbuja (psi)
    """
    a = 0.816
    b = 0.172
    c = -0.989
    if Correlacion == 1:
        a1 = 0.00091*(T-460) - (0.0125*API)
        Pb = 18.2*(((Rs/Yg)**0.83)*(10**a1)-1.4)
        return round(Pb,3)

    elif Correlacion == 2:
        pbb = ((Rs/Yg)**a)*(T**b)*(API**c)
        Pb = 10**(1.7669 + (1.7447*math.log(pbb,10))- (0.30218*(math.log(pbb,10))**2))
        return round(Pb,3)

#%%
#Funcion para Uo
def Uo(Correlacion, API, T):
    """
    :param Correlacion: Beggs & Robinson=1 o Glaso=2
    :param API: Gravedad API del petroleo
    :param T: Temperatura del sistema
    :return: Viscosidad del petroleo en cp
    """
    z = 3.024 - (0.02023*API)
    y = 10**z
    x = y*((T-460)**(-1.163))
    a = (10.313*math.log((T-460),10)) - 36.447
    if Correlacion == 1:
        uo = (10**x) - 1
        return round(uo,3)

    elif Correlacion == 2:
        uo = 3.141*(10**10)*(T-460)**(-3.414)*(math.log(API,10))**a
        return round(uo,3)
