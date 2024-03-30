package dispositivo

import (
	"net/http"
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
	Bateria    float32 // Quantidade de bateria em porcentagem
	Frequencia float32 // Valor em hz da Frequencia da corrente elétrica
	Amplitude  float32 // Valor da Amplitude da onda da corrente elétrica
}

// TODO: Transforma os dados recebidos em hz
func (d Dispositivo) turnToHz(uV ...float64) {
}

// Envia os dados em heartz recebidos para o broker
func (d *Dispositivo) sendToBroker(arr []byte) {
	http.Get("https://6606dbacbe53febb857ec850.mockapi.io/go/pessoa")
	d.Bateria -= 0.1
}
