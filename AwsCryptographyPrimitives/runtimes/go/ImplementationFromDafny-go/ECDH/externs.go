package ECDH

import (
	"crypto/ecdh"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/x509"
	"encoding/pem"
	"fmt"

	AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

func (CompanionStruct_Default___) GenerateKeyPair(curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec) Wrappers.Result {
	var privateKey []byte
	var pubKey []byte
	var err error

	curve, err := getNativeEcdhCurve(curveSpec)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	privateKey, pubKey, err = generateKeyPair(curve)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	return Wrappers.Companion_Result_.Create_Success_(Companion_EccKeyPair_.Create_EccKeyPair_(dafny.SeqOfBytes(privateKey), dafny.SeqOfBytes(pubKey)))
}

func (CompanionStruct_Default___) CalculateSharedSecret(curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec, privateKeyInput AwsCryptographyPrimitivesTypes.ECCPrivateKey, publicKeyInput AwsCryptographyPrimitivesTypes.ECCPublicKey) Wrappers.Result {
	curve, err := getNativeEcdhCurve(curveSpec)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}
	privateKeyPem, rest := pem.Decode(dafny.ToByteArray(privateKeyInput.Dtor_pem()))
	if len(rest) > 0 {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char("Invalid PEM format")...)))

	}

	privateKeyDer, err := x509.ParsePKCS8PrivateKey(privateKeyPem.Bytes)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	publicKeyDer, err := x509.ParsePKIXPublicKey(dafny.ToByteArray(publicKeyInput.Dtor_der()))
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	publicKeyEcdh, err := publicKeyDer.(*ecdsa.PublicKey).ECDH()
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	privateKeyEcdh, err := privateKeyDer.(*ecdsa.PrivateKey).ECDH()
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	privateKey, err := curve.NewPrivateKey(privateKeyEcdh.Bytes())
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	publicKey, err := curve.NewPublicKey(publicKeyEcdh.Bytes())
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	sharedSecret, err := privateKey.ECDH(publicKey)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))

	}

	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(sharedSecret))
}

func (CompanionStruct_Default___) CompressPublicKey(publicKeyInput dafny.Sequence, curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec) Wrappers.Result {
	pkixPublicKey, err := x509.ParsePKIXPublicKey(dafny.ToByteArray(publicKeyInput))
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	ecdhPublicKey := pkixPublicKey.(*ecdsa.PublicKey)
	curve, err := getNativeEcdhCurve(curveSpec)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	compressedPoint := elliptic.MarshalCompressed(ecdhCurveToEllipticCurve(curve), ecdhPublicKey.X, ecdhPublicKey.Y)
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(compressedPoint))

}

func (CompanionStruct_Default___) DecompressPublicKey(publicKeyInput dafny.Sequence, curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec) Wrappers.Result {
	publicKeyBytes := dafny.ToByteArray(publicKeyInput)

	curve, err := getNativeEcdhCurve(curveSpec)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	x, y := elliptic.UnmarshalCompressed(ecdhCurveToEllipticCurve(curve), publicKeyBytes)
	ecPublicKey := ecdsa.PublicKey{Curve: ecdhCurveToEllipticCurve(curve), X: x, Y: y}
	ecdhPublicKey, err := ecPublicKey.ECDH()
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	derivedEcdhKey, err := curve.NewPublicKey(ecdhPublicKey.Bytes())
	b, err := x509.MarshalPKIXPublicKey(derivedEcdhKey)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(b))

}

func ecdhCurveToEllipticCurve(ecdhCurve ecdh.Curve) elliptic.Curve {
	switch ecdhCurve {
	case ecdh.P256():
		return elliptic.P256()
	case ecdh.P384():
		return elliptic.P384()
	case ecdh.P521():
		return elliptic.P521()
	default:
		panic("Unsupported curve")
	}
}

func (CompanionStruct_Default___) ParsePublicKey(publicKeyInput dafny.Sequence) Wrappers.Result {
	publicKeyBytes := dafny.ToByteArray(publicKeyInput)

	var ecdhPublicKey *ecdh.PublicKey
	pkixPublicKey, err := x509.ParsePKIXPublicKey(publicKeyBytes)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	if ecdhPublicKey, err = pkixPublicKey.(*ecdsa.PublicKey).ECDH(); err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	encodedPublicKey, err := x509.MarshalPKIXPublicKey(ecdhPublicKey)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(encodedPublicKey))

}

func (companion CompanionStruct_Default___) ValidatePublicKey(curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec, publicKeyInput dafny.Sequence) Wrappers.Result {
	parseResult := companion.ParsePublicKey(publicKeyInput)
	if parseResult.IsFailure() {
		return parseResult
	}

	curve, err := getNativeEcdhCurve(curveSpec)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	encodedPublicKey, err := x509.ParsePKIXPublicKey(dafny.ToByteArray(parseResult.Dtor_value().(dafny.Sequence)))
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	ecdhPublicKey, err := encodedPublicKey.(*ecdsa.PublicKey).ECDH()

	if _, err := curve.NewPublicKey(ecdhPublicKey.Bytes()); err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(true)
	}

	return Wrappers.Companion_Result_.Create_Success_(true)
}

func (CompanionStruct_Default___) GetPublicKey(curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec, privateKey AwsCryptographyPrimitivesTypes.ECCPrivateKey) Wrappers.Result {
	privateKeyPem := dafny.ToByteArray(privateKey.Dtor_pem())
	privateKeyBytes, rest := pem.Decode(privateKeyPem)
	if len(rest) > 0 {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char("invalid PEM format")...)))
	}
	curve, err := getNativeEcdhCurve(curveSpec)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	pk, err := x509.ParsePKCS8PrivateKey(privateKeyBytes.Bytes)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	ecdhPk, err := pk.(*ecdsa.PrivateKey).ECDH()
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	newPrivateKey, err := curve.NewPrivateKey(ecdhPk.Bytes())
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	encodedPublicKey, err := x509.MarshalPKIXPublicKey(newPrivateKey.PublicKey())
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(encodedPublicKey))

}

func generateKeyPair(curve ecdh.Curve) ([]byte, []byte, error) {
	privateKey, err := curve.GenerateKey(rand.Reader)
	if err != nil {
		return nil, nil, err
	}
	publicKey := privateKey.PublicKey()
	if err != nil {
		return nil, nil, err
	}

	encodedPrivateKey, err := x509.MarshalPKCS8PrivateKey(privateKey)
	if err != nil {
		return nil, nil, err
	}

	if err != nil {
		return nil, nil, err
	}

	privateKeyPEM := &pem.Block{
		Type:  "PRIVATE KEY",
		Bytes: encodedPrivateKey,
	}
	encodedPublicKey, err := x509.MarshalPKIXPublicKey(publicKey)
	if err != nil {
		return nil, nil, err
	}

	return pem.EncodeToMemory(privateKeyPEM), encodedPublicKey, nil
}

func getNativeEcdhCurve(curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec) (ecdh.Curve, error) {
	switch curveSpec {
	case AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_():
		return ecdh.P256(), nil
	case AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_():
		return ecdh.P384(), nil
	case AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_():
		return ecdh.P521(), nil
	case AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_SM2_():
		//TODO: Fix this
		return nil, fmt.Errorf("invalid curve specification: SM2 not supported")
	default:
		return nil, fmt.Errorf("invalid curve specification: %s not supported", curveSpec)
	}
}
