from EEGGen import EEGGen
from logging import currentframe
from Wave import Wave
import chart
import numpy as np
import time

if __name__ == "__main__":
    wave = Wave("Delta", 0, 4, 0.9)
    inicio = time.time()
    frequency = []
    while True:
        current_time = time.time()
        wave.Generate()
        frequency.append(wave.actual)
        if current_time - inicio > 5:
            break
        time.sleep(1 / 100)
        print(wave.ToString())
    chart.plot(frequency)
