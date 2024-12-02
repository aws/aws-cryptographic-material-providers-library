// Package TestAwsKmsHierarchicalKeyring
// Dafny module TestAwsKmsHierarchicalKeyring compiled into Go

package TestAwsKmsHierarchicalKeyring

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
	m_TestAwsKmsEcdhKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestAwsKmsEcdhKeyring"
	m_TestAwsKmsEncryptedDataKeyFilter "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestAwsKmsEncryptedDataKeyFilter"
	m_TestConfig "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestConfig"
	m_TestCreateKeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeyStore"
	m_TestCreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeys"
	m_TestDiscoveryGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestDiscoveryGetKeys"
	m_TestErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestErrorMessages"
	m_TestGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestGetKeys"
	m_TestLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLocalCMC"
	m_TestLyingBranchKey "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLyingBranchKey"
	m_TestRawECDHKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestRawECDHKeyring"
	m_TestStormTracker "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestStormTracker"
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
var _ m_TestStormTracker.Dummy__
var _ m_TestLocalCMC.Dummy__
var _ m_TestRawECDHKeyring.Dummy__
var _ m_TestAwsKmsEncryptedDataKeyFilter.Dummy__
var _ m_TestAwsKmsEcdhKeyring.Dummy__

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
	return "TestAwsKmsHierarchicalKeyring.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) GetTestMaterials(suiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId) m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials {
	var out m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials{}
	_ = out
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(54,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_encryptionContext _dafny.Map
	_ = _2_encryptionContext
	var _out1 _dafny.Map
	_ = _out1
	_out1 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_2_encryptionContext = _out1
	var _3_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	_ = _3_suite
	_3_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(suiteId)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	_4_valueOrError1 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(suiteId, _2_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(59,33): " + (_4_valueOrError1).String())
	}
	var _5_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _5_encryptionMaterialsIn
	_5_encryptionMaterialsIn = (_4_valueOrError1).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	out = _5_encryptionMaterialsIn
	return out
	return out
}
func (_static *CompanionStruct_Default___) TestHierarchyClientESDKSuite() {
	var _0_branchKeyId _dafny.Sequence
	_ = _0_branchKeyId
	_0_branchKeyId = Companion_Default___.BRANCH__KEY__ID()
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(77,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_4_valueOrError1 = _out1
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(79,21): " + (_4_valueOrError1).String())
	}
	var _5_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _5_kmsClient
	_5_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_4_valueOrError1).Extract())
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(80,21): " + (_6_valueOrError2).String())
	}
	var _7_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _7_ddbClient
	_7_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_6_valueOrError2).Extract())
	var _8_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _8_kmsConfig
	_8_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _9_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _9_keyStoreConfig
	_9_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _8_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_7_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_5_kmsClient))
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_KeyStore.Companion_Default___.KeyStore(_9_keyStoreConfig)
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(93,20): " + (_10_valueOrError3).String())
	}
	var _11_keyStore *m_KeyStore.KeyStoreClient
	_ = _11_keyStore
	_11_keyStore = (_10_valueOrError3).Extract().(*m_KeyStore.KeyStoreClient)
	var _12_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyId), m_Wrappers.Companion_Option_.Create_None_(), _11_keyStore, _1_ttl, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_12_valueOrError4 = _out4
	if !(!((_12_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(95,28): " + (_12_valueOrError4).String())
	}
	var _13_hierarchyKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _13_hierarchyKeyring
	_13_hierarchyKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_12_valueOrError4).Extract())
	var _14_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _14_materials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__ESDK__ALG__SUITE__ID())
	_14_materials = _out5
	Companion_Default___.TestRoundtrip(_13_hierarchyKeyring, _14_materials, Companion_Default___.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyId)
	var _15_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	_ = _15_suite
	_15_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(Companion_Default___.TEST__ESDK__ALG__SUITE__ID())
	var _16_zeroedKey _dafny.Sequence
	_ = _16_zeroedKey
	_16_zeroedKey = _dafny.SeqCreate((_dafny.IntOfInt32(m_AlgorithmSuites.Companion_Default___.GetEncryptKeyLength(_15_suite))).Uint32(), func(coer0 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg0 _dafny.Int) interface{} {
			return coer0(arg0)
		}
	}(func(_17___v0 _dafny.Int) uint8 {
		return uint8(0)
	}))
	var _18_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = _14_materials
	_ = _18_dt__update__tmp_h0
	var _19_dt__update_hplaintextDataKey_h0 m_Wrappers.Option = m_Wrappers.Companion_Option_.Create_Some_(_16_zeroedKey)
	_ = _19_dt__update_hplaintextDataKey_h0
	_14_materials = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_((_18_dt__update__tmp_h0).Dtor_algorithmSuite(), (_18_dt__update__tmp_h0).Dtor_encryptionContext(), (_18_dt__update__tmp_h0).Dtor_encryptedDataKeys(), (_18_dt__update__tmp_h0).Dtor_requiredEncryptionContextKeys(), _19_dt__update_hplaintextDataKey_h0, (_18_dt__update__tmp_h0).Dtor_signingKey(), (_18_dt__update__tmp_h0).Dtor_symmetricSigningKeys())
	Companion_Default___.TestRoundtrip(_13_hierarchyKeyring, _14_materials, Companion_Default___.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyId)
}
func (_static *CompanionStruct_Default___) TestHierarchyClientDBESuite() {
	var _0_branchKeyId _dafny.Sequence
	_ = _0_branchKeyId
	_0_branchKeyId = Companion_Default___.BRANCH__KEY__ID()
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(120,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_4_valueOrError1 = _out1
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(122,21): " + (_4_valueOrError1).String())
	}
	var _5_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _5_kmsClient
	_5_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_4_valueOrError1).Extract())
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(123,21): " + (_6_valueOrError2).String())
	}
	var _7_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _7_ddbClient
	_7_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_6_valueOrError2).Extract())
	var _8_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _8_kmsConfig
	_8_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _9_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _9_keyStoreConfig
	_9_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _8_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_7_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_5_kmsClient))
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_KeyStore.Companion_Default___.KeyStore(_9_keyStoreConfig)
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(136,20): " + (_10_valueOrError3).String())
	}
	var _11_keyStore *m_KeyStore.KeyStoreClient
	_ = _11_keyStore
	_11_keyStore = (_10_valueOrError3).Extract().(*m_KeyStore.KeyStoreClient)
	var _12_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyId), m_Wrappers.Companion_Option_.Create_None_(), _11_keyStore, _1_ttl, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_12_valueOrError4 = _out4
	if !(!((_12_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(138,28): " + (_12_valueOrError4).String())
	}
	var _13_hierarchyKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _13_hierarchyKeyring
	_13_hierarchyKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_12_valueOrError4).Extract())
	var _14_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _14_materials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__DBE__ALG__SUITE__ID())
	_14_materials = _out5
	Companion_Default___.TestRoundtrip(_13_hierarchyKeyring, _14_materials, Companion_Default___.TEST__DBE__ALG__SUITE__ID(), _0_branchKeyId)
	var _15_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	_ = _15_suite
	_15_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(Companion_Default___.TEST__DBE__ALG__SUITE__ID())
	var _16_zeroedKey _dafny.Sequence
	_ = _16_zeroedKey
	_16_zeroedKey = _dafny.SeqCreate((_dafny.IntOfInt32(m_AlgorithmSuites.Companion_Default___.GetEncryptKeyLength(_15_suite))).Uint32(), func(coer1 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg1 _dafny.Int) interface{} {
			return coer1(arg1)
		}
	}(func(_17___v1 _dafny.Int) uint8 {
		return uint8(0)
	}))
	var _18_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = _14_materials
	_ = _18_dt__update__tmp_h0
	var _19_dt__update_hplaintextDataKey_h0 m_Wrappers.Option = m_Wrappers.Companion_Option_.Create_Some_(_16_zeroedKey)
	_ = _19_dt__update_hplaintextDataKey_h0
	_14_materials = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_((_18_dt__update__tmp_h0).Dtor_algorithmSuite(), (_18_dt__update__tmp_h0).Dtor_encryptionContext(), (_18_dt__update__tmp_h0).Dtor_encryptedDataKeys(), (_18_dt__update__tmp_h0).Dtor_requiredEncryptionContextKeys(), _19_dt__update_hplaintextDataKey_h0, (_18_dt__update__tmp_h0).Dtor_signingKey(), (_18_dt__update__tmp_h0).Dtor_symmetricSigningKeys())
	Companion_Default___.TestRoundtrip(_13_hierarchyKeyring, _14_materials, Companion_Default___.TEST__DBE__ALG__SUITE__ID(), _0_branchKeyId)
}
func (_static *CompanionStruct_Default___) TestBranchKeyIdSupplier() {
	var _0_branchKeyIdSupplier m_AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
	_ = _0_branchKeyIdSupplier
	var _nw0 *DummyBranchKeyIdSupplier = New_DummyBranchKeyIdSupplier_()
	_ = _nw0
	_nw0.Ctor__()
	_0_branchKeyIdSupplier = _nw0
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(164,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_4_valueOrError1 = _out1
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(166,21): " + (_4_valueOrError1).String())
	}
	var _5_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _5_kmsClient
	_5_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_4_valueOrError1).Extract())
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(167,21): " + (_6_valueOrError2).String())
	}
	var _7_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _7_ddbClient
	_7_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_6_valueOrError2).Extract())
	var _8_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _8_kmsConfig
	_8_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _9_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _9_keyStoreConfig
	_9_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _8_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_7_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_5_kmsClient))
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_KeyStore.Companion_Default___.KeyStore(_9_keyStoreConfig)
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(180,20): " + (_10_valueOrError3).String())
	}
	var _11_keyStore *m_KeyStore.KeyStoreClient
	_ = _11_keyStore
	_11_keyStore = (_10_valueOrError3).Extract().(*m_KeyStore.KeyStoreClient)
	var _12_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdSupplier), _11_keyStore, _1_ttl, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_12_valueOrError4 = _out4
	if !(!((_12_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(182,28): " + (_12_valueOrError4).String())
	}
	var _13_hierarchyKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _13_hierarchyKeyring
	_13_hierarchyKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_12_valueOrError4).Extract())
	var _14_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _14_materials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__DBE__ALG__SUITE__ID())
	_14_materials = _out5
	var _15_contextCaseA _dafny.Map
	_ = _15_contextCaseA
	_15_contextCaseA = ((_14_materials).Dtor_encryptionContext()).Update(Companion_Default___.BRANCH__KEY(), Companion_Default___.CASE__A())
	var _16_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = _14_materials
	_ = _16_dt__update__tmp_h0
	var _17_dt__update_hencryptionContext_h0 _dafny.Map = _15_contextCaseA
	_ = _17_dt__update_hencryptionContext_h0
	_14_materials = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_((_16_dt__update__tmp_h0).Dtor_algorithmSuite(), _17_dt__update_hencryptionContext_h0, (_16_dt__update__tmp_h0).Dtor_encryptedDataKeys(), (_16_dt__update__tmp_h0).Dtor_requiredEncryptionContextKeys(), (_16_dt__update__tmp_h0).Dtor_plaintextDataKey(), (_16_dt__update__tmp_h0).Dtor_signingKey(), (_16_dt__update__tmp_h0).Dtor_symmetricSigningKeys())
	Companion_Default___.TestRoundtrip(_13_hierarchyKeyring, _14_materials, Companion_Default___.TEST__DBE__ALG__SUITE__ID(), Companion_Default___.BRANCH__KEY__ID__A())
	var _18_contextCaseB _dafny.Map
	_ = _18_contextCaseB
	_18_contextCaseB = ((_14_materials).Dtor_encryptionContext()).Update(Companion_Default___.BRANCH__KEY(), Companion_Default___.CASE__B())
	var _19_dt__update__tmp_h1 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = _14_materials
	_ = _19_dt__update__tmp_h1
	var _20_dt__update_hencryptionContext_h1 _dafny.Map = _18_contextCaseB
	_ = _20_dt__update_hencryptionContext_h1
	_14_materials = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_((_19_dt__update__tmp_h1).Dtor_algorithmSuite(), _20_dt__update_hencryptionContext_h1, (_19_dt__update__tmp_h1).Dtor_encryptedDataKeys(), (_19_dt__update__tmp_h1).Dtor_requiredEncryptionContextKeys(), (_19_dt__update__tmp_h1).Dtor_plaintextDataKey(), (_19_dt__update__tmp_h1).Dtor_signingKey(), (_19_dt__update__tmp_h1).Dtor_symmetricSigningKeys())
	Companion_Default___.TestRoundtrip(_13_hierarchyKeyring, _14_materials, Companion_Default___.TEST__DBE__ALG__SUITE__ID(), Companion_Default___.BRANCH__KEY__ID__B())
}
func (_static *CompanionStruct_Default___) TestInvalidDataKeyError() {
	var _0_branchKeyIdSupplier m_AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
	_ = _0_branchKeyIdSupplier
	var _nw0 *DummyBranchKeyIdSupplier = New_DummyBranchKeyIdSupplier_()
	_ = _nw0
	_nw0.Ctor__()
	_0_branchKeyIdSupplier = _nw0
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(210,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_4_valueOrError1 = _out1
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(211,21): " + (_4_valueOrError1).String())
	}
	var _5_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _5_kmsClient
	_5_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_4_valueOrError1).Extract())
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(212,21): " + (_6_valueOrError2).String())
	}
	var _7_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _7_ddbClient
	_7_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_6_valueOrError2).Extract())
	var _8_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _8_kmsConfig
	_8_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _9_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _9_keyStoreConfig
	_9_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _8_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_7_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_5_kmsClient))
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_KeyStore.Companion_Default___.KeyStore(_9_keyStoreConfig)
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(223,20): " + (_10_valueOrError3).String())
	}
	var _11_keyStore *m_KeyStore.KeyStoreClient
	_ = _11_keyStore
	_11_keyStore = (_10_valueOrError3).Extract().(*m_KeyStore.KeyStoreClient)
	var _12_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdSupplier), _11_keyStore, _1_ttl, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_12_valueOrError4 = _out4
	if !(!((_12_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(224,28): " + (_12_valueOrError4).String())
	}
	var _13_hierarchyKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _13_hierarchyKeyring
	_13_hierarchyKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_12_valueOrError4).Extract())
	var _14_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _14_materials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__DBE__ALG__SUITE__ID())
	_14_materials = _out5
	var _15_contextCaseA _dafny.Map
	_ = _15_contextCaseA
	_15_contextCaseA = ((_14_materials).Dtor_encryptionContext()).Update(Companion_Default___.BRANCH__KEY(), Companion_Default___.CASE__A())
	var _16_contextCaseB _dafny.Map
	_ = _16_contextCaseB
	_16_contextCaseB = ((_14_materials).Dtor_encryptionContext()).Update(Companion_Default___.BRANCH__KEY(), Companion_Default___.CASE__B())
	var _17_materialsA m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _17_materialsA
	var _18_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = _14_materials
	_ = _18_dt__update__tmp_h0
	var _19_dt__update_hencryptionContext_h0 _dafny.Map = _15_contextCaseA
	_ = _19_dt__update_hencryptionContext_h0
	_17_materialsA = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_((_18_dt__update__tmp_h0).Dtor_algorithmSuite(), _19_dt__update_hencryptionContext_h0, (_18_dt__update__tmp_h0).Dtor_encryptedDataKeys(), (_18_dt__update__tmp_h0).Dtor_requiredEncryptionContextKeys(), (_18_dt__update__tmp_h0).Dtor_plaintextDataKey(), (_18_dt__update__tmp_h0).Dtor_signingKey(), (_18_dt__update__tmp_h0).Dtor_symmetricSigningKeys())
	var _20_materialsB m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _20_materialsB
	var _21_dt__update__tmp_h1 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = _14_materials
	_ = _21_dt__update__tmp_h1
	var _22_dt__update_hencryptionContext_h1 _dafny.Map = _16_contextCaseB
	_ = _22_dt__update_hencryptionContext_h1
	_20_materialsB = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_((_21_dt__update__tmp_h1).Dtor_algorithmSuite(), _22_dt__update_hencryptionContext_h1, (_21_dt__update__tmp_h1).Dtor_encryptedDataKeys(), (_21_dt__update__tmp_h1).Dtor_requiredEncryptionContextKeys(), (_21_dt__update__tmp_h1).Dtor_plaintextDataKey(), (_21_dt__update__tmp_h1).Dtor_signingKey(), (_21_dt__update__tmp_h1).Dtor_symmetricSigningKeys())
	Companion_Default___.TestInvalidDataKeyFailureCase(_13_hierarchyKeyring, _17_materialsA, _20_materialsB, Companion_Default___.TEST__DBE__ALG__SUITE__ID())
}
func (_static *CompanionStruct_Default___) TestInvalidDataKeyFailureCase(hierarchyKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring, encryptionMaterialsInEncrypt m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials, encryptionMaterialsInDecrypt m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials, algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (hierarchyKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(encryptionMaterialsInEncrypt))
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(253,34): " + (_0_valueOrError0).String())
	}
	var _1_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _1_encryptionMaterialsOut
	_1_encryptionMaterialsOut = (_0_valueOrError0).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(257,15): " + (_2_valueOrError1).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError1).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _4_valueOrError2
	_4_valueOrError2 = (_3_mpl).EncryptionMaterialsHasPlaintextDataKey((_1_encryptionMaterialsOut).Dtor_materials())
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(258,13): " + (_4_valueOrError2).String())
	}
	var _5___v2 _dafny.Tuple
	_ = _5___v2
	_5___v2 = (_4_valueOrError2).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_1_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(260,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _6_edk
	_6_edk = (((_1_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _7_valueOrError3
	_7_valueOrError3 = (_3_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(algorithmSuiteId, (encryptionMaterialsInDecrypt).Dtor_encryptionContext(), _dafny.SeqOf()))
	if !(!((_7_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(264,33): " + (_7_valueOrError3).String())
	}
	var _8_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _8_decryptionMaterialsIn
	_8_decryptionMaterialsIn = (_7_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _9_decryptionMaterialsOut m_Wrappers.Result
	_ = _9_decryptionMaterialsOut
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (hierarchyKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_8_decryptionMaterialsIn, _dafny.SeqOf(_6_edk)))
	_9_decryptionMaterialsOut = _out2
	if !((_9_decryptionMaterialsOut).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(277,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_9_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(278,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _10_valueOrError4
	_10_valueOrError4 = m_ErrorMessages.Companion_Default___.IncorrectDataKeys(_dafny.SeqOf(_6_edk), (_8_decryptionMaterialsIn).Dtor_algorithmSuite(), _dafny.SeqOfString(""))
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(279,32): " + (_10_valueOrError4).String())
	}
	var _11_expectedErrorMessage _dafny.Sequence
	_ = _11_expectedErrorMessage
	_11_expectedErrorMessage = (_10_valueOrError4).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(((_9_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), _11_expectedErrorMessage)) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(280,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRoundtrip(hierarchyKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring, encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials, algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId, expectedBranchKeyId _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (hierarchyKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(encryptionMaterialsIn))
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(293,34): " + (_0_valueOrError0).String())
	}
	var _1_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _1_encryptionMaterialsOut
	_1_encryptionMaterialsOut = (_0_valueOrError0).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(297,15): " + (_2_valueOrError1).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError1).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _4_valueOrError2
	_4_valueOrError2 = (_3_mpl).EncryptionMaterialsHasPlaintextDataKey((_1_encryptionMaterialsOut).Dtor_materials())
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(298,13): " + (_4_valueOrError2).String())
	}
	var _5___v3 _dafny.Tuple
	_ = _5___v3
	_5___v3 = (_4_valueOrError2).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_1_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(300,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _6_edk
	_6_edk = (((_1_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _7_valueOrError3
	_7_valueOrError3 = m_UTF8.Encode(expectedBranchKeyId)
	if !(!((_7_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(305,35): " + (_7_valueOrError3).String())
	}
	var _8_expectedBranchKeyIdUTF8 _dafny.Sequence
	_ = _8_expectedBranchKeyIdUTF8
	_8_expectedBranchKeyIdUTF8 = (_7_valueOrError3).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal((_6_edk).Dtor_keyProviderInfo(), _8_expectedBranchKeyIdUTF8)) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(306,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _9_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError4
	_9_valueOrError4 = (_3_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(algorithmSuiteId, (encryptionMaterialsIn).Dtor_encryptionContext(), _dafny.SeqOf()))
	if !(!((_9_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(308,33): " + (_9_valueOrError4).String())
	}
	var _10_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _10_decryptionMaterialsIn
	_10_decryptionMaterialsIn = (_9_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _11_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _11_valueOrError5
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (hierarchyKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_10_decryptionMaterialsIn, _dafny.SeqOf(_6_edk)))
	_11_valueOrError5 = _out2
	if !(!((_11_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(315,34): " + (_11_valueOrError5).String())
	}
	var _12_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _12_decryptionMaterialsOut
	_12_decryptionMaterialsOut = (_11_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_1_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_12_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(327,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSharedCacheWithSamePartitionIdAndSameLogicalKeyStoreName() {
	var _0_branchKeyIdWest _dafny.Sequence
	_ = _0_branchKeyIdWest
	_0_branchKeyIdWest = Companion_Default___.BRANCH__KEY__ID()
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(336,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_regionWest _dafny.Sequence
	_ = _4_regionWest
	_4_regionWest = _dafny.SeqOfString("us-west-2")
	var _5_regionEast _dafny.Sequence
	_ = _5_regionEast
	_5_regionEast = _dafny.SeqOfString("us-east-2")
	var _6_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_4_regionWest)
	_6_valueOrError1 = _out1
	if !(!((_6_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(341,25): " + (_6_valueOrError1).String())
	}
	var _7_kmsClientWest m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClientWest
	_7_kmsClientWest = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError1).Extract())
	var _8_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_5_regionEast)
	_8_valueOrError2 = _out2
	if !(!((_8_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(342,25): " + (_8_valueOrError2).String())
	}
	var _9_kmsClientEast m_ComAmazonawsKmsTypes.IKMSClient
	_ = _9_kmsClientEast
	_9_kmsClientEast = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_8_valueOrError2).Extract())
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(343,21): " + (_10_valueOrError3).String())
	}
	var _11_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _11_ddbClient
	_11_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_10_valueOrError3).Extract())
	var _12_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _12_kmsConfig
	_12_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _13_keyStoreConfigClientRegionWest m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _13_keyStoreConfigClientRegionWest
	_13_keyStoreConfigClientRegionWest = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_7_kmsClientWest))
	var _14_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_KeyStore.Companion_Default___.KeyStore(_13_keyStoreConfigClientRegionWest)
	_14_valueOrError4 = _out4
	if !(!((_14_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(359,36): " + (_14_valueOrError4).String())
	}
	var _15_keyStoreClientRegionWest *m_KeyStore.KeyStoreClient
	_ = _15_keyStoreClientRegionWest
	_15_keyStoreClientRegionWest = (_14_valueOrError4).Extract().(*m_KeyStore.KeyStoreClient)
	var _16_keyStoreConfigClientRegionEast m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _16_keyStoreConfigClientRegionEast
	_16_keyStoreConfigClientRegionEast = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_9_kmsClientEast))
	var _17_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = m_KeyStore.Companion_Default___.KeyStore(_16_keyStoreConfigClientRegionEast)
	_17_valueOrError5 = _out5
	if !(!((_17_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(375,36): " + (_17_valueOrError5).String())
	}
	var _18_keyStoreClientRegionEast *m_KeyStore.KeyStoreClient
	_ = _18_keyStoreClientRegionEast
	_18_keyStoreClientRegionEast = (_17_valueOrError5).Extract().(*m_KeyStore.KeyStoreClient)
	var _19_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_3_mpl).CreateCryptographicMaterialsCache(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateCryptographicMaterialsCacheInput_.Create_CreateCryptographicMaterialsCacheInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Default_(m_AwsCryptographyMaterialProvidersTypes.Companion_DefaultCache_.Create_DefaultCache_(int32(100)))))
	_19_valueOrError6 = _out6
	if !(!((_19_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(378,28): " + (_19_valueOrError6).String())
	}
	var _20_sharedCacheInput m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
	_ = _20_sharedCacheInput
	_20_sharedCacheInput = m_AwsCryptographyMaterialProvidersTypes.Companion_ICryptographicMaterialsCache_.CastTo_((_19_valueOrError6).Extract())
	var _21_sharedCache m_AwsCryptographyMaterialProvidersTypes.CacheType
	_ = _21_sharedCache
	_21_sharedCache = m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Shared_(_20_sharedCacheInput)
	var _22_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _22_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _15_keyStoreClientRegionWest, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_21_sharedCache), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("partitionId"))))
	_22_valueOrError7 = _out7
	if !(!((_22_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(396,29): " + (_22_valueOrError7).String())
	}
	var _23_hierarchyKeyring1 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _23_hierarchyKeyring1
	_23_hierarchyKeyring1 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_22_valueOrError7).Extract())
	var _24_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _24_valueOrError8
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _18_keyStoreClientRegionEast, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_21_sharedCache), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("partitionId"))))
	_24_valueOrError8 = _out8
	if !(!((_24_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(410,29): " + (_24_valueOrError8).String())
	}
	var _25_hierarchyKeyring2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _25_hierarchyKeyring2
	_25_hierarchyKeyring2 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_24_valueOrError8).Extract())
	var _26_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _26_materials
	var _out9 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out9
	_out9 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__ESDK__ALG__SUITE__ID())
	_26_materials = _out9
	var _27_encryptionMaterialsOutMismatchedRegion m_Wrappers.Result
	_ = _27_encryptionMaterialsOutMismatchedRegion
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_25_hierarchyKeyring2).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_26_materials))
	_27_encryptionMaterialsOutMismatchedRegion = _out10
	if !((_27_encryptionMaterialsOutMismatchedRegion).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(437,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	Companion_Default___.TestRoundtrip(_23_hierarchyKeyring1, _26_materials, Companion_Default___.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest)
	Companion_Default___.TestRoundtrip(_25_hierarchyKeyring2, _26_materials, Companion_Default___.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest)
}
func (_static *CompanionStruct_Default___) TestSharedCacheWithDifferentUnspecifiedPartitionIdAndSameLogicalKeyStoreName() {
	var _0_branchKeyIdWest _dafny.Sequence
	_ = _0_branchKeyIdWest
	_0_branchKeyIdWest = Companion_Default___.BRANCH__KEY__ID()
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(476,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_regionWest _dafny.Sequence
	_ = _4_regionWest
	_4_regionWest = _dafny.SeqOfString("us-west-2")
	var _5_regionEast _dafny.Sequence
	_ = _5_regionEast
	_5_regionEast = _dafny.SeqOfString("us-east-2")
	var _6_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_4_regionWest)
	_6_valueOrError1 = _out1
	if !(!((_6_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(481,25): " + (_6_valueOrError1).String())
	}
	var _7_kmsClientWest m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClientWest
	_7_kmsClientWest = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError1).Extract())
	var _8_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_5_regionEast)
	_8_valueOrError2 = _out2
	if !(!((_8_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(482,25): " + (_8_valueOrError2).String())
	}
	var _9_kmsClientEast m_ComAmazonawsKmsTypes.IKMSClient
	_ = _9_kmsClientEast
	_9_kmsClientEast = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_8_valueOrError2).Extract())
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(483,21): " + (_10_valueOrError3).String())
	}
	var _11_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _11_ddbClient
	_11_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_10_valueOrError3).Extract())
	var _12_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _12_kmsConfig
	_12_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _13_keyStoreConfigClientRegionWest m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _13_keyStoreConfigClientRegionWest
	_13_keyStoreConfigClientRegionWest = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_7_kmsClientWest))
	var _14_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_KeyStore.Companion_Default___.KeyStore(_13_keyStoreConfigClientRegionWest)
	_14_valueOrError4 = _out4
	if !(!((_14_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(499,36): " + (_14_valueOrError4).String())
	}
	var _15_keyStoreClientRegionWest *m_KeyStore.KeyStoreClient
	_ = _15_keyStoreClientRegionWest
	_15_keyStoreClientRegionWest = (_14_valueOrError4).Extract().(*m_KeyStore.KeyStoreClient)
	var _16_keyStoreConfigClientRegionEast m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _16_keyStoreConfigClientRegionEast
	_16_keyStoreConfigClientRegionEast = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_9_kmsClientEast))
	var _17_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = m_KeyStore.Companion_Default___.KeyStore(_16_keyStoreConfigClientRegionEast)
	_17_valueOrError5 = _out5
	if !(!((_17_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(515,36): " + (_17_valueOrError5).String())
	}
	var _18_keyStoreClientRegionEast *m_KeyStore.KeyStoreClient
	_ = _18_keyStoreClientRegionEast
	_18_keyStoreClientRegionEast = (_17_valueOrError5).Extract().(*m_KeyStore.KeyStoreClient)
	var _19_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_3_mpl).CreateCryptographicMaterialsCache(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateCryptographicMaterialsCacheInput_.Create_CreateCryptographicMaterialsCacheInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Default_(m_AwsCryptographyMaterialProvidersTypes.Companion_DefaultCache_.Create_DefaultCache_(int32(100)))))
	_19_valueOrError6 = _out6
	if !(!((_19_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(518,28): " + (_19_valueOrError6).String())
	}
	var _20_sharedCacheInput m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
	_ = _20_sharedCacheInput
	_20_sharedCacheInput = m_AwsCryptographyMaterialProvidersTypes.Companion_ICryptographicMaterialsCache_.CastTo_((_19_valueOrError6).Extract())
	var _21_sharedCache m_AwsCryptographyMaterialProvidersTypes.CacheType
	_ = _21_sharedCache
	_21_sharedCache = m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Shared_(_20_sharedCacheInput)
	var _22_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _22_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _15_keyStoreClientRegionWest, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_21_sharedCache), m_Wrappers.Companion_Option_.Create_None_()))
	_22_valueOrError7 = _out7
	if !(!((_22_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(536,29): " + (_22_valueOrError7).String())
	}
	var _23_hierarchyKeyring1 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _23_hierarchyKeyring1
	_23_hierarchyKeyring1 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_22_valueOrError7).Extract())
	var _24_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _24_valueOrError8
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _18_keyStoreClientRegionEast, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_21_sharedCache), m_Wrappers.Companion_Option_.Create_None_()))
	_24_valueOrError8 = _out8
	if !(!((_24_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(550,29): " + (_24_valueOrError8).String())
	}
	var _25_hierarchyKeyring2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _25_hierarchyKeyring2
	_25_hierarchyKeyring2 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_24_valueOrError8).Extract())
	var _26_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _26_materials
	var _out9 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out9
	_out9 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__ESDK__ALG__SUITE__ID())
	_26_materials = _out9
	var _27_encryptionMaterialsOutMismatchedRegion m_Wrappers.Result
	_ = _27_encryptionMaterialsOutMismatchedRegion
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_25_hierarchyKeyring2).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_26_materials))
	_27_encryptionMaterialsOutMismatchedRegion = _out10
	if !((_27_encryptionMaterialsOutMismatchedRegion).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(571,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	Companion_Default___.TestRoundtrip(_23_hierarchyKeyring1, _26_materials, Companion_Default___.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest)
	var _28_encryptionMaterialsOutMismatchedRegionFromCache m_Wrappers.Result
	_ = _28_encryptionMaterialsOutMismatchedRegionFromCache
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_25_hierarchyKeyring2).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_26_materials))
	_28_encryptionMaterialsOutMismatchedRegionFromCache = _out11
	if !((_28_encryptionMaterialsOutMismatchedRegionFromCache).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(588,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSharedCacheWithDifferentSpecifiedPartitionIdAndSameLogicalKeyStoreName() {
	var _0_branchKeyIdWest _dafny.Sequence
	_ = _0_branchKeyIdWest
	_0_branchKeyIdWest = Companion_Default___.BRANCH__KEY__ID()
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(596,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_regionWest _dafny.Sequence
	_ = _4_regionWest
	_4_regionWest = _dafny.SeqOfString("us-west-2")
	var _5_regionEast _dafny.Sequence
	_ = _5_regionEast
	_5_regionEast = _dafny.SeqOfString("us-east-2")
	var _6_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_4_regionWest)
	_6_valueOrError1 = _out1
	if !(!((_6_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(601,25): " + (_6_valueOrError1).String())
	}
	var _7_kmsClientWest m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClientWest
	_7_kmsClientWest = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError1).Extract())
	var _8_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_5_regionEast)
	_8_valueOrError2 = _out2
	if !(!((_8_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(602,25): " + (_8_valueOrError2).String())
	}
	var _9_kmsClientEast m_ComAmazonawsKmsTypes.IKMSClient
	_ = _9_kmsClientEast
	_9_kmsClientEast = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_8_valueOrError2).Extract())
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(603,21): " + (_10_valueOrError3).String())
	}
	var _11_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _11_ddbClient
	_11_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_10_valueOrError3).Extract())
	var _12_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _12_kmsConfig
	_12_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _13_keyStoreConfigClientRegionWest m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _13_keyStoreConfigClientRegionWest
	_13_keyStoreConfigClientRegionWest = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_7_kmsClientWest))
	var _14_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_KeyStore.Companion_Default___.KeyStore(_13_keyStoreConfigClientRegionWest)
	_14_valueOrError4 = _out4
	if !(!((_14_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(619,36): " + (_14_valueOrError4).String())
	}
	var _15_keyStoreClientRegionWest *m_KeyStore.KeyStoreClient
	_ = _15_keyStoreClientRegionWest
	_15_keyStoreClientRegionWest = (_14_valueOrError4).Extract().(*m_KeyStore.KeyStoreClient)
	var _16_keyStoreConfigClientRegionEast m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _16_keyStoreConfigClientRegionEast
	_16_keyStoreConfigClientRegionEast = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_9_kmsClientEast))
	var _17_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = m_KeyStore.Companion_Default___.KeyStore(_16_keyStoreConfigClientRegionEast)
	_17_valueOrError5 = _out5
	if !(!((_17_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(635,36): " + (_17_valueOrError5).String())
	}
	var _18_keyStoreClientRegionEast *m_KeyStore.KeyStoreClient
	_ = _18_keyStoreClientRegionEast
	_18_keyStoreClientRegionEast = (_17_valueOrError5).Extract().(*m_KeyStore.KeyStoreClient)
	var _19_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_3_mpl).CreateCryptographicMaterialsCache(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateCryptographicMaterialsCacheInput_.Create_CreateCryptographicMaterialsCacheInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Default_(m_AwsCryptographyMaterialProvidersTypes.Companion_DefaultCache_.Create_DefaultCache_(int32(100)))))
	_19_valueOrError6 = _out6
	if !(!((_19_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(638,28): " + (_19_valueOrError6).String())
	}
	var _20_sharedCacheInput m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
	_ = _20_sharedCacheInput
	_20_sharedCacheInput = m_AwsCryptographyMaterialProvidersTypes.Companion_ICryptographicMaterialsCache_.CastTo_((_19_valueOrError6).Extract())
	var _21_sharedCache m_AwsCryptographyMaterialProvidersTypes.CacheType
	_ = _21_sharedCache
	_21_sharedCache = m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Shared_(_20_sharedCacheInput)
	var _22_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _22_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _15_keyStoreClientRegionWest, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_21_sharedCache), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("partitionIdHK1"))))
	_22_valueOrError7 = _out7
	if !(!((_22_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(656,29): " + (_22_valueOrError7).String())
	}
	var _23_hierarchyKeyring1 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _23_hierarchyKeyring1
	_23_hierarchyKeyring1 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_22_valueOrError7).Extract())
	var _24_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _24_valueOrError8
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _18_keyStoreClientRegionEast, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_21_sharedCache), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("partitionIdHK2"))))
	_24_valueOrError8 = _out8
	if !(!((_24_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(671,29): " + (_24_valueOrError8).String())
	}
	var _25_hierarchyKeyring2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _25_hierarchyKeyring2
	_25_hierarchyKeyring2 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_24_valueOrError8).Extract())
	var _26_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _26_materials
	var _out9 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out9
	_out9 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__ESDK__ALG__SUITE__ID())
	_26_materials = _out9
	var _27_encryptionMaterialsOutMismatchedRegion m_Wrappers.Result
	_ = _27_encryptionMaterialsOutMismatchedRegion
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_25_hierarchyKeyring2).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_26_materials))
	_27_encryptionMaterialsOutMismatchedRegion = _out10
	if !((_27_encryptionMaterialsOutMismatchedRegion).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(692,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	Companion_Default___.TestRoundtrip(_23_hierarchyKeyring1, _26_materials, Companion_Default___.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest)
	var _28_encryptionMaterialsOutMismatchedRegionFromCache m_Wrappers.Result
	_ = _28_encryptionMaterialsOutMismatchedRegionFromCache
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_25_hierarchyKeyring2).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_26_materials))
	_28_encryptionMaterialsOutMismatchedRegionFromCache = _out11
	if !((_28_encryptionMaterialsOutMismatchedRegionFromCache).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(706,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSharedCacheWithSamePartitionIdAndDifferentLogicalKeyStoreName() {
	var _0_branchKeyIdWest _dafny.Sequence
	_ = _0_branchKeyIdWest
	_0_branchKeyIdWest = Companion_Default___.BRANCH__KEY__ID()
	var _1_ttl int64
	_ = _1_ttl
	_1_ttl = ((int64(1)) * (int64(60000))) * (int64(10))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(714,15): " + (_2_valueOrError0).String())
	}
	var _3_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _3_mpl
	_3_mpl = (_2_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _4_regionWest _dafny.Sequence
	_ = _4_regionWest
	_4_regionWest = _dafny.SeqOfString("us-west-2")
	var _5_regionEast _dafny.Sequence
	_ = _5_regionEast
	_5_regionEast = _dafny.SeqOfString("us-east-2")
	var _6_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_4_regionWest)
	_6_valueOrError1 = _out1
	if !(!((_6_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(719,25): " + (_6_valueOrError1).String())
	}
	var _7_kmsClientWest m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClientWest
	_7_kmsClientWest = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError1).Extract())
	var _8_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_5_regionEast)
	_8_valueOrError2 = _out2
	if !(!((_8_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(720,25): " + (_8_valueOrError2).String())
	}
	var _9_kmsClientEast m_ComAmazonawsKmsTypes.IKMSClient
	_ = _9_kmsClientEast
	_9_kmsClientEast = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_8_valueOrError2).Extract())
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_10_valueOrError3 = _out3
	if !(!((_10_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(721,21): " + (_10_valueOrError3).String())
	}
	var _11_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _11_ddbClient
	_11_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_10_valueOrError3).Extract())
	var _12_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _12_kmsConfig
	_12_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.KeyArn())
	var _13_logicalKeyStoreName _dafny.Sequence
	_ = _13_logicalKeyStoreName
	_13_logicalKeyStoreName = Companion_Default___.LogicalKeyStoreName()
	var _14_logicalKeyStoreNameNew _dafny.Sequence
	_ = _14_logicalKeyStoreNameNew
	_14_logicalKeyStoreNameNew = _dafny.Companion_Sequence_.Concatenate(_13_logicalKeyStoreName, _dafny.SeqOfString("New"))
	var _15_keyStoreConfigClientRegionWest m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _15_keyStoreConfigClientRegionWest
	_15_keyStoreConfigClientRegionWest = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, _13_logicalKeyStoreName, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_7_kmsClientWest))
	var _16_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _16_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_KeyStore.Companion_Default___.KeyStore(_15_keyStoreConfigClientRegionWest)
	_16_valueOrError4 = _out4
	if !(!((_16_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(741,36): " + (_16_valueOrError4).String())
	}
	var _17_keyStoreClientRegionWest *m_KeyStore.KeyStoreClient
	_ = _17_keyStoreClientRegionWest
	_17_keyStoreClientRegionWest = (_16_valueOrError4).Extract().(*m_KeyStore.KeyStoreClient)
	var _18_keyStoreConfigClientRegionEast m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _18_keyStoreConfigClientRegionEast
	_18_keyStoreConfigClientRegionEast = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(Companion_Default___.BranchKeyStoreName(), _12_kmsConfig, _14_logicalKeyStoreNameNew, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_11_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_9_kmsClientEast))
	var _19_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = m_KeyStore.Companion_Default___.KeyStore(_18_keyStoreConfigClientRegionEast)
	_19_valueOrError5 = _out5
	if !(!((_19_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(758,36): " + (_19_valueOrError5).String())
	}
	var _20_keyStoreClientRegionEast *m_KeyStore.KeyStoreClient
	_ = _20_keyStoreClientRegionEast
	_20_keyStoreClientRegionEast = (_19_valueOrError5).Extract().(*m_KeyStore.KeyStoreClient)
	var _21_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _21_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_3_mpl).CreateCryptographicMaterialsCache(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateCryptographicMaterialsCacheInput_.Create_CreateCryptographicMaterialsCacheInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Default_(m_AwsCryptographyMaterialProvidersTypes.Companion_DefaultCache_.Create_DefaultCache_(int32(100)))))
	_21_valueOrError6 = _out6
	if !(!((_21_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(761,28): " + (_21_valueOrError6).String())
	}
	var _22_sharedCacheInput m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
	_ = _22_sharedCacheInput
	_22_sharedCacheInput = m_AwsCryptographyMaterialProvidersTypes.Companion_ICryptographicMaterialsCache_.CastTo_((_21_valueOrError6).Extract())
	var _23_sharedCache m_AwsCryptographyMaterialProvidersTypes.CacheType
	_ = _23_sharedCache
	_23_sharedCache = m_AwsCryptographyMaterialProvidersTypes.Companion_CacheType_.Create_Shared_(_22_sharedCacheInput)
	var _24_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _24_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _17_keyStoreClientRegionWest, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_23_sharedCache), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("partitionId"))))
	_24_valueOrError7 = _out7
	if !(!((_24_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(779,29): " + (_24_valueOrError7).String())
	}
	var _25_hierarchyKeyring1 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _25_hierarchyKeyring1
	_25_hierarchyKeyring1 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_24_valueOrError7).Extract())
	var _26_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _26_valueOrError8
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_0_branchKeyIdWest), m_Wrappers.Companion_Option_.Create_None_(), _20_keyStoreClientRegionEast, _1_ttl, m_Wrappers.Companion_Option_.Create_Some_(_23_sharedCache), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("partitionId"))))
	_26_valueOrError8 = _out8
	if !(!((_26_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(793,29): " + (_26_valueOrError8).String())
	}
	var _27_hierarchyKeyring2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _27_hierarchyKeyring2
	_27_hierarchyKeyring2 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_26_valueOrError8).Extract())
	var _28_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _28_materials
	var _out9 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out9
	_out9 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__ESDK__ALG__SUITE__ID())
	_28_materials = _out9
	var _29_encryptionMaterialsOutMismatchedRegion m_Wrappers.Result
	_ = _29_encryptionMaterialsOutMismatchedRegion
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_27_hierarchyKeyring2).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_28_materials))
	_29_encryptionMaterialsOutMismatchedRegion = _out10
	if !((_29_encryptionMaterialsOutMismatchedRegion).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(814,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	Companion_Default___.TestRoundtrip(_25_hierarchyKeyring1, _28_materials, Companion_Default___.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest)
	var _30_encryptionMaterialsOutMismatchedRegionFromCache m_Wrappers.Result
	_ = _30_encryptionMaterialsOutMismatchedRegionFromCache
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_27_hierarchyKeyring2).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_28_materials))
	_30_encryptionMaterialsOutMismatchedRegionFromCache = _out11
	if !((_30_encryptionMaterialsOutMismatchedRegionFromCache).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(828,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) BranchKeyStoreName() _dafny.Sequence {
	return m_Fixtures.Companion_Default___.BranchKeyStoreName()
}
func (_static *CompanionStruct_Default___) LogicalKeyStoreName() _dafny.Sequence {
	return Companion_Default___.BranchKeyStoreName()
}
func (_static *CompanionStruct_Default___) BRANCH__KEY__ID() _dafny.Sequence {
	return m_Fixtures.Companion_Default___.BranchKeyId()
}
func (_static *CompanionStruct_Default___) BRANCH__KEY__ID__A() _dafny.Sequence {
	return Companion_Default___.BRANCH__KEY__ID()
}
func (_static *CompanionStruct_Default___) KeyArn() _dafny.Sequence {
	return m_Fixtures.Companion_Default___.KeyArn()
}
func (_static *CompanionStruct_Default___) TEST__ESDK__ALG__SUITE__ID() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
}
func (_static *CompanionStruct_Default___) TEST__DBE__ALG__SUITE__ID() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_DBE_(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384_())
}
func (_static *CompanionStruct_Default___) BRANCH__KEY() _dafny.Sequence {
	return m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("branchKey"))
}
func (_static *CompanionStruct_Default___) CASE__A() _dafny.Sequence {
	return m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("caseA"))
}
func (_static *CompanionStruct_Default___) CASE__B() _dafny.Sequence {
	return m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("caseB"))
}
func (_static *CompanionStruct_Default___) BRANCH__KEY__ID__B() _dafny.Sequence {
	return m_Fixtures.Companion_Default___.BranchKeyIdWithEC()
}

