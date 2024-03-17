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
    def __init__(self, name: str, min_freq: float, max_freq: float, flow: float, wave):
        self.name = name
        self.frequency = Frequency(min_freq, max_freq, flow)
        self.variation = random.uniform(min_freq, max_freq)
        self.actual = round(min_freq, 3)
        self.curve = random.choice(list(Sign))
        self.next = wave

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

    def GoToNextWave(self, frequency_list):
        transition_steps = 10
        for _ in range(transition_steps):
            transition_ratio = random.uniform(0.8, 1.2)
            if self.next is not None:
                transition_freq = (
                    self.actual
                    + (self.next.actual - self.actual)
                    * transition_ratio
                    / transition_steps
                )
                self.actual = round(transition_freq, 3)
                frequency_list.append(self.actual)
                time.sleep((1 / 5) / transition_steps)


if __name__ == "__main__":
    wave_definitions = []

    time_variation = 1 / 10

    inicio = time.time()
    current_time = time.time()
    frequency = []

    gamma = Wave(name="Gamma", min_freq=35, max_freq=100, flow=0.50, wave=None)
    beta = Wave(name="Beta", min_freq=10, max_freq=40, flow=0.65, wave=gamma)
    alpha = Wave(name="Alpha", min_freq=6, max_freq=12, flow=0.75, wave=beta)
    theta = Wave(name="Theta", min_freq=3, max_freq=8, flow=0.85, wave=alpha)
    delta = Wave(name="Delta", min_freq=0.5, max_freq=4, flow=0.95, wave=theta)

    current_wave = delta

    counter = 0

    while current_wave:
        if current_wave is None:
            break

        current_time = time.time()
        current_wave.Generate()
        frequency.append(current_wave.actual)

        if counter >= 100:
            current_wave.GoToNextWave(frequency)
            current_wave = current_wave.next
            counter = 0

        time.sleep(time_variation)
        counter += 1

    chart.plot(frequency)
