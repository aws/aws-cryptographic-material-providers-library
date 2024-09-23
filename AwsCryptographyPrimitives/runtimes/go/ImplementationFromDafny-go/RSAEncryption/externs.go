package RSAEncryption

import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"encoding/pem"
	"fmt"

	AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	"github.com/dafny-lang/DafnyRuntimeGo/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

func (CompanionStruct_Default___) GenerateKeyPairExtern(bits int32) (dafny.Sequence, dafny.Sequence) {

	privateKey, err := rsa.GenerateKey(rand.Reader, int(bits))
	if err != nil {
		panic(err)
	}
	encodePrivateKey, err := x509.MarshalPKCS8PrivateKey(privateKey)
	if err != nil {
		panic(err)
	}
	encodePublicKey, err := x509.MarshalPKIXPublicKey(&privateKey.PublicKey)
	if err != nil {
		panic(err)
	}
	return dafny.SeqOfBytes(pem.EncodeToMemory(&pem.Block{Type: "RSA PUBLIC KEY", Bytes: encodePublicKey})), dafny.SeqOfBytes(pem.EncodeToMemory(&pem.Block{Type: "RSA PRIVATE KEY", Bytes: encodePrivateKey}))
}

func (CompanionStruct_Default___) GetRSAKeyModulusLengthExtern(publicKeyInput dafny.Sequence) Wrappers.Result {
	derPublicKey, rest := pem.Decode(dafny.ToByteArray(publicKeyInput))
	if len(rest) > 0 {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char("dfewqfew")...)))
	}
	publicKey, err := x509.ParsePKIXPublicKey(derPublicKey.Bytes)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	return Wrappers.Companion_Result_.Create_Success_(uint32(publicKey.(*rsa.PublicKey).N.BitLen()))
}

func (CompanionStruct_Default___) DecryptExtern(paddingMode AwsCryptographyPrimitivesTypes.RSAPaddingMode, key dafny.Sequence, cipher_text dafny.Sequence) Wrappers.Result {
	derPrivateKey, rest := pem.Decode(dafny.ToByteArray(key))
	if len(rest) > 0 {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(fmt.Errorf("failed to decode PEM: invalid bytes:  %s", rest).Error())...)))
	}

	privateKey, err := x509.ParsePKCS8PrivateKey(derPrivateKey.Bytes)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	if paddingMode.Is_PKCS1() {
		encryptedBytes, err := rsa.DecryptPKCS1v15(rand.Reader, privateKey.(*rsa.PrivateKey), dafny.ToByteArray(cipher_text))
		if err != nil {
			return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
		}
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(encryptedBytes))
	}

	mode, err := getNativePaddingMode(paddingMode)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}

	res, err := rsa.DecryptOAEP(crypto.Hash(mode).New(), rand.Reader, privateKey.(*rsa.PrivateKey), dafny.ToByteArray(cipher_text), nil)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(res))
}
func (CompanionStruct_Default___) EncryptExtern(paddingMode AwsCryptographyPrimitivesTypes.RSAPaddingMode, key dafny.Sequence, plainText dafny.Sequence) Wrappers.Result {
	derPublicKey, rest := pem.Decode(dafny.ToByteArray(key))
	if len(rest) > 0 {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char("dfewqfew")...)))
	}

	publicKey, err := x509.ParsePKIXPublicKey(derPublicKey.Bytes)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	if paddingMode.Is_PKCS1() {
		encryptedBytes, err := rsa.EncryptPKCS1v15(rand.Reader, publicKey.(*rsa.PublicKey), dafny.ToByteArray(plainText))
		if err != nil {
			return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
		}
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(encryptedBytes))
	}

	hash1, err := getNativePaddingMode(paddingMode)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	encryptedBytes, err := rsa.EncryptOAEP(crypto.Hash(hash1).New(), rand.Reader, publicKey.(*rsa.PublicKey), dafny.ToByteArray(plainText), nil)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(dafny.SeqOfChars([]dafny.Char(err.Error())...)))
	}
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(encryptedBytes))
}

func getNativePaddingMode(mode AwsCryptographyPrimitivesTypes.RSAPaddingMode) (x509.SignatureAlgorithm, error) {
	switch mode {
	case AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.Create_PKCS1_():
		return x509.UnknownSignatureAlgorithm, nil
	case AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.Create_OAEP__SHA1_():
		return x509.SHA1WithRSA, nil
	case AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.Create_OAEP__SHA256_():
		return x509.SHA256WithRSA, nil
	case AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.Create_OAEP__SHA384_():
		return x509.SHA384WithRSA, nil
	case AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.Create_OAEP__SHA512_():
		return x509.SHA512WithRSA, nil
	default:
		return x509.UnknownSignatureAlgorithm, fmt.Errorf("unsupported padding mode")
	}
}
