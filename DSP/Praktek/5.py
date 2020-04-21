#DFT
import math
import array as array
import numpy as np
import matplotlib.pyplot as plt

K = 1024
N = 4
om = np.array((range(0, K)))

Xs = [0] * K
kom = [0] * N

om = [(i / K * 2 * math.pi) for i in om]

Xs = [(1 - 0.5 * math.cos(i) + 1.5 * 1j * math.sin(i)) for i in om]

ampXS = np.absolute(Xs)
phaseXS = np.angle(Xs)
realXS = np.real(Xs)
imagXS = np.imag(Xs)

