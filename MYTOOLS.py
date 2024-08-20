import math
pi = math.pi
PI_INT = int((pi-3)*(10**100))

e = math.e
E_INT = int((e-2)*(10**100))

def pi_real(n):
    return(str(math.pi)[:n+2])

def e_real(n):
    return(str(math.e)[:n+2])
