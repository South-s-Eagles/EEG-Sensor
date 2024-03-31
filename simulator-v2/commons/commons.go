// Funções comuns a todos o projeto que podem
// ser usadas fora do contexto de algum struct em si
package commons

import (
	"math"
)

const (
	amostraDaFrequencia       = 10 // Frequência de amostragem em Hz
	arredondamentoDaAmplitude = 10 // O quando vai arredondar a amplitude
)

// Função para calcular a Transformada de Fourier e encontrar a frequência dominante
func FrequenciaDominante(microvolts []int8) (freqDominante float64, maxAmplitude float64) {
	N := len(microvolts)

	// Aplicando a Transformada de Fourier
	var real, imag []float64
	for k := 0; k < N; k++ {
		var sumReal, sumImag float64
		for n := 0; n < N; n++ {
			angle := 2 * math.Pi * float64(k) * float64(n) / float64(N)
			sumReal += float64(microvolts[n]) * math.Cos(angle)
			sumImag -= float64(microvolts[n]) * math.Sin(angle)
		}
		real = append(real, sumReal)
		imag = append(imag, sumImag)
	}

	// Encontrando a amplitude e a frequência dominante
	for k := 0; k < N/2; k++ {
		amplitude := math.Sqrt(real[k]*real[k] + imag[k]*imag[k])
		if amplitude > maxAmplitude {
			maxAmplitude = amplitude
		}
		freqDominante = float64(k) * (amostraDaFrequencia / float64(N))
	}

	return freqDominante, maxAmplitude / arredondamentoDaAmplitude
}

func CalcularMedia(arr []int8) (media float32) {
	var soma int
	for _, v := range arr {
		soma += int(v)
	}
	media = float32(soma) / float32(len(arr))
	return media
}
