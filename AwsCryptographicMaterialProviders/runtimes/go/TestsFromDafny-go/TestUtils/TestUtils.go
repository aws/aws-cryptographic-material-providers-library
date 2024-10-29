// Package TestUtils
// Dafny module TestUtils compiled into Go

package TestUtils

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/ComAmazonawsDynamodbTypes"
	m_Com_Amazonaws_Dynamodb "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/Com_Amazonaws_Dynamodb"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/kms/ComAmazonawsKmsTypes"
	m_Com_Amazonaws_Kms "github.com/aws/aws-cryptographic-material-providers-library/kms/Com_Amazonaws_Kms"
	m_AlgorithmSuites "github.com/aws/aws-cryptographic-material-providers-library/mpl/AlgorithmSuites"
	m_AwsArnParsing "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsArnParsing"
	m_AwsCryptographyKeyStoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyKeyStoreOperations"
	m_AwsCryptographyKeyStoreTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyKeyStoreTypes"
	m_AwsCryptographyMaterialProvidersOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersOperations"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsDiscoveryKeyring"
	m_AwsKmsEcdhKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsEcdhKeyring"
	m_AwsKmsHierarchicalKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsHierarchicalKeyring"
	m_AwsKmsKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsKeyring"
	m_AwsKmsMrkAreUnique "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkAreUnique"
	m_AwsKmsMrkDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkDiscoveryKeyring"
	m_AwsKmsMrkKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkKeyring"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsRsaKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsRsaKeyring"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsUtils"
	m_CMM "github.com/aws/aws-cryptographic-material-providers-library/mpl/CMM"
	m_CacheConstants "github.com/aws/aws-cryptographic-material-providers-library/mpl/CacheConstants"
	m_CanonicalEncryptionContext "github.com/aws/aws-cryptographic-material-providers-library/mpl/CanonicalEncryptionContext"
	m_Commitment "github.com/aws/aws-cryptographic-material-providers-library/mpl/Commitment"
	m_Constants "github.com/aws/aws-cryptographic-material-providers-library/mpl/Constants"
	m_CreateKeyStoreTable "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeyStoreTable"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/DDBKeystoreOperations"
	m_DefaultCMM "github.com/aws/aws-cryptographic-material-providers-library/mpl/DefaultCMM"
	m_DefaultClientSupplier "github.com/aws/aws-cryptographic-material-providers-library/mpl/DefaultClientSupplier"
	m_Defaults "github.com/aws/aws-cryptographic-material-providers-library/mpl/Defaults"
	m_DiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/DiscoveryMultiKeyring"
	m_EcdhEdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/EcdhEdkWrapping"
	m_EdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/EdkWrapping"
	m_ErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/ErrorMessages"
	m_GetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/GetKeys"
	m_IntermediateKeyWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/IntermediateKeyWrapping"
	m_KMSKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/KMSKeystoreOperations"
	m_KeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStore"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStoreErrorMessages"
	m_Keyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/Keyring"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/mpl/KmsArn"
	m_LocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/LocalCMC"
	m_MaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/mpl/MaterialProviders"
	m_MaterialWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/MaterialWrapping"
	m_Materials "github.com/aws/aws-cryptographic-material-providers-library/mpl/Materials"
	m_MrkAwareDiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MrkAwareDiscoveryMultiKeyring"
	m_MrkAwareStrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MrkAwareStrictMultiKeyring"
	m_MultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MultiKeyring"
	m_RawAESKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/RawAESKeyring"
	m_RawECDHKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/RawECDHKeyring"
	m_RawRSAKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/RawRSAKeyring"
	m_RequiredEncryptionContextCMM "github.com/aws/aws-cryptographic-material-providers-library/mpl/RequiredEncryptionContextCMM"
	m_StormTracker "github.com/aws/aws-cryptographic-material-providers-library/mpl/StormTracker"
	m_StormTrackingCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/StormTrackingCMC"
	m_StrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/StrictMultiKeyring"
	m_Structure "github.com/aws/aws-cryptographic-material-providers-library/mpl/Structure"
	m_SynchronizedLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/SynchronizedLocalCMC"
	m_Utils "github.com/aws/aws-cryptographic-material-providers-library/mpl/Utils"
	m_CleanupItems "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/CleanupItems"
	m_Fixtures "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/Fixtures"
	m_TestConfig "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestConfig"
	m_TestCreateKeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeyStore"
	m_TestCreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeys"
	m_TestDiscoveryGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestDiscoveryGetKeys"
	m_TestErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestErrorMessages"
	m_TestGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestGetKeys"
	m_TestLyingBranchKey "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLyingBranchKey"
	m_TestVersionKey "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestVersionKey"
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
var _ m_ComAmazonawsDynamodbTypes.Dummy__
var _ m_ComAmazonawsKmsTypes.Dummy__
var _ m_AwsCryptographyKeyStoreTypes.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m_Actions.Dummy__
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
var _ m_AwsCryptographyMaterialProvidersTypes.Dummy__
var _ m_AwsArnParsing.Dummy__
var _ m_AwsKmsMrkMatchForDecrypt.Dummy__
var _ m_AwsKmsUtils.Dummy__
var _ m_KeyStoreErrorMessages.Dummy__
var _ m_KmsArn.Dummy__
var _ m_Structure.Dummy__
var _ m_KMSKeystoreOperations.Dummy__
var _ m_DDBKeystoreOperations.Dummy__
var _ m_CreateKeys.Dummy__
var _ m_CreateKeyStoreTable.Dummy__
var _ m_GetKeys.Dummy__
var _ m_AwsCryptographyKeyStoreOperations.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__
var _ m_KeyStore.Dummy__
var _ m_Base64.Dummy__
var _ m_AlgorithmSuites.Dummy__
var _ m_Materials.Dummy__
var _ m_Keyring.Dummy__
var _ m_MultiKeyring.Dummy__
var _ m_AwsKmsMrkAreUnique.Dummy__
var _ m_Constants.Dummy__
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
var _ m_MaterialWrapping.Dummy__
var _ m_CanonicalEncryptionContext.Dummy__
var _ m_IntermediateKeyWrapping.Dummy__
var _ m_EdkWrapping.Dummy__
var _ m_ErrorMessages.Dummy__
var _ m_AwsKmsKeyring.Dummy__
var _ m_StrictMultiKeyring.Dummy__
var _ m_AwsKmsDiscoveryKeyring.Dummy__
var _ m_DiscoveryMultiKeyring.Dummy__
var _ m_AwsKmsMrkDiscoveryKeyring.Dummy__
var _ m_MrkAwareDiscoveryMultiKeyring.Dummy__
var _ m_AwsKmsMrkKeyring.Dummy__
var _ m_MrkAwareStrictMultiKeyring.Dummy__
var _ m_LocalCMC.Dummy__
var _ m_SynchronizedLocalCMC.Dummy__
var _ m_StormTracker.Dummy__
var _ m_StormTrackingCMC.Dummy__
var _ m_CacheConstants.Dummy__
var _ m_AwsKmsHierarchicalKeyring.Dummy__
var _ m_AwsKmsRsaKeyring.Dummy__
var _ m_EcdhEdkWrapping.Dummy__
var _ m_RawECDHKeyring.Dummy__
var _ m_AwsKmsEcdhKeyring.Dummy__
var _ m_RawAESKeyring.Dummy__
var _ m_RawRSAKeyring.Dummy__
var _ m_CMM.Dummy__
var _ m_Defaults.Dummy__
var _ m_Commitment.Dummy__
var _ m_DefaultCMM.Dummy__
var _ m_DefaultClientSupplier.Dummy__
var _ m_Utils.Dummy__
var _ m_RequiredEncryptionContextCMM.Dummy__
var _ m_AwsCryptographyMaterialProvidersOperations.Dummy__
var _ m_MaterialProviders.Dummy__
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
var _ m_Base64Lemmas.Dummy__
var _ m_Fixtures.Dummy__
var _ m_TestGetKeys.Dummy__
var _ m_TestDiscoveryGetKeys.Dummy__
var _ m_CleanupItems.Dummy__
var _ m_TestCreateKeys.Dummy__
var _ m_TestCreateKeyStore.Dummy__
var _ m_TestLyingBranchKey.Dummy__
var _ m_TestVersionKey.Dummy__
var _ m_TestConfig.Dummy__
var _ m_TestErrorMessages.Dummy__

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
	return "TestUtils.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) GenerateInvalidEncryptionContext() _dafny.Map {
	var encCtx _dafny.Map = _dafny.EmptyMap
	_ = encCtx
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UTF8.Encode(_dafny.SeqOfString("a"))
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(115,46): " + (_0_valueOrError0).String())
	}
	var _1_validUTF8char _dafny.Sequence
	_ = _1_validUTF8char
	_1_validUTF8char = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_key _dafny.Sequence
	_ = _2_key
	_2_key = _dafny.SeqOf()
	for (_dafny.IntOfUint32((_2_key).Cardinality())).Cmp(m_StandardLibrary_UInt.Companion_Default___.UINT16__LIMIT()) < 0 {
		_2_key = _dafny.Companion_Sequence_.Concatenate(_2_key, _1_validUTF8char)
	}
	encCtx = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_2_key, _dafny.SeqOf(uint8(0)))
	return encCtx
}
func (_static *CompanionStruct_Default___) GenerateLargeValidEncryptionContext() _dafny.Map {
	var r _dafny.Map = _dafny.EmptyMap
	_ = r
	var _0_numMaxPairs _dafny.Int
	_ = _0_numMaxPairs
	_0_numMaxPairs = _dafny.IntOfInt64(9361)
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_UTF8.Encode(_dafny.SeqOfString("a"))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(135,15): " + (_1_valueOrError0).String())
	}
	var _2_val _dafny.Sequence
	_ = _2_val
	_2_val = (_1_valueOrError0).Extract().(_dafny.Sequence)
	var _3_encCtx _dafny.Map
	_ = _3_encCtx
	_3_encCtx = _dafny.NewMapBuilder().ToMap()
	var _4_i _dafny.Int
	_ = _4_i
	_4_i = _dafny.Zero
	for (((_3_encCtx).Cardinality()).Cmp(_0_numMaxPairs) < 0) && ((_4_i).Cmp(_dafny.IntOfInt64(65536)) < 0) {
		var _5_key _dafny.Sequence
		_ = _5_key
		_5_key = m_StandardLibrary_UInt.Companion_Default___.UInt16ToSeq((_4_i).Uint16())
		if m_UTF8.Companion_Default___.ValidUTF8Seq(_5_key) {
			_3_encCtx = (_3_encCtx).Update(_5_key, _2_val)
		}
		_4_i = (_4_i).Plus(_dafny.One)
	}
	r = _3_encCtx
	return r
	return r
}
func (_static *CompanionStruct_Default___) SmallEncryptionContext(v SmallEncryptionContextVariation) _dafny.Map {
	var encryptionContext _dafny.Map = _dafny.EmptyMap
	_ = encryptionContext
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UTF8.Encode(_dafny.SeqOfString("keyA"))
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(163,16): " + (_0_valueOrError0).String())
	}
	var _1_keyA _dafny.Sequence
	_ = _1_keyA
	_1_keyA = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UTF8.Encode(_dafny.SeqOfString("valA"))
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(164,16): " + (_2_valueOrError1).String())
	}
	var _3_valA _dafny.Sequence
	_ = _3_valA
	_3_valA = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _4_valueOrError2
	_4_valueOrError2 = m_UTF8.Encode(_dafny.SeqOfString("keyB"))
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(165,16): " + (_4_valueOrError2).String())
	}
	var _5_keyB _dafny.Sequence
	_ = _5_keyB
	_5_keyB = (_4_valueOrError2).Extract().(_dafny.Sequence)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _6_valueOrError3
	_6_valueOrError3 = m_UTF8.Encode(_dafny.SeqOfString("valB"))
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(166,16): " + (_6_valueOrError3).String())
	}
	var _7_valB _dafny.Sequence
	_ = _7_valB
	_7_valB = (_6_valueOrError3).Extract().(_dafny.Sequence)
	var _source0 SmallEncryptionContextVariation = v
	_ = _source0
	{
		{
			if _source0.Is_Empty() {
				encryptionContext = _dafny.NewMapBuilder().ToMap()
				goto Lmatch0
			}
		}
		{
			if _source0.Is_A() {
				encryptionContext = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_1_keyA, _3_valA)
				goto Lmatch0
			}
		}
		{
			if _source0.Is_AB() {
				encryptionContext = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_1_keyA, _3_valA).UpdateUnsafe(_5_keyB, _7_valB)
				goto Lmatch0
			}
		}
		{
			encryptionContext = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_5_keyB, _7_valB).UpdateUnsafe(_1_keyA, _3_valA)
		}
		goto Lmatch0
	}
