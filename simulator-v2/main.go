package main

import (
	"context"
	"encoding/json"
	"fmt"
	"time"

	"github.com/South-s-Eagles/EEG-electroencephalogram/aws"
	"github.com/South-s-Eagles/EEG-electroencephalogram/broker"
	_ "github.com/South-s-Eagles/EEG-electroencephalogram/broker"
	"github.com/South-s-Eagles/EEG-electroencephalogram/dispositivo"
)

const (
	sleepTime     = 2
	azToken       = "HostName=EEG-Simulator.azure-devices.net;DeviceId=eeg-simulator;SharedAccessKey=sxX+gQDWSpkpFbNfZ8xa1rifHRlO8n96aAIoTLnFe4I="
	dataRetention = 5 * time.Minute
)

func main() {
	client := aws.Client()

	azr, err := broker.NewAzureBroker(azToken)
	if err != nil {
		panic(err)
	}

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
				payload, err := json.Marshal(dataBuffer)
				if err != nil {
					fmt.Println("Erro ao serializar os dados:", err)
					continue
				}
				azr.SendMessage(payload)
				err = client.SendObject(context.TODO(), dataBuffer[len(dataBuffer)-1].ID, payload)
				if err != nil {
					fmt.Println("Erro ao enviar dados para o S3:", err)
				}

				dataBuffer = nil

				timer.Reset(dataRetention)
			}
		}
	}()

	for {
		d.Run()

		fmt.Println(d.Amplitude)
		fmt.Println(d.Frequencia)

		dataChan <- d

		time.Sleep(sleepTime * time.Second)
	}
}
