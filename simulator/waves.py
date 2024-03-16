# Project imports
import chart

# Lib imports
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


if __name__ == "__main__":
    wave_definitions = []

    time_variation = 1 / 1000

    inicio = time.time()
    current_time = time.time()
    frequency = []

    wave = Wave("Delta", 0.5, 4, 0.95)

    # Definindo o período total em segundos (um dia)
    total_period_seconds = 24 * 60 * 60

    while current_time - inicio < total_period_seconds:
        current_time = time.time()
        wave.generate_wave()
        frequency.append(wave.actual)
        time.sleep(time_variation)

    # Criando um array de tempo para representar as horas do dia
    tempo_dia = np.linspace(0, total_period_seconds, len(frequency))

    chart.plot(frequency)
