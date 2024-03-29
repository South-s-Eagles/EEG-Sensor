package main

import (
	"errors"
	"fmt"
	"net/http"

	"rsc.io/quote"
)

// NOTE:
// Dispositivo em si do eeg
// Ele é a "caixa preta" que vai ter os
// sensores. Tipo o produto final,
// que vai ter a "inteligência", ele
// vai ser o dispositivo IOT de fato,
// que vai conseguir enviar os dados tratados
// conseguir ter a inteligência de tratar os dados
// recebidos pelo sensor e guardar para enviar com
// calma para o broker (IOT HUB)
type Dispositivo struct{}

type Sensor struct{}

func main() {
	fmt.Println(quote.Go())
}

func soma(x int, y int) (int, error) {
	res := x + y

	if res > 10 {
		return 0, errors.New("total maior que 10")
	}

	return res, nil
}

func callExternalApiTest() (any, error) {
	return http.Get("https://6606dbacbe53febb857ec850.mockapi.io/go/pessoa")
}
