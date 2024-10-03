package Signature

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/x509"
	"fmt"

	"github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	dafny "github.com/dafny-lang/DafnyRuntimeGo/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

func (CompanionStruct_Default___) ExternKeyGen(algorithm AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm) Wrappers.Result {
	var privateKey []byte
	var pubKey []byte
	var err error

	curve, err := getNativeEC(algorithm)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	privateKey, pubKey, err = generateKeyPair(curve)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	return Wrappers.Companion_Result_.Create_Success_(Companion_SignatureKeyPair_.Create_SignatureKeyPair_(dafny.SeqOfBytes(pubKey), dafny.SeqOfBytes(privateKey)))
}

func (CompanionStruct_Default___) Sign(algorithm AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm, key dafny.Sequence, msg dafny.Sequence) Wrappers.Result {
	privateKey, err := x509.ParsePKCS8PrivateKey(dafny.ToByteArray(key))
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	res, err := ecdsa.SignASN1(rand.Reader, privateKey.(*ecdsa.PrivateKey), dafny.ToByteArray(msg))
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(res))
}

func (CompanionStruct_Default___) Verify(algorithm AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm, key dafny.Sequence, msg dafny.Sequence, sig dafny.Sequence) Wrappers.Result {
	curve, err := getNativeEC(algorithm)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	x, y := elliptic.UnmarshalCompressed(curve, dafny.ToByteArray(key))
	if x == nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char("Failed to decompress verification key")...)))
	}
	res := ecdsa.VerifyASN1(&ecdsa.PublicKey{Curve: curve, X: x, Y: y}, dafny.ToByteArray(msg), dafny.ToByteArray(sig))
	return Wrappers.Companion_Result_.Create_Success_(res)
}

func generateKeyPair(curve elliptic.Curve) ([]byte, []byte, error) {
	privateKey, err := ecdsa.GenerateKey(curve, rand.Reader)
	if err != nil {
		return nil, nil, err
	}
	publicKey := privateKey.PublicKey

	encodedPrivateKey, err := x509.MarshalPKCS8PrivateKey(privateKey)
	if err != nil {
		return nil, nil, err
	}

	return encodedPrivateKey, elliptic.MarshalCompressed(curve, publicKey.X, publicKey.Y), nil
}

func getNativeEC(curveSpec AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm) (elliptic.Curve, error) {
	switch curveSpec {
	case AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P256_():
		return elliptic.P256(), nil
	case AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_():
		return elliptic.P384(), nil
	default:
		return nil, fmt.Errorf("invalid curve specification: %s not supported", curveSpec)

	}
}
