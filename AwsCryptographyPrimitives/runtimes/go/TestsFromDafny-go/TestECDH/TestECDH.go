// Package TestECDH
// Dafny module TestECDH compiled into Go

package TestECDH

import (
	os "os"

	m_AESEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/AESEncryption"
	m_AtomicPrimitives "github.com/aws/aws-cryptographic-material-providers-library/primitives/AtomicPrimitives"
	m_AwsCryptographyPrimitivesOperations "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesOperations"
	m_AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	m_Digest "github.com/aws/aws-cryptographic-material-providers-library/primitives/Digest"
	m_ECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/ECDH"
	m_HKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/HKDF"
	m_HMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/HMAC"
	m_KdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/KdfCtr"
	m_RSAEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/RSAEncryption"
	m_Random "github.com/aws/aws-cryptographic-material-providers-library/primitives/Random"
	m_Signature "github.com/aws/aws-cryptographic-material-providers-library/primitives/Signature"
	m_WrappedHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHKDF"
	m_WrappedHMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHMAC"
	m_TestAwsCryptographyPrimitivesHMacDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMacDigest"
	m_TestKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDF"
	m_TestKDFK__TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDFK__TestVectors"
	m__System "github.com/dafny-lang/DafnyRuntimeGo/v4/System_"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	m_Actions "github.com/dafny-lang/DafnyStandardLibGo/Actions"
	m_Base64 "github.com/dafny-lang/DafnyStandardLibGo/Base64"
	m_Base64Lemmas "github.com/dafny-lang/DafnyStandardLibGo/Base64Lemmas"
	m_BoundedInts "github.com/dafny-lang/DafnyStandardLibGo/BoundedInts"
	m_DivInternals "github.com/dafny-lang/DafnyStandardLibGo/DivInternals"
	m_DivInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/DivInternalsNonlinear"
	m_DivMod "github.com/dafny-lang/DafnyStandardLibGo/DivMod"
	m_FileIO "github.com/dafny-lang/DafnyStandardLibGo/FileIO"
	m_FloatCompare "github.com/dafny-lang/DafnyStandardLibGo/FloatCompare"
	m_Functions "github.com/dafny-lang/DafnyStandardLibGo/Functions"
	m_GeneralInternals "github.com/dafny-lang/DafnyStandardLibGo/GeneralInternals"
	m_GetOpt "github.com/dafny-lang/DafnyStandardLibGo/GetOpt"
	m_HexStrings "github.com/dafny-lang/DafnyStandardLibGo/HexStrings"
	m_Logarithm "github.com/dafny-lang/DafnyStandardLibGo/Logarithm"
	m__Math "github.com/dafny-lang/DafnyStandardLibGo/Math_"
	m_ModInternals "github.com/dafny-lang/DafnyStandardLibGo/ModInternals"
	m_ModInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/ModInternalsNonlinear"
	m_Mul "github.com/dafny-lang/DafnyStandardLibGo/Mul"
	m_MulInternals "github.com/dafny-lang/DafnyStandardLibGo/MulInternals"
	m_MulInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/MulInternalsNonlinear"
	m_Power "github.com/dafny-lang/DafnyStandardLibGo/Power"
	m_Relations "github.com/dafny-lang/DafnyStandardLibGo/Relations"
	m_Seq "github.com/dafny-lang/DafnyStandardLibGo/Seq"
	m_Seq_MergeSort "github.com/dafny-lang/DafnyStandardLibGo/Seq_MergeSort"
	m_Sorting "github.com/dafny-lang/DafnyStandardLibGo/Sorting"
	m_StandardLibrary "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary"
	m_StandardLibraryInterop "github.com/dafny-lang/DafnyStandardLibGo/StandardLibraryInterop"
	m_StandardLibrary_String "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_UInt"
	m_Streams "github.com/dafny-lang/DafnyStandardLibGo/Streams"
	m_UTF8 "github.com/dafny-lang/DafnyStandardLibGo/UTF8"
	m_UnicodeStrings "github.com/dafny-lang/DafnyStandardLibGo/UnicodeStrings"
	m__Unicode "github.com/dafny-lang/DafnyStandardLibGo/Unicode_"
	m_Utf16EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf8EncodingForm"
	m_Wrappers "github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

var _ = os.Args
var _ _dafny.Dummy__
var _ m__System.Dummy__
var _ m_Wrappers.Dummy__
var _ m_BoundedInts.Dummy__
var _ m_StandardLibrary_UInt.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
var _ m_Random.Dummy__
var _ m_AESEncryption.Dummy__
var _ m_Digest.Dummy__
var _ m_HMAC.Dummy__
var _ m_WrappedHMAC.Dummy__
var _ m_HKDF.Dummy__
var _ m_WrappedHKDF.Dummy__
var _ m_Signature.Dummy__
var _ m_KdfCtr.Dummy__
var _ m_RSAEncryption.Dummy__
var _ m_ECDH.Dummy__
var _ m_AwsCryptographyPrimitivesOperations.Dummy__
var _ m_AtomicPrimitives.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m__Unicode.Dummy__
var _ m_Functions.Dummy__
var _ m_Utf8EncodingForm.Dummy__
var _ m_Utf16EncodingForm.Dummy__
var _ m_UnicodeStrings.Dummy__
var _ m_FileIO.Dummy__
var _ m_GeneralInternals.Dummy__
var _ m_MulInternalsNonlinear.Dummy__
var _ m_MulInternals.Dummy__
var _ m_Mul.Dummy__
var _ m_ModInternalsNonlinear.Dummy__
var _ m_DivInternalsNonlinear.Dummy__
var _ m_ModInternals.Dummy__
var _ m_DivInternals.Dummy__
var _ m_DivMod.Dummy__
var _ m_Power.Dummy__
var _ m_Logarithm.Dummy__
var _ m_StandardLibraryInterop.Dummy__
var _ m_Streams.Dummy__
var _ m_Sorting.Dummy__
var _ m_HexStrings.Dummy__
var _ m_GetOpt.Dummy__
var _ m_FloatCompare.Dummy__
var _ m_Base64.Dummy__
var _ m_Base64Lemmas.Dummy__
var _ m_Actions.Dummy__
var _ m_TestKDF.Dummy__
var _ m_TestKDFK__TestVectors.Dummy__
var _ m_TestAwsCryptographyPrimitivesHMacDigest.Dummy__

type Dummy__ struct{}

// Definition of class Default__
type Default__ struct {
	dummy byte
}

func New_Default___() *Default__ {
	_this := Default__{}

	return &_this
}

type CompanionStruct_Default___ struct {
}

var Companion_Default___ = CompanionStruct_Default___{}

func (_this *Default__) Equals(other *Default__) bool {
	return _this == other
}

func (_this *Default__) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*Default__)
	return ok && _this.Equals(other)
}

