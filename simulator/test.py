import numpy as np
import matplotlib.pyplot as plt


def simulate_eeg_signal(
    num_intervals=24, interval_length=3600, mean_magnitude=5, std_dev=1
):
    magnitudes = np.random.normal(mean_magnitude, std_dev, num_intervals)
    return magnitudes


def plot_eeg_signal(magnitudes):
    num_intervals = len(magnitudes)

    time_intervals = np.arange(num_intervals)

    plt.figure(figsize=(12, 6))
    plt.plot(time_intervals, magnitudes, color="blue")

    plt.xlabel("Intervalo de Tempo (horas)")
    plt.ylabel("Magnitude do Sinal do EEG (µV)")
    plt.title("Magnitude do Sinal do EEG ao Longo do Dia")

    plt.grid(True)
    plt.tight_layout()
    plt.grid(visible=False)
    plt.show()


if __name__ == "__main__":
    eeg_magnitudes = simulate_eeg_signal()

    plot_eeg_signal(eeg_magnitudes)
