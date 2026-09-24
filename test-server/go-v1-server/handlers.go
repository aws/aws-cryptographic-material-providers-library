// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Operation handlers: decode the request map, call the AtomicPrimitives client,
// and build the rpcv2Cbor response map. A client error becomes a
// PrimitivesError; a malformed request becomes a GenericServerError.

package main

import (
	"context"

	prim "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/awscryptographyprimitivessmithygenerated"
	prims "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/awscryptographyprimitivessmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

// appState holds the one AtomicPrimitives client shared across requests; the
// atomic primitive operations are stateless.
type appState struct {
	client *prim.Client
}

func newAppState() (*appState, error) {
	client, err := prim.NewClient(prims.CryptoConfig{})
	if err != nil {
		return nil, err
	}
	return &appState{client: client}, nil
}

func (s *appState) aesEncrypt(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.aesAlg("algorithm")
	iv := r.bytes("iv")
	key := r.bytes("key")
	message := r.bytes("message")
	aad := r.bytes("aad")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	out, err := s.client.AESEncrypt(ctx, prims.AESEncryptInput{
		EncAlg: alg, Iv: iv, Key: key, Msg: message, Aad: aad,
	})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{
		"ciphertext": cbor.Slice(out.CipherText),
		"authTag":    cbor.Slice(out.AuthTag),
	}, nil
}

func (s *appState) aesDecrypt(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.aesAlg("algorithm")
	key := r.bytes("key")
	ciphertext := r.bytes("ciphertext")
	authTag := r.bytes("authTag")
	iv := r.bytes("iv")
	aad := r.bytes("aad")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	plaintext, err := s.client.AESDecrypt(ctx, prims.AESDecryptInput{
		EncAlg: alg, Key: key, CipherTxt: ciphertext, AuthTag: authTag, Iv: iv, Aad: aad,
	})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{"plaintext": cbor.Slice(plaintext)}, nil
}

func (s *appState) generateRandomBytes(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	length := r.int32("length")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	data, err := s.client.GenerateRandomBytes(ctx, prims.GenerateRandomBytesInput{Length: length})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{"data": cbor.Slice(data)}, nil
}

func (s *appState) digest(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.digestAlg("algorithm")
	data := r.bytes("data")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	out, err := s.client.Digest(ctx, prims.DigestInput{DigestAlgorithm: alg, Message: data})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{"digest": cbor.Slice(out)}, nil
}

func (s *appState) hmac(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.digestAlg("algorithm")
	key := r.bytes("key")
	message := r.bytes("message")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	out, err := s.client.HMac(ctx, prims.HMacInput{DigestAlgorithm: alg, Key: key, Message: message})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{"digest": cbor.Slice(out)}, nil
}

func (s *appState) hkdf(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.digestAlg("algorithm")
	salt := r.bytes("salt")
	ikm := r.bytes("ikm")
	info := r.bytes("info")
	expectedLength := r.int32("expectedLength")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	out, err := s.client.Hkdf(ctx, prims.HkdfInput{
		DigestAlgorithm: alg, Salt: salt, Ikm: ikm, Info: info, ExpectedLength: expectedLength,
	})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{"okm": cbor.Slice(out)}, nil
}

func (s *appState) ecdsaGenerateKeyPair(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.ecdsaAlg("algorithm")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	out, err := s.client.GenerateECDSASignatureKey(ctx, prims.GenerateECDSASignatureKeyInput{
		SignatureAlgorithm: alg,
	})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{
		"verificationKey": cbor.Slice(out.VerificationKey),
		"signingKey":      cbor.Slice(out.SigningKey),
	}, nil
}

func (s *appState) ecdsaSign(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.ecdsaAlg("algorithm")
	signingKey := r.bytes("signingKey")
	message := r.bytes("message")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	signature, err := s.client.ECDSASign(ctx, prims.ECDSASignInput{
		SignatureAlgorithm: alg, SigningKey: signingKey, Message: message,
	})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{"signature": cbor.Slice(signature)}, nil
}

func (s *appState) ecdsaVerify(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	alg := r.ecdsaAlg("algorithm")
	verificationKey := r.bytes("verificationKey")
	message := r.bytes("message")
	signature := r.bytes("signature")
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	valid, err := s.client.ECDSAVerify(ctx, prims.ECDSAVerifyInput{
		SignatureAlgorithm: alg, VerificationKey: verificationKey, Message: message, Signature: signature,
	})
	if err != nil {
		return nil, primitivesError(err.Error())
	}
	return cbor.Map{"valid": cbor.Bool(valid)}, nil
}
