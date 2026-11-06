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

func (s *appState) createAwsKmsKeyring(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	kmsKeyId := r.str("kmsKeyId")
	kmsClientRegion := r.str("kmsClientRegion")
	var grantTokens []string
	if r.present("grantTokens") {
		grantTokens = r.stringList("grantTokens")
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}

	kmsConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(kmsClientRegion))
	if err != nil {
		return nil, generic("load AWS config for %s: %v", kmsClientRegion, err)
	}
	keyring, err := s.client.CreateAwsKmsKeyring(ctx, mpltypes.CreateAwsKmsKeyringInput{
		KmsKeyId:    kmsKeyId,
		KmsClient:   kms.NewFromConfig(kmsConfig),
		GrantTokens: grantTokens,
	})
	if err != nil {
		return nil, mplError(err.Error())
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"keyringId": cbor.String(register(s.keyrings, keyring))}, nil
}