Lmatch0:
	return encryptionContext
}
func (_static *CompanionStruct_Default___) GenerateMockEncryptedDataKey(keyProviderId _dafny.Sequence, keyProviderInfo _dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey {
	var edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptedDataKey_.Default()
	_ = edk
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UTF8.Encode(keyProviderId)
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(186,32): " + (_0_valueOrError0).String())
	}
	var _1_encodedkeyProviderId _dafny.Sequence
	_ = _1_encodedkeyProviderId
	_1_encodedkeyProviderId = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UTF8.Encode(keyProviderInfo)
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(187,34): " + (_2_valueOrError1).String())
	}
	var _3_encodedKeyProviderInfo _dafny.Sequence
	_ = _3_encodedKeyProviderInfo
	_3_encodedKeyProviderInfo = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _4_valueOrError2
	_4_valueOrError2 = m_UTF8.Encode(_dafny.SeqOfString("fakeCiphertext"))
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(188,26): " + (_4_valueOrError2).String())
	}
	var _5_fakeCiphertext _dafny.Sequence
	_ = _5_fakeCiphertext
	_5_fakeCiphertext = (_4_valueOrError2).Extract().(_dafny.Sequence)
	edk = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptedDataKey_.Create_EncryptedDataKey_(_1_encodedkeyProviderId, _3_encodedKeyProviderInfo, _5_fakeCiphertext)
	return edk
	return edk
}
func (_static *CompanionStruct_Default___) NamespaceAndName(n _dafny.Int) (_dafny.Sequence, _dafny.Sequence) {
	var namespace _dafny.Sequence = _dafny.EmptySeq.SetString()
	_ = namespace
	var name _dafny.Sequence = _dafny.EmptySeq.SetString()
	_ = name
	var _0_s _dafny.Sequence
	_ = _0_s
	_0_s = _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("child"), _dafny.SeqOfChars((_dafny.Char((n).Int32()))+(_dafny.Char('0'))))
	namespace = _dafny.Companion_Sequence_.Concatenate(_0_s, _dafny.SeqOfString(" Namespace"))
	name = _dafny.Companion_Sequence_.Concatenate(_0_s, _dafny.SeqOfString(" Name"))
	return namespace, name
}
func (_static *CompanionStruct_Default___) KMS__RSA__PUBLIC__KEY() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PUBLIC KEY-----\n"), _dafny.SeqOfString("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA27Uc/fBaMVhxCE/SpCMQ\n")), _dafny.SeqOfString("oSBRSzQJw+o2hBaA+FiPGtiJ/aPy7sn18aCkelaSj4kwoC79b/arNHlkjc7OJFsN\n")), _dafny.SeqOfString("/GoFKgNvaiY4lOeJqEiWQGSSgHtsJLdbO2u4OOSxh8qIRAMKbMgQDVX4FR/PLKeK\n")), _dafny.SeqOfString("fc2aCDvcNSpAM++8NlNmv7+xQBJydr5ce91eISbHkFRkK3/bAM+1iddupoRw4Wo2\n")), _dafny.SeqOfString("r3avzrg5xBHmzR7u1FTab22Op3Hgb2dBLZH43wNKAceVwKqKA8UNAxashFON7xK9\n")), _dafny.SeqOfString("yy4kfOL0Z/nhxRKe4jRZ/5v508qIzgzCksYy7Y3QbMejAtiYnr7s5/d5KWw0swou\n")), _dafny.SeqOfString("twIDAQAB\n")), _dafny.SeqOfString("-----END PUBLIC KEY-----"))
}
func (_static *CompanionStruct_Default___) KMS__RSA__PRIVATE__KEY__ARN() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297")
}
func (_static *CompanionStruct_Default___) SHARED__TEST__KEY__ARN() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
}
func (_static *CompanionStruct_Default___) ACCOUNT__IDS() _dafny.Sequence {
	return _dafny.SeqOf(_dafny.SeqOfString("658956600833"))
}
func (_static *CompanionStruct_Default___) PARTITION() _dafny.Sequence {
	return _dafny.SeqOfString("aws")
}
func (_static *CompanionStruct_Default___) KMS__ECC__256__KEY__ARN__S() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9")
}
func (_static *CompanionStruct_Default___) KMS__ECC__256__KEY__ARN__R() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5")
}
func (_static *CompanionStruct_Default___) KMS__ECC__384__KEY__ARN__S() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/7f35a704-f4fb-469d-98b1-62a1fa2cc44e")
}
func (_static *CompanionStruct_Default___) KMS__ECC__384__KEY__ARN__R() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/29f0bef9-1677-4e74-b67e-acefab1295ff")
}
func (_static *CompanionStruct_Default___) KMS__ECC__521__KEY__ARN__S() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/41b502e3-cc9d-442f-bd7b-d67faed0f22e")
}
func (_static *CompanionStruct_Default___) KMS__ECC__521__KEY__ARN__R() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/c45f1043-53bb-4f37-adc5-4d25d4a84f9d")
}
func (_static *CompanionStruct_Default___) KMS__ECC__256__PUBLIC__KEY__S() _dafny.Sequence {
	return _dafny.SeqOfString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE18m54QsLUnhWU7gT8hkAceNbZ/WBGNUUSPCeIKqOyX5psiqyC1TXPOJXqKKaVv5Mg91WV9UjpboblOhNU35nRw==")
}
func (_static *CompanionStruct_Default___) KMS__ECC__256__PUBLIC__KEY__R() _dafny.Sequence {
	return _dafny.SeqOfString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9istdPCuX9nF8EmA4tioe/k0TCa2M9VeBW1N9n0sxPA6uPVOfLtE4+KuYxAGT0dYoK6CY93nowUy1yS+R7A+wA==")
}
func (_static *CompanionStruct_Default___) KMS__ECC__384__PUBLIC__KEY__S() _dafny.Sequence {
	return _dafny.SeqOfString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEfQ0OHFvwskFVjQwfqV7jpo62I6uyGY+5SPRZb6CuJ96bVreLZXh485BcPv09O/DWnpTBm8LL+YcfsqM3ECvi2ee3bDGpH6xIdr28uvyG75t5wqBjYYtZQFDf/ydfG9mm")
}
func (_static *CompanionStruct_Default___) KMS__ECC__384__PUBLIC__KEY__R() _dafny.Sequence {
	return _dafny.SeqOfString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEWgGNWQ+vEwlMxyMQkSsOAYGfT6IlgEkcanEOSjbeEpEnh8JHEiBHQ6QaROxJ7c3nEkbjbi0m+7ejBEGtkiqaY5Dsv5u1iV4fc/2v1RzPba1ZtudEmM16Eyy9LHswdJ7v")
}
func (_static *CompanionStruct_Default___) KMS__ECC__521__PUBLIC__KEY__S() _dafny.Sequence {
	return _dafny.SeqOfString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAz86qnfp3s0cl+73PQhlUstfdg9EZDA/jtLjBTWYp/1EB7RHNm8q5hMg5kBfjRDUFhbRBMlUV1xBOTgqzoSWj4oAABnQKiXXGGyu6PMN4D9nVMDsOpJ1pWU7rQexWDahBrK+5hx3beFXUpvvFRQrGAt2icUXm18VO6Qwbp0da9jyGDSY=")
}
func (_static *CompanionStruct_Default___) KMS__ECC__521__PUBLIC__KEY__R() _dafny.Sequence {
	return _dafny.SeqOfString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAxLxcjtYfqc4+4oJZY0gGv2Ehu++CnVFea6uwXgEgLifq4eDSSVmQYvU8majsufpBXQwVjnDlQ7pGRw1j6K4FaLAAgYuMrmrwKtx/ZZtkbXzCwrqJY+sfCk8U5m89DX331cdBAhR2uVSPL2d5hp8up5v+EBpNArtdC5lZMx2ZrwKKYuQ=")
}
func (_static *CompanionStruct_Default___) ECC__P256__PRIVATE() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n")), _dafny.SeqOfString("22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n")), _dafny.SeqOfString("7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) ECC__P256__PUBLIC() _dafny.Sequence {
	return _dafny.SeqOfString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEp1IMe0q5R4TyJ9zHGX3N3BCLPPlxX+yb4XLldcFhCxmfAI7sJyoxNInpRMEmOR2M1ghe+9xbyWlhmBmBoUm2vA==")
}
func (_static *CompanionStruct_Default___) ECC__P256__PRIVATE__R() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgxpnoWJBwDUkwvLHA\n")), _dafny.SeqOfString("YZgRRby9FdJtxAMvAcPPW6iaD+2hRANCAASihMmHeVwzccmYmFKPO5rlR+M3MBRH\n")), _dafny.SeqOfString("zdCaw8TGxfX25tCKkhQUm6kUlPqaCzirEYPbUt3wK8XJ6jF5iRzuGxad\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----\n"))
}
func (_static *CompanionStruct_Default___) ECC__P256__PUBLIC__R() _dafny.Sequence {
	return _dafny.SeqOfString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEooTJh3lcM3HJmJhSjzua5UfjNzAUR83QmsPExsX19ubQipIUFJupFJT6mgs4qxGD21Ld8CvFyeoxeYkc7hsWnQ==")
}
func (_static *CompanionStruct_Default___) ECC__P384__PRIVATE() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n")), _dafny.SeqOfString("6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n")), _dafny.SeqOfString("GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n")), _dafny.SeqOfString("b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) ECC__P384__PUBLIC() _dafny.Sequence {
	return _dafny.SeqOfString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEGsj1ugd2lRilhQWwx90nrjIYmNhiDxvrQRB5jGd0FGhuqjZ0MV0vkKUfeSFskFmYyJ8g5NrqXm9U4rz9FGGsvnSEvDKwRTO6CwbCSKsRokUNRDxSKQS7+JprXjpmuarf")
}
func (_static *CompanionStruct_Default___) ECC__P384__PRIVATE__R() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDBX0BpijAta/CndWCkA\n")), _dafny.SeqOfString("hl4fu2mIlnsh8umliaBBDHjA2T/3eeYWid5m96Bs2QxYIn6hZANiAAR/qhoNylqV\n")), _dafny.SeqOfString("2084hlZEXr8XWj9DuZ0WHgJ/rniicwqxXEFwPCkeh7VvpO7+tN8HxUoWpPLSdkCK\n")), _dafny.SeqOfString("nWeq6senikNb4RNp3Na43wPyF2SjQI/uzujHjlrVrea2zvJP7rsLdAI=\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----\n"))
}
func (_static *CompanionStruct_Default___) ECC__P384__PUBLIC__R() _dafny.Sequence {
	return _dafny.SeqOfString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEf6oaDcpaldtPOIZWRF6/F1o/Q7mdFh4Cf654onMKsVxBcDwpHoe1b6Tu/rTfB8VKFqTy0nZAip1nqurHp4pDW+ETadzWuN8D8hdko0CP7s7ox45a1a3mts7yT+67C3QC")
}
func (_static *CompanionStruct_Default___) ECC__P521__PRIVATE() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n")), _dafny.SeqOfString("xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n")), _dafny.SeqOfString("oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n")), _dafny.SeqOfString("I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n")), _dafny.SeqOfString("C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n")), _dafny.SeqOfString("Qg==\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) ECC__P521__PUBLIC() _dafny.Sequence {
	return _dafny.SeqOfString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQB3jJzJGnYdp5HrVE3A7yhOFgnHU3SBSmg6sLTCG6v8uTeBCO+zsWMCj+yHRgQvZ/xpHDSFsekfdc3NwCHfWu1azkBffh4rZ25Qci9btzepFoVHwt7q8tdU/HZDVvi21ZJl/Ad/rOlWhEFimvkmAXpj1dOWiYVNMWmhfzIbCxsCi6T6UI=")
}
func (_static *CompanionStruct_Default___) ECC__P521__PRIVATE__R() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-----BEGIN PRIVATE KEY-----\n"), _dafny.SeqOfString("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIAGQrViOzSEfLFHdlp\n")), _dafny.SeqOfString("rFcl/iWrPt7vWyga71fnLOzj4nTWBJ/Pua+xOVfTGjgplH4t16sRl4qk113Zv8zY\n")), _dafny.SeqOfString("XfgTJvChgYkDgYYABACKN7raKlNTwzxw97HarkQB7+9cTvw1grfhwW6AkUIS8b6J\n")), _dafny.SeqOfString("7CgTTSKZ6M5XQ0leYOZMkqXgjlpUfki4G3XXa4hw0wBUw+x9qtoAlwJNYhUsYg7N\n")), _dafny.SeqOfString("bm7IF9TQSuAzWgrSfIjOJfjrHjBR0TLmtk26xxKZIw36JSl9qb9b8LqlLk8uW6eE\n")), _dafny.SeqOfString("Lw==\n")), _dafny.SeqOfString("-----END PRIVATE KEY-----"))
}
func (_static *CompanionStruct_Default___) ECC__P521__PUBLIC__R() _dafny.Sequence {
	return _dafny.SeqOfString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAije62ipTU8M8cPex2q5EAe/vXE78NYK34cFugJFCEvG+iewoE00imejOV0NJXmDmTJKl4I5aVH5IuBt112uIcNMAVMPsfaraAJcCTWIVLGIOzW5uyBfU0ErgM1oK0nyIziX46x4wUdEy5rZNuscSmSMN+iUpfam/W/C6pS5PLlunhC8=")
}

