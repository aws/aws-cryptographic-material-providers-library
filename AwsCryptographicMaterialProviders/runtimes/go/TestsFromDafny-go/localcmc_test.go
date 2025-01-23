package main

import (
	"context"
	"crypto/rand"
	"fmt"
	"math/big"
	"sync"
	"testing"
	"time"

	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographykeystoresmithygeneratedtypes"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/test/awscryptographymaterialproviderssmithygenerated"
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
	client, err := awscryptographymaterialproviderssmithygenerated.NewClient(awscryptographymaterialproviderssmithygeneratedtypes.MaterialProvidersConfig{})
	if err != nil {
		panic(err)
	}
	cacheType := awscryptographymaterialproviderssmithygeneratedtypes.CacheTypeMemberDefault{
		Value: awscryptographymaterialproviderssmithygeneratedtypes.DefaultCache{
			EntryCapacity: 10,
		},
	}
	cache, err := client.CreateCryptographicMaterialsCache(context.Background(), awscryptographymaterialproviderssmithygeneratedtypes.CreateCryptographicMaterialsCacheInput{
		Cache: &cacheType,
	})
	if err != nil {
		panic(err)
	}

	for range numWorkers {
		wg.Add(1)
		go func() {
			processWorker(ops, &wg, errChannel, cache)
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

func processWorker(ops <-chan int, wg *sync.WaitGroup, errChannel chan<- error, cache awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsCache) {
	defer wg.Done()
	for range ops {
		err := testLotsOfAdding(cache)
		if err != nil {
			errChannel <- err
		}
	}
}

func testLotsOfAdding(cache awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsCache) error {
	randIndex, err := rand.Int(rand.Reader, big.NewInt(int64(idSize)))
	beaconKeyIdentifier := identifiers[randIndex.Int64()]
	getCacheEntryInput := awscryptographymaterialproviderssmithygeneratedtypes.GetCacheEntryInput{
		Identifier: []byte(beaconKeyIdentifier),
	}
	op, err := cache.GetCacheEntry(getCacheEntryInput)
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
				ExpiryTime:   time.Now().Unix() + 100,
				Materials:    &materials,
			}
			err := cache.PutCacheEntry(putCacheEntryInput)
			if err != nil {
				return (err)
			}
		default:
			return err
		}
	} else {
		if op.Materials.(*awscryptographymaterialproviderssmithygeneratedtypes.MaterialsMemberBeaconKey).Value.BeaconKeyIdentifier != beaconKeyIdentifier {
			return fmt.Errorf("beacon key identifier mismatch: %s != %s", op.Materials.(*awscryptographymaterialproviderssmithygeneratedtypes.MaterialsMemberBeaconKey).Value.BeaconKeyIdentifier, beaconKeyIdentifier)
		}
		fmt.Printf("Cache hit with beacon key identifier %s \n", beaconKeyIdentifier)
	}
	return nil
}
