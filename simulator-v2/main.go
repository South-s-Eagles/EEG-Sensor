package main

import (
	"fmt"
	_ "time"

	_ "github.com/South-s-Eagles/EEG-electroencephalogram/broker"
	"github.com/South-s-Eagles/EEG-electroencephalogram/dispositivo"
)

const (
	sleepTime = 2
	// NOTE: Colocar aqui para pegar de env de ambiente.
	azToken = "HostName=ivan02221071.azure-devices.net;DeviceId=ivan02221071;SharedAccessKey=WgwvQTOkaRNUdYoD8cS2HnDZcQXkgyBDTAIoTAVFArg="
)

func main() {
	d, err := dispositivo.NewDispositivo(1)
	if err != nil {
		panic(err)
	}

	// Chame a função listarSensores no valor do tipo Dispositivo
	fmt.Println(d.Amplitude)
}
