import numpy as np
import matplotlib.pyplot as plt
import time
import sql


def generate_eeg_data(duration=10, sampling_rate=1000, noise_level=0.5):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    eeg_signal = 0.2 * np.sin(2 * np.pi * 10 * t) + 0.1 * np.sin(2 * np.pi * 5 * t)

    num_peaks = 5
    peak_times = np.sort(np.random.uniform(0, duration, num_peaks))
    peak_amplitudes = np.random.uniform(1, 2, num_peaks)

    for peak_time, peak_amplitude in zip(peak_times, peak_amplitudes):
        eeg_signal[int(peak_time * sampling_rate)] += peak_amplitude

    noise = noise_level * np.random.normal(size=len(t))
    eeg_signal += noise

    # Calcular média a cada segundo
    avg_values = []
    for i in range(0, len(eeg_signal), sampling_rate):
        avg_values.append(np.mean(eeg_signal[i : i + sampling_rate]))

    return t, avg_values


def insert_average_values_to_db(t, avg_values):
    for tempo, value in zip(t, avg_values):
        # Converte os valores para string (se necessário)
        tempo_str = str(tempo)
        value_str = str(value)
        # Insere os valores no banco de dados
        sql.insert_value(tempo_str, value_str)


if __name__ == "__main__":
    duration = 10
    sampling_rate = 1000
    noise_level = 0.5

    while True:
        t, avg_values = generate_eeg_data(duration, sampling_rate, noise_level)
        print(f"Tempo é de {t.max()}")
        print(f"Média do sinal por segundo é de {type(avg_values)}")
        insert_average_values_to_db(t, avg_values)
        time.sleep(1)
