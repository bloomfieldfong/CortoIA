import numpy as np 


def derivateJ(theta, x, y):
    arreglo = []
    ##para las sumatorias de 1 hasta la posicion m 
    for i in range(x.shape[0]):
        ##shape en la posicion 0 de x es m 
        sumas = (1/(x.shape[0])) * (theta[i]*x[i]-y[i]) * x[i]
        arreglo.append(sumas) 
    ##nos retorna todas las derivadas
    return arreglo


