// Package KMSKeystoreOperations
// Dafny module KMSKeystoreOperations compiled into Go

package KMSKeystoreOperations

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/ComAmazonawsDynamodbTypes"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/kms/ComAmazonawsKmsTypes"
	m_AwsArnParsing "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsArnParsing"
	m_AwsCryptographyKeyStoreTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyKeyStoreTypes"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsUtils"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStoreErrorMessages"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/mpl/KmsArn"
	m_Structure "github.com/aws/aws-cryptographic-material-providers-library/mpl/Structure"
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
var _ m_ComAmazonawsDynamodbTypes.Dummy__
var _ m_ComAmazonawsKmsTypes.Dummy__
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
var _ m_AwsCryptographyKeyStoreTypes.Dummy__
var _ m_AwsCryptographyMaterialProvidersTypes.Dummy__
var _ m_AwsArnParsing.Dummy__
var _ m_AwsKmsMrkMatchForDecrypt.Dummy__
var _ m_AwsKmsUtils.Dummy__
var _ m_KeyStoreErrorMessages.Dummy__
var _ m_KmsArn.Dummy__
var _ m_Structure.Dummy__

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
	return "KMSKeystoreOperations.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) ReplaceRegion(arn _dafny.Sequence, region _dafny.Sequence) _dafny.Sequence {
	var _0_parsed m_Wrappers.Result = m_AwsArnParsing.Companion_Default___.ParseAwsKmsArn(arn)
	_ = _0_parsed
	if (_0_parsed).Is_Failure() {
		return arn
	} else if !(m_AwsArnParsing.Companion_Default___.IsMultiRegionAwsKmsArn((_0_parsed).Dtor_value().(m_AwsArnParsing.AwsArn))) {
		return arn
	} else {
		var _1_newArn _dafny.Sequence = ((_0_parsed).Dtor_value().(m_AwsArnParsing.AwsArn)).ToArnString(m_Wrappers.Companion_Option_.Create_Some_(region))
		_ = _1_newArn
		if m_ComAmazonawsKmsTypes.Companion_Default___.IsValid__KeyIdType(_1_newArn) {
			return _1_newArn
		} else {
			return arn
		}
	}
}
func (_static *CompanionStruct_Default___) GetArn(kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration, discoverdArn _dafny.Sequence) _dafny.Sequence {
	var _source0 m_AwsCryptographyKeyStoreTypes.KMSConfiguration = kmsConfiguration
	_ = _source0
	{
		if _source0.Is_kmsKeyArn() {
			var _0_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn).KmsKeyArn
			_ = _0_arn
			return _0_arn
		}
	}
	{
		if _source0.Is_kmsMRKeyArn() {
			var _1_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsMRKeyArn).KmsMRKeyArn
			_ = _1_arn
			return _1_arn
		}
	}
	{
		if _source0.Is_discovery() {
			var _2_obj m_AwsCryptographyKeyStoreTypes.Discovery = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery).Discovery
			_ = _2_obj
			return discoverdArn
		}
	}
	{
		var _3_region m_AwsCryptographyKeyStoreTypes.MRDiscovery = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_mrDiscovery).MrDiscovery
		_ = _3_region
		return Companion_Default___.ReplaceRegion(discoverdArn, (_3_region).Dtor_region())
	}
}
func (_static *CompanionStruct_Default___) AttemptKmsOperation_q(kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration, encryptionContext _dafny.Map) bool {
	var _source0 m_AwsCryptographyKeyStoreTypes.KMSConfiguration = kmsConfiguration
	_ = _source0
	{
		if _source0.Is_kmsKeyArn() {
			var _0_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn).KmsKeyArn
			_ = _0_arn
			return (_dafny.Companion_Sequence_.Equal(_0_arn, (encryptionContext).Get(m_Structure.Companion_Default___.KMS__FIELD()).(_dafny.Sequence))) && (m_KmsArn.Companion_Default___.ValidKmsArn_q(_0_arn))
		}
	}
	{
		if _source0.Is_kmsMRKeyArn() {
			var _1_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsMRKeyArn).KmsMRKeyArn
			_ = _1_arn
			return (Companion_Default___.MrkMatch(_1_arn, (encryptionContext).Get(m_Structure.Companion_Default___.KMS__FIELD()).(_dafny.Sequence))) && (m_KmsArn.Companion_Default___.ValidKmsArn_q(_1_arn))
		}
	}
	{
		if _source0.Is_discovery() {
			var _2_obj m_AwsCryptographyKeyStoreTypes.Discovery = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery).Discovery
			_ = _2_obj
			return m_KmsArn.Companion_Default___.ValidKmsArn_q((encryptionContext).Get(m_Structure.Companion_Default___.KMS__FIELD()).(_dafny.Sequence))
		}
	}
	{
		var _3_obj m_AwsCryptographyKeyStoreTypes.MRDiscovery = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_mrDiscovery).MrDiscovery
		_ = _3_obj
		return m_KmsArn.Companion_Default___.ValidKmsArn_q((encryptionContext).Get(m_Structure.Companion_Default___.KMS__FIELD()).(_dafny.Sequence))
	}
}
func (_static *CompanionStruct_Default___) Compatible_q(kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration, keyId _dafny.Sequence) bool {
	var _source0 m_AwsCryptographyKeyStoreTypes.KMSConfiguration = kmsConfiguration
	_ = _source0
	{
		if _source0.Is_kmsKeyArn() {
			var _0_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn).KmsKeyArn
			_ = _0_arn
			return _dafny.Companion_Sequence_.Equal(_0_arn, keyId)
		}
	}
	{
		var _1_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsMRKeyArn).KmsMRKeyArn
		_ = _1_arn
		return Companion_Default___.MrkMatch(_1_arn, keyId)
	}
}
func (_static *CompanionStruct_Default___) OptCompatible_q(kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration, keyId m_Wrappers.Option) bool {
	return ((keyId).Is_Some()) && (Companion_Default___.Compatible_q(kmsConfiguration, (keyId).Dtor_value().(_dafny.Sequence)))
}
func (_static *CompanionStruct_Default___) MrkMatch(x _dafny.Sequence, y _dafny.Sequence) bool {
	var _0_xArn m_Wrappers.Result = m_AwsArnParsing.Companion_Default___.ParseAwsKmsArn(x)
	_ = _0_xArn
	var _1_yArn m_Wrappers.Result = m_AwsArnParsing.Companion_Default___.ParseAwsKmsArn(y)
	_ = _1_yArn
	if ((_0_xArn).Is_Failure()) || ((_1_yArn).Is_Failure()) {
		return false
	} else {
		return m_AwsKmsMrkMatchForDecrypt.Companion_Default___.AwsKmsMrkMatchForDecrypt(m_AwsArnParsing.Companion_AwsKmsIdentifier_.Create_AwsKmsArnIdentifier_((_0_xArn).Dtor_value().(m_AwsArnParsing.AwsArn)), m_AwsArnParsing.Companion_AwsKmsIdentifier_.Create_AwsKmsArnIdentifier_((_1_yArn).Dtor_value().(m_AwsArnParsing.AwsArn)))
	}
}
func (_static *CompanionStruct_Default___) HasKeyId(kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration) bool {
	return ((kmsConfiguration).Is_kmsKeyArn()) || ((kmsConfiguration).Is_kmsMRKeyArn())
}
func (_static *CompanionStruct_Default___) GetKeyId(kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration) _dafny.Sequence {
	var _source0 m_AwsCryptographyKeyStoreTypes.KMSConfiguration = kmsConfiguration
	_ = _source0
	{
		if _source0.Is_kmsKeyArn() {
			var _0_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn).KmsKeyArn
			_ = _0_arn
			return _0_arn
		}
	}
	{
		var _1_arn _dafny.Sequence = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsMRKeyArn).KmsMRKeyArn
		_ = _1_arn
		return _1_arn
	}
}
func (_static *CompanionStruct_Default___) GenerateKey(encryptionContext _dafny.Map, kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration, grantTokens _dafny.Sequence, kmsClient m_ComAmazonawsKmsTypes.IKMSClient) m_Wrappers.Result {
	var res m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsKmsTypes.Companion_GenerateDataKeyWithoutPlaintextResponse_.Default())
	_ = res
	var _0_kmsKeyArn _dafny.Sequence
	_ = _0_kmsKeyArn
	_0_kmsKeyArn = Companion_Default___.GetKeyId(kmsConfiguration)
	var _1_generatorRequest m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest
	_ = _1_generatorRequest
	_1_generatorRequest = m_ComAmazonawsKmsTypes.Companion_GenerateDataKeyWithoutPlaintextRequest_.Create_GenerateDataKeyWithoutPlaintextRequest_(_0_kmsKeyArn, m_Wrappers.Companion_Option_.Create_Some_(encryptionContext), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(int32(32)), m_Wrappers.Companion_Option_.Create_Some_(grantTokens), m_Wrappers.Companion_Option_.Create_None_())
	var _2_maybeGenerateResponse m_Wrappers.Result
	_ = _2_maybeGenerateResponse
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (kmsClient).GenerateDataKeyWithoutPlaintext(_1_generatorRequest)
	_2_maybeGenerateResponse = _out0
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsKmsTypes.Companion_GenerateDataKeyWithoutPlaintextResponse_.Default())
	_ = _3_valueOrError0
	_3_valueOrError0 = (_2_maybeGenerateResponse).MapFailure(func(coer11 func(m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg11 interface{}) interface{} {
			return coer11(arg11.(m_ComAmazonawsKmsTypes.Error))
		}
	}(func(_4_e m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsKms_(_4_e)
	}))
	if (_3_valueOrError0).IsFailure() {
		res = (_3_valueOrError0).PropagateFailure()
		return res
	}
	var _5_generateResponse m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
	_ = _5_generateResponse
	_5_generateResponse = (_3_valueOrError0).Extract().(m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse)
	var _6_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _6_valueOrError1
	_6_valueOrError1 = m_Wrappers.Companion_Default___.Need((true) && (((_5_generateResponse).Dtor_KeyId()).Is_Some()), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
	if (_6_valueOrError1).IsFailure() {
		res = (_6_valueOrError1).PropagateFailure()
		return res
	}
	var _7_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _7_valueOrError2
	_7_valueOrError2 = m_Wrappers.Companion_Default___.Need((((_5_generateResponse).Dtor_CiphertextBlob()).Is_Some()) && (m_ComAmazonawsKmsTypes.Companion_Default___.IsValid__CiphertextType(((_5_generateResponse).Dtor_CiphertextBlob()).Dtor_value().(_dafny.Sequence))), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")))
	if (_7_valueOrError2).IsFailure() {
		res = (_7_valueOrError2).PropagateFailure()
		return res
	}
	res = m_Wrappers.Companion_Result_.Create_Success_(_5_generateResponse)
	return res
	return res
}
func (_static *CompanionStruct_Default___) ReEncryptKey(ciphertext _dafny.Sequence, sourceEncryptionContext _dafny.Map, destinationEncryptionContext _dafny.Map, kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration, grantTokens _dafny.Sequence, kmsClient m_ComAmazonawsKmsTypes.IKMSClient) m_Wrappers.Result {
	var res m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsKmsTypes.Companion_ReEncryptResponse_.Default())
	_ = res
	var _0_kmsKeyArn _dafny.Sequence
	_ = _0_kmsKeyArn
	_0_kmsKeyArn = Companion_Default___.GetKeyId(kmsConfiguration)
	var _1_reEncryptRequest m_ComAmazonawsKmsTypes.ReEncryptRequest
	_ = _1_reEncryptRequest
	_1_reEncryptRequest = m_ComAmazonawsKmsTypes.Companion_ReEncryptRequest_.Create_ReEncryptRequest_(ciphertext, m_Wrappers.Companion_Option_.Create_Some_(sourceEncryptionContext), m_Wrappers.Companion_Option_.Create_Some_(_0_kmsKeyArn), _0_kmsKeyArn, m_Wrappers.Companion_Option_.Create_Some_(destinationEncryptionContext), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(grantTokens), m_Wrappers.Companion_Option_.Create_None_())
	var _2_maybeReEncryptResponse m_Wrappers.Result
	_ = _2_maybeReEncryptResponse
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (kmsClient).ReEncrypt(_1_reEncryptRequest)
	_2_maybeReEncryptResponse = _out0
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsKmsTypes.Companion_ReEncryptResponse_.Default())
	_ = _3_valueOrError0
	_3_valueOrError0 = (_2_maybeReEncryptResponse).MapFailure(func(coer12 func(m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg12 interface{}) interface{} {
			return coer12(arg12.(m_ComAmazonawsKmsTypes.Error))
		}
	}(func(_4_e m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsKms_(_4_e)
	}))
	if (_3_valueOrError0).IsFailure() {
		res = (_3_valueOrError0).PropagateFailure()
		return res
	}
	var _5_reEncryptResponse m_ComAmazonawsKmsTypes.ReEncryptResponse
	_ = _5_reEncryptResponse
	_5_reEncryptResponse = (_3_valueOrError0).Extract().(m_ComAmazonawsKmsTypes.ReEncryptResponse)
	var _6_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _6_valueOrError1
	_6_valueOrError1 = m_Wrappers.Companion_Default___.Need((((((_5_reEncryptResponse).Dtor_SourceKeyId()).Is_Some()) && (((_5_reEncryptResponse).Dtor_KeyId()).Is_Some())) && (_dafny.Companion_Sequence_.Equal(((_5_reEncryptResponse).Dtor_SourceKeyId()).Dtor_value().(_dafny.Sequence), _0_kmsKeyArn))) && (_dafny.Companion_Sequence_.Equal(((_5_reEncryptResponse).Dtor_KeyId()).Dtor_value().(_dafny.Sequence), _0_kmsKeyArn)), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Invalid response from KMS ReEncrypt:: Invalid Key Id")))
	if (_6_valueOrError1).IsFailure() {
		res = (_6_valueOrError1).PropagateFailure()
		return res
	}
	var _7_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _7_valueOrError2
	_7_valueOrError2 = m_Wrappers.Companion_Default___.Need((((_5_reEncryptResponse).Dtor_CiphertextBlob()).Is_Some()) && (m_ComAmazonawsKmsTypes.Companion_Default___.IsValid__CiphertextType(((_5_reEncryptResponse).Dtor_CiphertextBlob()).Dtor_value().(_dafny.Sequence))), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")))
	if (_7_valueOrError2).IsFailure() {
		res = (_7_valueOrError2).PropagateFailure()
		return res
	}
	res = m_Wrappers.Companion_Result_.Create_Success_(_5_reEncryptResponse)
	return res
	return res
}
func (_static *CompanionStruct_Default___) DecryptKey(encryptionContext _dafny.Map, item _dafny.Map, kmsConfiguration m_AwsCryptographyKeyStoreTypes.KMSConfiguration, grantTokens _dafny.Sequence, kmsClient m_ComAmazonawsKmsTypes.IKMSClient) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsKmsTypes.Companion_DecryptResponse_.Default())
	_ = output
	var _0_kmsKeyArn _dafny.Sequence
	_ = _0_kmsKeyArn
	_0_kmsKeyArn = Companion_Default___.GetArn(kmsConfiguration, (encryptionContext).Get(m_Structure.Companion_Default___.KMS__FIELD()).(_dafny.Sequence))
	var _1_maybeDecryptResponse m_Wrappers.Result
	_ = _1_maybeDecryptResponse
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (kmsClient).Decrypt(m_ComAmazonawsKmsTypes.Companion_DecryptRequest_.Create_DecryptRequest_(((item).Get(m_Structure.Companion_Default___.BRANCH__KEY__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Dtor_B(), m_Wrappers.Companion_Option_.Create_Some_(encryptionContext), m_Wrappers.Companion_Option_.Create_Some_(grantTokens), m_Wrappers.Companion_Option_.Create_Some_(_0_kmsKeyArn), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_1_maybeDecryptResponse = _out0
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsKmsTypes.Companion_DecryptResponse_.Default())
	_ = _2_valueOrError0
	_2_valueOrError0 = (_1_maybeDecryptResponse).MapFailure(func(coer13 func(m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg13 interface{}) interface{} {
			return coer13(arg13.(m_ComAmazonawsKmsTypes.Error))
		}
	}(func(_3_e m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsKms_(_3_e)
	}))
	if (_2_valueOrError0).IsFailure() {
		output = (_2_valueOrError0).PropagateFailure()
		return output
	}
	var _4_decryptResponse m_ComAmazonawsKmsTypes.DecryptResponse
	_ = _4_decryptResponse
	_4_decryptResponse = (_2_valueOrError0).Extract().(m_ComAmazonawsKmsTypes.DecryptResponse)
	var _5_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _5_valueOrError1
	_5_valueOrError1 = m_Wrappers.Companion_Default___.Need((((_4_decryptResponse).Dtor_Plaintext()).Is_Some()) && ((_dafny.IntOfInt64(32)).Cmp(_dafny.IntOfUint32((((_4_decryptResponse).Dtor_Plaintext()).Dtor_value().(_dafny.Sequence)).Cardinality())) == 0), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
	if (_5_valueOrError1).IsFailure() {
		output = (_5_valueOrError1).PropagateFailure()
		return output
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(_4_decryptResponse)
	return output
}

// End of class Default__
