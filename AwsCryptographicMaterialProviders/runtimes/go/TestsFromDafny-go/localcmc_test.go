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
	// Similar to threadPoolSize = 10
	const numWorkers = 1
	// Similar to invocationCount = 300000
	const totalOperations = 1
	// Similar to timeOut = 10000
	timeout := time.After(1000 * time.Second)
	// Create a WaitGroup to track all operations
	var wg sync.WaitGroup
	// Create buffered channel to control concurrent operations
	ops := make(chan struct{}, totalOperations)
	// Fill the ops channel with work items
	for i := 0; i < totalOperations; i++ {
		ops <- struct{}{}
	}
	close(ops)
	// Launch worker goroutines
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go TestLotsOfAdding(t)
	}
	// Wait for either completion or timeout
	done := make(chan struct{})
	go func() {
		wg.Wait()
		close(done)
	}()
	select {
	case <-timeout:
		t.Fatal("Test timed out")
	case <-done:
		// Test completed successfully
	}
}

func TestLotsOfAdding(t *testing.T) {
	client, err := awscryptographymaterialproviderssmithygenerated.NewClient(awscryptographymaterialproviderssmithygeneratedtypes.MaterialProvidersConfig{})
	if err != nil {
		t.Fatal(err)
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
		t.Fatal(err)
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
			t.Fatal(err)
		}
	}
}
