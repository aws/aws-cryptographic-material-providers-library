// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Decoding of the rpcv2Cbor request wire form: structure members are keyed by
// the Smithy member name, blobs travel as CBOR byte strings, enums as the
// Smithy enum name strings. A missing or mistyped required member is the
// harness's fault, so every accessor reports it as a GenericServerError.

package main

import (
	"fmt"

	mpltypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

// esdkSuites maps each wire suite name (the MPL constant name) to the MPL's
// ESDK suite id, whose value is the suite's two-byte message-format id.
var esdkSuites = map[string]mpltypes.ESDKAlgorithmSuiteId{
	"ALG_AES_128_GCM_IV12_TAG16_NO_KDF":                 mpltypes.ESDKAlgorithmSuiteIdAlgAes128GcmIv12Tag16NoKdf,
	"ALG_AES_192_GCM_IV12_TAG16_NO_KDF":                 mpltypes.ESDKAlgorithmSuiteIdAlgAes192GcmIv12Tag16NoKdf,
	"ALG_AES_256_GCM_IV12_TAG16_NO_KDF":                 mpltypes.ESDKAlgorithmSuiteIdAlgAes256GcmIv12Tag16NoKdf,
	"ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256":            mpltypes.ESDKAlgorithmSuiteIdAlgAes128GcmIv12Tag16HkdfSha256,
	"ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256":            mpltypes.ESDKAlgorithmSuiteIdAlgAes192GcmIv12Tag16HkdfSha256,
	"ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256":            mpltypes.ESDKAlgorithmSuiteIdAlgAes256GcmIv12Tag16HkdfSha256,
	"ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256": mpltypes.ESDKAlgorithmSuiteIdAlgAes128GcmIv12Tag16HkdfSha256EcdsaP256,
	"ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384": mpltypes.ESDKAlgorithmSuiteIdAlgAes192GcmIv12Tag16HkdfSha384EcdsaP384,
	"ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384": mpltypes.ESDKAlgorithmSuiteIdAlgAes256GcmIv12Tag16HkdfSha384EcdsaP384,
	"ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY":            mpltypes.ESDKAlgorithmSuiteIdAlgAes256GcmHkdfSha512CommitKey,
	"ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384": mpltypes.ESDKAlgorithmSuiteIdAlgAes256GcmHkdfSha512CommitKeyEcdsaP384,
}

var commitmentPolicies = map[string]mpltypes.ESDKCommitmentPolicy{
	"ESDK_FORBID_ENCRYPT_ALLOW_DECRYPT":    mpltypes.ESDKCommitmentPolicyForbidEncryptAllowDecrypt,
	"ESDK_REQUIRE_ENCRYPT_ALLOW_DECRYPT":   mpltypes.ESDKCommitmentPolicyRequireEncryptAllowDecrypt,
	"ESDK_REQUIRE_ENCRYPT_REQUIRE_DECRYPT": mpltypes.ESDKCommitmentPolicyRequireEncryptRequireDecrypt,
}

var aesWrappingAlgs = map[string]mpltypes.AesWrappingAlg{
	"ALG_AES128_GCM_IV12_TAG16": mpltypes.AesWrappingAlgAlgAes128GcmIv12Tag16,
	"ALG_AES192_GCM_IV12_TAG16": mpltypes.AesWrappingAlgAlgAes192GcmIv12Tag16,
	"ALG_AES256_GCM_IV12_TAG16": mpltypes.AesWrappingAlgAlgAes256GcmIv12Tag16,
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

// reqReader pulls members from one request map, holding the first extraction
// error so a handler reads every field then checks err once.
type reqReader struct {
	m   cbor.Map
	err error
}

func (r *reqReader) fail(format string, args ...any) {
	if r.err == nil {
		r.err = fmt.Errorf(format, args...)
	}
}

func (r *reqReader) present(key string) bool {
	_, ok := member(r.m, key)
	return ok
}

func (r *reqReader) required(key string) cbor.Value {
	if r.err != nil {
		return nil
	}
	v, ok := member(r.m, key)
	if !ok {
		r.fail("missing required member %s", key)
		return nil
	}
	return v
}

func (r *reqReader) bytes(key string) []byte {
	v := r.required(key)
	if v == nil {
		return nil
	}
	b, ok := v.(cbor.Slice)
	if !ok {
		r.fail("member %s: expected a byte string, got %T", key, v)
		return nil
	}
	return []byte(b)
}

func (r *reqReader) optionalBytes(key string) []byte {
	if !r.present(key) {
		return nil
	}
	return r.bytes(key)
}

func (r *reqReader) str(key string) string {
	v := r.required(key)
	if v == nil {
		return ""
	}
	s, ok := v.(cbor.String)
	if !ok {
		r.fail("member %s: expected a text string, got %T", key, v)
		return ""
	}
	return string(s)
}

func (r *reqReader) int64(key string) int64 {
	v := r.required(key)
	if v == nil {
		return 0
	}
	n, err := cbor.AsInt64(v)
	if err != nil {
		r.fail("member %s: %v", key, err)
	}
	return n
}

func (r *reqReader) structure(key string) *reqReader {
	v := r.required(key)
	m, ok := v.(cbor.Map)
	if v != nil && !ok {
		r.fail("member %s: expected a structure, got %T", key, v)
	}
	return &reqReader{m: m, err: r.err}
}

func (r *reqReader) list(key string) cbor.List {
	v := r.required(key)
	if v == nil {
		return nil
	}
	l, ok := v.(cbor.List)
	if !ok {
		r.fail("member %s: expected a list, got %T", key, v)
		return nil
	}
	return l
}

// stringMap reads a string-to-string map member; absent means empty.
func (r *reqReader) stringMap(key string) map[string]string {
	out := map[string]string{}
	if !r.present(key) {
		return out
	}
	v := r.required(key)
	m, ok := v.(cbor.Map)
	if !ok {
		r.fail("member %s: expected a map, got %T", key, v)
		return out
	}
	for k, entry := range m {
		s, ok := entry.(cbor.String)
		if !ok {
			r.fail("member %s.%s: expected a text string, got %T", key, k, entry)
			continue
		}
		out[k] = string(s)
	}
	return out
}

// stringList reads a list-of-strings member; absent means empty.
func (r *reqReader) stringList(key string) []string {
	out := []string{}
	if !r.present(key) {
		return out
	}
	for _, entry := range r.list(key) {
		s, ok := entry.(cbor.String)
		if !ok {
			r.fail("member %s: expected text strings, got %T", key, entry)
			continue
		}
		out = append(out, string(s))
	}
	return out
}

// optionalBytesList reads a list-of-blobs member, or nil when absent.
func (r *reqReader) optionalBytesList(key string) [][]byte {
	if !r.present(key) {
		return nil
	}
	out := [][]byte{}
	for _, entry := range r.list(key) {
		b, ok := entry.(cbor.Slice)
		if !ok {
			r.fail("member %s: expected byte strings, got %T", key, entry)
			continue
		}
		out = append(out, []byte(b))
	}
	return out
}

func lookupEnum[T any](r *reqReader, key string, values map[string]T) T {
	var zero T
	name := r.str(key)
	if r.err != nil {
		return zero
	}
	mapped, ok := values[name]
	if !ok {
		r.fail("member %s: unknown enum value %q", key, name)
		return zero
	}
	return mapped
}

func (r *reqReader) suiteName(key string) string {
	name := r.str(key)
	if r.err == nil {
		if _, ok := esdkSuites[name]; !ok {
			r.fail("member %s: unknown algorithm suite %q", key, name)
		}
	}
	return name
}

func (r *reqReader) suiteID(key string) mpltypes.AlgorithmSuiteId {
	return &mpltypes.AlgorithmSuiteIdMemberESDK{Value: lookupEnum(r, key, esdkSuites)}
}

func (r *reqReader) commitmentPolicy(key string) mpltypes.CommitmentPolicy {
	return &mpltypes.CommitmentPolicyMemberESDK{Value: lookupEnum(r, key, commitmentPolicies)}
}

func (r *reqReader) aesWrappingAlg(key string) mpltypes.AesWrappingAlg {
	return lookupEnum(r, key, aesWrappingAlgs)
}

func (r *reqReader) edks(key string) []mpltypes.EncryptedDataKey {
	out := []mpltypes.EncryptedDataKey{}
	for _, entry := range r.list(key) {
		m, ok := entry.(cbor.Map)
		if !ok {
			r.fail("member %s: expected structures, got %T", key, entry)
			continue
		}
		e := &reqReader{m: m}
		edk := mpltypes.EncryptedDataKey{
			KeyProviderId:   e.str("keyProviderId"),
			KeyProviderInfo: e.bytes("keyProviderInfo"),
			Ciphertext:      e.bytes("ciphertext"),
		}
		if e.err != nil {
			r.fail("member %s: %v", key, e.err)
		}
		out = append(out, edk)
	}
	return out
}

// suiteNameOf maps an MPL suite id back to its wire name.
func suiteNameOf(id mpltypes.AlgorithmSuiteId) (string, *serverError) {
	esdk, ok := id.(*mpltypes.AlgorithmSuiteIdMemberESDK)
	if !ok {
		return "", generic("the MPL returned a non-ESDK algorithm suite, which the model cannot carry")
	}
	for name, value := range esdkSuites {
		if value == esdk.Value {
			return name, nil
		}
	}
	return "", generic("unrecognized ESDK algorithm suite %s", esdk.Value)
}
