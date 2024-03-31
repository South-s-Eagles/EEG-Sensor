package main

import (
	_ "github.com/South-s-Eagles/EEG-electroencephalogram/broker"
	"github.com/South-s-Eagles/EEG-electroencephalogram/dispositivo"
)

const (
	sleepTime = 2
	// NOTE: Colocar aqui para pegar de env de ambiente.
	azToken = ""
)

func main() {
	d, err := dispositivo.NewDispositivo(8)
	if err != nil {
		panic(err)
	}
	for {
		d.Run()
	}
}
