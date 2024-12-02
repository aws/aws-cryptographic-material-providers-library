// Package TestStormTracker
// Dafny module TestStormTracker compiled into Go

package TestStormTracker

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
	m_TestUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestUtils"
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
var _ m_TestUtils.Dummy__

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
	return "TestStormTracker.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) MakeMat(data _dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Materials {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_Materials_.Create_BranchKey_(m_AwsCryptographyKeyStoreTypes.Companion_BranchKeyMaterials_.Create_BranchKeyMaterials_(_dafny.SeqOfString("spoo"), data, _dafny.NewMapBuilder().ToMap(), data))
}
func (_static *CompanionStruct_Default___) MakeGet(data _dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_GetCacheEntryInput_.Create_GetCacheEntryInput_(data, m_Wrappers.Companion_Option_.Create_None_())
}
func (_static *CompanionStruct_Default___) MakeDel(data _dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_DeleteCacheEntryInput_.Create_DeleteCacheEntryInput_(data)
}
func (_static *CompanionStruct_Default___) MakePut(data _dafny.Sequence, expiryTime int64) m_AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_PutCacheEntryInput_.Create_PutCacheEntryInput_(data, Companion_Default___.MakeMat(data), int64(123456789), expiryTime, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
}
func (_static *CompanionStruct_Default___) StormTrackerBasics() {
	var _0_st *m_StormTracker.StormTracker
	_ = _0_st
	var _nw0 *m_StormTracker.StormTracker = m_StormTracker.New_StormTracker_()
	_ = _nw0
	_nw0.Ctor__(m_StormTracker.Companion_Default___.DefaultStorm())
	_0_st = _nw0
	var _1_abc _dafny.Sequence
	_ = _1_abc
	_1_abc = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("abc"))
	var _2_cde _dafny.Sequence
	_ = _2_cde
	_2_cde = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("cde"))
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _3_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_1_abc), int64(10000))
	_3_valueOrError0 = _out0
	if !(!((_3_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(55,15): " + (_3_valueOrError0).String())
	}
	var _4_res m_StormTracker.CacheState
	_ = _4_res
	_4_res = (_3_valueOrError0).Extract().(m_StormTracker.CacheState)
	if !((_4_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(56,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _5_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_1_abc), int64(10000))
	_5_valueOrError1 = _out1
	if !(!((_5_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(57,11): " + (_5_valueOrError1).String())
	}
	_4_res = (_5_valueOrError1).Extract().(m_StormTracker.CacheState)
	if !((_4_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(58,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_0_st).PutCacheEntry(Companion_Default___.MakePut(_1_abc, int64(10000)))
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(59,16): " + (_6_valueOrError2).String())
	}
	var _7_res2 _dafny.Tuple
	_ = _7_res2
	_7_res2 = (_6_valueOrError2).Extract().(_dafny.Tuple)
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _8_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_0_st).PutCacheEntry(Companion_Default___.MakePut(_2_cde, int64(10000)))
	_8_valueOrError3 = _out3
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(60,12): " + (_8_valueOrError3).String())
	}
	_7_res2 = (_8_valueOrError3).Extract().(_dafny.Tuple)
	var _9_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _9_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_1_abc), int64(10001))
	_9_valueOrError4 = _out4
	if !(!((_9_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(61,11): " + (_9_valueOrError4).String())
	}
	_4_res = (_9_valueOrError4).Extract().(m_StormTracker.CacheState)
	if !((_4_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(62,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _10_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_1_abc), int64(10001))
	_10_valueOrError5 = _out5
	if !(!((_10_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(63,11): " + (_10_valueOrError5).String())
	}
	_4_res = (_10_valueOrError5).Extract().(m_StormTracker.CacheState)
	if !((_4_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(64,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _11_res3 m_Wrappers.Result
	_ = _11_res3
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_0_st).GetCacheEntry(Companion_Default___.MakeGet(_1_abc))
	_11_res3 = _out6
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_0_st).GetCacheEntry(Companion_Default___.MakeGet(_1_abc))
	_11_res3 = _out7
	var _12_res4 m_Wrappers.Result
	_ = _12_res4
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_0_st).GetFromCache(Companion_Default___.MakeGet(_1_abc))
	_12_res4 = _out8
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_0_st).GetFromCache(Companion_Default___.MakeGet(_1_abc))
	_12_res4 = _out9
	var _13_res5 m_Wrappers.Result
	_ = _13_res5
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_0_st).DeleteCacheEntry(Companion_Default___.MakeDel(_1_abc))
	_13_res5 = _out10
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_0_st).DeleteCacheEntry(Companion_Default___.MakeDel(_1_abc))
	_13_res5 = _out11
}
func (_static *CompanionStruct_Default___) StormTrackerFanOut() {
	var _0_st *m_StormTracker.StormTracker
	_ = _0_st
	var _nw0 *m_StormTracker.StormTracker = m_StormTracker.New_StormTracker_()
	_ = _nw0
	_nw0.Ctor__(func(_pat_let2_0 m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
		return func(_1_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
			return func(_pat_let3_0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
				return func(_2_dt__update_hfanOut_h0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
					return m_AwsCryptographyMaterialProvidersTypes.Companion_StormTrackingCache_.Create_StormTrackingCache_((_1_dt__update__tmp_h0).Dtor_entryCapacity(), (_1_dt__update__tmp_h0).Dtor_entryPruningTailSize(), (_1_dt__update__tmp_h0).Dtor_gracePeriod(), (_1_dt__update__tmp_h0).Dtor_graceInterval(), _2_dt__update_hfanOut_h0, (_1_dt__update__tmp_h0).Dtor_inFlightTTL(), (_1_dt__update__tmp_h0).Dtor_sleepMilli())
				}(_pat_let3_0)
			}(int32(3))
		}(_pat_let2_0)
	}(m_StormTracker.Companion_Default___.DefaultStorm()))
	_0_st = _nw0
	var _3_one _dafny.Sequence
	_ = _3_one
	_3_one = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("one"))
	var _4_two _dafny.Sequence
	_ = _4_two
	_4_two = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("two"))
	var _5_three _dafny.Sequence
	_ = _5_three
	_5_three = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("three"))
	var _6_four _dafny.Sequence
	_ = _6_four
	_6_four = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("four"))
	var _7_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _7_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_3_one), int64(10000))
	_7_valueOrError0 = _out0
	if !(!((_7_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(84,15): " + (_7_valueOrError0).String())
	}
	var _8_res m_StormTracker.CacheState
	_ = _8_res
	_8_res = (_7_valueOrError0).Extract().(m_StormTracker.CacheState)
	if !((_8_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(85,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _9_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _9_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_4_two), int64(10000))
	_9_valueOrError1 = _out1
	if !(!((_9_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(86,11): " + (_9_valueOrError1).String())
	}
	_8_res = (_9_valueOrError1).Extract().(m_StormTracker.CacheState)
	if !((_8_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(87,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _10_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_5_three), int64(10000))
	_10_valueOrError2 = _out2
	if !(!((_10_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(88,11): " + (_10_valueOrError2).String())
	}
	_8_res = (_10_valueOrError2).Extract().(m_StormTracker.CacheState)
	if !((_8_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(89,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _11_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _11_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_6_four), int64(10000))
	_11_valueOrError3 = _out3
	if !(!((_11_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(90,11): " + (_11_valueOrError3).String())
	}
	_8_res = (_11_valueOrError3).Extract().(m_StormTracker.CacheState)
	if !((_8_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(91,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) StormTrackerTTL() {
	var _0_st *m_StormTracker.StormTracker
	_ = _0_st
	var _nw0 *m_StormTracker.StormTracker = m_StormTracker.New_StormTracker_()
	_ = _nw0
	_nw0.Ctor__(func(_pat_let4_0 m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
		return func(_1_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
			return func(_pat_let5_0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
				return func(_2_dt__update_hinFlightTTL_h0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
					return func(_pat_let6_0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
						return func(_3_dt__update_hfanOut_h0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
							return m_AwsCryptographyMaterialProvidersTypes.Companion_StormTrackingCache_.Create_StormTrackingCache_((_1_dt__update__tmp_h0).Dtor_entryCapacity(), (_1_dt__update__tmp_h0).Dtor_entryPruningTailSize(), (_1_dt__update__tmp_h0).Dtor_gracePeriod(), (_1_dt__update__tmp_h0).Dtor_graceInterval(), _3_dt__update_hfanOut_h0, _2_dt__update_hinFlightTTL_h0, (_1_dt__update__tmp_h0).Dtor_sleepMilli())
						}(_pat_let6_0)
					}(int32(3))
				}(_pat_let5_0)
			}(int32(5))
		}(_pat_let4_0)
	}(m_StormTracker.Companion_Default___.DefaultStorm()))
	_0_st = _nw0
	var _4_one _dafny.Sequence
	_ = _4_one
	_4_one = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("one"))
	var _5_two _dafny.Sequence
	_ = _5_two
	_5_two = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("two"))
	var _6_three _dafny.Sequence
	_ = _6_three
	_6_three = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("three"))
	var _7_four _dafny.Sequence
	_ = _7_four
	_7_four = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("four"))
	var _8_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _8_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_4_one), int64(10000))
	_8_valueOrError0 = _out0
	if !(!((_8_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(103,15): " + (_8_valueOrError0).String())
	}
	var _9_res m_StormTracker.CacheState
	_ = _9_res
	_9_res = (_8_valueOrError0).Extract().(m_StormTracker.CacheState)
	if !((_9_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(104,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _10_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_5_two), int64(10000))
	_10_valueOrError1 = _out1
	if !(!((_10_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(105,11): " + (_10_valueOrError1).String())
	}
	_9_res = (_10_valueOrError1).Extract().(m_StormTracker.CacheState)
	if !((_9_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(106,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _11_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _11_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_6_three), int64(10000))
	_11_valueOrError2 = _out2
	if !(!((_11_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,11): " + (_11_valueOrError2).String())
	}
	_9_res = (_11_valueOrError2).Extract().(m_StormTracker.CacheState)
	if !((_9_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _12_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _12_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_7_four), int64(10000))
	_12_valueOrError3 = _out3
	if !(!((_12_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(109,11): " + (_12_valueOrError3).String())
	}
	_9_res = (_12_valueOrError3).Extract().(m_StormTracker.CacheState)
	if !((_9_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(110,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _13_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _13_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_7_four), int64(10001))
	_13_valueOrError4 = _out4
	if !(!((_13_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(111,11): " + (_13_valueOrError4).String())
	}
	_9_res = (_13_valueOrError4).Extract().(m_StormTracker.CacheState)
	if !((_9_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(112,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _14_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _14_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_7_four), int64(10003))
	_14_valueOrError5 = _out5
	if !(!((_14_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(113,11): " + (_14_valueOrError5).String())
	}
	_9_res = (_14_valueOrError5).Extract().(m_StormTracker.CacheState)
	if !((_9_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(114,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _15_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _15_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_7_four), int64(10005))
	_15_valueOrError6 = _out6
	if !(!((_15_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(115,11): " + (_15_valueOrError6).String())
	}
	_9_res = (_15_valueOrError6).Extract().(m_StormTracker.CacheState)
	if !((_9_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(116,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) StormTrackerGraceInterval() {
	var _0_st *m_StormTracker.StormTracker
	_ = _0_st
	var _nw0 *m_StormTracker.StormTracker = m_StormTracker.New_StormTracker_()
	_ = _nw0
	_nw0.Ctor__(func(_pat_let7_0 m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
		return func(_1_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
			return func(_pat_let8_0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
				return func(_2_dt__update_hgraceInterval_h0 int32) m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
					return m_AwsCryptographyMaterialProvidersTypes.Companion_StormTrackingCache_.Create_StormTrackingCache_((_1_dt__update__tmp_h0).Dtor_entryCapacity(), (_1_dt__update__tmp_h0).Dtor_entryPruningTailSize(), (_1_dt__update__tmp_h0).Dtor_gracePeriod(), _2_dt__update_hgraceInterval_h0, (_1_dt__update__tmp_h0).Dtor_fanOut(), (_1_dt__update__tmp_h0).Dtor_inFlightTTL(), (_1_dt__update__tmp_h0).Dtor_sleepMilli())
				}(_pat_let8_0)
			}(int32(3))
		}(_pat_let7_0)
	}(m_StormTracker.Companion_Default___.DefaultStorm()))
	_0_st = _nw0
	var _3_one _dafny.Sequence
	_ = _3_one
	_3_one = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("one"))
	var _4_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _4_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_3_one), int64(10000))
	_4_valueOrError0 = _out0
	if !(!((_4_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,15): " + (_4_valueOrError0).String())
	}
	var _5_res m_StormTracker.CacheState
	_ = _5_res
	_5_res = (_4_valueOrError0).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _6_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_3_one), int64(10000))
	_6_valueOrError1 = _out1
	if !(!((_6_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,11): " + (_6_valueOrError1).String())
	}
	_5_res = (_6_valueOrError1).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _7_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _7_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_3_one), int64(10001))
	_7_valueOrError2 = _out2
	if !(!((_7_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,11): " + (_7_valueOrError2).String())
	}
	_5_res = (_7_valueOrError2).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _8_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_3_one), int64(10002))
	_8_valueOrError3 = _out3
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,11): " + (_8_valueOrError3).String())
	}
	_5_res = (_8_valueOrError3).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_EmptyWait()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(132,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _9_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _9_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_3_one), int64(10003))
	_9_valueOrError4 = _out4
	if !(!((_9_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(133,11): " + (_9_valueOrError4).String())
	}
	_5_res = (_9_valueOrError4).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(134,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) StormTrackerGracePeriod() {
	var _0_st *m_StormTracker.StormTracker
	_ = _0_st
	var _nw0 *m_StormTracker.StormTracker = m_StormTracker.New_StormTracker_()
	_ = _nw0
	_nw0.Ctor__(m_StormTracker.Companion_Default___.DefaultStorm())
	_0_st = _nw0
	var _1_one _dafny.Sequence
	_ = _1_one
	_1_one = m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("one"))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (_0_st).PutCacheEntry(Companion_Default___.MakePut(_1_one, int64(10010)))
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(143,16): " + (_2_valueOrError0).String())
	}
	var _3_res2 _dafny.Tuple
	_ = _3_res2
	_3_res2 = (_2_valueOrError0).Extract().(_dafny.Tuple)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _4_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_1_one), int64(9999))
	_4_valueOrError1 = _out1
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,15): " + (_4_valueOrError1).String())
	}
	var _5_res m_StormTracker.CacheState
	_ = _5_res
	_5_res = (_4_valueOrError1).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_Full()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_1_one), int64(10000))
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,11): " + (_6_valueOrError2).String())
	}
	_5_res = (_6_valueOrError2).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_EmptyFetch()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_StormTracker.Companion_CacheState_.Default())
	_ = _7_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_0_st).GetFromCacheWithTime(Companion_Default___.MakeGet(_1_one), int64(10000))
	_7_valueOrError3 = _out3
	if !(!((_7_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(149,11): " + (_7_valueOrError3).String())
	}
	_5_res = (_7_valueOrError3).Extract().(m_StormTracker.CacheState)
	if !((_5_res).Is_Full()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(150,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
