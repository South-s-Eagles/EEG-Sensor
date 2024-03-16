import random
import matplotlib.pyplot as plt
import time
from enum import Enum


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
        self.actual = round(min_freq, 2)
        self.curve = random.choice(list(Sign))
        self.flow = flow

    def to_string(self):
        return f"name: {self.name}\nmin_freq: {self.min_freq}\nmax_freq: {self.max_freq}\nvariation: {self.variation}\nactual: {self.actual}\ncurve: {self.curve.value}"

    def generate_wave(self):
        self.curve = self.curve.choose_sign(self.flow)

        variation_ratio = random.uniform(0.001, 0.003)
        variation_amount = self.actual * variation_ratio

        if self.is_max_out_of_bound():
            self.curve = Sign.MINUS
        if self.is_min_out_of_bound():
            self.curve = Sign.PLUS

        if self.curve == Sign.MINUS:
            self.actual = round(max(self.min_freq, self.actual - variation_amount), 2)
        else:
            self.actual = round(min(self.max_freq, self.actual + variation_amount), 2)

    def is_max_out_of_bound(self) -> bool:
        return self.actual >= self.max_freq

    def is_min_out_of_bound(self) -> bool:
        return self.actual <= self.min_freq


def plot_frequency_graph(frequencies, title):
    plt.plot(frequencies)
    plt.xlabel(f"Tempo em minutos")
    plt.ylabel("Frequência (em Hz)")
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    duration = 10000
    time_variation = 1 / 1000
