import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import random
import numpy as np
import time
import sql

def comportamentoNoturno(cortisol):
    i = random.random()
    if(i >= 0.6):
        return manter(cortisol)
    else:
        return diminuir(cortisol)
    
def comportamentoDiurno(cortisol):
    i = random.random()
    if(i >= 0.6):
        return manter(cortisol)
    else:
        return aumentar(cortisol)

def aumentar(cortisol):
    if(cortisol < 30):
        return cortisol + 0.05
    else:
        return cortisol

def diminuir(cortisol):
    if(cortisol >= 3):
        return cortisol - 0.01
    else:
        return cortisol

def manter(cortisol):
    return cortisol

def gerar_dados():
    cortisol = random.randint(3, 10)
    sql.insert_value("cortisol", str(time.time()), cortisol)