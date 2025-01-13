package main

import (
	"context"
	"crypto/rand"
	"math/big"
	"sync"
	"testing"
	"time"

	"github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographykeystoresmithygeneratedtypes"
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographymaterialproviderssmithygenerated"
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
)

// Test setup
var (
	identifiers = []string{
		"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
		"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
		"eighteen", "nineteen", "twenty", "twenty one",
	}
	idSize = len(identifiers)
)

func TestConcurrentCacheOperations(t *testing.T) {
	const numWorkers = 10
	totalOperations := 300000
	timeout := time.After(10 * time.Second)
	go func() {
		<-timeout
		panic("operation timed out")
	}()
	// Create a WaitGroup to track all operations
	var wg sync.WaitGroup
	// Create buffered channel to control concurrent operations
	ops := make(chan int, totalOperations)
	errChannel := make(chan error, numWorkers)
	for range numWorkers {
		wg.Add(1)
		go func() {
			processWorker(ops, &wg, errChannel)
		}()
	}
	// Fill the ops channel with work items
	for i := range totalOperations {
		ops <- i
	}
	close(ops)
	// Wait for completion in a separate goroutine
	go func() {
		wg.Wait()
		close(errChannel)
	}()
	// Check for errors in the main test goroutine
	for err := range errChannel {
		if err != nil {
			t.Fatal(err)
		}
	}
}

func processWorker(ops <-chan int, wg *sync.WaitGroup, errChannel chan<- error) {
	defer wg.Done()
	for range ops {
		err := testLotsOfAdding()
		if err != nil {
			errChannel <- err
		}
	}
}

func testLotsOfAdding() error {
	client, err := awscryptographymaterialproviderssmithygenerated.NewClient(awscryptographymaterialproviderssmithygeneratedtypes.MaterialProvidersConfig{})
	if err != nil {
		return err
	}
	cache := awscryptographymaterialproviderssmithygeneratedtypes.CacheTypeMemberDefault{
		Value: awscryptographymaterialproviderssmithygeneratedtypes.DefaultCache{
			EntryCapacity: 10,
		},
	}
	test, err := client.CreateCryptographicMaterialsCache(context.Background(), awscryptographymaterialproviderssmithygeneratedtypes.CreateCryptographicMaterialsCacheInput{
		Cache: &cache,
	})
	if err != nil {
		return err
	}
	randIndex, err := rand.Int(rand.Reader, big.NewInt(int64(idSize)))
	beaconKeyIdentifier := identifiers[randIndex.Int64()]
	getCacheEntryInput := awscryptographymaterialproviderssmithygeneratedtypes.GetCacheEntryInput{
		Identifier: []byte(beaconKeyIdentifier),
	}
	_, err = test.GetCacheEntry(getCacheEntryInput)
	if err != nil {
		switch err.(type) {
		case awscryptographymaterialproviderssmithygeneratedtypes.EntryDoesNotExist:
			materials := awscryptographymaterialproviderssmithygeneratedtypes.MaterialsMemberBeaconKey{
				Value: awscryptographykeystoresmithygeneratedtypes.BeaconKeyMaterials{
					BeaconKeyIdentifier: beaconKeyIdentifier,
					BeaconKey:           []byte(beaconKeyIdentifier),
					EncryptionContext:   map[string]string{},
				},
			}

			putCacheEntryInput := awscryptographymaterialproviderssmithygeneratedtypes.PutCacheEntryInput{
				Identifier:   []byte(beaconKeyIdentifier),
				CreationTime: time.Now().Unix(),
				ExpiryTime:   time.Now().Unix() + 1,
				Materials:    &materials,
			}
			test.PutCacheEntry(putCacheEntryInput)
		default:
			return err
		}
	}
	return nil
}
