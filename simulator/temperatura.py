import datetime
import random
import time
import matplotlib.pyplot as plt
import sql

def capturar_dados():
    x =  ({
        "graus": random.uniform(15, 35),
        "data_atual": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    sql.insert_value("temperatura", x["data_atual"], x["graus"])
            