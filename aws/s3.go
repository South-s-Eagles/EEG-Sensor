package aws

import (
	"bytes"
	"context"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/joho/godotenv"
)

var (
	bucketName string
	region     string
)

func init() {
	if err := godotenv.Load(); err != nil {
		log.Fatal("Erro ao carregar o arquivo .env")
	}

	bucketName = os.Getenv("AWS_BUCKET_NAME")
	region = os.Getenv("AWS_REGION")
}

// Wrapper para abstrair o client s3
type S3ClientWrapper struct {
	Client *s3.Client
}

// Construtor para criar o client do s3
func NewS3ClientWrapper(client *s3.Client) *S3ClientWrapper {
	return &S3ClientWrapper{
		Client: client,
	}
}

// Função para enviar um array de byte para o s3, com o nome do arquivo sendo a data atual.json
func (w *S3ClientWrapper) SendObject(ctx context.Context, id string, data []byte) error {
	bk := bucketName
	key := fmt.Sprintf("%s/%s.json", id, time.Now().Format("2006-01-02T15-04-05"))
	_, err := w.Client.PutObject(ctx, &s3.PutObjectInput{
		Bucket: &bk,
		Key:    &key,
		Body:   bytes.NewReader(data),
	})
	if err != nil {
		return fmt.Errorf("falha ao enviar objeto para o bucket S3: %v", err)
	}

	return nil
}
