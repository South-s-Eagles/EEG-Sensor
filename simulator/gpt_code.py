import numpy as np
import matplotlib.pyplot as plt
import time


def generate_eeg_data(duration=10, sampling_rate=1000, noise_level=0.5):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    # Gerar sinal de EEG simulado com picos reais
    eeg_signal = 0.2 * np.sin(2 * np.pi * 10 * t) + 0.1 * np.sin(2 * np.pi * 5 * t)

    # Adicionar picos reais (eventos)
    num_peaks = 5
    peak_times = np.sort(np.random.uniform(0, duration, num_peaks))
    peak_amplitudes = np.random.uniform(1, 2, num_peaks)

    for peak_time, peak_amplitude in zip(peak_times, peak_amplitudes):
        eeg_signal[int(peak_time * sampling_rate)] += peak_amplitude

    # Adicionar ruído
    noise = noise_level * np.random.normal(size=len(t))
    eeg_signal += noise

    return t, eeg_signal


def plot_eeg_data(t, eeg_signal):
    plt.figure(figsize=(12, 6))
    plt.plot(t, eeg_signal, label="EEG Signal")
    plt.title("Simulated EEG Data with Realistic Peaks")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    duration = 10  # segundos
    sampling_rate = 1000  # Hz
    noise_level = 0.5

    while True:
        t, eeg_signal = generate_eeg_data(duration, sampling_rate, noise_level)
        print(f"Tempo é de {t}")
        print(f"Signal é de {eeg_signal}")
        time.sleep(1)
