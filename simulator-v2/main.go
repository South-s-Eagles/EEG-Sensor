package main

import (
	"fmt"
	"net/http"

	_ "rsc.io/quote"
)

// Dispositivo em si do EEG
// Ele é a "caixa preta" que vai ter os
// sensores, vai ser o dispositivo IOT de fato,
// que vai conseguir enviar os dados tratados
// conseguir ter a inteligência de tratar os dados
// recebidos pelo sensor e guardar para enviar com
// calma para o broker (IOT HUB)
type Dispositivo struct {
	Sensor     Sensor  // Sensores que existem no Dispositivo
	Frequencia float64 // Valor em hz da Frequencia da corrente elétrica
	Amplitude  float64 // Valor da Amplitude da onda da corrente elétrica
}

// TODO: Transforma os dados recebidos em hz
func (d Dispositivo) turnToHz(uV ...float64) {
}

// Envia os dados em heartz recebidos para o broker
func (d Dispositivo) sendToBroker() {
	http.Get("https://6606dbacbe53febb857ec850.mockapi.io/go/pessoa")
}

// O sensor Eletrodo é apenas o sensor,
// ele tem a função apenas de capturar
// os dados (corrente elétrica) em
// uV (microvolts) e enviar para o Dispositivo
type Sensor struct {
	Valor float64 // Valor em microvolt da corrente elétrica
}

func (s Sensor) generateValue() int {
	return 0
}

func main() {
	sensor := Sensor{
		Valor: 10.0,
	}

	fmt.Println(sensor.generateValue())
}
