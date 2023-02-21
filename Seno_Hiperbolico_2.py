import numpy as np

def seno_hiperbolico(x):
    y = (np.exp(x) - np.exp(-x))/2
    return y 

y1 = seno_hiperbolico(np.pi)
print(y1)