// End of class Default__

// Definition of datatype SmallEncryptionContextVariation
type SmallEncryptionContextVariation struct {
	Data_SmallEncryptionContextVariation_
}

func (_this SmallEncryptionContextVariation) Get_() Data_SmallEncryptionContextVariation_ {
	return _this.Data_SmallEncryptionContextVariation_
}

type Data_SmallEncryptionContextVariation_ interface {
	isSmallEncryptionContextVariation()
}

type CompanionStruct_SmallEncryptionContextVariation_ struct {
}

var Companion_SmallEncryptionContextVariation_ = CompanionStruct_SmallEncryptionContextVariation_{}

type SmallEncryptionContextVariation_Empty struct {
}

func (SmallEncryptionContextVariation_Empty) isSmallEncryptionContextVariation() {}

func (CompanionStruct_SmallEncryptionContextVariation_) Create_Empty_() SmallEncryptionContextVariation {
	return SmallEncryptionContextVariation{SmallEncryptionContextVariation_Empty{}}
}

func (_this SmallEncryptionContextVariation) Is_Empty() bool {
	_, ok := _this.Get_().(SmallEncryptionContextVariation_Empty)
	return ok
}

type SmallEncryptionContextVariation_A struct {
}

func (SmallEncryptionContextVariation_A) isSmallEncryptionContextVariation() {}

