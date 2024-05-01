package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"time"

	_ "github.com/South-s-Eagles/EEG-electroencephalogram/aws"
	"github.com/South-s-Eagles/EEG-electroencephalogram/database"
	"github.com/South-s-Eagles/EEG-electroencephalogram/dispositivo"
	"github.com/joho/godotenv"
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
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Não foi possível carregar .env file:", err)
	}

	databaseName := os.Getenv("DATABASE_NAME")
	colletionName := os.Getenv("DATABASE_COLLECTION_NAME")
	databaseClient := database.ConnectorClient()
	coll := databaseClient.Database(databaseName).Collection(colletionName)

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

				res, err := coll.InsertOne(context.Background(), externalPayload)
				if err != nil {
					fmt.Println("Erro ocorreu para mandar os dados para o database")
					fmt.Println(err)
				} else {
					fmt.Println(res)
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
