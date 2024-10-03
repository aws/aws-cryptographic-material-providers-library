package TestECDH

import (
	AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	"github.com/dafny-lang/DafnyRuntimeGo/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

// TODO: Check the key bytes in Dafny and ensure it's a valid infinity/out-of-bounds key by running it through Java / NET
func (CompanionStruct_Default___) GetInfinityPublicKey(curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec) Wrappers.Result {
	if curveSpec.Is_SM2() {
		return Wrappers.Companion_Result_.Create_Failure_(dafny.SeqOfBytes([]byte{}))
	}

	if curveSpec.Is_ECC__NIST__P256() {
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes([]byte{
			48, 25, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61,
			3, 1, 7, 3, 2, 0, 0,
		}))
	}

	if curveSpec.Is_ECC__NIST__P384() {
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes([]byte{
			48, 22, 48, 16, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 5, 43, 129, 4, 0, 34, 3,
			2, 0, 0,
		}))
	}

	if curveSpec.Is_ECC__NIST__P521() {
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes([]byte{
			48, 22, 48, 16, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 5, 43, 129, 4, 0, 35, 3,
			2, 0, 0,
		}))
	}

	panic("Unsupported curve spec")

}

func (CompanionStruct_Default___) GetOutOfBoundsPublicKey(curveSpec AwsCryptographyPrimitivesTypes.ECDHCurveSpec) Wrappers.Result {
	if curveSpec.Is_SM2() {
		return Wrappers.Companion_Result_.Create_Failure_(dafny.SeqOfBytes([]byte{}))
	}

	if curveSpec.Is_ECC__NIST__P256() {
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes([]byte{
			48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61,
			3, 1, 7, 3, 66, 0, 4, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255,
		}))
	}

	if curveSpec.Is_ECC__NIST__P384() {
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes([]byte{
			48, 118, 48, 16, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 5, 43, 129, 4, 0, 34, 3,
			98, 0, 4, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255,
		}))
	}

	if curveSpec.Is_ECC__NIST__P521() {
		return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes([]byte{
			48, 129, 155, 48, 16, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 5, 43, 129, 4, 0,
			35, 3, 129, 134, 0, 4, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
			255, 255, 255, 255, 255, 255, 255, 255, 255,
		}))
	}

	panic("Unsupported curve spec")
}
