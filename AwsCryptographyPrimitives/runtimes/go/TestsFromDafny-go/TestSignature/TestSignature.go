// Package TestSignature
// Dafny module TestSignature compiled into Go

package TestSignature

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
	m_ConstantTime "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/ConstantTime"
	m_ConstantTimeTest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/ConstantTimeTest"
	m_TestAwsCryptographyPrimitivesAesKdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesAesKdfCtr"
	m_TestAwsCryptographyPrimitivesDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesDigest"
	m_TestAwsCryptographyPrimitivesGenerateRandomBytes "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesGenerateRandomBytes"
	m_TestAwsCryptographyPrimitivesHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHKDF"
	m_TestAwsCryptographyPrimitivesHMacDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMacDigest"
	m_TestECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestECDH"
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
var _ m_TestECDH.Dummy__
var _ m_TestAwsCryptographyPrimitivesHKDF.Dummy__
var _ m_TestAwsCryptographyPrimitivesGenerateRandomBytes.Dummy__
var _ m_TestAwsCryptographyPrimitivesDigest.Dummy__
var _ m_ConstantTime.Dummy__
var _ m_ConstantTimeTest.Dummy__
var _ m_TestAwsCryptographyPrimitivesAesKdfCtr.Dummy__

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
	return "TestSignature.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) RequireGoodKeyLengths(alg m_AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm, sigKeyPair m_Signature.SignatureKeyPair) {
	if !((_dafny.IntOfUint32(((sigKeyPair).Dtor_verificationKey()).Cardinality())).Cmp(m_Signature.Companion_Default___.FieldSize(alg)) == 0) {
		panic("test/TestSignature.dfy(24,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) YCompression(alg m_AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm, fieldSize _dafny.Int) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_Signature.Companion_SignatureKeyPair_.Default())
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Signature.Companion_Default___.ExternKeyGen(alg)
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestSignature.dfy(28,15): " + (_0_valueOrError0).String())
	}
	var _1_res m_Signature.SignatureKeyPair
	_ = _1_res
	_1_res = (_0_valueOrError0).Extract().(m_Signature.SignatureKeyPair)
	Companion_Default___.RequireGoodKeyLengths(alg, _1_res)
	var _2_public _dafny.Sequence
	_ = _2_public
	var _3_secret _dafny.Sequence
	_ = _3_secret
	var _rhs0 _dafny.Sequence = (_1_res).Dtor_verificationKey()
	_ = _rhs0
	var _rhs1 _dafny.Sequence = (_1_res).Dtor_signingKey()
	_ = _rhs1
	_2_public = _rhs0
	_3_secret = _rhs1
	if !((_dafny.IntOfUint32((_3_secret).Cardinality())).Sign() == 1) {
		panic("test/TestSignature.dfy(33,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((_2_public).Cardinality())).Cmp((_dafny.One).Plus(((fieldSize).Plus(_dafny.IntOfInt64(7))).DivBy(_dafny.IntOfInt64(8)))) == 0) {
		panic("test/TestSignature.dfy(34,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((((_2_public).Select(0).(uint8)) == (uint8(2))) || (((_2_public).Select(0).(uint8)) == (uint8(3)))) {
		panic("test/TestSignature.dfy(35,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) VerifyMessage(alg m_AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UTF8.Encode(_dafny.SeqOfString("Hello, World!"))
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestSignature.dfy(39,19): " + (_0_valueOrError0).String())
	}
	var _1_message _dafny.Sequence
	_ = _1_message
	_1_message = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_genInput m_AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput
	_ = _2_genInput
	_2_genInput = m_AwsCryptographyPrimitivesTypes.Companion_GenerateECDSASignatureKeyInput_.Create_GenerateECDSASignatureKeyInput_(alg)
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_Signature.Companion_SignatureKeyPair_.Default())
	_ = _3_valueOrError1
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Signature.Companion_Default___.ExternKeyGen(alg)
	_3_valueOrError1 = _out0
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/TestSignature.dfy(41,16): " + (_3_valueOrError1).String())
	}
	var _4_keys m_Signature.SignatureKeyPair
	_ = _4_keys
	_4_keys = (_3_valueOrError1).Extract().(m_Signature.SignatureKeyPair)
	Companion_Default___.RequireGoodKeyLengths(alg, _4_keys)
	var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _5_valueOrError2
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Signature.Companion_Default___.Sign(alg, (_4_keys).Dtor_signingKey(), _1_message)
	_5_valueOrError2 = _out1
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("test/TestSignature.dfy(44,21): " + (_5_valueOrError2).String())
	}
	var _6_signature _dafny.Sequence
	_ = _6_signature
	_6_signature = (_5_valueOrError2).Extract().(_dafny.Sequence)
	var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(false)
	_ = _7_valueOrError3
	_7_valueOrError3 = m_Signature.Companion_Default___.Verify(alg, (_4_keys).Dtor_verificationKey(), _1_message, _6_signature)
	if !(!((_7_valueOrError3).IsFailure())) {
		panic("test/TestSignature.dfy(45,24): " + (_7_valueOrError3).String())
	}
	var _8_shouldBeTrue bool
	_ = _8_shouldBeTrue
	_8_shouldBeTrue = (_7_valueOrError3).Extract().(bool)
	if !(_8_shouldBeTrue) {
		panic("test/TestSignature.dfy(46,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _9_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(false)
	_ = _9_valueOrError4
	_9_valueOrError4 = m_Signature.Companion_Default___.Verify(alg, (_4_keys).Dtor_verificationKey(), _dafny.Companion_Sequence_.Concatenate(_1_message, _dafny.SeqOf(uint8(1))), _6_signature)
	if !(!((_9_valueOrError4).IsFailure())) {
		panic("test/TestSignature.dfy(48,25): " + (_9_valueOrError4).String())
	}
	var _10_shouldBeFalse bool
	_ = _10_shouldBeFalse
	_10_shouldBeFalse = (_9_valueOrError4).Extract().(bool)
	if !(!(_10_shouldBeFalse)) {
		panic("test/TestSignature.dfy(49,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) YCompression384() {
	Companion_Default___.YCompression(Companion_Default___.P384(), _dafny.IntOfInt64(384))
}
func (_static *CompanionStruct_Default___) YCompression256() {
	Companion_Default___.YCompression(Companion_Default___.P256(), _dafny.IntOfInt64(256))
}
func (_static *CompanionStruct_Default___) VerifyMessage384() {
	Companion_Default___.VerifyMessage(Companion_Default___.P384())
}
func (_static *CompanionStruct_Default___) VerifyMessage256() {
	Companion_Default___.VerifyMessage(Companion_Default___.P256())
}
func (_static *CompanionStruct_Default___) P384() m_AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_()
}
func (_static *CompanionStruct_Default___) P256() m_AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P256_()
}

// End of class Default__
