// Responsável pela conexão com azure IOTHUB.
// Tem a inteligência de conseguir se conectar com
// a Azure e enviar mensagem para o broker.
package broker

import (
	"context"
	"errors"
	"log"
	"sync"

	"github.com/amenzhinsky/iothub/iotdevice"
	iotmqtt "github.com/amenzhinsky/iothub/iotdevice/transport/mqtt"
)

// AzureBroker representa o cliente do broker do Azure IoT Hub.
type AzureBroker struct {
	client *iotdevice.Client
	once   sync.Once
}

// Cria uma nova instância de AzureBroker.
func NewAzureBroker(connectionString string) (*AzureBroker, error) {
	broker := &AzureBroker{}
	var err error
	broker.once.Do(func() {
		broker.client, err = iotdevice.NewFromConnectionString(iotmqtt.New(), connectionString)
		if err != nil {
			log.Fatal(err)
		}

		if err = broker.client.Connect(context.Background()); err != nil {
			log.Fatal(err)
		}
	})
	return broker, err
}

// Envia uma mensagem para o IoT Hub.
func (b *AzureBroker) SendMessage(message []byte) error {
	if b.client == nil {
		return errors.New("conexão com o broker não inicializada")
	}

	return b.client.SendEvent(context.Background(), message)
}
