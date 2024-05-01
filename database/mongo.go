package database

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var (
	databaseUri   string
	databaseName  string
	colletionName string
)

func init() {
	if err := godotenv.Load(); err != nil {
		log.Fatal("Erro ao carregar o arquivo .env")
	}

	databaseUri = os.Getenv("DATABASE_URI")
	databaseName = os.Getenv("DATABASE_NAME")
	colletionName = os.Getenv("DATABASE_COLLECTION")
}

// conecta ao banco de dados MongoDB e retorna o cliente MongoDB.
func NewMongoClient(ctx context.Context) (*mongo.Collection, error) {
	serverAPI := options.ServerAPI(options.ServerAPIVersion1)
	opts := options.Client().ApplyURI(databaseUri).SetServerAPIOptions(serverAPI)

	client, err := mongo.Connect(ctx, opts)
	if err != nil {
		return nil, fmt.Errorf("falha ao conectar ao banco de dados MongoDB: %w", err)
	}

	err = pingDatabase(client)
	if err != nil {
		return nil, fmt.Errorf("falha ao verificar a conexão com o banco de dados MongoDB: %w", err)
	}

	log.Println("Conexão bem-sucedida com o banco de dados MongoDB")

	connect(client)

	return client.Database(databaseName).Collection(colletionName), nil
}

func connect(client *mongo.Client) error {
	return client.Connect(context.Background())
}

// faz o ping caso funcione certinho a conexão
func pingDatabase(client *mongo.Client) error {
	var result struct{}
	err := client.Database("admin").RunCommand(context.Background(), bson.D{{"ping", 1}}).Decode(&result)
	if err != nil {
		return fmt.Errorf("falha ao executar ping no banco de dados MongoDB: %w", err)
	}
	return nil
}
