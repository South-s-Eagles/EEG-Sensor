package aws

import (
	"bytes"
	"context"
	"fmt"
	"log"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

const bucketName = "raw-souths-eagle-ivan"

type S3ClientWrapper struct {
	Client *s3.Client
}

func Client() *S3ClientWrapper {
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		log.Fatal(err)
	}

	cfg.Region = "us-east-1"

	client := s3.NewFromConfig(cfg)

	return &S3ClientWrapper{
		Client: client,
	}
}

func (w *S3ClientWrapper) ListObjects() {
	output, err := w.Client.ListObjectsV2(context.TODO(), &s3.ListObjectsV2Input{
		Bucket: aws.String("raw-souths-eagle-ivan"),
	})
	if err != nil {
		log.Fatal(err)
	}

	log.Println("first page results:")
	for _, object := range output.Contents {
		log.Printf("key=%s size=%d", aws.ToString(object.Key), object.Size)
	}
}

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

	fmt.Printf("Objeto %s enviado com sucesso para o S3", string(data))

	return nil
}
