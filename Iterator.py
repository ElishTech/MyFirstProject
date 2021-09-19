import numpy as np

def sin_x(x):
    if x==0:
        return 1
    return np.sin(x)/x

def cos_x(x):
    if x==0:
        return 1
    return np.cos(x)/x

range=list( range(-100,101,1))
#range=[x for x in range(-100,101,1)]
comprehension=list( cos_x(x) for x in range)
