package HMAC

import (
	"crypto/hmac"
	"crypto/sha256"
	"crypto/sha512"
	"github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	"hash"

	"github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

type Native_Hmac struct {
	HMac
	algo func() hash.Hash
	hash hash.Hash
}

func (defaultStruct CompanionStruct_Default___) Digest(hMacInput AwsCryptographyPrimitivesTypes.HMacInput) Wrappers.Result {
	companionHMac := Companion_HMac_
	hMac := companionHMac.Build(hMacInput.Dtor_digestAlgorithm()).Dtor_value().(HMac)
	hMac.Init(hMacInput.Dtor_key())
	hMac.BlockUpdate(hMacInput.Dtor_message())
	return defaultStruct.CreateDigestSuccess(hMac.GetResult())
}

func (nativeHmac *Native_Hmac) Init(key dafny.Sequence) {
	keyBytes := dafny.ToByteArray(key)
	nativeHmac.hash = hmac.New(nativeHmac.algo, keyBytes)
}

func (nativeHmac *Native_Hmac) BlockUpdate(message dafny.Sequence) {
	_, err := nativeHmac.hash.Write(dafny.ToByteArray(message))
	if err != nil {
		panic(err)
	}
}

func (nativeHmac *Native_Hmac) String() string {
	return ""
}
func (nativeHmac *Native_Hmac) GetResult() dafny.Sequence {
	res := nativeHmac.hash.Sum(nil)
	// reset the hash for future use. or maybe reinit it like rust?
	nativeHmac.hash.Reset()
	return dafny.SeqOfBytes(res)
}

func (CompanionStruct_HMac_) Build(digestAlgo AwsCryptographyPrimitivesTypes.DigestAlgorithm) Wrappers.Result {
	var algo func() hash.Hash
	if digestAlgo.Is_SHA__256() {
		algo = sha256.New
	}
	if digestAlgo.Is_SHA__384() {
		algo = sha512.New384
	}
	if digestAlgo.Is_SHA__512() {
		algo = sha512.New
	}

	native := Native_Hmac{
		algo: algo,
	}
	return Wrappers.Companion_Result_.Create_Success_(HMac(&native))
}
