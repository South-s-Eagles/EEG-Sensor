import numpy as np
import time
import sql

def generate_data():
    time_points = np.linspace(0, 10, 100)  
    heart_rate = 60 + 40 * np.sqrt(time_points) + np.random.normal(0, 5, size=len(time_points))
    return time_points, heart_rate

def simulate_sensor():
    time_points, heart_rate  = generate_data()
    for t, hr in zip(time_points, heart_rate):

        sql.insert_value("heart-rate", str(t), hr)