// End of class Default__

// Definition of class DummyBranchKeyIdSupplier
type DummyBranchKeyIdSupplier struct {
	dummy byte
}

func New_DummyBranchKeyIdSupplier_() *DummyBranchKeyIdSupplier {
	_this := DummyBranchKeyIdSupplier{}

	return &_this
}

type CompanionStruct_DummyBranchKeyIdSupplier_ struct {
}

var Companion_DummyBranchKeyIdSupplier_ = CompanionStruct_DummyBranchKeyIdSupplier_{}

func (_this *DummyBranchKeyIdSupplier) Equals(other *DummyBranchKeyIdSupplier) bool {
	return _this == other
}

func (_this *DummyBranchKeyIdSupplier) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*DummyBranchKeyIdSupplier)
	return ok && _this.Equals(other)
}

func (*DummyBranchKeyIdSupplier) String() string {
	return "TestAwsKmsHierarchicalKeyring.DummyBranchKeyIdSupplier"
}

func Type_DummyBranchKeyIdSupplier_() _dafny.TypeDescriptor {
	return type_DummyBranchKeyIdSupplier_{}
}

type type_DummyBranchKeyIdSupplier_ struct {
}

func (_this type_DummyBranchKeyIdSupplier_) Default() interface{} {
	return (*DummyBranchKeyIdSupplier)(nil)
}

