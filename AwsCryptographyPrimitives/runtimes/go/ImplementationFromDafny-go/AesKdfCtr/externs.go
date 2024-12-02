package AesKdfCtr

import (
	"crypto/aes"
	"crypto/cipher"

	dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

func AesKdfCtrStream(nonce dafny.Sequence, key dafny.Sequence, length uint32) Wrappers.Result {

	block, err := aes.NewCipher(dafny.ToByteArray(key))

	if err != nil {
		panic(err)
	}

	stream := cipher.NewCTR(block, dafny.ToByteArray(nonce))

	result := make([]byte, length)

	stream.XORKeyStream(result, make([]byte, length))
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(result))
}