func (CompanionStruct_SmallEncryptionContextVariation_) Create_A_() SmallEncryptionContextVariation {
	return SmallEncryptionContextVariation{SmallEncryptionContextVariation_A{}}
}

func (_this SmallEncryptionContextVariation) Is_A() bool {
	_, ok := _this.Get_().(SmallEncryptionContextVariation_A)
	return ok
}

type SmallEncryptionContextVariation_AB struct {
}

func (SmallEncryptionContextVariation_AB) isSmallEncryptionContextVariation() {}

func (CompanionStruct_SmallEncryptionContextVariation_) Create_AB_() SmallEncryptionContextVariation {
	return SmallEncryptionContextVariation{SmallEncryptionContextVariation_AB{}}
}

func (_this SmallEncryptionContextVariation) Is_AB() bool {
	_, ok := _this.Get_().(SmallEncryptionContextVariation_AB)
	return ok
}

type SmallEncryptionContextVariation_BA struct {
}

func (SmallEncryptionContextVariation_BA) isSmallEncryptionContextVariation() {}

func (CompanionStruct_SmallEncryptionContextVariation_) Create_BA_() SmallEncryptionContextVariation {
	return SmallEncryptionContextVariation{SmallEncryptionContextVariation_BA{}}
}

func (_this SmallEncryptionContextVariation) Is_BA() bool {
	_, ok := _this.Get_().(SmallEncryptionContextVariation_BA)
	return ok
}

