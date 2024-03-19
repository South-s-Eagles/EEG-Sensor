import numpy as np
import matplotlib.pyplot as plt
import time
import sql

def simulate_glucose():

    glucose_level = 100 + np.random.normal(0, 5)
    glucose_level = max(glucose_level, 0)
    
    sql.insert_value("glicose",  str(time.time()), glucose_level)