import matplotlib.pyplot as plt
import numpy as np


def plot(frequency):
    fig, ax = plt.subplots()

    # Supondo que frequency seja uma lista com a frequência em cada hora do dia
    hours_of_day = np.arange(len(frequency))

    ax.plot(hours_of_day, frequency, color="black", label="Frequência")

    # Desenha linhas horizontais para as diferentes ondas
    ax.axhline(y=4, color="green", linestyle="--", label="Delta (0.5-4 Hz)")
    ax.axhline(y=8, color="red", linestyle="--", label="Theta (4-8 Hz)")
    ax.axhline(y=12, color="blue", linestyle="--", label="Alpha (8-12 Hz)")
    ax.axhline(y=40, color="orange", linestyle="--", label="Beta (12-40 Hz)")
    ax.axhline(y=100, color="purple", linestyle="--", label="Gamma (40-100 Hz)")

    # Adiciona legendas personalizadas
    ax.legend(loc="upper right")
    plt.ylabel("Frequência (em Hz)")
    plt.xlabel("Hora do Dia")
    plt.title("Magnitude do Sinal do EEG ao Longo do Dia")

    ax.text(0, 4, "Delta", color="green", ha="right")
    ax.text(0, 8, "Theta", color="red", ha="right")
    ax.text(0, 12, "Alpha", color="blue", ha="right")
    ax.text(0, 40, "Beta", color="orange", ha="right")
    ax.text(0, 100, "Gamma", color="purple", ha="right")

    # Define os rótulos do eixo x como as horas do dia
    hour_labels = ["12AM", "3AM", "6AM", "9AM", "12PM", "3PM", "6PM", "9PM", "12AM"]

    # Distribuir igualmente os rótulos do eixo x
    hour_indices = np.linspace(0, len(hours_of_day) - 1, len(hour_labels), dtype=int)
    ax.set_xticks(hour_indices)
    ax.set_xticklabels(hour_labels)

    plt.tight_layout()

    plt.show()


def plot_microvolt(avg_per_second, time, wave):
    plt.plot(time[: len(avg_per_second)], avg_per_second)
    plt.title(f"Average {wave.capitalize()} Wave EEG per Second")
    plt.xlabel("Time (s)")
    plt.ylabel("Average Voltage (uV)")
    plt.show()
