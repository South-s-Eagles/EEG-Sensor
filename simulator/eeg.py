from random import choice
import numpy as np
import matplotlib.pyplot as plt
import time
import sql


def generate_eeg_wave(wave_type, duration=1, fs=1000):
    num_samples = int(duration * fs)
    if wave_type == "delta":
        eeg_wave = np.random.normal(loc=2, scale=1, size=num_samples)
    elif wave_type == "theta":
        eeg_wave = np.random.normal(loc=4, scale=1, size=num_samples)
    elif wave_type == "alpha":
        eeg_wave = np.random.normal(loc=6, scale=1, size=num_samples)
    elif wave_type == "beta":
        eeg_wave = np.random.normal(loc=8, scale=1, size=num_samples)
    else:
        raise ValueError("Invalid wave type")
    return eeg_wave


def generate():
    waves = [("delta", 1, 10), ("theta", 1, 50), ("alpha", 1, 100), ("beta", 1, 1000)]

    wave_choose = choice(waves)
    eeg_wave = generate_eeg_wave(*wave_choose)
    duration = wave_choose[1]
    fs = wave_choose[2]
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    for voltage in eeg_wave:
        current_time_ms = int(time.time() * 1000)
        print(f"Time: {current_time_ms}, Voltage: {voltage}")
        sql.insert_value("eeg", str(current_time_ms), voltage)
