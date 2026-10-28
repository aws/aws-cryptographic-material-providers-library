// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Hierarchical keyring handlers: the key store, the materials cache, and the
// keyring itself, each held in its own registry behind a UUID handle.

package main

import (
	"context"
	"math"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/kms"

	keystore "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographykeystoresmithygenerated"
	keystoretypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographykeystoresmithygeneratedtypes"
	mpltypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

func (s *appState) createKeyStoreClient(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	ddbTableName := r.str("ddbTableName")
	logicalKeyStoreName := r.str("logicalKeyStoreName")
	kmsWire := r.structure("kmsConfiguration")
	kmsConfiguration := kmsConfigurationFromWire(kmsWire)
	if kmsWire.err != nil {
		r.fail("%v", kmsWire.err)
	}
	kmsClientRegion := r.str("kmsClientRegion")
	ddbClientRegion := r.str("ddbClientRegion")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}

	kmsConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(kmsClientRegion))
	if err != nil {
		return nil, generic("load AWS config for %s: %v", kmsClientRegion, err)
	}
	ddbConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(ddbClientRegion))
	if err != nil {
		return nil, generic("load AWS config for %s: %v", ddbClientRegion, err)
	}
	keyStore, err := keystore.NewClient(keystoretypes.KeyStoreConfig{
		DdbTableName:        ddbTableName,
		LogicalKeyStoreName: logicalKeyStoreName,
		KmsConfiguration:    kmsConfiguration,
		KmsClient:           kms.NewFromConfig(kmsConfig),
		DdbClient:           dynamodb.NewFromConfig(ddbConfig),
	})
	if err != nil {
		return nil, mplError(err.Error())
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"keyStoreId": cbor.String(register(s.keyStores, keyStore))}, nil
}

// kmsConfigurationFromWire reads the model's KmsConfiguration union: exactly
// one member is set.
func kmsConfigurationFromWire(w *reqReader) keystoretypes.KMSConfiguration {
	if w.err != nil {
		return nil
	}
	if len(w.m) != 1 {
		w.fail("kmsConfiguration must set exactly one member")
		return nil
	}
	switch {
	case w.present("kmsKeyArn"):
		return &keystoretypes.KMSConfigurationMemberkmsKeyArn{Value: w.str("kmsKeyArn")}
	case w.present("kmsMRKeyArn"):
		return &keystoretypes.KMSConfigurationMemberkmsMRKeyArn{Value: w.str("kmsMRKeyArn")}
	case w.present("discovery"):
		return &keystoretypes.KMSConfigurationMemberdiscovery{Value: keystoretypes.Discovery{}}
	case w.present("mrDiscovery"):
		mrDiscovery := w.structure("mrDiscovery")
		region := mrDiscovery.str("region")
		if mrDiscovery.err != nil {
			w.fail("%v", mrDiscovery.err)
		}
		return &keystoretypes.KMSConfigurationMembermrDiscovery{
			Value: keystoretypes.MRDiscovery{Region: region},
		}
	}
	w.fail("unknown kmsConfiguration member")
	return nil
}

func (s *appState) createCryptographicMaterialsCache(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	entryCapacity := r.int64("entryCapacity")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	if entryCapacity < math.MinInt32 || entryCapacity > math.MaxInt32 {
		return nil, generic("member entryCapacity is not an Integer: %d", entryCapacity)
	}
	cache, err := s.client.CreateCryptographicMaterialsCache(ctx, mpltypes.CreateCryptographicMaterialsCacheInput{
		Cache: &mpltypes.CacheTypeMemberDefault{
			Value: mpltypes.DefaultCache{EntryCapacity: int32(entryCapacity)},
		},
	})
	if err != nil {
		return nil, mplError(err.Error())
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"cacheId": cbor.String(register(s.caches, cache))}, nil
}

func (s *appState) createAwsKmsHierarchicalKeyring(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	keyStore, serr := lookup(s, s.keyStores, m, "keyStoreId")
	if serr != nil {
		return nil, serr
	}
	r := reqReader{m: m}
	input := mpltypes.CreateAwsKmsHierarchicalKeyringInput{
		KeyStore:   keyStore,
		TtlSeconds: r.int64("ttlSeconds"),
	}
	if r.present("branchKeyId") {
		branchKeyId := r.str("branchKeyId")
		input.BranchKeyId = &branchKeyId
	}
	if r.present("branchKeyIdSupplier") {
		w := r.structure("branchKeyIdSupplier")
		input.BranchKeyIdSupplier = staticBranchKeyIdSupplier{
			encryptionContextKey: w.str("encryptionContextKey"),
			branchKeyIds:         w.stringMap("branchKeyIds"),
		}
		if w.err != nil {
			r.fail("%v", w.err)
		}
	}
	if r.present("partitionId") {
		partitionId := r.str("partitionId")
		input.PartitionId = &partitionId
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	if r.present("cacheId") {
		cache, serr := lookup(s, s.caches, m, "cacheId")
		if serr != nil {
			return nil, serr
		}
		input.Cache = &mpltypes.CacheTypeMemberShared{Value: cache}
	}
	keyring, err := s.client.CreateAwsKmsHierarchicalKeyring(ctx, input)
	if err != nil {
		return nil, mplError(err.Error())
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"keyringId": cbor.String(register(s.keyrings, keyring))}, nil
}

// staticBranchKeyIdSupplier is the model's StaticBranchKeyIdSupplier: the
// branch key id mapped to the encryption context value under
// encryptionContextKey, or a failure.
type staticBranchKeyIdSupplier struct {
	encryptionContextKey string
	branchKeyIds         map[string]string
}

func (s staticBranchKeyIdSupplier) GetBranchKeyId(input mpltypes.GetBranchKeyIdInput) (*mpltypes.GetBranchKeyIdOutput, error) {
	if value, ok := input.EncryptionContext[s.encryptionContextKey]; ok {
		if branchKeyId, ok := s.branchKeyIds[value]; ok {
			return &mpltypes.GetBranchKeyIdOutput{BranchKeyId: branchKeyId}, nil
		}
	}
	return nil, mpltypes.AwsCryptographicMaterialProvidersException{
		Message: "no branch key id for encryption context key " + s.encryptionContextKey,
	}
}
