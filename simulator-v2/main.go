package main

import (
	"encoding/json"
	"fmt"

	"github.com/South-s-Eagles/EEG-electroencephalogram/broker"
	_ "github.com/South-s-Eagles/EEG-electroencephalogram/broker"
	"github.com/South-s-Eagles/EEG-electroencephalogram/dispositivo"
)

const (
	sleepTime = 2
	azToken   = ""
)

func main() {

	azr, err := broker.NewAzureBroker(azToken)
	if err != nil {
		panic(err)
	}

	d, err := dispositivo.NewDispositivo(8)
	if err != nil {
		panic(err)
	}
	for {
		d.Run()

		fmt.Println(d.Amplitude)
		fmt.Println(d.Frequencia)

		payload, err := json.Marshal(d)
		if err != nil {
			panic(err)
		}

		azr.SendMessage(payload)
	}
}
