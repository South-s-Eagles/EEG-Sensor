// Responsável pela conexão com azure IOTHUB.
// Tem a inteligência de conseguir se conectar com
// a Azure e enviar mensagem para o broker.
package broker

import (
	"context"
	"errors"
	"fmt"
	"sync"

	"github.com/amenzhinsky/iothub/iotdevice"
	iotmqtt "github.com/amenzhinsky/iothub/iotdevice/transport/mqtt"
)

// AzureBroker representa o cliente do broker do Azure IoT Hub.
type AzureBroker struct {
	client *iotdevice.Client
	once   sync.Once
}

// NewAzureBroker cria uma nova instância de AzureBroker.
func NewAzureBroker(connectionString string) (*AzureBroker, error) {
	broker := &AzureBroker{}
	var initErr error

	broker.once.Do(func() {
		client, err := iotdevice.NewFromConnectionString(iotmqtt.New(), connectionString)
		if err != nil {
			initErr = fmt.Errorf("falha ao criar o cliente de conexão com Azure IOTHUB: %w", err)
			return
		}

		if err := client.Connect(context.Background()); err != nil {
			initErr = fmt.Errorf("falha ao estabelecer a conexão com Azure IOTHUB: %w", err)
			return
		}

		broker.client = client
	})

	if initErr != nil {
		return nil, initErr
	}

	return broker, nil
}

// Envia uma mensagem para o IoT Hub.
func (b *AzureBroker) SendMessage(message []byte) error {
	if b.client == nil {
		return errors.New("conexão com o broker não inicializada")
	}

	return b.client.SendEvent(context.Background(), message)
}
