// Funções comuns a todos o projeto que podem
// ser usadas fora do contexto de algum struct em si
package commons

const (
	samplingFrequency = 1000 // Frequência de amostragem em Hz
)

// Função para calcular a frequência em Hertz com base nos valores fornecidos em microvolts
func ParaFrequenciaEmHeartz(values []int8) float64 {
	numSamples := len(values)
	frequency := float64(numSamples) / float64(samplingFrequency)
	return frequency
}
