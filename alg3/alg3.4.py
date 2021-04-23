import numpy as np
import matplotlib.pyplot as plt
from cmath import pi, exp

def Fast_Fourier_transform(funkcja):
    n = len(funkcja)
    if n <= 1:
        return funkcja
    parzyste = Fast_Fourier_transform(funkcja[0::2])
    nieparzyste = Fast_Fourier_transform(funkcja[1::2])
    macierz = np.zeros(n).astype(np.complex64)
    for i in range(n // 2):
        macierz[i] = parzyste[i] + exp(-2j * pi * i / n) * nieparzyste[i]
        macierz[i + n // 2] = parzyste[i] - exp(-2j * pi * i / n) * nieparzyste[i]

    return macierz


n = 256
x = np.linspace(0, n * 1 / 400, n)
y = np.sin(64 * np.pi * x) + 0.5 * np.sin(128 * np.pi * x)

x_fft = np.linspace(0, 200, 128)
y_fft = Fast_Fourier_transform(y)

fig, ax = plt.subplots()
ax.plot(x_fft, 1 / 128 * np.abs(y_fft[:n // 2]))
plt.show()

# t = np.arange(0, 4 * np.pi, 0.1)
# y1 = 5 * np.sin(t) + 3 * np.sin(2 * t) + 5 * np.sin(5 * t)




