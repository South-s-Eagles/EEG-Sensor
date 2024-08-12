import random
import pandas as pd
from datetime import datetime, timedelta

def esta_no_intervalo(hora, intervalos_picos):
    for intervalo in intervalos_picos:
        inicio, fim = intervalo
        if inicio <= hora < fim:
            return True
    return False

def gerar_coordenadas_area():
    """
    Gera coordenadas aleatórias (latitude e longitude) dentro dos limites especificados.
    
    :return: Tupla (latitude, longitude)
    """
    lat_min, lat_max = -23.880815, -23.238822
    lon_min, lon_max = -46.863556, -46.308746
    
    latitude = round(random.uniform(lat_min, lat_max), 6)
    longitude = round(random.uniform(lon_min, lon_max), 6)
    
    return latitude, longitude

def gerar_dados_eeg_varias_pessoas(inicio, fim, intervalos_picos, pessoas):
    """
    Gera dados simulados de EEG e coordenadas para o período de tempo especificado para várias pessoas, com variações de frequência.

    :param inicio: Data e hora de início no formato 'YYYY-MM-DD HH:MM:SS'
    :param fim: Data e hora de término no formato 'YYYY-MM-DD HH:MM:SS'
    :param intervalos_picos: Lista de tuplas com intervalos de horas para picos de estresse (ex: [(16, 18), (20, 22)])
    :param pessoas: Lista de identificadores de pessoas (ex: ['Pessoa1', 'Pessoa2'])
    :return: DataFrame com dados de EEG simulados para todas as pessoas
    """
    data_inicio = datetime.strptime(inicio, '%Y-%m-%d %H:%M:%S')
    data_fim = datetime.strptime(fim, '%Y-%m-%d %H:%M:%S')

    dados = []

    for id in range(1, pessoas):

        data_atual = data_inicio
        latitude, longitude = gerar_coordenadas_area()
        while data_atual <= data_fim:
            hora = data_atual.hour

            if esta_no_intervalo(hora, intervalos_picos):
                frequencia_media = round(random.uniform(30.0, 50.0), 2)
            elif 0 <= hora < 6:
                frequencia_media = round(random.uniform(0.5, 10.0), 2)
            else:
                frequencia_media = round(random.uniform(10.0, 30.0), 2)


            dados.append([id, data_atual, frequencia_media, latitude, longitude])
            data_atual += timedelta(minutes=2)

    df = pd.DataFrame(dados, columns=['Dispotivo_id', 'Timestamp', 'Frequencia_Hz', 'Latitude', 'Longitude'])
    return df

inicio = '2024-08-01 00:00:00'
fim = '2024-08-01 23:59:59'
intervalos_picos = [(12, 18)] 
quantidade_devices = 5

df_eeg = gerar_dados_eeg_varias_pessoas(inicio, fim, intervalos_picos, quantidade_devices)

print(df_eeg.head())

df_eeg.to_csv('dados_eeg.csv', index=False)
