from EEGGen import EEGGen
import chart

if __name__ == "__main__":
    eeg = EEGGen()
    eeg.AddWave(1, 3)
    chart.plot(eeg.Generate(1))
