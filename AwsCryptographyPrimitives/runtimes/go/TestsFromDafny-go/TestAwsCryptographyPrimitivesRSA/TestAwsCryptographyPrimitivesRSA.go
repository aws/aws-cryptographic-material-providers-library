// Package TestAwsCryptographyPrimitivesRSA
// Dafny module TestAwsCryptographyPrimitivesRSA compiled into Go

package TestAwsCryptographyPrimitivesRSA

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
	m_TestHKDF__Rfc5869TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestHKDF__Rfc5869TestVectors"
	m_TestKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDF"
	m_TestKDFK__TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDFK__TestVectors"
	m_TestSignature "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestSignature"
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
	m_SortedSets "github.com/dafny-lang/DafnyStandardLibGo/SortedSets"
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
var _ m_TestSignature.Dummy__
var _ m_TestHKDF__Rfc5869TestVectors.Dummy__

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
	return "TestAwsCryptographyPrimitivesRSA.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) RSAEncryptTests() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestRSA.dfy(52,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_keys m_Wrappers.Result
	_ = _2_keys
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).GenerateRSAKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateRSAKeyPairInput_.Create_GenerateRSAKeyPairInput_(int32(2048)))
	_2_keys = _out1
	if !((_2_keys).Is_Success()) {
		panic("test/TestRSA.dfy(54,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	Companion_Default___.BasicRSAEncryptTest(m_AwsCryptographyPrimitivesTypes.Companion_RSAEncryptInput_.Create_RSAEncryptInput_(m_AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.Create_OAEP__SHA256_(), (((_2_keys).Dtor_value().(m_AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput)).Dtor_publicKey()).Dtor_pem(), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102))), (_2_keys).Dtor_value().(m_AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput))
}
func (_static *CompanionStruct_Default___) GetRSAKeyModulusLength() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestRSA.dfy(68,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UTF8.Encode(Companion_Default___.RSA__PUBLIC__2048())
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/TestRSA.dfy(72,25): " + (_2_valueOrError1).String())
	}
	var _3_publicKey2048 _dafny.Sequence
	_ = _3_publicKey2048
	_3_publicKey2048 = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError2
	_4_valueOrError2 = (_1_client).GetRSAKeyModulusLength(m_AwsCryptographyPrimitivesTypes.Companion_GetRSAKeyModulusLengthInput_.Create_GetRSAKeyModulusLengthInput_(_3_publicKey2048))
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("test/TestRSA.dfy(73,22): " + (_4_valueOrError2).String())
	}
	var _5_length2048 m_AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput
	_ = _5_length2048
	_5_length2048 = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput)
	if !(((_5_length2048).Dtor_length()) == (int32(2048))) {
		panic("test/TestRSA.dfy(75,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _6_valueOrError3
	_6_valueOrError3 = m_UTF8.Encode(Companion_Default___.RSA__PUBLIC__3072())
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("test/TestRSA.dfy(78,25): " + (_6_valueOrError3).String())
	}
	var _7_publicKey3072 _dafny.Sequence
	_ = _7_publicKey3072
	_7_publicKey3072 = (_6_valueOrError3).Extract().(_dafny.Sequence)
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError4
	_8_valueOrError4 = (_1_client).GetRSAKeyModulusLength(m_AwsCryptographyPrimitivesTypes.Companion_GetRSAKeyModulusLengthInput_.Create_GetRSAKeyModulusLengthInput_(_7_publicKey3072))
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("test/TestRSA.dfy(79,22): " + (_8_valueOrError4).String())
	}
	var _9_length3072 m_AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput
	_ = _9_length3072
	_9_length3072 = (_8_valueOrError4).Extract().(m_AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput)
	if !(((_9_length3072).Dtor_length()) == (int32(3072))) {
		panic("test/TestRSA.dfy(81,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _10_valueOrError5
	_10_valueOrError5 = m_UTF8.Encode(Companion_Default___.RSA__PUBLIC__4096())
	if !(!((_10_valueOrError5).IsFailure())) {
		panic("test/TestRSA.dfy(84,25): " + (_10_valueOrError5).String())
	}
	var _11_publicKey4096 _dafny.Sequence
	_ = _11_publicKey4096
	_11_publicKey4096 = (_10_valueOrError5).Extract().(_dafny.Sequence)
	var _12_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError6
	_12_valueOrError6 = (_1_client).GetRSAKeyModulusLength(m_AwsCryptographyPrimitivesTypes.Companion_GetRSAKeyModulusLengthInput_.Create_GetRSAKeyModulusLengthInput_(_11_publicKey4096))
	if !(!((_12_valueOrError6).IsFailure())) {
		panic("test/TestRSA.dfy(85,22): " + (_12_valueOrError6).String())
	}
	var _13_length4096 m_AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput
	_ = _13_length4096
	_13_length4096 = (_12_valueOrError6).Extract().(m_AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput)
	if !(((_13_length4096).Dtor_length()) == (int32(4096))) {
		panic("test/TestRSA.dfy(87,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) BasicRSADecryptTests(input m_AwsCryptographyPrimitivesTypes.RSADecryptInput, expectedOutput _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestRSA.dfy(95,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).RSADecrypt(input)
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/TestRSA.dfy(96,18): " + (_2_valueOrError1).String())
	}
	var _3_output _dafny.Sequence
	_ = _3_output
	_3_output = (_2_valueOrError1).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_3_output, expectedOutput)) {
		panic("test/TestRSA.dfy(98,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) BasicRSAEncryptTest(input m_AwsCryptographyPrimitivesTypes.RSAEncryptInput, keypair m_AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestRSA.dfy(107,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).RSAEncrypt(input)
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/TestRSA.dfy(108,18): " + (_2_valueOrError1).String())
	}
	var _3_output _dafny.Sequence
	_ = _3_output
	_3_output = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_decryptInput m_AwsCryptographyPrimitivesTypes.RSADecryptInput
	_ = _4_decryptInput
	_4_decryptInput = m_AwsCryptographyPrimitivesTypes.Companion_RSADecryptInput_.Create_RSADecryptInput_((input).Dtor_padding(), ((keypair).Dtor_privateKey()).Dtor_pem(), _3_output)
	Companion_Default___.BasicRSADecryptTests(_4_decryptInput, (input).Dtor_plaintext())
}
func (_static *CompanionStruct_Default___) TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM() {
	var _0_allPadding _dafny.Set
	_ = _0_allPadding
	_0_allPadding = func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter0 := _dafny.Iterate(m_AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.AllSingletonConstructors()); ; {
			_compr_0, _ok0 := _iter0()
			if !_ok0 {
				break
			}
			var _1_p m_AwsCryptographyPrimitivesTypes.RSAPaddingMode
			_1_p = interface{}(_compr_0).(m_AwsCryptographyPrimitivesTypes.RSAPaddingMode)
			_coll0.Add(_1_p)
		}
		return _coll0.ToSet()
	}()
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError0
	_2_valueOrError0 = m_UTF8.Encode(Companion_Default___.StaticPublicKeyFromGenerateRSAKeyPair())
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("test/TestRSA.dfy(122,51): " + (_2_valueOrError0).String())
	}
	var _3_PublicKeyFromGenerateRSAKeyPairPemBytes _dafny.Sequence
	_ = _3_PublicKeyFromGenerateRSAKeyPairPemBytes
	_3_PublicKeyFromGenerateRSAKeyPairPemBytes = (_2_valueOrError0).Extract().(_dafny.Sequence)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _4_valueOrError1
	_4_valueOrError1 = m_UTF8.Encode(Companion_Default___.StaticPrivateKeyFromGenerateRSAKeyPair())
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("test/TestRSA.dfy(123,52): " + (_4_valueOrError1).String())
	}
	var _5_PrivateKeyFromGenerateRSAKeyPairPemBytes _dafny.Sequence
	_ = _5_PrivateKeyFromGenerateRSAKeyPairPemBytes
	_5_PrivateKeyFromGenerateRSAKeyPairPemBytes = (_4_valueOrError1).Extract().(_dafny.Sequence)
	var _6_KeyFromGenerateRSAKeyPair m_AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
	_ = _6_KeyFromGenerateRSAKeyPair
	_6_KeyFromGenerateRSAKeyPair = m_AwsCryptographyPrimitivesTypes.Companion_GenerateRSAKeyPairOutput_.Create_GenerateRSAKeyPairOutput_(m_AwsCryptographyPrimitivesTypes.Companion_RSAPublicKey_.Create_RSAPublicKey_(int32(2048), _3_PublicKeyFromGenerateRSAKeyPairPemBytes), m_AwsCryptographyPrimitivesTypes.Companion_RSAPrivateKey_.Create_RSAPrivateKey_(int32(2048), _5_PrivateKeyFromGenerateRSAKeyPairPemBytes))
	var _7_paddingSeq _dafny.Sequence
	_ = _7_paddingSeq
	_7_paddingSeq = m_SortedSets.SetToSequence(_0_allPadding)
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_7_paddingSeq).Cardinality())
	_ = _hi0
	for _8_paddingIdx := _dafny.Zero; _8_paddingIdx.Cmp(_hi0) < 0; _8_paddingIdx = _8_paddingIdx.Plus(_dafny.One) {
		var _9_padding m_AwsCryptographyPrimitivesTypes.RSAPaddingMode
		_ = _9_padding
		_9_padding = (_7_paddingSeq).Select((_8_paddingIdx).Uint32()).(m_AwsCryptographyPrimitivesTypes.RSAPaddingMode)
		Companion_Default___.BasicRSAEncryptTest(m_AwsCryptographyPrimitivesTypes.Companion_RSAEncryptInput_.Create_RSAEncryptInput_(_9_padding, ((_6_KeyFromGenerateRSAKeyPair).Dtor_publicKey()).Dtor_pem(), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102))), _6_KeyFromGenerateRSAKeyPair)
	}
}
func (_static *CompanionStruct_Default___) TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM() {
	var _0_allPadding _dafny.Set
	_ = _0_allPadding
	_0_allPadding = func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter1 := _dafny.Iterate(m_AwsCryptographyPrimitivesTypes.Companion_RSAPaddingMode_.AllSingletonConstructors()); ; {
			_compr_0, _ok1 := _iter1()
			if !_ok1 {
				break
			}
			var _1_p m_AwsCryptographyPrimitivesTypes.RSAPaddingMode
			_1_p = interface{}(_compr_0).(m_AwsCryptographyPrimitivesTypes.RSAPaddingMode)
			_coll0.Add(_1_p)
		}
		return _coll0.ToSet()
	}()
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError0
	_2_valueOrError0 = m_UTF8.Encode(Companion_Default___.StaticPublicKeyFromTestVectors())
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("test/TestRSA.dfy(155,44): " + (_2_valueOrError0).String())
	}
	var _3_PublicKeyFromTestVectorsPemBytes _dafny.Sequence
	_ = _3_PublicKeyFromTestVectorsPemBytes
	_3_PublicKeyFromTestVectorsPemBytes = (_2_valueOrError0).Extract().(_dafny.Sequence)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _4_valueOrError1
	_4_valueOrError1 = m_UTF8.Encode(Companion_Default___.StaticPrivateKeyFromTestVectors())
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("test/TestRSA.dfy(156,45): " + (_4_valueOrError1).String())
	}
	var _5_PrivateKeyFromTestVectorsPemBytes _dafny.Sequence
	_ = _5_PrivateKeyFromTestVectorsPemBytes
	_5_PrivateKeyFromTestVectorsPemBytes = (_4_valueOrError1).Extract().(_dafny.Sequence)
	var _6_KeyFromTestVectorsPair m_AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
	_ = _6_KeyFromTestVectorsPair
	_6_KeyFromTestVectorsPair = m_AwsCryptographyPrimitivesTypes.Companion_GenerateRSAKeyPairOutput_.Create_GenerateRSAKeyPairOutput_(m_AwsCryptographyPrimitivesTypes.Companion_RSAPublicKey_.Create_RSAPublicKey_(int32(4096), _3_PublicKeyFromTestVectorsPemBytes), m_AwsCryptographyPrimitivesTypes.Companion_RSAPrivateKey_.Create_RSAPrivateKey_(int32(4096), _5_PrivateKeyFromTestVectorsPemBytes))
	var _7_paddingSeq _dafny.Sequence
	_ = _7_paddingSeq
	_7_paddingSeq = m_SortedSets.SetToSequence(_0_allPadding)
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_7_paddingSeq).Cardinality())
	_ = _hi0
	for _8_paddingIdx := _dafny.Zero; _8_paddingIdx.Cmp(_hi0) < 0; _8_paddingIdx = _8_paddingIdx.Plus(_dafny.One) {
		var _9_padding m_AwsCryptographyPrimitivesTypes.RSAPaddingMode
		_ = _9_padding
		_9_padding = (_7_paddingSeq).Select((_8_paddingIdx).Uint32()).(m_AwsCryptographyPrimitivesTypes.RSAPaddingMode)
		Companion_Default___.BasicRSAEncryptTest(m_AwsCryptographyPrimitivesTypes.Companion_RSAEncryptInput_.Create_RSAEncryptInput_(_9_padding, ((_6_KeyFromTestVectorsPair).Dtor_publicKey()).Dtor_pem(), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102))), _6_KeyFromTestVectorsPair)
	}
}
func (_static *CompanionStruct_Default___) StaticPublicKeyFromGenerateRSAKeyPair() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PUBLIC KEY-----\n"), _dafny.SeqOfString("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0RbkftAm30eFm+o6JraW\n")), _dafny.SeqOfString("AbWR+2grPfQk3i3w4eCsZHDQib6iUwX0MVADd2DjTnlkYa1DytDHRKfWHjtTniQ/\n")), _dafny.SeqOfString("EdKbENIFC5mLgh1Max7n9nQ6bmo4EvH2s4pUr3YBSys/dXpRDUCD/Mt4G+qDE8DT\n")), _dafny.SeqOfString("NSe8dqX5U44HwImQmKzvLYvD5gUY7eM5co4ZpfYrlRRVNkpv5qVNK7bz9KvQmKfP\n")), _dafny.SeqOfString("bQfzyvOZgSqQyHKfxbCM6ByE8Dd0NoI1ALwBY8wCXn/+6q4xLWTywu4nGIXs5Vt7\n")), _dafny.SeqOfString("vrMqwHSvYaNQKjUyPjsG3xPMwKruh30mGzc2KlKLZ+MiV+SNAiooqVkL6CxH4yJc\n")), _dafny.SeqOfString("NwIDAQAB\n")), _dafny.SeqOfString("-----END PUBLIC KEY-----\n"))
}
func (_static *CompanionStruct_Default___) StaticPrivateKeyFromGenerateRSAKeyPair() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDRFuR+0CbfR4Wb\n")), _dafny.SeqOfString("6jomtpYBtZH7aCs99CTeLfDh4KxkcNCJvqJTBfQxUAN3YONOeWRhrUPK0MdEp9Ye\n")), _dafny.SeqOfString("O1OeJD8R0psQ0gULmYuCHUxrHuf2dDpuajgS8fazilSvdgFLKz91elENQIP8y3gb\n")), _dafny.SeqOfString("6oMTwNM1J7x2pflTjgfAiZCYrO8ti8PmBRjt4zlyjhml9iuVFFU2Sm/mpU0rtvP0\n")), _dafny.SeqOfString("q9CYp89tB/PK85mBKpDIcp/FsIzoHITwN3Q2gjUAvAFjzAJef/7qrjEtZPLC7icY\n")), _dafny.SeqOfString("hezlW3u+syrAdK9ho1AqNTI+OwbfE8zAqu6HfSYbNzYqUotn4yJX5I0CKiipWQvo\n")), _dafny.SeqOfString("LEfjIlw3AgMBAAECggEAWe7DTCpCtgHg3X2jEnixT73lsuGMy+KBoxDWjYkiDTea\n")), _dafny.SeqOfString("8sxMrHIgpL86JnRFgMDk5MBuKsOfGhAooCs7XYdQm11fNh5nbiRWZZotftu1wQMg\n")), _dafny.SeqOfString("CNLmGHv7dSD4KNoUV10cN+7rAsyvmKF5oWQ+idYD4labkNr1wTMTcYSZ7ZlgbNFr\n")), _dafny.SeqOfString("ZFwsZizD4RrpwwyrpZ25f/H95p9fQrZXrB3Wt5aNn0uhTcQL0KfnvMamZNPfxj9b\n")), _dafny.SeqOfString("j6CWpyXtFOMc8nuT4fKOh7q4A87UsduBBhdAk4m4m98WvlIZIUW89w3kzIfr9zCT\n")), _dafny.SeqOfString("VxflBzeEDSM8+Sy1TJNRBBwhRnQ/gNLLD+e6/O/MTQKBgQD/vRxZvyJkWaRYkGeS\n")), _dafny.SeqOfString("VVAZQJOSQUPpVC5U3y2ghV8Dm30BfMEtySdD9hXd635X7e0dvIqwxJAwFgJ+SYT2\n")), _dafny.SeqOfString("NNE8wiIKolQH1h01cYK+kwAohB6vQPLymYwzc9HNcevCDFkt7VVRgnwUHk6BXz4T\n")), _dafny.SeqOfString("LsF/jYTUdzCyFfjYWGTOEh7PkwKBgQDRTZSe2Tqua2Groi75tmXMAzI6jQsiBqTn\n")), _dafny.SeqOfString("Jv0es+IMWZyh2yMy9x6numM7IBBamgt+6hNEKaUmQxoEFbo0dUsEx35RH2Pdkr8X\n")), _dafny.SeqOfString("IuXuh3IdRgRCV9WxnecBD32Cci9qLN1aaVJHfdA2dW4LAb7m4/GeuiS/8ZatXEm2\n")), _dafny.SeqOfString("Kf0YZAx/TQKBgEpbQtX5U9eXlMhHXEXY1kwxUXbx0PwThNEaftqwTJrw55y6GDTm\n")), _dafny.SeqOfString("yqrg7ySyJu8L96hwvGZ/EGlazOjJGYa4fqnKzDkJT6NjpuR2F4yvkxk0qPNN0BWn\n")), _dafny.SeqOfString("fXMsVrEEUYb/LiLDYc4sQUVcNnk5JwRO0OX0UM2xxg/RgaPtt4mPDTRPAoGBAJsY\n")), _dafny.SeqOfString("1izv5CAjyniY8h5xHvYS2EGzCrDoI4J2zdLWkYd9UChQbsDxhnHcGHRTykqZJDOj\n")), _dafny.SeqOfString("2SsFgS/dQYYNY7JDyJd+DQioLiSe/aNzZNdg3xr6K2XOGLhJvkh25han7qLLJCw/\n")), _dafny.SeqOfString("J416mbQBSM43OPN3rjBk1560s2c7oBOxAa/1U51xAoGBAOYFMvdk6H359yaJGmsN\n")), _dafny.SeqOfString("kY7lS6heh4cHfSM7Hw02lh/ovasdQm+afcnDWEW0XQYM6KQCcJiwbIK/kPkVsvJe\n")), _dafny.SeqOfString("o6gynyWoHrrQuRdmffPvzT50paccJuupeHAtfOAue5y57FQUc4Xm4Qj3P7cQJr9z\n")), _dafny.SeqOfString("UMCUAooEJcdmAUyVUy5BQc7P\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----\n"))
}
func (_static *CompanionStruct_Default___) StaticPublicKeyFromTestVectors() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PUBLIC KEY-----\n"), _dafny.SeqOfString("MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs7RoNYEPAIws89VV+kra\n")), _dafny.SeqOfString("rVv/4wbdmUAaAKWgWuxZi5na9GJSmnhCkqyLRm7wPbQY4LCoa5/IMUxkHLsYDPdu\n")), _dafny.SeqOfString("udY0Qm0GcoxOlvJKHYo4RjF7HyiS34D6dvyO4Gd3aq0mZHoxSGCxW/7hf03wEMzc\n")), _dafny.SeqOfString("iVJXWHXhaI0lD6nrzIEgLrE4L+3V2LeAQjvZsTKd+bYMqeZOL2syiVVIAU8POwAG\n")), _dafny.SeqOfString("GVBroJoveFm/SUp6lCiN0M2kTeyQA2ax3QTtZSAa8nwrI7U52XOzVmdMicJsy2Pg\n")), _dafny.SeqOfString("uW98te3MuODdK24yNkHIkYameP/Umf/SJshUJQd5a/TUp3XE+HhOWAumx22tIDlC\n")), _dafny.SeqOfString("vZS11cuk2fp0WeHUnXaC19N5qWKfvHEKSugzty/z3lGP7ItFhrF2X1qJHeAAsL11\n")), _dafny.SeqOfString("kjo6Lc48KsE1vKvbnW4VLyB3wdNiVvmUNO29tPXwaR0Q5Gbr3jk3nUzdkEHouHWQ\n")), _dafny.SeqOfString("41lubOHCCBN3V13mh/MgtNhESHjfmmOnh54ErD9saA1d7CjTf8g2wqmjEqvGSW6N\n")), _dafny.SeqOfString("q7zhcWR2tp1olflS7oHzul4/I3hnkfL6Kb2xAWWaQKvg3mtsY2OPlzFEP0tR5UcH\n")), _dafny.SeqOfString("Pfp5CeS1Xzg7hN6vRICW6m4l3u2HJFld2akDMm1vnSz8RCbPW7jp7YBxUkWJmypM\n")), _dafny.SeqOfString("tG7Yv2aGZXGbUtM8o1cZarECAwEAAQ==\n")), _dafny.SeqOfString("-----END PUBLIC KEY-----"))
}
func (_static *CompanionStruct_Default___) StaticPrivateKeyFromTestVectors() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCztGg1gQ8AjCzz\n")), _dafny.SeqOfString("1VX6StqtW//jBt2ZQBoApaBa7FmLmdr0YlKaeEKSrItGbvA9tBjgsKhrn8gxTGQc\n")), _dafny.SeqOfString("uxgM92651jRCbQZyjE6W8kodijhGMXsfKJLfgPp2/I7gZ3dqrSZkejFIYLFb/uF/\n")), _dafny.SeqOfString("TfAQzNyJUldYdeFojSUPqevMgSAusTgv7dXYt4BCO9mxMp35tgyp5k4vazKJVUgB\n")), _dafny.SeqOfString("Tw87AAYZUGugmi94Wb9JSnqUKI3QzaRN7JADZrHdBO1lIBryfCsjtTnZc7NWZ0yJ\n")), _dafny.SeqOfString("wmzLY+C5b3y17cy44N0rbjI2QciRhqZ4/9SZ/9ImyFQlB3lr9NSndcT4eE5YC6bH\n")), _dafny.SeqOfString("ba0gOUK9lLXVy6TZ+nRZ4dSddoLX03mpYp+8cQpK6DO3L/PeUY/si0WGsXZfWokd\n")), _dafny.SeqOfString("4ACwvXWSOjotzjwqwTW8q9udbhUvIHfB02JW+ZQ07b209fBpHRDkZuveOTedTN2Q\n")), _dafny.SeqOfString("Qei4dZDjWW5s4cIIE3dXXeaH8yC02ERIeN+aY6eHngSsP2xoDV3sKNN/yDbCqaMS\n")), _dafny.SeqOfString("q8ZJbo2rvOFxZHa2nWiV+VLugfO6Xj8jeGeR8vopvbEBZZpAq+Dea2xjY4+XMUQ/\n")), _dafny.SeqOfString("S1HlRwc9+nkJ5LVfODuE3q9EgJbqbiXe7YckWV3ZqQMybW+dLPxEJs9buOntgHFS\n")), _dafny.SeqOfString("RYmbKky0bti/ZoZlcZtS0zyjVxlqsQIDAQABAoICAEr3m/GWIXgNAkPGX9PGnmtr\n")), _dafny.SeqOfString("0dgX6SIhh7d1YOwNZV3DlYAV9HfUa5Fcwc1kQny7QRWbHOepBI7sW2dQ9buTDXIh\n")), _dafny.SeqOfString("VjPP37yxo6d89EZWfxtpUP+yoXL0D4jL257qCvtJuJZ6E00qaVMDhXbiQKABlo8C\n")), _dafny.SeqOfString("9sVEiABhwXBDZsctpwtTiykTgv6hrrPy2+H8R8MAm0/VcBCAG9kG5r8FCEmIvQKa\n")), _dafny.SeqOfString("dgvNxrfiWNZuZ6yfLmpJH54SbhG9Kb4WbCKfvh4ihqyi0btRdSM6fMeLgG9o/zrc\n")), _dafny.SeqOfString("s54B0kHeLOYNVo0j7FQpZBFeSIbmHfln4RKBh7ntrTke/Ejbh3NbiPvxWSP0P067\n")), _dafny.SeqOfString("SYWPkQpip2q0ION81wSQZ1haP2GewFFu4IEjG3DlqqpKKGLqXrmjMufnildVFpBx\n")), _dafny.SeqOfString("ir+MgvgQfEBoGEx0aElyO7QuRYaEiXeb/BhMZeC5O65YhJrWSuTVizh3xgJWjgfV\n")), _dafny.SeqOfString("aYwYgxN8SBXBhXLIVvnPhadTqsW1C/aevLOk110eSFWcHf+FCK781ykIzcpXoRGX\n")), _dafny.SeqOfString("OwWcZzC/fmSABS0yH56ow+I0tjdLIEEMhoa4/kkamioHOJ4yyB+W1DO6/DnMyQlx\n")), _dafny.SeqOfString("g7y2WsAaIEBoWUARy776k70xPPMtYAxzFXI9KhqRVrPfeaRZ+ojeyLyr3GQGyyoo\n")), _dafny.SeqOfString("cuGRdMUblsmODv4ixmOxAoIBAQDvkznvVYNdP3Eg5vQeLm/qsP6dLejLijBLeq9i\n")), _dafny.SeqOfString("7DZH2gRpKcflXZxCkRjsKDDE+fgDcBYEp2zYfRIVvgrxlTQZdaSG+GoDcbjbNQn3\n")), _dafny.SeqOfString("djCCtOOACioN/vg2zFlX4Bs6Q+NaV7g5qP5SUaxUBjuHLe7Nc+ZkyheMHuNYVLvk\n")), _dafny.SeqOfString("HL/IoWyANpZYjMUU3xMbL/J29Gz7CPGr8Si28TihAHGfcNgn8S04OQZhTX+bU805\n")), _dafny.SeqOfString("/+7B4XW47Mthg/u7hlqFl+YIAaSJYvWkEaVP1A9I7Ve0aMDSMWwzTg9cle2uVaL3\n")), _dafny.SeqOfString("+PTzWY5coBlHKjqAg9ufhYSDhAqBd/JOSlv8RwcA3PDXJ6C/AoIBAQDABmXXYQky\n")), _dafny.SeqOfString("7phExXBvkLtJt2TBGjjwulf4R8TC6W5F51jJuoqY/mTqYcLcOn2nYGVwoFvPsy/Q\n")), _dafny.SeqOfString("CTjfODwJBXzbloXtYFR3PWAeL1Y6+7Cm+koMWIPJyVbD5Fzm+gZStM0GwP8FhDt2\n")), _dafny.SeqOfString("Wt8fWEyXmoLdAy6RAwiEmCagEh8o+13oBfwnBllbz7TxaErsUuR+XVgl/iHwztdv\n")), _dafny.SeqOfString("cdJKyRgaFfWSh9aiO7EMV2rBGWsoX09SRvprPFAGx8Ffm7YcqIk34QXsQyc45Dyn\n")), _dafny.SeqOfString("CwkvypxHoaB3ot/48FeFm9IubApb/ctv+EgkBfL4S4bdwRXS1rt+0+QihBoFyP2o\n")), _dafny.SeqOfString("J91cdm4hEWCPAoIBAQC6l11hFaYZo0bWDGsHcr2B+dZkzxPoKznQH76n+jeQoLIc\n")), _dafny.SeqOfString("wgjJkK4afm39yJOrZtEOxGaxu0CgIFFMk9ZsL/wC9EhvQt02z4TdXiLkFK5VrtMd\n")), _dafny.SeqOfString("r0zv16y06VWQhqBOMf/KJlX6uq9RqADi9HO6pkC+zc0cpPXQEWKaMmygju+kMG2U\n")), _dafny.SeqOfString("Mm/IieMZjWCRJTfgBCE5J88qTsqaKagkZXcZakdAXKwOhQN+F2EStiM6UCZB5PrO\n")), _dafny.SeqOfString("S8dfrO8ML+ki8Zqck8L1qhiNb5zkXtKExy4u+gNr8khGcT6vqqoSxOoH3mPRgOfL\n")), _dafny.SeqOfString("Jnppne8wlwIf7Vq3H8ka6zPSXEHma999gZcmy9t7AoIBAGbQhiLl79j3a0wXMvZp\n")), _dafny.SeqOfString("Vf5IVYgXFDnAbG2hb7a06bhAAIgyexcjzsC4C2+DWdgOgwHkuoPg+062QV8zauGh\n")), _dafny.SeqOfString("sJKaa6cHlvIpSJeg3NjD/nfJN3CYzCd0yCIm2Z9Ka6xI5iYhm+pGPNhIG4Na8deS\n")), _dafny.SeqOfString("gVL46yv1pc/o73VxfoGg5UzgN3xlp97Cva0sHEGguHr4W8Qr59xZw3wGQ4SLW35M\n")), _dafny.SeqOfString("F6qXVNKUh12GSMCPbZK2RXBWVKqqJmca+WzJoJ6DlsT2lQdFhXCus9L007xlDXxF\n")), _dafny.SeqOfString("C/hCmw1dEl+VaNo2Ou26W/zdwTKYhNlxBwsg4SB8nPNxXIsmlBBY54froFhriNfn\n")), _dafny.SeqOfString("x/0CggEAUzz+VMtjoEWw2HSHLOXrO4EmwJniNgiiwfX3DfZE4tMNZgqZwLkq67ns\n")), _dafny.SeqOfString("T0n3b0XfAOOkLgMZrUoOxPHkxFeyLLf7pAEJe7QNB+Qilw8e2zVqtiJrRk6uDIGJ\n")), _dafny.SeqOfString("Sv+yM52zkImZAe2jOdU3KeUZxSMmb5vIoiPBm+tb2WupAg3YdpKn1/jWTpVmV/+G\n")), _dafny.SeqOfString("UtTLVE6YpAyFp1gMxhutE9vfIS94ek+vt03AoEOlltt6hqZfv3xmY8vGuAjlnj12\n")), _dafny.SeqOfString("zHaq+fhCRPsbsZkzJ9nIVdXYnNIEGtMGNnxax7tYRej/UXqyazbxHiJ0iPF4PeDn\n")), _dafny.SeqOfString("dzxtGxpeTBi+KhKlca8SlCdCqYwG6Q==\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) RSA__PUBLIC__2048() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PUBLIC KEY-----\n"), _dafny.SeqOfString("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqBvECLsPdF1J5DOkaA1n\n")), _dafny.SeqOfString("UrGwNT9ard3KSMaPypla/5Jhz0veCz1OSjnx35+FE3q7omHQBmKRs6XDkj4tJ5vh\n")), _dafny.SeqOfString("1baw2yzgIAqW9lOXK64GiYy0maH2NfRxGbj5LhVq5T4YOkKh9D3GFbfT9/NpcsOZ\n")), _dafny.SeqOfString("M2HDX8Z+M0HM3XymtcfpHk5o6QF1lbBW+rDJEcYhPN0obBufCXaasgsBRP5Ei2b5\n")), _dafny.SeqOfString("18xpy9M19By1yuC9mlNcpE5v5A8fq/qLLT4s34/6dnVxKX6gIoWDzDrUNrnPe0p5\n")), _dafny.SeqOfString("pqZ1SHalrELMf/liXPrf94+0cF8g1fYVGGo+MZsG5/HRngLiskP25w5smMT51U1y\n")), _dafny.SeqOfString("gQIDAQAB\n")), _dafny.SeqOfString("-----END PUBLIC KEY-----"))
}
func (_static *CompanionStruct_Default___) RSA__PUBLIC__3072() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PUBLIC KEY-----\n"), _dafny.SeqOfString("MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAnrUonUAKKpZE+LbQfq6I\n")), _dafny.SeqOfString("gAR//GNnT7L6P3LCboXu44StJtvVyAmHZXPgdkxxT1EKLFx+Tys3B7jhgno9cs67\n")), _dafny.SeqOfString("Scf0pLjJAmXOVHa6881oxi5zeP0e6+KzOPugg3C+EknS2PSHTLsdTrkgZU+oUjde\n")), _dafny.SeqOfString("AgRSgmWrp8aMM1WpoLmNcWC/Pi0mSziVnIzE3WhkZ2Ccetz/viRL60VHlTwNQPVa\n")), _dafny.SeqOfString("7fqbcSqBxm/VjDzYvDwzmU+4GNEs5hrA2IFDxxsYZAU8HdASQM18A8W7n0Okaa4e\n")), _dafny.SeqOfString("c4svyKVFkncbNCqetynLU0A5ny7I5WVXV7DNi2VMjD/mZsEt8IrwfuWSMKuIPxs/\n")), _dafny.SeqOfString("Nb/4Psr7ZvbKSlaMwEpyReHvYYqM7dd6A4Y9FirnrpAPaqlfm8UFtHKQvUckxRoR\n")), _dafny.SeqOfString("05kzNN2jIRJtMwGpn+40tiei7eBGMmIn41/dnkM7GOJau4BarSJMiREK1yH9hh1C\n")), _dafny.SeqOfString("GbrQu6i0F9G0uBDITen9/uPX9cxK5pNHAxeWzr2UP1UzAgMBAAE=\n")), _dafny.SeqOfString("-----END PUBLIC KEY-----"))
}
func (_static *CompanionStruct_Default___) RSA__PUBLIC__4096() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PUBLIC KEY-----\n"), _dafny.SeqOfString("MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs86OIUN9RbdEdyQb2tGQ\n")), _dafny.SeqOfString("miDmmeJaYKanLB0lfWiuO85kJK8edZyLkHIzps81qwgVSzbMCBB7QGcMyPbb3wbE\n")), _dafny.SeqOfString("B4EJ32v3cuMVUs6sOvOYV4g1c1Hi1WVqnCeH+3RSFBfb7RL7SvSUmilX2tNV6uZy\n")), _dafny.SeqOfString("BmMSGBJ/IMzxoHjKSFn6r1ttwov8X5DmNTyIp4qG3qyL1qhpla1bUE5Nb6uMHI2v\n")), _dafny.SeqOfString("qMM+8zSPcRN40CfaQATxevNs/69++XJ+5L1nKU9fMwust1GEbtJ6cIBwAuqlyMm9\n")), _dafny.SeqOfString("CnZ+tn56FEVPrUrsQX35QRNjbi0jjKI8ItkdyJ5fLixCjJ20tCo5jeL5KJ32Rjuw\n")), _dafny.SeqOfString("BlB2KQrgdw5VEMrMlTJz9oozUv8GFzjtS4kx+tAsWhji5s0jry4QFYG01Q4ezVPb\n")), _dafny.SeqOfString("TYdxg1Yz265EyLmF0+/ZQtO1kQc7tXHD5Gzzwyqot/UdJwlXStUGB2yEe62HQ2LT\n")), _dafny.SeqOfString("9Ly3V7rUDJzO44zuFVjqchRPYWNdiYl8BVP/ak2bMtcowk06T9bo1tRf4HJWfpIM\n")), _dafny.SeqOfString("GF27MXqykKHxcmOb0UfGIfI0eUtkid4gJdCxhidiILj6SHpEr+oa/Oogz01rVCdm\n")), _dafny.SeqOfString("mbWmgFxmiKse8NXNQR+7qhMYX5GgdeSbp/Lg24HF9mvnd0S2wHkC86lGyQtvzrsd\n")), _dafny.SeqOfString("DdUJZ2jqiKvMLdMKNFHFGGUCAwEAAQ==\n")), _dafny.SeqOfString("-----END PUBLIC KEY-----"))
}

// End of class Default__
