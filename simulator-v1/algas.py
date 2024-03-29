import threading
import cortisol
import glicose
import eeg
import heartrate
import temperatura
import time
import chart

def run_data_collection():

    segundos = []
    SECONDS = 1 / 10

    try:
        while True:
            inicio = time.time()
            cortisol.gerar_dados()
            glicose.simulate_glucose()
            eeg.generate()
            heartrate.simulate_sensor()
            temperatura.capturar_dados()
            fim = time.time()
            segundos.append(round(fim - inicio, 2))
            time.sleep(SECONDS)
    except KeyboardInterrupt:
        chart.simple_plot(segundos, SECONDS)

def main():
    num_threads = 5
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=run_data_collection)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
