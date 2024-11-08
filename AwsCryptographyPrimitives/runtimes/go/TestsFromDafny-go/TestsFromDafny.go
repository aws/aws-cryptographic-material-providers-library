// Dafny program the_program compiled into Go
package main

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
	m_TestAwsCryptographyPrimitivesAES "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesAES"
	m_TestAwsCryptographyPrimitivesAesKdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesAesKdfCtr"
	m_TestAwsCryptographyPrimitivesDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesDigest"
	m_TestAwsCryptographyPrimitivesGenerateRandomBytes "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesGenerateRandomBytes"
	m_TestAwsCryptographyPrimitivesHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHKDF"
	m_TestAwsCryptographyPrimitivesHMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMAC"
	m_TestAwsCryptographyPrimitivesHMacDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMacDigest"
	m_TestAwsCryptographyPrimitivesRSA "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesRSA"
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
	m_JSON_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_API"
	m_JSON_ConcreteSyntax_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_Spec"
	m_JSON_ConcreteSyntax_SpecProperties "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_SpecProperties"
	m_JSON_Deserializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer"
	m_JSON_Deserializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_ByteStrConversion"
	m_JSON_Deserializer_Uint16StrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_Uint16StrConversion"
	m_JSON_Errors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Errors"
	m_JSON_Grammar "github.com/dafny-lang/DafnyStandardLibGo/JSON_Grammar"
	m_JSON_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer"
	m_JSON_Serializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer_ByteStrConversion"
	m_JSON_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_Spec"
	m_JSON_Utils_Cursors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Cursors"
	m_JSON_Utils_Lexers_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Core"
	m_JSON_Utils_Lexers_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Strings"
	m_JSON_Utils_Parsers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Parsers"
	m_JSON_Utils_Seq "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Seq"
	m_JSON_Utils_Str "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str"
	m_JSON_Utils_Str_CharStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrConversion"
	m_JSON_Utils_Str_CharStrEscaping "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrEscaping"
	m_JSON_Utils_Vectors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Vectors"
	m_JSON_Utils_Views_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Core"
	m_JSON_Utils_Views_Writers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Writers"
	m_JSON_Values "github.com/dafny-lang/DafnyStandardLibGo/JSON_Values"
	m_JSON_ZeroCopy_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_API"
	m_JSON_ZeroCopy_Deserializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer"
	m_JSON_ZeroCopy_Deserializer_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_API"
	m_JSON_ZeroCopy_Deserializer_ArrayParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ArrayParams"
	m_JSON_ZeroCopy_Deserializer_Arrays "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Arrays"
	m_JSON_ZeroCopy_Deserializer_Constants "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Constants"
	m_JSON_ZeroCopy_Deserializer_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Core"
	m_JSON_ZeroCopy_Deserializer_Numbers "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Numbers"
	m_JSON_ZeroCopy_Deserializer_ObjectParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ObjectParams"
	m_JSON_ZeroCopy_Deserializer_Objects "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Objects"
	m_JSON_ZeroCopy_Deserializer_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Strings"
	m_JSON_ZeroCopy_Deserializer_Values "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Values"
	m_JSON_ZeroCopy_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Serializer"
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
var _ m_TestAwsCryptographyPrimitivesRSA.Dummy__
var _ m_TestAwsCryptographyPrimitivesHMAC.Dummy__
var _ m_TestAwsCryptographyPrimitivesAES.Dummy__
var _ m_JSON_Utils_Views_Core.Dummy__
var _ m_JSON_Utils_Views_Writers.Dummy__
var _ m_JSON_Utils_Lexers_Core.Dummy__
var _ m_JSON_Utils_Lexers_Strings.Dummy__
var _ m_JSON_Utils_Cursors.Dummy__
var _ m_JSON_Utils_Parsers.Dummy__
var _ m_JSON_Utils_Str_CharStrConversion.Dummy__
var _ m_JSON_Utils_Str_CharStrEscaping.Dummy__
var _ m_JSON_Utils_Str.Dummy__
var _ m_JSON_Utils_Seq.Dummy__
var _ m_JSON_Utils_Vectors.Dummy__
var _ m_JSON_Errors.Dummy__
var _ m_JSON_Values.Dummy__
var _ m_JSON_Spec.Dummy__
var _ m_JSON_Grammar.Dummy__
var _ m_JSON_Serializer_ByteStrConversion.Dummy__
var _ m_JSON_Serializer.Dummy__
var _ m_JSON_Deserializer_Uint16StrConversion.Dummy__
var _ m_JSON_Deserializer_ByteStrConversion.Dummy__
var _ m_JSON_Deserializer.Dummy__
var _ m_JSON_ConcreteSyntax_Spec.Dummy__
var _ m_JSON_ConcreteSyntax_SpecProperties.Dummy__
var _ m_JSON_ZeroCopy_Serializer.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Core.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Strings.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Numbers.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ObjectParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Objects.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ArrayParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Arrays.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Constants.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Values.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_API.Dummy__
var _ m_JSON_ZeroCopy_Deserializer.Dummy__
var _ m_JSON_ZeroCopy_API.Dummy__
var _ m_JSON_API.Dummy__

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
	return "_module.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Test____Main____(__noArgsParameter _dafny.Sequence) {
	var _0_success bool
	_ = _0_success
	_0_success = true
	_dafny.Print((_dafny.SeqOfString("TestKDFK_TestVectors.ExpectInternalTestVectors: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _1_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_1_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestKDFK__TestVectors.Companion_Default___.ExpectInternalTestVectors()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesHMacDigest.DigestTests: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _2_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_2_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesHMacDigest.Companion_Default___.DigestTests()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestKeyGen: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _3_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_3_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestKeyGen()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestGetPublicKeyFromPrivatePem: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _4_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_4_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestGetPublicKeyFromPrivatePem()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestGetPublicKeyFromPrivateIncorrectCruve: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _5_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_5_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestGetPublicKeyFromPrivateIncorrectCruve()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestValidatePublicKeySuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _6_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_6_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestValidatePublicKeySuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestValidatePublicKeyFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _7_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_7_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestValidatePublicKeyFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestValidatePublicKeyFailurePointAtINFFailOnLoad: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _8_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_8_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestValidatePublicKeyFailurePointAtINFFailOnLoad()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestValidatePublicKeyFailurePointAtINF: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _9_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_9_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestValidatePublicKeyFailurePointAtINF()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _10_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_10_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestValidatePublicKeyFailurePointGreaterThanP: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _11_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_11_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestValidatePublicKeyFailurePointGreaterThanP()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestGenerateSharedSecret: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _12_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_12_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestGenerateSharedSecret()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestCompressDecompressPublicKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _13_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_13_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestCompressDecompressPublicKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestCompressDecompressConstantPublicKeys: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _14_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_14_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestCompressDecompressConstantPublicKeys()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestPublicKeyValidationTestVectorsInfinity: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _15_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_15_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestPublicKeyValidationTestVectorsInfinity()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestECDH.TestPublicKeyValidationTestVectorsOutOfBounds: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _16_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_16_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestECDH.Companion_Default___.TestPublicKeyValidationTestVectorsOutOfBounds()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesHKDF.TestCase1: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _17_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_17_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesHKDF.Companion_Default___.TestCase1()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesGenerateRandomBytes.BasicGenerateRandomBytes: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _18_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_18_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesGenerateRandomBytes.Companion_Default___.BasicGenerateRandomBytes()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesDigest.DigestTests: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _19_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_19_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesDigest.Companion_Default___.DigestTests()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("ConstantTimeTest.ConstantTimeTest: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _20_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_20_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_ConstantTimeTest.Companion_Default___.ConstantTimeTest()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesAesKdfCtr.AesKdfCtrTests: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _21_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_21_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesAesKdfCtr.Companion_Default___.AesKdfCtrTests()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestSignature.YCompression384: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _22_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_22_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestSignature.Companion_Default___.YCompression384()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestSignature.YCompression256: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _23_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_23_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestSignature.Companion_Default___.YCompression256()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestSignature.VerifyMessage384: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _24_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_24_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestSignature.Companion_Default___.VerifyMessage384()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestSignature.VerifyMessage256: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _25_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_25_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestSignature.Companion_Default___.VerifyMessage256()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestHKDF_Rfc5869TestVectors.ExpectRFCTestVectors: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _26_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_26_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestHKDF__Rfc5869TestVectors.Companion_Default___.ExpectRFCTestVectors()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesRSA.RSAEncryptTests: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _27_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_27_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesRSA.Companion_Default___.RSAEncryptTests()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesRSA.GetRSAKeyModulusLength: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _28_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_28_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesRSA.Companion_Default___.GetRSAKeyModulusLength()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _29_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_29_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesRSA.Companion_Default___.TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _30_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_30_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesRSA.Companion_Default___.TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesHMAC.HMACTests: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _31_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_31_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesHMAC.Companion_Default___.HMACTests()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesAES.AESDecryptTests: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _32_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_32_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesAES.Companion_Default___.AESDecryptTests()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsCryptographyPrimitivesAES.AESEncryptTests: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _33_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_33_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsCryptographyPrimitivesAES.Companion_Default___.AESEncryptTests()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	if !(_0_success) {
		panic("<stdin>(1,0): " + (_dafny.SeqOfString("Test failures occurred: see above.\n")).String())
	}
}

// End of class Default__
func main() {
	defer _dafny.CatchHalt()
	Companion_Default___.Test____Main____(_dafny.FromMainArguments(os.Args))
}
