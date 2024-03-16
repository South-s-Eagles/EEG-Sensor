# Project imports
import chart

# Lib imports
import random
import time
from enum import Enum
import numpy as np


class Sign(Enum):
    PLUS = "+"
    MINUS = "-"

    def ChooseSign(self, wave_variation: float):
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

    def ToString(self):
        return f"name: {self.name}\nmin_freq: {self.frequency.min}\nmax_freq: {self.frequency.max}\nvariation: {self.variation}\nactual: {self.actual}\ncurve: {self.curve.value}"

    def IsMaxOutOfBound(self) -> bool:
        return self.actual >= self.frequency.max

    def IsMinOutOfBound(self) -> bool:
        return self.actual <= self.frequency.min

    def Generate(self):
        self.curve = self.curve.ChooseSign(self.frequency.flow)

        variation_ratio = random.uniform(0.01, 0.03)
        variation_amount = self.actual * variation_ratio

        if self.IsMaxOutOfBound():
            self.curve = Sign.MINUS
        if self.IsMinOutOfBound():
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

    while True:
        current_time = time.time()
        wave.Generate()
        frequency.append(wave.actual)
        time.sleep(time_variation)
        if current_time - inicio > 1:
            break

    chart.plot(frequency)
