#%%
import math

#%%
#Funcion para Rs
def rs(correlacion, P, API, T, Yg = None, Yo = None):
    """
    :param correlacion: Standing o Glaso
    :param P: Presion del sistema (psi)
    :param API: Gravedad API del petroleo
    :param T: Temperatura del sistema (°R)
    :param Yg: Densidad del gas
    :param Yo: Densidad del petroleo
    :return: Solubilidad del gas (Rs) [pcn/bn]
    """
    if correlacion == 'standing':
        x1 = 0.0125*API - 0.00091*(T-460)
        Rs = Yg*(((P/18.2)+1.4)*(10**x1))**1.2048
        return Rs
    elif correlacion == 'glaso':
        x2 = 2.8869 - (14.811 - (3.3093*math.log(P,10)))**0.5
        Pb = 10**x2
        Rs = Yg*(((API**0.989/(T-469)**0.172)*Pb))**1.2255
        return Rs

#%%
#Funcion para Bo

def Bo(correlacion, Rs, T, Yg, Yo = None, API = None):
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
    if API != None:
        yo = 141.5/(131.5 + API)
        if correlacion == 'marhoun':
            f = (Rs**a)*(Yg**b)*(yo**c)
            bo = 0.497069 + (0.862963*(10**-3))*T + (0.182524*(10**-2))*f + \
                 (0.318099*(10**-5))*(f**2)
            return bo
        elif correlacion == 'petrosky':
            bo = 1.0113 + (7.2046*(10**-5))*(((Rs**0.3778)*(Yg**0.2914/yo**0.6265))+
                                             ((0.24626)*(T-460)**0.5371))**3.0936
            return bo
    elif API == None:
        if correlacion == 'marhoun':
            f = (Rs ** a) * (Yg ** b) * (Yo ** c)
            bo = 0.497069 + (0.862963 * (10 ** -3)) * T + (0.182524 * (10 ** -2)) * f\
                 + (0.318099 * (10 ** -5)) * (f ** 2)
            return bo
        elif correlacion == 'petrosky':
            bo = 1.0113 + (7.2046 * (10 ** -5)) * (
                        ((Rs ** 0.3778) * (Yg ** 0.2914 / Yo ** 0.6265)) +
                        ((0.24626) * (T - 460) ** 0.5371)) ** 3.0936

#%%
b = Bo('petrosky', 24.18, 528, 0.85, None, 40)
print (b)