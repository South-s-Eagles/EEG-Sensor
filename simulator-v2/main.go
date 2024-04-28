package main

import (
	"context"
	"encoding/json"
	"fmt"
	"time"

	"github.com/South-s-Eagles/EEG-electroencephalogram/aws"
	"github.com/South-s-Eagles/EEG-electroencephalogram/dispositivo"
)

const (
	sleepTime     = 2
	azToken       = ""
	dataRetention = 5 * time.Second
)

type ExternalPayload struct {
	DispositivoId     string `json:"dispositivoId"`
	Dispositivo       string `json:"dispositivo"`
	Valor             int16  `json:"valor"`
	UnidadeMedida     string `json:"unidadeMedida"`
	ConteudoAdicional string `json:"conteudoAdicional"`
}

func main() {
	client := aws.Client()

	d, err := dispositivo.NewDispositivo(8)
	if err != nil {
		panic(err)
	}

	dataChan := make(chan *dispositivo.Dispositivo)

	go func() {
		var dataBuffer []*dispositivo.Dispositivo
		timer := time.NewTimer(dataRetention)
		defer timer.Stop()

		for {
			select {
			case newData := <-dataChan:
				dataBuffer = append(dataBuffer, newData)
			case <-timer.C:
				fmt.Println("Enviando os dados para armazenamento")
				devicePayload, err := json.Marshal(dataBuffer)
				if err != nil {
					fmt.Println("Erro ao serializar devicePayload:", err)
					continue
				}

				externalPayload := &ExternalPayload{
					DispositivoId:     dataBuffer[len(dataBuffer)-1].ID,
					Dispositivo:       "electroencephalogram",
					Valor:             10,
					UnidadeMedida:     "Hz",
					ConteudoAdicional: string(devicePayload),
				}

				externalPayloadJson, err := json.Marshal(externalPayload)
				if err != nil {
					fmt.Println("Erro ao serializar externalPayload:", err)
					continue
				}

				err = client.SendObject(context.TODO(), dataBuffer[len(dataBuffer)-1].ID, externalPayloadJson)
				if err != nil {
					fmt.Println(err)
				}

				dataBuffer = nil

				timer.Reset(dataRetention)
			}
		}
	}()

	for {
		d.Run()

		dataChan <- d

		time.Sleep(sleepTime * time.Second)
	}
}
