package broker

import (
	"context"
	"log"

	"github.com/amenzhinsky/iothub/iotdevice"
	iotmqtt "github.com/amenzhinsky/iothub/iotdevice/transport/mqtt"
)

//	func main() {
//		ctx := context.Background()
//
//		// Configurar credenciais para Azure
//		cred, err := azidentity.NewDefaultAzureCredential(nil)
//		if err != nil {
//			panic(err)
//		}
//
//		clientFactory, err := armiothub.NewClientFactory("HostName=ivan02221071.azure-devices.net;DeviceId=ivan02221071;SharedAccessKey=WgwvQTOkaRNUdYoD8cS2HnDZcQXkgyBDTAIoTAVFArg=", cred, nil)
//		if err != nil {
//			panic(err)
//		}
//
//		client := clientFactory.GetIoTHubClient()
//
//		fmt.Println(client)
//	}
func main() {
	c, err := iotdevice.NewFromConnectionString(
		iotmqtt.New(), "HostName=ivan02221071.azure-devices.net;DeviceId=ivan02221071;SharedAccessKey=WgwvQTOkaRNUdYoD8cS2HnDZcQXkgyBDTAIoTAVFArg=",
	)
	if err != nil {
		log.Fatal(err)
	}

	// connect to the iothub
	if err = c.Connect(context.Background()); err != nil {
		log.Fatal(err)
	}

	// send a device-to-cloud message
	if err = c.SendEvent(context.Background(), []byte(`hello`)); err != nil {
		log.Fatal(err)
	}
}
