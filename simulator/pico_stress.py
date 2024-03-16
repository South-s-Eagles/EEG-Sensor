import numpy as np
import matplotlib.pyplot as plt
import random


def generate_eeg_data():
    hours_in_day = 24
    time = np.arange(0, hours_in_day, 1)

    eeg_data = []
    for t in time:
        frequency = 10 + np.sin(2 * np.pi * t / hours_in_day) * 5
        if t == 14:
            frequency += 10
        eeg_data.append(frequency)

    return time, eeg_data


time, eeg_data = generate_eeg_data()

plt.figure(figsize=(10, 6))
plt.plot(time, eeg_data, color="blue")
plt.title("Simulação de Frequência do EEG ao Longo do Dia")
plt.xlabel("Horário do Dia (horas)")
plt.ylabel("Frequência do EEG (Hz)")
plt.grid(True)

plt.axvline(x=14, color="red", linestyle="--", linewidth=1)

plt.show()
