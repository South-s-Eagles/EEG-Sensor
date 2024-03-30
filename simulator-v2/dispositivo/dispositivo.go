package dispositivo

import (
	"errors"
	"fmt"
)

// Dispositivo em si do EEG
// Ele é a "caixa preta" que vai ter os
// sensores, vai ser o dispositivo IOT de fato,
// que vai conseguir enviar os dados tratados
// conseguir ter a inteligência de tratar os dados
// recebidos pelo sensor e guardar para enviar com
// calma para o broker (IOT HUB)
type Dispositivo struct {
	Sensores   []Sensor // Sensores que existem no Dispositivo
	Bateria    float32  // Quantidade de bateria em porcentagem
	Frequencia float32  // Valor em hz da Frequencia da corrente elétrica
	Amplitude  float32  // Valor da Amplitude da onda da corrente elétrica
	ligado     bool     // Estado do Dispositivo se está ligado ou desligado
}

// Lista todos os sensores no dispositivo
func (d *Dispositivo) listarSensores() {
	for i, v := range d.Sensores {
		fmt.Printf("Sensor: %d, %s", i, v.toString())
	}
}

func NewDispositivo(sensorQtd int8) (Dispositivo, error) {
	// if sensorQtd > 10 {
	// 	return nil, errors.New("não é possível criar um dispositivo com mais de 10 sensores")
	// }

	sensores := criarSensoresEmLote(int(sensorQtd))

	d := Dispositivo{
		Sensores:   sensores,
		Bateria:    100.0,
		Frequencia: 0,
		Amplitude:  0,
		ligado:     true,
	}

	return d, nil
}

// TODO: Transforma os dados recebidos em hz
func (d *Dispositivo) transformarParaHeartz(uV ...float64) {
}

// Envia os dados em heartz recebidos para o broker
// NOTE: Sera que faz sentido isso aqui ainda?
func (d *Dispositivo) enviarMensagem(arr []byte) {
	fmt.Println("dados enviados para o broker")
	d.reduzirBateria(0.1)
}

// Reduz a bateria
func (d *Dispositivo) reduzirBateria(value float32) {
	d.Bateria -= value
	err := d.validarBateria()
	if err != nil {
		fmt.Println("Desligando dispositvo")
		d.desligarDevice()
	}
}

// Validar a vida da bateria.
func (d *Dispositivo) validarBateria() error {
	if d.Bateria <= 0 {
		d.ligado = false
		return errors.New("bateria descarregada")
	}
	return nil
}

// Desliga o dispositivo
func (d *Dispositivo) desligarDevice() {
	d.ligado = false
}
