package broker

import (
	"fmt"

	"github.com/Azure/azure-sdk-for-go/sdk/azidentity"
	"github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/iothub/armiothub"
)

func main() {
	cred, err := azidentity.NewDefaultAzureCredential(nil)
	if err != nil {
		fmt.Println("deu ruim")
	}
	clientFactory, err := armiothub.NewClientFactory("fiowenf", cred, nil)
	if err != nil {
		fmt.Println("deu ruim")
	}

	fmt.Println(clientFactory)
}
