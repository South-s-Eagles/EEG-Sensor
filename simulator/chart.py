import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def plot(frequency):
    fig, ax = plt.subplots()
    ax.plot(frequency, color="black", label="Frequência")

    # Desenha linhas horizontais para as diferentes ondas
    ax.axhline(y=4, color="green", linestyle="--", label="Delta (0.5-4 Hz)")
    ax.axhline(y=8, color="red", linestyle="--", label="Theta (4-8 Hz)")
    ax.axhline(y=12, color="blue", linestyle="--", label="Alpha (8-12 Hz)")
    ax.axhline(y=40, color="orange", linestyle="--", label="Beta (12-40 Hz)")
    ax.axhline(y=100, color="purple", linestyle="--", label="Gamma (40-100 Hz)")

    # Adiciona legendas personalizadas
    ax.legend(loc="upper right")
    plt.ylabel("Frequência (em Hz)")
    plt.title("Ondas")

    # Adiciona descrições às linhas
    ax.text(0, 4, "Delta", color="green", ha="right")
    ax.text(0, 8, "Theta", color="red", ha="right")
    ax.text(0, 12, "Alpha", color="blue", ha="right")
    ax.text(0, 40, "Beta", color="orange", ha="right")
    ax.text(0, 100, "Gamma", color="purple", ha="right")

    plt.show()