func (_this type_DummyBranchKeyIdSupplier_) String() string {
	return "TestAwsKmsHierarchicalKeyring.DummyBranchKeyIdSupplier"
}
func (_this *DummyBranchKeyIdSupplier) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){m_AwsCryptographyMaterialProvidersTypes.Companion_IBranchKeyIdSupplier_.TraitID_}
}

var _ m_AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier = &DummyBranchKeyIdSupplier{}
var _ _dafny.TraitOffspring = &DummyBranchKeyIdSupplier{}

func (_this *DummyBranchKeyIdSupplier) GetBranchKeyId(input m_AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput) m_Wrappers.Result {
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AwsCryptographyMaterialProvidersTypes.Companion_IBranchKeyIdSupplier_.GetBranchKeyId(_this, input)
	return _out0
}
func (_this *DummyBranchKeyIdSupplier) Ctor__() {
	{
	}
}
func (_this *DummyBranchKeyIdSupplier) GetBranchKeyId_k(input m_AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyMaterialProvidersTypes.Companion_GetBranchKeyIdOutput_.Default())
		_ = output
		var _0_context _dafny.Map
		_ = _0_context
		_0_context = (input).Dtor_encryptionContext()
		if (((_0_context).Keys()).Contains(Companion_Default___.BRANCH__KEY())) && (_dafny.Companion_Sequence_.Equal((_0_context).Get(Companion_Default___.BRANCH__KEY()).(_dafny.Sequence), Companion_Default___.CASE__A())) {
			output = m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_GetBranchKeyIdOutput_.Create_GetBranchKeyIdOutput_(Companion_Default___.BRANCH__KEY__ID__A()))
			return output
		} else if (((_0_context).Keys()).Contains(Companion_Default___.BRANCH__KEY())) && (_dafny.Companion_Sequence_.Equal((_0_context).Get(Companion_Default___.BRANCH__KEY()).(_dafny.Sequence), Companion_Default___.CASE__B())) {
			output = m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_GetBranchKeyIdOutput_.Create_GetBranchKeyIdOutput_(Companion_Default___.BRANCH__KEY__ID__B()))
			return output
		} else {
			output = m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Can't determine branchKeyId from context")))
			return output
		}
		return output
	}
}

// End of class DummyBranchKeyIdSupplier
