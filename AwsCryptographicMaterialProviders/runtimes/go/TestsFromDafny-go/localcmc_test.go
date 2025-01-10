package main

import (
	"context"
	"testing"

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

func TestLotsOfAdding(t *testing.T) {
	client, err := awscryptographymaterialproviderssmithygenerated.NewClient(awscryptographymaterialproviderssmithygeneratedtypes.MaterialProvidersConfig{})
	if err != nil {
		t.Fatal(err)
	}
	cache := awscryptographymaterialproviderssmithygeneratedtypes.CacheTypeMemberDefault{
		Value: awscryptographymaterialproviderssmithygeneratedtypes.DefaultCache{
			EntryCapacity: 100,
		},
	}
	test, err := client.CreateCryptographicMaterialsCache(context.Background(), awscryptographymaterialproviderssmithygeneratedtypes.CreateCryptographicMaterialsCacheInput{
		Cache: &cache,
	})
	awscryptographymaterialproviderssmithygeneratedtypes.GetCacheEntryInput{
		Identifier: &identifiers[0],
	}
	test.GetCacheEntry()
	// cache := mpl.CreateCryptographicMaterialsCache(100, 16*1024*1024)
}
