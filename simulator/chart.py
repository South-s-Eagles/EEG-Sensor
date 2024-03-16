import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.interpolate import interp1d
import numpy as np


def plot(frequency, seconds):
    plt.plot(frequency)
    plt.xlabel(f"{seconds} segundo(s)")
    plt.ylabel("Frequência (em Hz)")
    plt.title("Ondas")
    plt.show()


def plot_eeg_with_normal_curve(frequency, time):
    mu, std = norm.fit(frequency)
    plt.plot(time, frequency, marker="o", linestyle="None", label="Dados de EEG")

    xmin, xmax = min(time), max(time)
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)

    plt.plot(x, p, "k", linewidth=2, label="Curva Normal")
    plt.legend()

    title = "Distribuição de Frequência no EEG\nMédia: %.2f, Desvio Padrão: %.2f" % (
        mu,
        std,
    )
    plt.title(title)
    plt.xlabel("Tempo")
    plt.ylabel("Frequência (Hz)")
    plt.show()


def plot_with_smooth_curve(frequency, time):
    f = interp1d(time, frequency, kind="cubic")

    time_smooth = np.linspace(min(time), max(time), 300)

    frequency_smooth = f(time_smooth)

    plt.plot(time, frequency, "bo", label="Dados de EEG")  # Pontos de dados do EEG
    plt.plot(time_smooth, frequency_smooth, "r-", label="Curva Suavizada")
    plt.legend()

    plt.title("Dados de EEG com Curva Suavizada")
    plt.xlabel("Tempo")
    plt.ylabel("Frequência (Hz)")
    plt.show()