func (*Default__) String() string {
	return "TestECDH.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestKeyGen() {
	var _0_supportedCurves _dafny.Sequence
	_ = _0_supportedCurves
	_0_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_supportedCurves).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _2_curve
		_2_curve = (_0_supportedCurves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
		_ = _3_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_2_curve))
		_3_valueOrError0 = _out0
		if !(!((_3_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(148,21): " + (_3_valueOrError0).String())
		}
		var _4_keypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
		_ = _4_keypair
		_4_keypair = (_3_valueOrError0).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	}
}
func (_static *CompanionStruct_Default___) TestGetPublicKeyFromPrivatePem() {
	var _0_pemPrivateKeys _dafny.Sequence
	_ = _0_pemPrivateKeys
	_0_pemPrivateKeys = _dafny.SeqOf(Companion_Default___.ECC__P256__PRIVATE(), Companion_Default___.ECC__P384__PRIVATE(), Companion_Default___.ECC__P521__PRIVATE())
	var _1_derPublicKeys _dafny.Sequence
	_ = _1_derPublicKeys
	_1_derPublicKeys = _dafny.SeqOf(Companion_Default___.ECC__P256__PUBLIC(), Companion_Default___.ECC__384__PUBLIC(), Companion_Default___.ECC__P521__PUBLIC())
	var _2_supportedCurves _dafny.Sequence
	_ = _2_supportedCurves
	_2_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_2_supportedCurves).Cardinality())
	_ = _hi0
	for _3_i := _dafny.Zero; _3_i.Cmp(_hi0) < 0; _3_i = _3_i.Plus(_dafny.One) {
		var _4_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _4_curve
		_4_curve = (_2_supportedCurves).Select((_3_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _5_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
		_ = _5_valueOrError0
		_5_valueOrError0 = m_UTF8.Encode((_0_pemPrivateKeys).Select((_3_i).Uint32()).(_dafny.Sequence))
		if !(!((_5_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(165,24): " + (_5_valueOrError0).String())
		}
		var _6_privateKey _dafny.Sequence
		_ = _6_privateKey
		_6_privateKey = (_5_valueOrError0).Extract().(_dafny.Sequence)
		var _7_looseHexPublicKey _dafny.Sequence
		_ = _7_looseHexPublicKey
		var _out0 _dafny.Sequence
		_ = _out0
		_out0 = Companion_Default___.ExpectLooseHexString((_1_derPublicKeys).Select((_3_i).Uint32()).(_dafny.Sequence))
		_7_looseHexPublicKey = _out0
		var _8_publicKeyBytes _dafny.Sequence
		_ = _8_publicKeyBytes
		_8_publicKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_7_looseHexPublicKey)
		var _9_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_ParsePublicKeyOutput_.Default())
		_ = _9_valueOrError1
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__ParsePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ParsePublicKeyInput_.Create_ParsePublicKeyInput_(_8_publicKeyBytes))
		_9_valueOrError1 = _out1
		if !(!((_9_valueOrError1).IsFailure())) {
			panic("test/TestECDH.dfy(169,31): " + (_9_valueOrError1).String())
		}
		var _10_expectedPublicKey m_AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput
		_ = _10_expectedPublicKey
		_10_expectedPublicKey = (_9_valueOrError1).Extract().(m_AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput)
		var _11_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GetPublicKeyFromPrivateKeyOutput_.Default())
		_ = _11_valueOrError2
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = m_ECDH.Companion_Default___.GetPublicKeyFromPrivate(m_AwsCryptographyPrimitivesTypes.Companion_GetPublicKeyFromPrivateKeyInput_.Create_GetPublicKeyFromPrivateKeyInput_(_4_curve, m_AwsCryptographyPrimitivesTypes.Companion_ECCPrivateKey_.Create_ECCPrivateKey_(_6_privateKey)))
		_11_valueOrError2 = _out2
		if !(!((_11_valueOrError2).IsFailure())) {
			panic("test/TestECDH.dfy(174,23): " + (_11_valueOrError2).String())
		}
		var _12_publicKey m_AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput
		_ = _12_publicKey
		_12_publicKey = (_11_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput)
		if !(_dafny.Companion_Sequence_.Equal((_12_publicKey).Dtor_publicKey(), ((_10_expectedPublicKey).Dtor_publicKey()).Dtor_der())) {
			panic("test/TestECDH.dfy(181,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestGetPublicKeyFromPrivateIncorrectCruve() {
	var _0_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
	_ = _0_curve
	_0_curve = Companion_Default___.P384()
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_UTF8.Encode(Companion_Default___.ECC__P256__PRIVATE())
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/TestECDH.dfy(188,22): " + (_1_valueOrError0).String())
	}
	var _2_privateKey _dafny.Sequence
	_ = _2_privateKey
	_2_privateKey = (_1_valueOrError0).Extract().(_dafny.Sequence)
	var _3_looseHexPublicKey _dafny.Sequence
	_ = _3_looseHexPublicKey
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = Companion_Default___.ExpectLooseHexString(Companion_Default___.ECC__P256__PUBLIC())
	_3_looseHexPublicKey = _out0
	var _4_publicKeyBytes _dafny.Sequence
	_ = _4_publicKeyBytes
	_4_publicKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_3_looseHexPublicKey)
	var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_ParsePublicKeyOutput_.Default())
	_ = _5_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_ECDH.Companion_Default___.Go__ParsePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ParsePublicKeyInput_.Create_ParsePublicKeyInput_(_4_publicKeyBytes))
	_5_valueOrError1 = _out1
	if !(!((_5_valueOrError1).IsFailure())) {
		panic("test/TestECDH.dfy(192,29): " + (_5_valueOrError1).String())
	}
	var _6_expectedPublicKey m_AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput
	_ = _6_expectedPublicKey
	_6_expectedPublicKey = (_5_valueOrError1).Extract().(m_AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput)
	var _7_publicKey m_Wrappers.Result
	_ = _7_publicKey
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_ECDH.Companion_Default___.GetPublicKeyFromPrivate(m_AwsCryptographyPrimitivesTypes.Companion_GetPublicKeyFromPrivateKeyInput_.Create_GetPublicKeyFromPrivateKeyInput_(_0_curve, m_AwsCryptographyPrimitivesTypes.Companion_ECCPrivateKey_.Create_ECCPrivateKey_(_2_privateKey)))
	_7_publicKey = _out2
	if !((_7_publicKey).Is_Failure()) {
		panic("test/TestECDH.dfy(204,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) ExpectLooseHexString(s _dafny.Sequence) _dafny.Sequence {
	var s2 _dafny.Sequence = _dafny.EmptySeq.SetString()
	_ = s2
	if !(m_HexStrings.Companion_Default___.IsLooseHexString(s)) {
		panic("test/TestECDH.dfy(210,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	s2 = s
	return s2
	return s2
}
func (_static *CompanionStruct_Default___) TestValidatePublicKeySuccess() {
	var _0_supportedCurves _dafny.Sequence
	_ = _0_supportedCurves
	_0_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_supportedCurves).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _2_curve
		_2_curve = (_0_supportedCurves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
		_ = _3_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_2_curve))
		_3_valueOrError0 = _out0
		if !(!((_3_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(221,22): " + (_3_valueOrError0).String())
		}
		var _4_keypairA m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
		_ = _4_keypairA
		_4_keypairA = (_3_valueOrError0).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
		var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
		_ = _5_valueOrError1
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_2_curve))
		_5_valueOrError1 = _out1
		if !(!((_5_valueOrError1).IsFailure())) {
			panic("test/TestECDH.dfy(226,22): " + (_5_valueOrError1).String())
		}
		var _6_keypairB m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
		_ = _6_keypairB
		_6_keypairB = (_5_valueOrError1).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
		var _7_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyOutput_.Default())
		_ = _7_valueOrError2
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_(_2_curve, ((_6_keypairB).Dtor_publicKey()).Dtor_der()))
		_7_valueOrError2 = _out2
		if !(!((_7_valueOrError2).IsFailure())) {
			panic("test/TestECDH.dfy(232,29): " + (_7_valueOrError2).String())
		}
		var _8_validPublicKeyB m_AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
		_ = _8_validPublicKeyB
		_8_validPublicKeyB = (_7_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput)
	}
}
func (_static *CompanionStruct_Default___) TestValidatePublicKeyFailure() {
	var _0_supportedCurves _dafny.Sequence
	_ = _0_supportedCurves
	_0_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_supportedCurves).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _hi1 _dafny.Int = _dafny.IntOfUint32((_0_supportedCurves).Cardinality())
		_ = _hi1
		for _2_j := _dafny.Zero; _2_j.Cmp(_hi1) < 0; _2_j = _2_j.Plus(_dafny.One) {
			var _3_curve__i m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
			_ = _3_curve__i
			_3_curve__i = (_0_supportedCurves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
			var _4_curve__j m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
			_ = _4_curve__j
			_4_curve__j = (_0_supportedCurves).Select((_2_j).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
			var _5_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
			_ = _5_valueOrError0
			var _out0 m_Wrappers.Result
			_ = _out0
			_out0 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_3_curve__i))
			_5_valueOrError0 = _out0
			if !(!((_5_valueOrError0).IsFailure())) {
				panic("test/TestECDH.dfy(252,24): " + (_5_valueOrError0).String())
			}
			var _6_keypairA m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
			_ = _6_keypairA
			_6_keypairA = (_5_valueOrError0).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
			var _7_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
			_ = _7_valueOrError1
			var _out1 m_Wrappers.Result
			_ = _out1
			_out1 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_4_curve__j))
			_7_valueOrError1 = _out1
			if !(!((_7_valueOrError1).IsFailure())) {
				panic("test/TestECDH.dfy(257,24): " + (_7_valueOrError1).String())
			}
			var _8_keypairB m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
			_ = _8_keypairB
			_8_keypairB = (_7_valueOrError1).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
			var _9_validPublicKeyB m_Wrappers.Result
			_ = _9_validPublicKeyB
			var _out2 m_Wrappers.Result
			_ = _out2
			_out2 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_(_3_curve__i, ((_8_keypairB).Dtor_publicKey()).Dtor_der()))
			_9_validPublicKeyB = _out2
			if !(_3_curve__i).Equals(_4_curve__j) {
				if !((_9_validPublicKeyB).Is_Failure()) {
					panic("test/TestECDH.dfy(271,10): " + (_dafny.SeqOfString("expectation violation")).String())
				}
			} else {
				if !((_9_validPublicKeyB).Is_Success()) {
					panic("test/TestECDH.dfy(273,10): " + (_dafny.SeqOfString("expectation violation")).String())
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) TestValidatePublicKeyFailurePointAtINFFailOnLoad() {
	var _0_publicKeysWithPointsAtINF _dafny.Sequence
	_ = _0_publicKeysWithPointsAtINF
	_0_publicKeysWithPointsAtINF = _dafny.SeqOf(Companion_Default___.ECC__256__PUBLIC__INF__FAIL__ON__LOAD(), Companion_Default___.ECC__384__PUBLIC__INF__FAIL__ON__LOAD(), Companion_Default___.ECC__521__PUBLIC__INF__FAIL__ON__LOAD())
	var _1_supportedCurves _dafny.Sequence
	_ = _1_supportedCurves
	_1_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_1_supportedCurves).Cardinality())
	_ = _hi0
	for _2_i := _dafny.Zero; _2_i.Cmp(_hi0) < 0; _2_i = _2_i.Plus(_dafny.One) {
		var _3_looseHexPublicKey _dafny.Sequence
		_ = _3_looseHexPublicKey
		var _out0 _dafny.Sequence
		_ = _out0
		_out0 = Companion_Default___.ExpectLooseHexString((_0_publicKeysWithPointsAtINF).Select((_2_i).Uint32()).(_dafny.Sequence))
		_3_looseHexPublicKey = _out0
		var _4_publicKeyBytes _dafny.Sequence
		_ = _4_publicKeyBytes
		_4_publicKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_3_looseHexPublicKey)
		var _5_validPublicKey m_Wrappers.Result
		_ = _5_validPublicKey
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_((_1_supportedCurves).Select((_2_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _4_publicKeyBytes))
		_5_validPublicKey = _out1
		if !((_5_validPublicKey).Is_Failure()) {
			panic("test/TestECDH.dfy(297,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !(((_5_validPublicKey).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Is_AwsCryptographicPrimitivesError()) {
			panic("test/TestECDH.dfy(299,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _6_errMsg _dafny.Sequence
		_ = _6_errMsg
		_6_errMsg = ((_5_validPublicKey).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Dtor_message()
		if !((((((_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__RUST())) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__GO()))) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__JAVA()))) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__NET6()))) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__NET48()))) || (Companion_Default___.Seq__contains(_6_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__PYTHON()))) {
			panic("test/TestECDH.dfy(302,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestValidatePublicKeyFailurePointAtINF() {
	var _0_publicKeysWithPointsAtINF _dafny.Sequence
	_ = _0_publicKeysWithPointsAtINF
	_0_publicKeysWithPointsAtINF = _dafny.SeqOf(Companion_Default___.ECC__256__PUBLIC__INF(), Companion_Default___.ECC__384__PUBLIC__INF(), Companion_Default___.ECC__521__PUBLIC__INF())
	var _1_supportedCurves _dafny.Sequence
	_ = _1_supportedCurves
	_1_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_1_supportedCurves).Cardinality())
	_ = _hi0
	for _2_i := _dafny.Zero; _2_i.Cmp(_hi0) < 0; _2_i = _2_i.Plus(_dafny.One) {
		var _3_looseHexPublicKey _dafny.Sequence
		_ = _3_looseHexPublicKey
		var _out0 _dafny.Sequence
		_ = _out0
		_out0 = Companion_Default___.ExpectLooseHexString((_0_publicKeysWithPointsAtINF).Select((_2_i).Uint32()).(_dafny.Sequence))
		_3_looseHexPublicKey = _out0
		var _4_publicKeyBytes _dafny.Sequence
		_ = _4_publicKeyBytes
		_4_publicKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_3_looseHexPublicKey)
		var _5_validPublicKey m_Wrappers.Result
		_ = _5_validPublicKey
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_((_1_supportedCurves).Select((_2_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _4_publicKeyBytes))
		_5_validPublicKey = _out1
		if !((_5_validPublicKey).Is_Failure()) {
			panic("test/TestECDH.dfy(328,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad() {
	var _0_publicKeysWithPointsGreaterThanP _dafny.Sequence
	_ = _0_publicKeysWithPointsGreaterThanP
	_0_publicKeysWithPointsGreaterThanP = _dafny.SeqOf(Companion_Default___.ECC__P256__PUBLIC__GP__FAIL__ON__LOAD(), Companion_Default___.ECC__P384__PUBLIC__GP__FAIL__ON__LOAD(), Companion_Default___.ECC__P521__PUBLIC__GP__FAIL__ON__LOAD())
	var _1_supportedCurves _dafny.Sequence
	_ = _1_supportedCurves
	_1_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_1_supportedCurves).Cardinality())
	_ = _hi0
	for _2_i := _dafny.Zero; _2_i.Cmp(_hi0) < 0; _2_i = _2_i.Plus(_dafny.One) {
		var _3_looseHexPublicKey _dafny.Sequence
		_ = _3_looseHexPublicKey
		var _out0 _dafny.Sequence
		_ = _out0
		_out0 = Companion_Default___.ExpectLooseHexString((_0_publicKeysWithPointsGreaterThanP).Select((_2_i).Uint32()).(_dafny.Sequence))
		_3_looseHexPublicKey = _out0
		var _4_publicKeyBytes _dafny.Sequence
		_ = _4_publicKeyBytes
		_4_publicKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_3_looseHexPublicKey)
		var _5_validPublicKey m_Wrappers.Result
		_ = _5_validPublicKey
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_((_1_supportedCurves).Select((_2_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _4_publicKeyBytes))
		_5_validPublicKey = _out1
		if !((_5_validPublicKey).Is_Failure()) {
			panic("test/TestECDH.dfy(349,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !(((_5_validPublicKey).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Is_AwsCryptographicPrimitivesError()) {
			panic("test/TestECDH.dfy(351,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _6_errMsg _dafny.Sequence
		_ = _6_errMsg
		_6_errMsg = ((_5_validPublicKey).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Dtor_message()
		if !((((((Companion_Default___.Seq__contains(_6_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__JAVA())) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__RUST()))) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__GO()))) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__NET6()))) || (_dafny.Companion_Sequence_.Equal(_6_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__NE48()))) || (Companion_Default___.Seq__contains(_6_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__PYTHON()))) {
			panic("test/TestECDH.dfy(353,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestValidatePublicKeyFailurePointGreaterThanP() {
	var _0_publicKeysWithPointsGreaterThanP _dafny.Sequence
	_ = _0_publicKeysWithPointsGreaterThanP
	_0_publicKeysWithPointsGreaterThanP = _dafny.SeqOf(Companion_Default___.ECC__P256__PUBLIC__GP(), Companion_Default___.ECC__P384__PUBLIC__GP(), Companion_Default___.ECC__P521__PUBLIC__GP())
	var _1_supportedCurves _dafny.Sequence
	_ = _1_supportedCurves
	_1_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_1_supportedCurves).Cardinality())
	_ = _hi0
	for _2_i := _dafny.Zero; _2_i.Cmp(_hi0) < 0; _2_i = _2_i.Plus(_dafny.One) {
		var _3_looseHexPublicKey _dafny.Sequence
		_ = _3_looseHexPublicKey
		var _out0 _dafny.Sequence
		_ = _out0
		_out0 = Companion_Default___.ExpectLooseHexString((_0_publicKeysWithPointsGreaterThanP).Select((_2_i).Uint32()).(_dafny.Sequence))
		_3_looseHexPublicKey = _out0
		var _4_publicKeyBytes _dafny.Sequence
		_ = _4_publicKeyBytes
		_4_publicKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_3_looseHexPublicKey)
		var _5_validPublicKey m_Wrappers.Result
		_ = _5_validPublicKey
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_((_1_supportedCurves).Select((_2_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _4_publicKeyBytes))
		_5_validPublicKey = _out1
		if !((_5_validPublicKey).Is_Failure()) {
			panic("test/TestECDH.dfy(379,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestGenerateSharedSecret() {
	var _0_supportedCurves _dafny.Sequence
	_ = _0_supportedCurves
	_0_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_supportedCurves).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _2_curve
		_2_curve = (_0_supportedCurves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
		_ = _3_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_2_curve))
		_3_valueOrError0 = _out0
		if !(!((_3_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(389,22): " + (_3_valueOrError0).String())
		}
		var _4_keypairA m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
		_ = _4_keypairA
		_4_keypairA = (_3_valueOrError0).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
		var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
		_ = _5_valueOrError1
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_2_curve))
		_5_valueOrError1 = _out1
		if !(!((_5_valueOrError1).IsFailure())) {
			panic("test/TestECDH.dfy(394,22): " + (_5_valueOrError1).String())
		}
		var _6_keypairB m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
		_ = _6_keypairB
		_6_keypairB = (_5_valueOrError1).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
		if !((!((_4_keypairA).Dtor_privateKey()).Equals((_6_keypairB).Dtor_privateKey())) && (!((_4_keypairA).Dtor_publicKey()).Equals((_6_keypairB).Dtor_publicKey()))) {
			panic("test/TestECDH.dfy(400,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _7_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyOutput_.Default())
		_ = _7_valueOrError2
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_(_2_curve, ((_6_keypairB).Dtor_publicKey()).Dtor_der()))
		_7_valueOrError2 = _out2
		if !(!((_7_valueOrError2).IsFailure())) {
			panic("test/TestECDH.dfy(405,29): " + (_7_valueOrError2).String())
		}
		var _8_validPublicKeyB m_AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
		_ = _8_validPublicKeyB
		_8_validPublicKeyB = (_7_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput)
		var _9_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretOutput_.Default())
		_ = _9_valueOrError3
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = m_ECDH.Companion_Default___.DeriveSharedSecret(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretInput_.Create_DeriveSharedSecretInput_(_2_curve, (_4_keypairA).Dtor_privateKey(), (_6_keypairB).Dtor_publicKey()))
		_9_valueOrError3 = _out3
		if !(!((_9_valueOrError3).IsFailure())) {
			panic("test/TestECDH.dfy(412,27): " + (_9_valueOrError3).String())
		}
		var _10_sharedSecretA m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
		_ = _10_sharedSecretA
		_10_sharedSecretA = (_9_valueOrError3).Extract().(m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput)
		var _11_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretOutput_.Default())
		_ = _11_valueOrError4
		var _out4 m_Wrappers.Result
		_ = _out4
		_out4 = m_ECDH.Companion_Default___.DeriveSharedSecret(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretInput_.Create_DeriveSharedSecretInput_(_2_curve, (_6_keypairB).Dtor_privateKey(), (_4_keypairA).Dtor_publicKey()))
		_11_valueOrError4 = _out4
		if !(!((_11_valueOrError4).IsFailure())) {
			panic("test/TestECDH.dfy(420,27): " + (_11_valueOrError4).String())
		}
		var _12_sharedSecretB m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
		_ = _12_sharedSecretB
		_12_sharedSecretB = (_11_valueOrError4).Extract().(m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput)
		if !((_10_sharedSecretA).Equals(_12_sharedSecretB)) {
			panic("test/TestECDH.dfy(428,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestCompressDecompressPublicKey() {
	var _0_supportedCurves _dafny.Sequence
	_ = _0_supportedCurves
	_0_supportedCurves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_supportedCurves).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _2_curve
		_2_curve = (_0_supportedCurves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
		_ = _3_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_ECDH.Companion_Default___.GenerateEccKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(_2_curve))
		_3_valueOrError0 = _out0
		if !(!((_3_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(437,21): " + (_3_valueOrError0).String())
		}
		var _4_keypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
		_ = _4_keypair
		_4_keypair = (_3_valueOrError0).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
		var _5_originalPublicKey m_AwsCryptographyPrimitivesTypes.ECCPublicKey
		_ = _5_originalPublicKey
		_5_originalPublicKey = (_4_keypair).Dtor_publicKey()
		var _6_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_CompressPublicKeyOutput_.Default())
		_ = _6_valueOrError1
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__CompressPublicKey(m_AwsCryptographyPrimitivesTypes.Companion_CompressPublicKeyInput_.Create_CompressPublicKeyInput_(_5_originalPublicKey, _2_curve))
		_6_valueOrError1 = _out1
		if !(!((_6_valueOrError1).IsFailure())) {
			panic("test/TestECDH.dfy(444,39): " + (_6_valueOrError1).String())
		}
		var _7_compressedPublicKeyResult m_AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
		_ = _7_compressedPublicKeyResult
		_7_compressedPublicKeyResult = (_6_valueOrError1).Extract().(m_AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput)
		if !(!_dafny.Companion_Sequence_.Equal((_7_compressedPublicKeyResult).Dtor_compressedPublicKey(), (_5_originalPublicKey).Dtor_der())) {
			panic("test/TestECDH.dfy(451,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _8_compressedPublicKey _dafny.Sequence
		_ = _8_compressedPublicKey
		_8_compressedPublicKey = (_7_compressedPublicKeyResult).Dtor_compressedPublicKey()
		var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_DecompressPublicKeyOutput_.Default())
		_ = _9_valueOrError2
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = m_ECDH.Companion_Default___.Go__DecompressPublicKey(m_AwsCryptographyPrimitivesTypes.Companion_DecompressPublicKeyInput_.Create_DecompressPublicKeyInput_(_8_compressedPublicKey, _2_curve))
		_9_valueOrError2 = _out2
		if !(!((_9_valueOrError2).IsFailure())) {
			panic("test/TestECDH.dfy(455,41): " + (_9_valueOrError2).String())
		}
		var _10_decompressedPublicKeyResult m_AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
		_ = _10_decompressedPublicKeyResult
		_10_decompressedPublicKeyResult = (_9_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput)
		var _11_decompressedPublicKey m_AwsCryptographyPrimitivesTypes.ECCPublicKey
		_ = _11_decompressedPublicKey
		_11_decompressedPublicKey = (_10_decompressedPublicKeyResult).Dtor_publicKey()
		if !(_dafny.Companion_Sequence_.Equal((_5_originalPublicKey).Dtor_der(), (_11_decompressedPublicKey).Dtor_der())) {
			panic("test/TestECDH.dfy(464,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestCompressDecompressConstantPublicKeys() {
	var _0_derX509PublicKeys _dafny.Sequence
	_ = _0_derX509PublicKeys
	_0_derX509PublicKeys = _dafny.SeqOf(Companion_Default___.ECC__P256__PUBLIC(), Companion_Default___.ECC__384__PUBLIC(), Companion_Default___.ECC__P521__PUBLIC())
	var _1_compressedKeys _dafny.Sequence
	_ = _1_compressedKeys
	_1_compressedKeys = _dafny.SeqOf(Companion_Default___.ECC__P256__PUBLIC__COMPRESSED(), Companion_Default___.ECC__384__PUBLIC__COMPRESSED(), Companion_Default___.ECC__P521__PUBLIC__COMPRESSED())
	var _2_curves _dafny.Sequence
	_ = _2_curves
	_2_curves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_2_curves).Cardinality())
	_ = _hi0
	for _3_i := _dafny.Zero; _3_i.Cmp(_hi0) < 0; _3_i = _3_i.Plus(_dafny.One) {
		var _4_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _4_curve
		_4_curve = (_2_curves).Select((_3_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _5_originalPublicKey _dafny.Sequence
		_ = _5_originalPublicKey
		var _out0 _dafny.Sequence
		_ = _out0
		_out0 = Companion_Default___.ExpectLooseHexString((_0_derX509PublicKeys).Select((_3_i).Uint32()).(_dafny.Sequence))
		_5_originalPublicKey = _out0
		var _6_publicKeyBytes _dafny.Sequence
		_ = _6_publicKeyBytes
		_6_publicKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_5_originalPublicKey)
		var _7_compressedKey _dafny.Sequence
		_ = _7_compressedKey
		var _out1 _dafny.Sequence
		_ = _out1
		_out1 = Companion_Default___.ExpectLooseHexString((_1_compressedKeys).Select((_3_i).Uint32()).(_dafny.Sequence))
		_7_compressedKey = _out1
		var _8_compressedKeyBytes _dafny.Sequence
		_ = _8_compressedKeyBytes
		_8_compressedKeyBytes = m_HexStrings.Companion_Default___.FromHexString(_7_compressedKey)
		var _9_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_CompressPublicKeyOutput_.Default())
		_ = _9_valueOrError0
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = m_ECDH.Companion_Default___.Go__CompressPublicKey(m_AwsCryptographyPrimitivesTypes.Companion_CompressPublicKeyInput_.Create_CompressPublicKeyInput_(m_AwsCryptographyPrimitivesTypes.Companion_ECCPublicKey_.Create_ECCPublicKey_(_6_publicKeyBytes), _4_curve))
		_9_valueOrError0 = _out2
		if !(!((_9_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(481,39): " + (_9_valueOrError0).String())
		}
		var _10_compressedPublicKeyResult m_AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
		_ = _10_compressedPublicKeyResult
		_10_compressedPublicKeyResult = (_9_valueOrError0).Extract().(m_AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput)
		if !(_dafny.Companion_Sequence_.Equal((_10_compressedPublicKeyResult).Dtor_compressedPublicKey(), _8_compressedKeyBytes)) {
			panic("test/TestECDH.dfy(488,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _11_compressedPublicKey _dafny.Sequence
		_ = _11_compressedPublicKey
		_11_compressedPublicKey = (_10_compressedPublicKeyResult).Dtor_compressedPublicKey()
		var _12_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_DecompressPublicKeyOutput_.Default())
		_ = _12_valueOrError1
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = m_ECDH.Companion_Default___.Go__DecompressPublicKey(m_AwsCryptographyPrimitivesTypes.Companion_DecompressPublicKeyInput_.Create_DecompressPublicKeyInput_(_11_compressedPublicKey, _4_curve))
		_12_valueOrError1 = _out3
		if !(!((_12_valueOrError1).IsFailure())) {
			panic("test/TestECDH.dfy(492,41): " + (_12_valueOrError1).String())
		}
		var _13_decompressedPublicKeyResult m_AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
		_ = _13_decompressedPublicKeyResult
		_13_decompressedPublicKeyResult = (_12_valueOrError1).Extract().(m_AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput)
		var _14_decompressedPublicKey m_AwsCryptographyPrimitivesTypes.ECCPublicKey
		_ = _14_decompressedPublicKey
		_14_decompressedPublicKey = (_13_decompressedPublicKeyResult).Dtor_publicKey()
		if !(_dafny.Companion_Sequence_.Equal(_6_publicKeyBytes, (_14_decompressedPublicKey).Dtor_der())) {
			panic("test/TestECDH.dfy(501,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestPublicKeyValidationTestVectorsInfinity() {
	var _0_curves _dafny.Sequence
	_ = _0_curves
	_0_curves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_curves).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _2_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = Companion_Default___.GetInfinityPublicKey((_0_curves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec))
		_2_valueOrError0 = _out0
		if !(!((_2_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(511,25): " + (_2_valueOrError0).String())
		}
		var _3_der__ecc__inf _dafny.Sequence
		_ = _3_der__ecc__inf
		_3_der__ecc__inf = (_2_valueOrError0).Extract().(_dafny.Sequence)
		var _4_validPublicKeyB m_Wrappers.Result
		_ = _4_validPublicKeyB
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_((_0_curves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_der__ecc__inf))
		_4_validPublicKeyB = _out1
		if !((_4_validPublicKeyB).Is_Failure()) {
			panic("test/TestECDH.dfy(519,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !(((_4_validPublicKeyB).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Is_AwsCryptographicPrimitivesError()) {
			panic("test/TestECDH.dfy(520,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _5_errMsg _dafny.Sequence
		_ = _5_errMsg
		_5_errMsg = ((_4_validPublicKeyB).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Dtor_message()
		if !((((((_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__JAVA())) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__RUST()))) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__GO()))) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__NET6()))) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__NET48()))) || (Companion_Default___.Seq__contains(_5_errMsg, Companion_Default___.INFINITY__POINT__ERR__MSG__PYTHON()))) {
			panic("test/TestECDH.dfy(523,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestPublicKeyValidationTestVectorsOutOfBounds() {
	var _0_curves _dafny.Sequence
	_ = _0_curves
	_0_curves = _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_curves).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _2_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = Companion_Default___.GetOutOfBoundsPublicKey((_0_curves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec))
		_2_valueOrError0 = _out0
		if !(!((_2_valueOrError0).IsFailure())) {
			panic("test/TestECDH.dfy(540,25): " + (_2_valueOrError0).String())
		}
		var _3_der__ecc__inf _dafny.Sequence
		_ = _3_der__ecc__inf
		_3_der__ecc__inf = (_2_valueOrError0).Extract().(_dafny.Sequence)
		var _4_validPublicKeyB m_Wrappers.Result
		_ = _4_validPublicKeyB
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_ECDH.Companion_Default___.Go__ValidatePublicKey(m_AwsCryptographyPrimitivesTypes.Companion_ValidatePublicKeyInput_.Create_ValidatePublicKeyInput_((_0_curves).Select((_1_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_der__ecc__inf))
		_4_validPublicKeyB = _out1
		if !((_4_validPublicKeyB).Is_Failure()) {
			panic("test/TestECDH.dfy(548,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !(((_4_validPublicKeyB).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Is_AwsCryptographicPrimitivesError()) {
			panic("test/TestECDH.dfy(549,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _5_errMsg _dafny.Sequence
		_ = _5_errMsg
		_5_errMsg = ((_4_validPublicKeyB).Dtor_error().(m_AwsCryptographyPrimitivesTypes.Error)).Dtor_message()
		if !((((((Companion_Default___.Seq__contains(_5_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__JAVA())) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__RUST()))) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.BAD__X509__KEY__ERR__MSG__GO()))) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__NET6()))) || (_dafny.Companion_Sequence_.Equal(_5_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__NE48()))) || (Companion_Default___.Seq__contains(_5_errMsg, Companion_Default___.OUT__OF__BOUNDS__ERR__MSG__PYTHON()))) {
			panic("test/TestECDH.dfy(552,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) Seq__contains(haystack _dafny.Sequence, needle _dafny.Sequence) bool {
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (_dafny.IntOfUint32((needle).Cardinality())).Sign() == 0 {
		return true
	} else if (_dafny.IntOfUint32((haystack).Cardinality())).Sign() == 0 {
		return false
	} else if (_dafny.IntOfUint32((haystack).Cardinality())).Cmp(_dafny.IntOfUint32((needle).Cardinality())) < 0 {
		return false
	} else if (_dafny.AreEqual((needle).Select(0).(interface{}), (haystack).Select(0).(interface{}))) && (_dafny.Companion_Sequence_.IsPrefixOf((needle).Drop(1), (haystack).Drop(1))) {
		return true
	} else {
		var _in0 _dafny.Sequence = (haystack).Drop(1)
		_ = _in0
		var _in1 _dafny.Sequence = needle
		_ = _in1
		haystack = _in0
		needle = _in1
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) P256() m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()
}
func (_static *CompanionStruct_Default___) P384() m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_()
}
func (_static *CompanionStruct_Default___) P521() m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_()
}
func (_static *CompanionStruct_Default___) ECC__P256__PRIVATE() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n")), _dafny.SeqOfString("22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n")), _dafny.SeqOfString("7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) ECC__P384__PRIVATE() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n")), _dafny.SeqOfString("6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n")), _dafny.SeqOfString("GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n")), _dafny.SeqOfString("b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) ECC__P521__PRIVATE() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n")), _dafny.SeqOfString("xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n")), _dafny.SeqOfString("oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n")), _dafny.SeqOfString("I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n")), _dafny.SeqOfString("C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n")), _dafny.SeqOfString("Qg==\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) ECC__P256__PUBLIC() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3059301306072a8648ce3d020106082a8648ce3d03010703420004a7520c7b4ab9478"), _dafny.SeqOfString("4f227dcc7197dcddc108b3cf9715fec9be172e575c1610b199f008eec272a313489")), _dafny.SeqOfString("e944c126391d8cd6085efbdc5bc96961981981a149b6bc"))
}
func (_static *CompanionStruct_Default___) ECC__384__PUBLIC() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3076301006072a8648ce3d020106052b81040022036200041ac8f5ba07769518a58505"), _dafny.SeqOfString("b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c")), _dafny.SeqOfString("905998c89f20e4daea5e6f54e2bcfd1461acbe7484bc32b04533ba0b06c248ab11a2")), _dafny.SeqOfString("450d443c522904bbf89a6b5e3a66b9aadf"))
}
func (_static *CompanionStruct_Default___) ECC__P521__PUBLIC() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("30819b301006072a8648ce3d020106052b81040023038186000401de32732469d8769e"), _dafny.SeqOfString("47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb2")), _dafny.SeqOfString("1d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39017df878ad9db941c8bd6e")), _dafny.SeqOfString("dcdea45a151f0b7babcb5d53f1d90d5be2db564997f01dfeb3a55a11058a6be49805")), _dafny.SeqOfString("e98f574e5a261534c5a685fcc86c2c6c0a2e93e942"))
}
func (_static *CompanionStruct_Default___) ECC__256__PUBLIC__INF__FAIL__ON__LOAD() _dafny.Sequence {
	return _dafny.SeqOfString("3019301306072a8648ce3d020106082a8648ce3d03010703020000")
}
func (_static *CompanionStruct_Default___) ECC__384__PUBLIC__INF__FAIL__ON__LOAD() _dafny.Sequence {
	return _dafny.SeqOfString("3016301006072a8648ce3d020106052b8104002203020000")
}
func (_static *CompanionStruct_Default___) ECC__521__PUBLIC__INF__FAIL__ON__LOAD() _dafny.Sequence {
	return _dafny.SeqOfString("3016301006072a8648ce3d020106052b8104002303020000")
}
func (_static *CompanionStruct_Default___) BAD__X509__KEY__ERR__MSG__RUST() _dafny.Sequence {
	return _dafny.SeqOfString("Invalid X509 Public Key.")
}
func (_static *CompanionStruct_Default___) BAD__X509__KEY__ERR__MSG__GO() _dafny.Sequence {
	return _dafny.SeqOfString("x509: failed to unmarshal elliptic curve point")
}
func (_static *CompanionStruct_Default___) INFINITY__POINT__ERR__MSG__JAVA() _dafny.Sequence {
	return _dafny.SeqOfString("encoded key spec not recognized: Point at infinity")
}
func (_static *CompanionStruct_Default___) INFINITY__POINT__ERR__MSG__NET6() _dafny.Sequence {
	return _dafny.SeqOfString("Point at infinity (Parameter 'q')")
}
func (_static *CompanionStruct_Default___) INFINITY__POINT__ERR__MSG__NET48() _dafny.Sequence {
	return _dafny.SeqOfString("Point at infinity\r\nParameter name: q")
}
func (_static *CompanionStruct_Default___) INFINITY__POINT__ERR__MSG__PYTHON() _dafny.Sequence {
	return _dafny.SeqOfString("Cannot load an EC public key where the point is at infinity")
}
func (_static *CompanionStruct_Default___) ECC__256__PUBLIC__INF() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3059301306072a864886f70d0106082a864886f70d03010703420004000000000000"), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000"))
}
func (_static *CompanionStruct_Default___) ECC__384__PUBLIC__INF() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3076301006072a864886f70d0106052b810400220362000400000000000000000000"), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000"))
}
func (_static *CompanionStruct_Default___) ECC__521__PUBLIC__INF() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3081ee3010060772a8648ce3d02106052b81040023038186000400000000000000000"), _dafny.SeqOfString("000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("0000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000"))
}
func (_static *CompanionStruct_Default___) ECC__P256__PUBLIC__GP__FAIL__ON__LOAD() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3059301306072a8648ce3d020106082a8648ce3d03010703420004fffffffffffffffff"), _dafny.SeqOfString("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")), _dafny.SeqOfString("ffffffffffffffffffffffffffffffffffffffffff"))
}
func (_static *CompanionStruct_Default___) ECC__P384__PUBLIC__GP__FAIL__ON__LOAD() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3076301006072a8648ce3d020106052b8104002203620004fffffffffffffffffffffff"), _dafny.SeqOfString("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")), _dafny.SeqOfString("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")), _dafny.SeqOfString("fffffffffffffffffffffffffffff"))
}
func (_static *CompanionStruct_Default___) ECC__P521__PUBLIC__GP__FAIL__ON__LOAD() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("30819b301006072a8648ce3d020106052b810400230381860004ffffffffffffffffffff"), _dafny.SeqOfString("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")), _dafny.SeqOfString("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")), _dafny.SeqOfString("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")), _dafny.SeqOfString("ffffffffffffffffffffffffffffffffff"))
}
func (_static *CompanionStruct_Default___) OUT__OF__BOUNDS__ERR__MSG__JAVA() _dafny.Sequence {
	return _dafny.SeqOfString("encoded key spec not recognized: x value invalid for")
}
func (_static *CompanionStruct_Default___) OUT__OF__BOUNDS__ERR__MSG__NET6() _dafny.Sequence {
	return _dafny.SeqOfString("value invalid for Fp field element (Parameter 'x')")
}
func (_static *CompanionStruct_Default___) OUT__OF__BOUNDS__ERR__MSG__NE48() _dafny.Sequence {
	return _dafny.SeqOfString("value invalid for Fp field element\r\nParameter name: x")
}
func (_static *CompanionStruct_Default___) OUT__OF__BOUNDS__ERR__MSG__PYTHON() _dafny.Sequence {
	return _dafny.SeqOfString("Invalid key")
}
func (_static *CompanionStruct_Default___) ECC__P256__PUBLIC__GP() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3059301306072a864886f70d0106082a864886f70d03010703420004000000000000000"), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("000000001"))
}
func (_static *CompanionStruct_Default___) ECC__P384__PUBLIC__GP() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3076301006072a864886f70d0106052b810400220362000400000000000000000000000"), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("0000000000000000000000000000001"))
}
func (_static *CompanionStruct_Default___) ECC__P521__PUBLIC__GP() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("3081ee3010060772a8648ce3d02106052b8104002303818600040000000000000000000"), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000000000000000000000000000000000000000000")), _dafny.SeqOfString("00000000000000000000000000000000001"))
}
func (_static *CompanionStruct_Default___) ECC__P256__PUBLIC__COMPRESSED() _dafny.Sequence {
	return _dafny.SeqOfString("02a7520c7b4ab94784f227dcc7197dcddc108b3cf9715fec9be172e575c1610b19")
}
func (_static *CompanionStruct_Default___) ECC__384__PUBLIC__COMPRESSED() _dafny.Sequence {
	return _dafny.SeqOfString("031ac8f5ba07769518a58505b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c905998")
}
func (_static *CompanionStruct_Default___) ECC__P521__PUBLIC__COMPRESSED() _dafny.Sequence {
	return _dafny.SeqOfString("0201de32732469d8769e47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb21d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39")
}

// End of class Default__