func (CompanionStruct_SmallEncryptionContextVariation_) Default() SmallEncryptionContextVariation {
	return Companion_SmallEncryptionContextVariation_.Create_Empty_()
}

func (_ CompanionStruct_SmallEncryptionContextVariation_) AllSingletonConstructors() _dafny.Iterator {
	i := -1
	return func() (interface{}, bool) {
		i++
		switch i {
		case 0:
			return Companion_SmallEncryptionContextVariation_.Create_Empty_(), true
		case 1:
			return Companion_SmallEncryptionContextVariation_.Create_A_(), true
		case 2:
			return Companion_SmallEncryptionContextVariation_.Create_AB_(), true
		case 3:
			return Companion_SmallEncryptionContextVariation_.Create_BA_(), true
		default:
			return SmallEncryptionContextVariation{}, false
		}
	}
}

func (_this SmallEncryptionContextVariation) String() string {
	switch _this.Get_().(type) {
	case nil:
		return "null"
	case SmallEncryptionContextVariation_Empty:
		{
			return "TestUtils.SmallEncryptionContextVariation.Empty"
		}
	case SmallEncryptionContextVariation_A:
		{
			return "TestUtils.SmallEncryptionContextVariation.A"
		}
	case SmallEncryptionContextVariation_AB:
		{
			return "TestUtils.SmallEncryptionContextVariation.AB"
		}
	case SmallEncryptionContextVariation_BA:
		{
			return "TestUtils.SmallEncryptionContextVariation.BA"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this SmallEncryptionContextVariation) Equals(other SmallEncryptionContextVariation) bool {
	switch _this.Get_().(type) {
	case SmallEncryptionContextVariation_Empty:
		{
			_, ok := other.Get_().(SmallEncryptionContextVariation_Empty)
			return ok
		}
	case SmallEncryptionContextVariation_A:
		{
			_, ok := other.Get_().(SmallEncryptionContextVariation_A)
			return ok
		}
	case SmallEncryptionContextVariation_AB:
		{
			_, ok := other.Get_().(SmallEncryptionContextVariation_AB)
			return ok
		}
	case SmallEncryptionContextVariation_BA:
		{
			_, ok := other.Get_().(SmallEncryptionContextVariation_BA)
			return ok
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this SmallEncryptionContextVariation) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(SmallEncryptionContextVariation)
	return ok && _this.Equals(typed)
}

func Type_SmallEncryptionContextVariation_() _dafny.TypeDescriptor {
	return type_SmallEncryptionContextVariation_{}
}

type type_SmallEncryptionContextVariation_ struct {
}

func (_this type_SmallEncryptionContextVariation_) Default() interface{} {
	return Companion_SmallEncryptionContextVariation_.Default()
}

func (_this type_SmallEncryptionContextVariation_) String() string {
	return "TestUtils.SmallEncryptionContextVariation"
}
func (_this SmallEncryptionContextVariation) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = SmallEncryptionContextVariation{}

// End of datatype SmallEncryptionContextVariation
