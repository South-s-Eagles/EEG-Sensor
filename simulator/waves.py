import random
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
import time
from enum import Enum
from scipy.stats import norm
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


class Wave:
    def __init__(self, name: str, min_freq: float, max_freq: float, flow: float):
        self.name = name
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.variation = random.uniform(min_freq, max_freq)
        self.actual = round(min_freq, 3)
        self.curve = random.choice(list(Sign))
        self.flow = flow

    def to_string(self):
        return f"name: {self.name}\nmin_freq: {self.min_freq}\nmax_freq: {self.max_freq}\nvariation: {self.variation}\nactual: {self.actual}\ncurve: {self.curve.value}"

    def is_max_out_of_bound(self) -> bool:
        return self.actual >= self.max_freq

    def is_min_out_of_bound(self) -> bool:
        return self.actual <= self.min_freq

    def generate_wave(self):
        self.curve = self.curve.choose_sign(self.flow)

        variation_ratio = random.uniform(0.01, 0.03)
        variation_amount = self.actual * variation_ratio

        if self.is_max_out_of_bound():
            self.curve = Sign.MINUS
        if self.is_min_out_of_bound():
            self.curve = Sign.PLUS

        if self.curve == Sign.MINUS:
            self.actual = round(max(self.min_freq, self.actual - variation_amount), 3)
        else:
            self.actual = round(min(self.max_freq, self.actual + variation_amount), 3)

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
    mu, std = norm.fit(frequency)  # Calcula a média e o desvio padrão dos dados
    plt.plot(
        time, frequency, marker="o", linestyle="None", label="Dados de EEG"
    )  # Plotando os dados de EEG

    # Calcula os limites para o gráfico da distribuição normal
    xmin, xmax = min(time), max(time)
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)

    # Plota a curva normal
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


if __name__ == "__main__":
    # wave_definitions = []

    # time_variation = 1 / 1000

    # inicio = time.time()
    # current_time = time.time()
    # frequency = []

    time = np.linspace(0, 10, 100)  # Tempo de 0 a 10 segundos
    frequency = np.random.normal(
        loc=10, scale=2, size=100
    )  # Dados fictícios de frequência com média 10 e desvio padrão 2
    plot_eeg_with_normal_curve(frequency, time)

    # wave = Wave("Delta", 0.5, 4, 0.98)
    # wave = Wave("Theta", 4, 8, 0.85)
    # wave = Wave("Alpha", 8, 12, 0.75)
    # wave = Wave("Beta", 12, 25, 0.45)
    # wave = Wave("Gamma", 25, 40, 0.25)

    # while current_time - inicio < 1:
    #     current_time = time.time()
    #     wave.generate_wave()
    #     frequency.append(wave.actual)
    #     print(wave.to_string())
    #     time.sleep(time_variation)
    #
    # plot(frequency, 5)
