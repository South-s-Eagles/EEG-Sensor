package dispositivo

import (
	"fmt"
	"math/rand"
)

const maxVoltage = 10

// O sensor Eletrodo é apenas o sensor,
// ele tem a função apenas de capturar
// os dados (corrente elétrica) em
// uV (microvolts) e enviar para o Dispositivo
type Sensor struct {
	Valor   int8   `json:"valor"`   // Valor em microvolt da corrente elétrica
	Posicao string `json:"posicao"` // posicão do cérebro que está o sensor
}

// Função construtora para criar e inicializar um Sensor
func NewSensor() *Sensor {
	sensor := &Sensor{}
	sensor.Valor = 0
	sensor.Posicao = "Nil"
	return sensor
}

// Cria o sensor em lote de acordo com a quantidade passada
func criarSensoresEmLote(quantidade int) []Sensor {
	sensores := make([]Sensor, quantidade)
	for i := 0; i < quantidade; i++ {
		sensores[i] = *NewSensor()
	}
	return sensores
}

// Função para gerar valores aleatórios para o sensor
func (s *Sensor) gerarValores() {
	s.Valor = int8(rand.Intn(maxVoltage + 1))
}

// Formatar toString da struct
func (s Sensor) toString() string {
	return fmt.Sprintf("Posicao: %s\nValor: %d", s.Posicao, s.Valor)
}
