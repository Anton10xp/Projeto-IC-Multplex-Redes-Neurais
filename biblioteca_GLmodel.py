# GL_model module
# Program written by Ariadne Costa
# Last changes: 06 August 2018

import pylab
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import os

def CreateFolder(name_folder):
    """ cria uma pasta com nome da srt name_folder caso ela ainda nao exista no diretorio atual"""
    if (os.path.isdir(name_folder) == False): # se a pasta ainda nao existe, cria ela
         os.makedirs(name_folder)

def CalculateNormalizedPotentials(theta):
    """ devolve Vb, Vr, Vm para dado theta em graus"""
    alpha = 1.0
    Vmedia = 0.0
    theta_rad = math.pi*theta/180
    Vb = alpha*( (-1/(6**(0.5)))*math.cos(theta_rad) + (1/(2**(0.5)))*math.sin(theta_rad) ) - Vmedia
    Vr = alpha*( (-1/(6**(0.5)))*math.cos(theta_rad) - (1/(2**(0.5)))*math.sin(theta_rad) ) - Vmedia
    Vm = alpha*( (2/(6**(0.5)))*math.cos(theta_rad) ) - Vmedia
    return Vb,Vr,Vm

def CalculatePhiERF(V,Vm,sigma):
    """ devolve a funcao de disparo Phi integral da Gaussiana (erf) para
    um neuronio com potencial atual V, o potencial medio de disparo Vm e
    o parametro de desvio da funcao \sigma"""
    Vaux = (V - Vm)/(sigma*math.sqrt(2.0))
    Phi = (0.5 + 0.5*math.erf(Vaux))
    return Phi

def CalculateRho_Recurrence(Javg,Jdev,sigma,mu,Vb,Vr,Vm):
    """ devolve densidade media (Rho_avg) obtida por equacoes recorrentes,
    dados Javg,Jdev,sigma,mu"""
    # Parameter
    total_ks = 201  #de 1 a total_ks-1, onde 1 eh o valor inicializado

    name_Javg = str("%.3f" % Javg)
    Vk_avg = np.zeros(total_ks)
    Vk_dev = np.zeros(total_ks)
    Phi_dev = np.zeros(total_ks)
    P = np.zeros(total_ks)
    Q = np.zeros(total_ks)
    Qacu = np.zeros(total_ks)

    # Valores iniciais (k = 0)
    Vk_avg[1] = Vr + Javg
    name_Vinicial = str("%.4f" % Vk_avg[1])
    Vk_dev[1] = Jdev
    Qacu[1] = 1

    soma = 0.0
    for k in range(2,total_ks):
        # calculo de Vavg e V
        Vk_avg[k] = Vb + (Vk_avg[k-1] - Vb)*mu + Javg
        Vk_dev[k] = math.sqrt((Vk_dev[k-1] + mu)**2 + Jdev**2)

        # calculo da Phi (Pk)
        Phi_dev = math.sqrt(sigma**2 + Vk_dev[k]**2)
        Phi = CalculatePhiERF(Vk_avg[k],Vm,Phi_dev)
        P[k] = Phi

        # calculo de Qk acumulada e normal
        Qacu[k] = Qacu[k-1]*(1-P[k])
        Q[k-1] = Qacu[k-1] - Qacu[k]

        # calculo de Rho
        soma += (k-1)*Q[k-1]

    Rho = 1.0/soma
    return Rho

def Bisection(a,b,nivel,Jdev,sigma,mu,Vb,Vr,Vm):
    """devolve o valor de Javg, no intervalo [a,b] tal que Rho_avg ~ nivel
    a e b sao os valores iniciais minimo e maximo para calculo da bissecao"""
    # Parameters
    tol_Javg = 0.0001
    tol_Rho_avg = 0.00001

    fa = CalculateRho_Recurrence(a,Jdev,sigma,mu,Vb,Vr,Vm)
    assert fa<nivel
    fb = CalculateRho_Recurrence(b,Jdev,sigma,mu,Vb,Vr,Vm)
    assert fb>nivel
    while True:
        c = (b + a)/float(2)
        fc = CalculateRho_Recurrence(c,Jdev,sigma,mu,Vb,Vr,Vm)
        if (abs(fc-nivel)<tol_Rho_avg and abs(a-b)<tol_Javg):
            return c
        if (fc < nivel):
            a = c; fa=fc
        else:
            b=c; fb=fc


def CheckSpiking(prob):
    """ checa se o neuronio deve disparar ou nao """
    x = np.random.uniform()
    if (x <= prob):
        S = 1
    else:
        S = 0
    return S

def UpdatePotential(V_old,Vr,Vb,S,mu,J):
   """ atualiza potencial do neuronio """
   if (S == 0):
       V = Vb + mu*(V_old-Vb) + J
   else:
       V = Vr + J
   return V

#def DefineAxesForContourPlot(x,y,z):
#    """devolve os valores dos eixos x, y e z para gerar o countorf plot"""
#    xi = np.linspace(min(x),max(x),1000)
#    yi = np.linspace(min(y),max(y),1000)
#    zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')
