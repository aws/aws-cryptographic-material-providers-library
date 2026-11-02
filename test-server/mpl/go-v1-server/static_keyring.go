// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// The static keyring handler: a keyring this server implements itself, as a
// customer's keyring would, that returns fixed materials.

package main

import (
	"context"

	mpltypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

func (s *appState) createStaticKeyring(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	var keyring staticKeyring
	if r.present("encryptionMaterials") {
		materials := s.encryptionMaterialsFromWire(r.structure("encryptionMaterials"), &r)
		keyring.encryptionMaterials = &materials
	}
	if r.present("decryptionMaterials") {
		materials := s.decryptionMaterialsFromWire(r.structure("decryptionMaterials"), &r)
		keyring.decryptionMaterials = &materials
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"keyringId": cbor.String(register[mpltypes.IKeyring](s.keyrings, keyring))}, nil
}

// staticKeyring is the model's static keyring: OnEncrypt and OnDecrypt return
// the fixed materials, or the input materials when none were given.
type staticKeyring struct {
	encryptionMaterials *mpltypes.EncryptionMaterials
	decryptionMaterials *mpltypes.DecryptionMaterials
}

func (k staticKeyring) OnEncrypt(input mpltypes.OnEncryptInput) (*mpltypes.OnEncryptOutput, error) {
	materials := input.Materials
	if k.encryptionMaterials != nil {
		materials = *k.encryptionMaterials
	}
	return &mpltypes.OnEncryptOutput{Materials: materials}, nil
}

func (k staticKeyring) OnDecrypt(input mpltypes.OnDecryptInput) (*mpltypes.OnDecryptOutput, error) {
	materials := input.Materials
	if k.decryptionMaterials != nil {
		materials = *k.decryptionMaterials
	}
	return &mpltypes.OnDecryptOutput{Materials: materials}, nil
}
