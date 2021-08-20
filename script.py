# librerias
import pandas as pd
import numpy as np
import random

# variables
variables = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
            "5", "6", "7", "8", "9", "0"]

# funcion aleatorio
def aleatorio():
    result = random.randint(0, 35)
    return result

# generar texto plano dinamico
codigo = []
iteraciones = 1000000

for i in range(0, iteraciones):
    add = variables[aleatorio()]
    codigo.append(add)
    #print(i, x, add)

# creando codigos a insertar
resultado = ""
resultado_final = resultado.join(codigo)
codigo_usar = []

for i in range(0, len(codigo), 9):
    if i > 9:
        hack = "L" + resultado_final[i-9:i]
        codigo_usar.append(hack)

    else:
        pass
print('codigos creados: ', len(codigo_usar))        