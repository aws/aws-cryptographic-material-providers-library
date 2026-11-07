// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

package main

import (
	"context"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/kms"

	mpltypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

// createAwsKmsKeyring passes an absent kmsKeyId to the MPL as the empty
// string, since the Go input's KmsKeyId is not a pointer, and an absent
// kmsClient as a nil client.
func (s *appState) createAwsKmsKeyring(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	var kmsKeyId string
	if r.present("kmsKeyId") {
		kmsKeyId = r.str("kmsKeyId")
	}
	var kmsClient *reqReader
	if r.present("kmsClient") {
		kmsClient = r.structure("kmsClient")
	}
	var grantTokens []string
	if r.present("grantTokens") {
		grantTokens = r.stringList("grantTokens")
	}
	var region string
	var endpoint *string
	if kmsClient != nil {
		region = kmsClient.str("region")
		if kmsClient.present("endpoint") {
			value := kmsClient.str("endpoint")
			endpoint = &value
		}
		if kmsClient.err != nil {
			r.fail("%v", kmsClient.err)
		}
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}

	input := mpltypes.CreateAwsKmsKeyringInput{
		KmsKeyId:    kmsKeyId,
		GrantTokens: grantTokens,
	}
	if kmsClient != nil {
		kmsConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(region))
		if err != nil {
			return nil, generic("load AWS config for %s: %v", region, err)
		}
		input.KmsClient = kms.NewFromConfig(kmsConfig, func(o *kms.Options) {
			o.BaseEndpoint = endpoint
		})
	}
	keyring, err := s.client.CreateAwsKmsKeyring(ctx, input)
	if err != nil {
		return nil, mplFailure(err)
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"keyringId": cbor.String(register(s.keyrings, keyring))}, nil
}
