# Tarea4
Solución de la Tarea 4 del curso Modelos Probabilísticos de Señales y Sistemas. Estudiante: Jesús Rojas. Grupo 01

# Parte 1

En una modulación BPSK asignando una señal seno normalizada, se verá que cada vez que haya un 1, se verá la gráfica del seno, y cuando haya un 0 en la cadena de bits, se observará la función contraria. Esto se confirma al observarse la siguiente imagen que representa el comportamiento de los primeros 5 bits de la señal.

https://raw.githubusercontent.com/JRB-08/Tarea4/master/SenalTransmitida.png

# Parte 2

Se obtuvo una potencia promedio de la señal modulada de 0,4900009800019598

# Parte 3

Se simuló un canal ruidoso para cada valor de SNR (desde -2dB hasta 3dB).

Los primeros 5 bits de la señal modulada, una vez atravesado cada canal, se observan en las siguientes imágenes

Para un canal con SNR = -2dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/Rxm2.png

Para un canal con SNR = -1dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/Rxm1.png

Para un canal con SNR = 0dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/Rx0.png

Para un canal con SNR = 1dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/Rx1.png

Para un canal con SNR = 2dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/Rx2.png

Para un canal con SNR = 3dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/Rx3.png


# Parte 4

Para la PSD (Densidad Espectral de Potencia) se obtuvieron las siguientes gráficas.

Antes de atravesar los canales ruidosos:
https://raw.githubusercontent.com/JRB-08/Tarea4/master/PSDnormal.png

Después de atravesar el canal ruidoso con SNR = -2dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/PSDSNR-2.png

Después de atravesar el canal ruidoso con SNR = -1dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/PSDSNR-1.png

Después de atravesar el canal ruidoso con SNR = 0dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/PSDSNR0.png

Después de atravesar el canal ruidoso con SNR = 1dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/PSDSNR1.png

Después de atravesar el canal ruidoso con SNR = 2dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/PSDSNR2.png

Después de atravesar el canal ruidoso con SNR = 3dB
https://raw.githubusercontent.com/JRB-08/Tarea4/master/PSDSNR3.png

# Parte 5

Para este caso específico se obtuvo que:

Para el canal con SNR de -2dB, hay un total de 11.0 errores en 10000 bits para una tasa de error de 0.0011.

Para el canal con SNR de -1dB, hay un total de 4.0 errores en 10000 bits para una tasa de error de 0.0004.

Para el canal con SNR de 0dB, hay un total de 2.0 errores en 10000 bits para una tasa de error de 0.0002.

Para el canal con SNR de 1dB, hay un total de 0.0 errores en 10000 bits para una tasa de error de 0.0.

Para el canal con SNR de 2dB, hay un total de 0.0 errores en 10000 bits para una tasa de error de 0.0.

Para el canal con SNR de 3dB, hay un total de 0.0 errores en 10000 bits para una tasa de error de 0.0.

Esto cambia para cada simulación, pues el valor del ruido es aleatorio. Pero se observa que entre mayor sea el SNR, menor será la tasa de error durante la decodificación.

# Parte 6

Finalmente, se graficó la tasa de error en función del SNR. Y se obtuvo la siguiente gráfica.

https://raw.githubusercontent.com/JRB-08/Tarea4/master/BERvsSNR.png
