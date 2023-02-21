import numpy as np
def cilindro(r,h):
    S = 2*np.pi*r**2 + 2*np.pi*r*h
    V = np.pi*(r**2)*h
    return S,V

superficie,volume = cilindro(4,10)
print(f'S = {superficie:.2f} e V = {volume:.2f}')