#### Modelos Probabilísticos de Señales y Sistemas
#### Tarea 4
#### Nombre: Jesús Rojas Barrantes
#### Carne: B46040
#### Grupo: 01

import numpy as np

from scipy import stats

import scipy.stats.mstats as ms

import matplotlib.pyplot as plt

import csv

import pandas as pd

from scipy import integrate

from scipy import signal

#Extraer los datos de una versión modificada de xy.csv sin la primera columna
bitspd = pd.read_csv("bits10k.csv")
#Convertir los datos en una cadena de bits
bits = np.array(bitspd.to_numpy()).astype("int")



#################################################
################ Parte 1 ########################
#################################################

#Número de bits
N = len(bits)

# Frecuencia de operación
f = 5000 # Hz

# Duración del período de cada símbolo (onda)
T = 1/f # 0,2 ms

# Número de puntos de muestreo por período
p = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

# Creación de la forma de onda de la portadora - seno
portadora = np.sin(2*np.pi * f * tp)

# Frecuencia de muestreo
fs = p/T # 250 kHz

# Creación de la línea temporal para toda la señal
t = np.linspace(0, N*T, N*p)

# Inicializar el vector de la señal modulada 
senal = np.zeros(t.shape)

# Creación de la señal modulada BPSK
for k, b in enumerate(bits):
    senal[k*p:(k+1)*p] = (2*b-1) * portadora

# Visualización de los primeros bits modulados
pb = 5
plt.figure()
plt.plot(senal[0:pb*p])
plt.savefig('SenalTransmitida.png')


########################################################
################ Parte 2 ###############################
########################################################


# Potencia instantánea
Pinst = senal**2

# Potencia promedio a partir de la potencia instantánea (W)
Ps = integrate.trapz(Pinst, t) / (N * T)

print('La potencia promedio de la señal modulada es', Ps)


#########################################################
################ Parte 3 ################################
#########################################################

#Definición de un vector con los valores de SNR 
vectorSNR = [-2,-1,0,1,2,3]

#función de la Potencia del ruido
def Pn(snr):
  return Ps/(10**(snr/10))

#función de la desviación estándar del ruido
def sigma(pn):
  return np.sqrt(pn)

#Canales según el SNR
Rxm2 = 0
Rxm1 = 0
Rx0 = 0
Rx1 = 0 
Rx2 = 0
Rx3 = 0

for i in range(len(vectorSNR)):
  #Crear el ruido para cada SNR
  ruido = np.random.normal(0, sigma(Pn(vectorSNR[i])), senal.shape)
  #Simulación de cada señal recibida
  if i == 0:
    Rxm2 = Rxm2 + senal + ruido
  elif i == 1:
    Rxm1 = Rxm1 + senal + ruido
  elif i == 2:
    Rx0 = Rx0 + senal + ruido
  elif i == 3:
    Rx1 = Rx1 + senal + ruido
  elif i == 4:
    Rx2 = Rx2 + senal + ruido
  else:
    Rx3 = Rx3 + senal + ruido


# Visualización de los primeros bits recibidos par canal con SNR = -2
pb = 5
plt.cla()
plt.figure()
plt.plot(Rxm2[0:pb*p])
plt.savefig('Rxm2.png')
# Visualización de los primeros bits recibidos par canal con SNR = -1
plt.cla()
plt.figure()
plt.plot(Rxm1[0:pb*p])
plt.savefig('Rxm1.png')
# Visualización de los primeros bits recibidos par canal con SNR = 0
plt.cla()
plt.figure()
plt.plot(Rx0[0:pb*p])
plt.savefig('Rx0.png')
# Visualización de los primeros bits recibidos par canal con SNR = 1
plt.cla()
plt.figure()
plt.plot(Rx1[0:pb*p])
plt.savefig('Rx1.png')
# Visualización de los primeros bits recibidos par canal con SNR = 2
plt.cla()
plt.figure()
plt.plot(Rx2[0:pb*p])
plt.savefig('Rx2.png')
# Visualización de los primeros bits recibidos par canal con SNR = 3
plt.cla()
plt.figure()
plt.plot(Rx3[0:pb*p])
plt.savefig('Rx3.png')


#########################################################
################ Parte 4 ################################
#########################################################

# Antes del canal ruidoso
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.cla()
plt.figure()
plt.semilogy(fw, PSD)
plt.title('PSD antes del canal ruidoso')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('PSDnormal.png')

# Después del canal ruidoso con SNR = -2dB
fw, PSD = signal.welch(Rxm2, fs, nperseg=1024)
plt.cla()
plt.figure()
plt.semilogy(fw, PSD)
plt.title('PSD despues del canal ruidoso, SNR = -2dB')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('PSDSNR-2dB.png')

# Después del canal ruidoso con SNR = -1dB
fw, PSD = signal.welch(Rxm1, fs, nperseg=1024)
plt.cla()
plt.figure()
plt.semilogy(fw, PSD)
plt.title('PSD despues del canal ruidoso, SNR = -1dB')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('PSDSNR-1dB.png')

