package dispositivo

import (
	"fmt"
	"math/rand"
)

// O sensor Eletrodo é apenas o sensor,
// ele tem a função apenas de capturar
// os dados (corrente elétrica) em
// uV (microvolts) e enviar para o Dispositivo
type Sensor struct {
	Valor   int8   // Valor em microvolt da corrente elétrica
	Posicao string // posicão do cérebro que está o sensor
}

// Função construtora para criar e inicializar um Sensor
func NewSensor() *Sensor {
	sensor := &Sensor{}
	sensor.gerarValores(int8(rand.Intn(11)))
	return sensor
}

func criarSensoresEmLote(quantidade int) []Sensor {
	sensores := make([]Sensor, quantidade)
	for i := 0; i < quantidade; i++ {
		sensores[i] = *NewSensor()
	}
	return sensores
}

// Função para gerar valores aleatórios para o sensor
func (s *Sensor) gerarValores(value int8) {
	s.Valor = value
	s.Posicao = fmt.Sprintf("Posicao %d", value)
}

func (s Sensor) toString() string {
	return fmt.Sprintf("Posicao: %s\nValor: %d", s.Posicao, s.Valor)
}
