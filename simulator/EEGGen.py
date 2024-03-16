import numpy as np


class EEGComponent:
    def __init__(self, freq, amp, start=0, reps=np.inf):
        self.freq = freq
        self.amp = amp
        self.start = start
        if reps != np.inf:
            reps = np.round(reps)
        self.reps = reps

    def AddToEEG(self, eeg, sr):
        startN = int(round(self.start * sr))
        stopN = startN + np.round((self.reps / self.freq) * sr)
        if stopN > len(eeg):
            stopN = len(eeg)
        stopN = int(stopN)
        width = stopN - startN
        tvals = np.linspace(0, width / sr, width)
        eeg[startN:stopN] += self.amp * np.sin(2 * np.pi * tvals * self.freq)


class EEGGen:
    def __init__(self, sampling_rate=250):
        self.sampling_rate = sampling_rate
        self.components = []
        self.spikes = []
        self.time_coords = None

    def AddComp(self, component):
        self.components.append(component)

    def AddWave(self, freq, amp, start=0, reps=np.inf):
        self.AddComp(EEGComponent(freq, amp, start, reps))

    def Generate(self, duration, random_state=None):
        if random_state is not None:
            np.random.seed(random_state)
        N = int(round(duration * self.sampling_rate))
        eeg = np.zeros(N)
        self.time_coords = np.linspace(0, N / self.sampling_rate, N)

        for comp in self.components:
            comp.AddToEEG(eeg, self.sampling_rate)

        for spike in self.spikes:
            si = int(round(spike[0] * 0.3))
            if (si >= 0) and (si < N):
                eeg[si] += spike[1]

        return eeg
