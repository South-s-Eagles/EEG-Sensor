package dispositivo

import "math/rand"

// O sensor Eletrodo é apenas o sensor,
// ele tem a função apenas de capturar
// os dados (corrente elétrica) em
// uV (microvolts) e enviar para o Dispositivo
type Sensor struct {
	Valor   int8   // Valor em microvolt da corrente elétrica
	Posicao string // posicão do cérebro que está o sensor
}

func (s *Sensor) generateValue() {
	s.Valor = int8(rand.Intn(11))
	s.Posicao = "Posicao 1"
}
