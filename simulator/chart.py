import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.interpolate import interp1d
import numpy as np


def plot(frequency):
    plt.plot(frequency)
    plt.ylabel("Frequência (em Hz)")
    plt.title("Ondas")
    plt.show()
