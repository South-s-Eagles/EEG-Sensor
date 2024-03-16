import random
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
import time
from enum import Enum
from scipy.stats import norm
from scipy.interpolate import interp1d
import numpy as np


class Sign(Enum):
    PLUS = "+"
    MINUS = "-"

    def choose_sign(self, wave_variation: float):
        if random.random() < wave_variation:
            return self
        else:
            if self.name == "PLUS":
                return Sign.MINUS
            return Sign.PLUS


class Frequency:
    def __init__(self, min: float, max: float, flow: float):
        self.min = min
        self.max = max
        self.flow = flow


class Wave:
    def __init__(self, name: str, min_freq: float, max_freq: float, flow: float):
        self.name = name
        self.frequency = Frequency(min_freq, max_freq, flow)
        self.variation = random.uniform(min_freq, max_freq)
        self.actual = round(min_freq, 3)
        self.curve = random.choice(list(Sign))

    def to_string(self):
        return f"name: {self.name}\nmin_freq: {self.frequency.min}\nmax_freq: {self.frequency.max}\nvariation: {self.variation}\nactual: {self.actual}\ncurve: {self.curve.value}"

    def is_max_out_of_bound(self) -> bool:
        return self.actual >= self.frequency.max

    def is_min_out_of_bound(self) -> bool:
        return self.actual <= self.frequency.min

    def generate_wave(self):
        self.curve = self.curve.choose_sign(self.frequency.flow)

        variation_ratio = random.uniform(0.01, 0.03)
        variation_amount = self.actual * variation_ratio

        if self.is_max_out_of_bound():
            self.curve = Sign.MINUS
        if self.is_min_out_of_bound():
            self.curve = Sign.PLUS

        if self.curve == Sign.MINUS:
            self.actual = round(
                max(self.frequency.min, self.actual - variation_amount), 3
            )
        else:
            self.actual = round(
                min(self.frequency.max, self.actual + variation_amount), 3
            )

    def plot_frequency_graph(self, frequencies, seconds):
        plt.plot(frequencies)
        plt.xlabel(f"{seconds} segundo(s)")
        plt.ylabel("Frequência (em Hz)")
        plt.title(f"Ondas {self.name}")
        plt.show()


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
    # Interpolação cúbica para suavizar as linhas
    f = interp1d(time, frequency, kind="cubic")

    # Novo conjunto de pontos de tempo para a curva suavizada
    time_smooth = np.linspace(min(time), max(time), 300)

    # Calcula os valores de frequência para a curva suavizada
    frequency_smooth = f(time_smooth)

    # Plota os pontos de dados do EEG e a curva suavizada
    plt.plot(time, frequency, "bo", label="Dados de EEG")  # Pontos de dados do EEG
    plt.plot(
        time_smooth, frequency_smooth, "r-", label="Curva Suavizada"
    )  # Curva suavizada
    plt.legend()

    plt.title("Dados de EEG com Curva Suavizada")
    plt.xlabel("Tempo")
    plt.ylabel("Frequência (Hz)")
    plt.show()


if __name__ == "__main__":
    wave_definitions = []

    time_variation = 1 / 1000

    inicio = time.time()
    current_time = time.time()
    frequency = []

    wave = Wave("Delta", 0.5, 4, 0.95)
    # wave = Wave("Theta", 4, 8, 0.85)
    # wave = Wave("Alpha", 8, 12, 0.7)
    # wave = Wave("Beta", 12, 25, 0.45)
    # wave = Wave("Gamma", 25, 40, 0.25)

    while current_time - inicio < 1:
        current_time = time.time()
        wave.generate_wave()
        frequency.append(wave.actual)
        time.sleep(time_variation)

    # plot(frequency, 1)
    # plot_eeg_with_normal_curve(frequency, time=np.linspace(0, 10, len(frequency)))
    #
    time = np.linspace(0, 10, len(frequency))
    plot_with_smooth_curve(frequency, time)
