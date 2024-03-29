package dispositivo

import (
	"fmt"
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
	Frequencia float64 // Valor em hz da Frequencia da corrente elétrica
	Amplitude  float64 // Valor da Amplitude da onda da corrente elétrica
}

// Quando trabalhamos com structs podemos passar
// um objeto a parte como uma copia do objeto orinal
// ou o objeto em SI, passando o ponteiro dele, e alterando
// ele mesmo. fazemos isso com o *.
// Se não passamos o * o objeto real, não é alterado
func (d *Dispositivo) testComPonteiro() {
	fmt.Println(&d)
}

func (d Dispositivo) testSemPonteiro() {
	fmt.Println(&d)
}

// TODO: Transforma os dados recebidos em hz
func (d Dispositivo) turnToHz(uV ...float64) {
}

// Envia os dados em heartz recebidos para o broker
func (d Dispositivo) sendToBroker() {
	http.Get("https://6606dbacbe53febb857ec850.mockapi.io/go/pessoa")
}