# Después del canal ruidoso con SNR = 0dB
fw, PSD = signal.welch(Rx0, fs, nperseg=1024)
plt.cla()
plt.figure()
plt.semilogy(fw, PSD)
plt.title('PSD despues del canal ruidoso, SNR = 0dB')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('PSDSNR0dB.png')

# Después del canal ruidoso con SNR = 1dB
fw, PSD = signal.welch(Rx1, fs, nperseg=1024)
plt.cla()
plt.figure()
plt.semilogy(fw, PSD)
plt.title('PSD despues del canal ruidoso, SNR = 1dB')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('PSDSNR1dB.png')

# Después del canal ruidoso con SNR = 2dB
fw, PSD = signal.welch(Rx2, fs, nperseg=1024)
plt.cla()
plt.figure()
plt.semilogy(fw, PSD)
plt.title('PSD despues del canal ruidoso, SNR = 2dB')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('PSDSNR2dB.png')

# Después del canal ruidoso con SNR = 3dB
fw, PSD = signal.welch(Rx3, fs, nperseg=1024)
plt.cla()
plt.figure()
plt.semilogy(fw, PSD)
plt.title('PSD despues del canal ruidoso, SNR = 3dB')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('PSDSNR3dB.png')

#########################################################
################ Parte 5 ################################
#########################################################

# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(portadora**2)

# Inicialización de los vectores de bits recibidos
bitsRxm2 = np.zeros(bits.shape)
bitsRxm1 = np.zeros(bits.shape)
bitsRx0 = np.zeros(bits.shape)
bitsRx1 = np.zeros(bits.shape)
bitsRx2 = np.zeros(bits.shape)
bitsRx3 = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía para el canal de SNR = -2dB
for k, b in enumerate(bits):
    Ep = np.sum(Rxm2[k*p:(k+1)*p] * portadora)
    if Ep > Es/2:
        bitsRxm2[k] = 1
    else:
        bitsRxm2[k] = 0

errm2 = np.sum(np.abs(bits - bitsRxm2))
BERm2 = errm2/N
print('Para el canal con SNR de -2dB, hay un total de {} errores en {} bits para una tasa de error de {}.'.format(errm2, N, BERm2))

# Decodificación de la señal por detección de energía para el canal de SNR = -1dB
for k, b in enumerate(bits):
    Ep = np.sum(Rxm1[k*p:(k+1)*p] * portadora)
    if Ep > Es/2:
        bitsRxm1[k] = 1
    else:
        bitsRxm1[k] = 0

errm1 = np.sum(np.abs(bits - bitsRxm1))
BERm1 = errm1/N
print('Para el canal con SNR de -1dB, hay un total de {} errores en {} bits para una tasa de error de {}.'.format(errm1, N, BERm1))

# Decodificación de la señal por detección de energía para el canal de SNR = 0dB
for k, b in enumerate(bits):
    Ep = np.sum(Rx0[k*p:(k+1)*p] * portadora)
    if Ep > Es/2:
        bitsRx0[k] = 1
    else:
        bitsRx0[k] = 0

err0 = np.sum(np.abs(bits - bitsRx0))
BER0 = err0/N
print('Para el canal con SNR de 0dB, hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err0, N, BER0))

# Decodificación de la señal por detección de energía para el canal de SNR = 1dB
for k, b in enumerate(bits):
    Ep = np.sum(Rx1[k*p:(k+1)*p] * portadora)
    if Ep > Es/2:
        bitsRx1[k] = 1
    else:
        bitsRx1[k] = 0

err1 = np.sum(np.abs(bits - bitsRx1))
BER1 = err1/N
print('Para el canal con SNR de 1dB, hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err1, N, BER1))

# Decodificación de la señal por detección de energía para el canal de SNR = 2dB
for k, b in enumerate(bits):
    Ep = np.sum(Rx2[k*p:(k+1)*p] * portadora)
    if Ep > Es/2:
        bitsRx2[k] = 1
    else:
        bitsRx2[k] = 0

err2 = np.sum(np.abs(bits - bitsRx2))
BER2 = err2/N
print('Para el canal con SNR de 2dB, hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err2, N, BER2))

# Decodificación de la señal por detección de energía para el canal de SNR = 3dB
for k, b in enumerate(bits):
    Ep = np.sum(Rx3[k*p:(k+1)*p] * portadora)
    if Ep > Es/2:
        bitsRx3[k] = 1
    else:
        bitsRx3[k] = 0

err3 = np.sum(np.abs(bits - bitsRx3))
BER3 = err3/N
print('Para el canal con SNR de 3dB, hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err3, N, BER3))


#########################################################
################ Parte 6 ################################
#########################################################

#Vector con las tasas de error de bits
BER = [BERm2, BERm1, BER0, BER1, BER2, BER3]
plt.cla()
plt.plot(vectorSNR, BER)
plt.savefig('BERvsSNR.png')