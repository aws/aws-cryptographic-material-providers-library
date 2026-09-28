// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Decoding of the rpcv2Cbor request wire form into AtomicPrimitives inputs:
// structure members are keyed by the Smithy member name, blobs travel as CBOR
// byte strings, integers as CBOR integers, and enums as the Smithy enum value
// strings mapped to library constants through the tables below.

package main

import (
	"fmt"

	prims "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/awscryptographyprimitivessmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

// Enum tables: wire enum value -> library constant.

var digestAlgorithms = map[string]prims.DigestAlgorithm{
	"SHA_256": prims.DigestAlgorithmSha256,
	"SHA_384": prims.DigestAlgorithmSha384,
	"SHA_512": prims.DigestAlgorithmSha512,
}

var ecdsaAlgorithms = map[string]prims.ECDSASignatureAlgorithm{
	"ECDSA_P256": prims.ECDSASignatureAlgorithmEcdsaP256,
	"ECDSA_P384": prims.ECDSASignatureAlgorithmEcdsaP384,
}

// aesAlgorithms maps each wire algorithm to its AES-GCM parameters in bytes: a
// 12-byte IV, a 16-byte tag, and the key length the algorithm name encodes.
var aesAlgorithms = map[string]prims.AES_GCM{
	"AES_128_GCM": {IvLength: 12, KeyLength: 16, TagLength: 16},
	"AES_192_GCM": {IvLength: 12, KeyLength: 24, TagLength: 16},
	"AES_256_GCM": {IvLength: 12, KeyLength: 32, TagLength: 16},
}

func decodeBody(payload []byte) (cbor.Map, error) {
	v, err := cbor.Decode(payload)
	if err != nil {
		return nil, err
	}
	m, ok := v.(cbor.Map)
	if !ok {
		return nil, fmt.Errorf("expected a CBOR map, got %T", v)
	}
	return m, nil
}

// member returns the value for key, treating CBOR null/undefined as absent.
func member(m cbor.Map, key string) (cbor.Value, bool) {
	v, ok := m[key]
	if !ok {
		return nil, false
	}
	switch v.(type) {
	case *cbor.Nil, *cbor.Undefined:
		return nil, false
	}
	return v, true
}

func requireBytes(m cbor.Map, key string) ([]byte, error) {
	v, ok := member(m, key)
	if !ok {
		return nil, fmt.Errorf("missing required member %s", key)
	}
	b, ok := v.(cbor.Slice)
	if !ok {
		return nil, fmt.Errorf("member %s: expected a byte string, got %T", key, v)
	}
	return []byte(b), nil
}

func requireInt32(m cbor.Map, key string) (int32, error) {
	v, ok := member(m, key)
	if !ok {
		return 0, fmt.Errorf("missing required member %s", key)
	}
	n, err := cbor.AsInt32(v)
	if err != nil {
		return 0, fmt.Errorf("member %s: %v", key, err)
	}
	return n, nil
}

func requireEnum[T any](m cbor.Map, key string, values map[string]T) (T, error) {
	var zero T
	v, ok := member(m, key)
	if !ok {
		return zero, fmt.Errorf("missing required member %s", key)
	}
	s, ok := v.(cbor.String)
	if !ok {
		return zero, fmt.Errorf("member %s: expected a text string, got %T", key, v)
	}
	mapped, ok := values[string(s)]
	if !ok {
		return zero, fmt.Errorf("member %s: unknown enum value %q", key, string(s))
	}
	return mapped, nil
}

// reqReader pulls required members from one request map, holding the first
// extraction error so a handler reads every field then checks err once.
type reqReader struct {
	m   cbor.Map
	err error
}

func (r *reqReader) bytes(key string) []byte {
	if r.err != nil {
		return nil
	}
	b, err := requireBytes(r.m, key)
	r.err = err
	return b
}

func (r *reqReader) int32(key string) int32 {
	if r.err != nil {
		return 0
	}
	n, err := requireInt32(r.m, key)
	r.err = err
	return n
}

func (r *reqReader) digestAlg(key string) prims.DigestAlgorithm {
	if r.err != nil {
		return ""
	}
	v, err := requireEnum(r.m, key, digestAlgorithms)
	r.err = err
	return v
}

func (r *reqReader) ecdsaAlg(key string) prims.ECDSASignatureAlgorithm {
	if r.err != nil {
		return ""
	}
	v, err := requireEnum(r.m, key, ecdsaAlgorithms)
	r.err = err
	return v
}

func (r *reqReader) aesAlg(key string) prims.AES_GCM {
	if r.err != nil {
		return prims.AES_GCM{}
	}
	v, err := requireEnum(r.m, key, aesAlgorithms)
	r.err = err
	return v
}
