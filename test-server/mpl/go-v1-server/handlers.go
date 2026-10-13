// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Operation handlers: decode the request map, call the MaterialProviders
// client, and build the rpcv2Cbor response map. Keyrings and CMMs are held in
// typed registries behind UUID handles; a handle is only looked up in the
// registry of the kind the operation expects. A library error becomes an
// MPLClientError; a malformed request or bad handle a GenericServerError.

package main

import (
	"context"
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"sync"

	mpl "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygenerated"
	mpltypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

type appState struct {
	client    *mpl.Client
	suiteInfo map[string]mpltypes.AlgorithmSuiteInfo

	mu       sync.Mutex
	keyrings map[string]mpltypes.IKeyring
	cmms     map[string]mpltypes.ICryptographicMaterialsManager
}

func newAppState() (*appState, error) {
	client, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
	if err != nil {
		return nil, err
	}
	// Resolve every suite's AlgorithmSuiteInfo once from its two-byte id.
	suiteInfo := map[string]mpltypes.AlgorithmSuiteInfo{}
	for name, id := range esdkSuites {
		binary, err := hex.DecodeString(string(id)[2:])
		if err != nil {
			return nil, fmt.Errorf("suite %s: %v", name, err)
		}
		info, err := client.GetAlgorithmSuiteInfo(context.Background(), binary)
		if err != nil {
			return nil, fmt.Errorf("suite %s: %v", name, err)
		}
		suiteInfo[name] = *info
	}
	return &appState{
		client:    client,
		suiteInfo: suiteInfo,
		keyrings:  map[string]mpltypes.IKeyring{},
		cmms:      map[string]mpltypes.ICryptographicMaterialsManager{},
	}, nil
}

// ---------------------------------------------------------------------------
// Construction
// ---------------------------------------------------------------------------

func (s *appState) createRawAesKeyring(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	input := mpltypes.CreateRawAesKeyringInput{
		KeyNamespace: r.str("keyNamespace"),
		KeyName:      r.str("keyName"),
		WrappingKey:  r.bytes("wrappingKey"),
		WrappingAlg:  r.aesWrappingAlg("wrappingAlg"),
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	keyring, err := s.client.CreateRawAesKeyring(ctx, input)
	if err != nil {
		return nil, mplError(err.Error())
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"keyringId": cbor.String(register(s.keyrings, keyring))}, nil
}

func (s *appState) createDefaultCmm(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	keyring, serr := s.keyring(m)
	if serr != nil {
		return nil, serr
	}
	cmm, err := s.client.CreateDefaultCryptographicMaterialsManager(ctx,
		mpltypes.CreateDefaultCryptographicMaterialsManagerInput{Keyring: keyring})
	if err != nil {
		return nil, mplError(err.Error())
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	return cbor.Map{"cmmId": cbor.String(register(s.cmms, cmm))}, nil
}

// ---------------------------------------------------------------------------
// Materials initialization + keyring interface
// ---------------------------------------------------------------------------

func (s *appState) initializeEncryptionMaterials(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	input := mpltypes.InitializeEncryptionMaterialsInput{
		AlgorithmSuiteId:              r.suiteID("algorithmSuiteId"),
		EncryptionContext:             r.stringMap("encryptionContext"),
		RequiredEncryptionContextKeys: r.stringList("requiredEncryptionContextKeys"),
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	materials, err := s.client.InitializeEncryptionMaterials(ctx, input)
	if err != nil {
		return nil, mplError(err.Error())
	}
	wire, serr := encryptionMaterialsToWire(*materials)
	if serr != nil {
		return nil, serr
	}
	return cbor.Map{"materials": wire}, nil
}

func (s *appState) initializeDecryptionMaterials(ctx context.Context, m cbor.Map) (cbor.Value, *serverError) {
	r := reqReader{m: m}
	input := mpltypes.InitializeDecryptionMaterialsInput{
		AlgorithmSuiteId:              r.suiteID("algorithmSuiteId"),
		EncryptionContext:             r.stringMap("encryptionContext"),
		RequiredEncryptionContextKeys: r.stringList("requiredEncryptionContextKeys"),
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	materials, err := s.client.InitializeDecryptionMaterials(ctx, input)
	if err != nil {
		return nil, mplError(err.Error())
	}
	wire, serr := decryptionMaterialsToWire(*materials)
	if serr != nil {
		return nil, serr
	}
	return cbor.Map{"materials": wire}, nil
}

func (s *appState) onEncrypt(m cbor.Map) (cbor.Value, *serverError) {
	keyring, serr := s.keyring(m)
	if serr != nil {
		return nil, serr
	}
	r := reqReader{m: m}
	materials := s.encryptionMaterialsFromWire(r.structure("materials"), &r)
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	output, err := keyring.OnEncrypt(mpltypes.OnEncryptInput{Materials: materials})
	if err != nil {
		return nil, mplError(err.Error())
	}
	wire, serr := encryptionMaterialsToWire(output.Materials)
	if serr != nil {
		return nil, serr
	}
	return cbor.Map{"materials": wire}, nil
}

func (s *appState) onDecrypt(m cbor.Map) (cbor.Value, *serverError) {
	keyring, serr := s.keyring(m)
	if serr != nil {
		return nil, serr
	}
	r := reqReader{m: m}
	input := mpltypes.OnDecryptInput{
		Materials:         s.decryptionMaterialsFromWire(r.structure("materials"), &r),
		EncryptedDataKeys: r.edks("encryptedDataKeys"),
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	output, err := keyring.OnDecrypt(input)
	if err != nil {
		return nil, mplError(err.Error())
	}
	wire, serr := decryptionMaterialsToWire(output.Materials)
	if serr != nil {
		return nil, serr
	}
	return cbor.Map{"materials": wire}, nil
}

// ---------------------------------------------------------------------------
// CMM
// ---------------------------------------------------------------------------

func (s *appState) getEncryptionMaterials(m cbor.Map) (cbor.Value, *serverError) {
	cmm, serr := s.cmm(m)
	if serr != nil {
		return nil, serr
	}
	r := reqReader{m: m}
	input := mpltypes.GetEncryptionMaterialsInput{
		EncryptionContext: r.stringMap("encryptionContext"),
		CommitmentPolicy:  r.commitmentPolicy("commitmentPolicy"),
	}
	if r.present("algorithmSuiteId") {
		input.AlgorithmSuiteId = r.suiteID("algorithmSuiteId")
	}
	if r.present("maxPlaintextLength") {
		length := r.int64("maxPlaintextLength")
		input.MaxPlaintextLength = &length
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	output, err := cmm.GetEncryptionMaterials(input)
	if err != nil {
		return nil, mplError(err.Error())
	}
	materials := output.EncryptionMaterials
	if materials.PlaintextDataKey == nil {
		return nil, mplError("no plaintext data key in materials")
	}
	suite, serr := suiteNameOf(materials.AlgorithmSuite.Id)
	if serr != nil {
		return nil, serr
	}
	out := cbor.Map{
		"algorithmSuiteId":  cbor.String(suite),
		"encryptionContext": stringMapToWire(materials.EncryptionContext),
		"encryptedDataKeys": edksToWire(materials.EncryptedDataKeys),
		"plaintextDataKey":  cbor.Slice(materials.PlaintextDataKey),
	}
	putOptionalBytes(out, "signingKey", materials.SigningKey)
	putOptionalBytesList(out, "symmetricSigningKeys", materials.SymmetricSigningKeys)
	return out, nil
}

func (s *appState) decryptMaterials(m cbor.Map) (cbor.Value, *serverError) {
	cmm, serr := s.cmm(m)
	if serr != nil {
		return nil, serr
	}
	r := reqReader{m: m}
	input := mpltypes.DecryptMaterialsInput{
		AlgorithmSuiteId:  r.suiteID("algorithmSuiteId"),
		CommitmentPolicy:  r.commitmentPolicy("commitmentPolicy"),
		EncryptedDataKeys: r.edks("encryptedDataKeys"),
		EncryptionContext: r.stringMap("encryptionContext"),
	}
	if r.present("reproducedEncryptionContext") {
		input.ReproducedEncryptionContext = r.stringMap("reproducedEncryptionContext")
	}
	if r.err != nil {
		return nil, generic("%v", r.err)
	}
	output, err := cmm.DecryptMaterials(input)
	if err != nil {
		return nil, mplError(err.Error())
	}
	materials := output.DecryptionMaterials
	if materials.PlaintextDataKey == nil {
		return nil, mplError("no plaintext data key in materials")
	}
	out := cbor.Map{
		"plaintextDataKey":  cbor.Slice(materials.PlaintextDataKey),
		"encryptionContext": stringMapToWire(materials.EncryptionContext),
	}
	putOptionalBytes(out, "verificationKey", materials.VerificationKey)
	putOptionalBytes(out, "symmetricSigningKey", materials.SymmetricSigningKey)
	return out, nil
}

// ---------------------------------------------------------------------------
// Registry
// ---------------------------------------------------------------------------

// register stores resource under a fresh v4 UUID. Caller holds s.mu.
func register[T any](registry map[string]T, resource T) string {
	var b [16]byte
	_, _ = rand.Read(b[:])
	b[6] = (b[6] & 0x0f) | 0x40
	b[8] = (b[8] & 0x3f) | 0x80
	id := fmt.Sprintf("%x-%x-%x-%x-%x", b[0:4], b[4:6], b[6:8], b[8:10], b[10:16])
	registry[id] = resource
	return id
}

func lookup[T any](s *appState, registry map[string]T, m cbor.Map, key string) (T, *serverError) {
	var zero T
	r := reqReader{m: m}
	id := r.str(key)
	if r.err != nil {
		return zero, generic("%v", r.err)
	}
	if id == "" {
		return zero, generic("%s must be non-empty", key)
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	resource, ok := registry[id]
	if !ok {
		return zero, generic("unknown %s: %s", key, id)
	}
	return resource, nil
}

func (s *appState) keyring(m cbor.Map) (mpltypes.IKeyring, *serverError) {
	return lookup(s, s.keyrings, m, "keyringId")
}

func (s *appState) cmm(m cbor.Map) (mpltypes.ICryptographicMaterialsManager, *serverError) {
	return lookup(s, s.cmms, m, "cmmId")
}

// ---------------------------------------------------------------------------
// Materials conversion
// ---------------------------------------------------------------------------

func (s *appState) suiteInfoFor(r *reqReader) mpltypes.AlgorithmSuiteInfo {
	return s.suiteInfo[r.suiteName("algorithmSuiteId")]
}

func (s *appState) encryptionMaterialsFromWire(w *reqReader, parent *reqReader) mpltypes.EncryptionMaterials {
	materials := mpltypes.EncryptionMaterials{
		AlgorithmSuite:                s.suiteInfoFor(w),
		EncryptionContext:             w.stringMap("encryptionContext"),
		EncryptedDataKeys:             w.edks("encryptedDataKeys"),
		RequiredEncryptionContextKeys: w.stringList("requiredEncryptionContextKeys"),
		PlaintextDataKey:              w.optionalBytes("plaintextDataKey"),
		SigningKey:                    w.optionalBytes("signingKey"),
		SymmetricSigningKeys:          w.optionalBytesList("symmetricSigningKeys"),
	}
	if w.err != nil {
		parent.fail("member materials: %v", w.err)
	}
	return materials
}

func (s *appState) decryptionMaterialsFromWire(w *reqReader, parent *reqReader) mpltypes.DecryptionMaterials {
	materials := mpltypes.DecryptionMaterials{
		AlgorithmSuite:                s.suiteInfoFor(w),
		EncryptionContext:             w.stringMap("encryptionContext"),
		RequiredEncryptionContextKeys: w.stringList("requiredEncryptionContextKeys"),
		PlaintextDataKey:              w.optionalBytes("plaintextDataKey"),
		VerificationKey:               w.optionalBytes("verificationKey"),
		SymmetricSigningKey:           w.optionalBytes("symmetricSigningKey"),
	}
	if w.err != nil {
		parent.fail("member materials: %v", w.err)
	}
	return materials
}

func encryptionMaterialsToWire(materials mpltypes.EncryptionMaterials) (cbor.Map, *serverError) {
	suite, serr := suiteNameOf(materials.AlgorithmSuite.Id)
	if serr != nil {
		return nil, serr
	}
	out := cbor.Map{
		"algorithmSuiteId":              cbor.String(suite),
		"encryptionContext":             stringMapToWire(materials.EncryptionContext),
		"encryptedDataKeys":             edksToWire(materials.EncryptedDataKeys),
		"requiredEncryptionContextKeys": stringListToWire(materials.RequiredEncryptionContextKeys),
	}
	putOptionalBytes(out, "plaintextDataKey", materials.PlaintextDataKey)
	putOptionalBytes(out, "signingKey", materials.SigningKey)
	putOptionalBytesList(out, "symmetricSigningKeys", materials.SymmetricSigningKeys)
	return out, nil
}

func decryptionMaterialsToWire(materials mpltypes.DecryptionMaterials) (cbor.Map, *serverError) {
	suite, serr := suiteNameOf(materials.AlgorithmSuite.Id)
	if serr != nil {
		return nil, serr
	}
	out := cbor.Map{
		"algorithmSuiteId":              cbor.String(suite),
		"encryptionContext":             stringMapToWire(materials.EncryptionContext),
		"requiredEncryptionContextKeys": stringListToWire(materials.RequiredEncryptionContextKeys),
	}
	putOptionalBytes(out, "plaintextDataKey", materials.PlaintextDataKey)
	putOptionalBytes(out, "verificationKey", materials.VerificationKey)
	putOptionalBytes(out, "symmetricSigningKey", materials.SymmetricSigningKey)
	return out, nil
}

func edksToWire(edks []mpltypes.EncryptedDataKey) cbor.List {
	out := cbor.List{}
	for _, edk := range edks {
		out = append(out, cbor.Map{
			"keyProviderId":   cbor.String(edk.KeyProviderId),
			"keyProviderInfo": cbor.Slice(edk.KeyProviderInfo),
			"ciphertext":      cbor.Slice(edk.Ciphertext),
		})
	}
	return out
}

func stringMapToWire(m map[string]string) cbor.Map {
	out := cbor.Map{}
	for k, v := range m {
		out[k] = cbor.String(v)
	}
	return out
}

func stringListToWire(l []string) cbor.List {
	out := cbor.List{}
	for _, v := range l {
		out = append(out, cbor.String(v))
	}
	return out
}

// Absent optional members are omitted rather than sent as null.
func putOptionalBytes(m cbor.Map, key string, value []byte) {
	if value != nil {
		m[key] = cbor.Slice(value)
	}
}

func putOptionalBytesList(m cbor.Map, key string, values [][]byte) {
	if values != nil {
		out := cbor.List{}
		for _, v := range values {
			out = append(out, cbor.Slice(v))
		}
		m[key] = out
	}
}
