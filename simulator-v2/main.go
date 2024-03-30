package main

import (
	"encoding/json"
	"fmt"
)

type Pessoa struct {
	Nome  string `json:"nome"`
	Idade int    `json:"idade"`
	dade  int    `json:"idade"`
	dde   int    `json:"idade"`
	de    int    `json:"idade"`
}

func main() {
	pessoa := Pessoa{
		Nome:  "João",
		Idade: 30,
		dade:  30,
		dde:   30,
		de:    30,
	}

	jsonData, err := json.Marshal(pessoa)
	if err != nil {
		fmt.Println("Erro ao converter para JSON:", err)
		return
	}

	fmt.Printf("Tamanho do test Test (teste): %d bytes\n", len(jsonData))
	fmt.Println(string(jsonData))
}
