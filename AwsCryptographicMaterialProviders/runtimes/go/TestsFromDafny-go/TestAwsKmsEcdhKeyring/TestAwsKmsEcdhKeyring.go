// Package TestAwsKmsEcdhKeyring
// Dafny module TestAwsKmsEcdhKeyring compiled into Go

package TestAwsKmsEcdhKeyring

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
	return "TestAwsKmsEcdhKeyring.Default__"
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(44,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(49,33): " + (_4_valueOrError1).String())
	}
	var _5_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _5_encryptionMaterialsIn
	_5_encryptionMaterialsIn = (_4_valueOrError1).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	out = _5_encryptionMaterialsIn
	return out
	return out
}
func (_static *CompanionStruct_Default___) TestKmsEcdhConfigurationFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(63,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(65,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPublicKeyDiscovery_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPublicKeyDiscoveryInput_.Create_KmsPublicKeyDiscoveryInput_(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__R())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_4_valueOrError2 = _out2
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(67,48): " + (_4_valueOrError2).String())
	}
	var _5_kmsEcdhKeyringDiscoveryConfiguration m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _5_kmsEcdhKeyringDiscoveryConfiguration
	_5_kmsEcdhKeyringDiscoveryConfiguration = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError2).Extract())
	var _6_encryptionContext _dafny.Map
	_ = _6_encryptionContext
	var _out3 _dafny.Map
	_ = _out3
	_out3 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_6_encryptionContext = _out3
	var _7_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _7_algorithmSuiteId
	_7_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError3
	_8_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_7_algorithmSuiteId, _6_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(83,33): " + (_8_valueOrError3).String())
	}
	var _9_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _9_encryptionMaterialsIn
	_9_encryptionMaterialsIn = (_8_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _10_encryptionMaterialsOut m_Wrappers.Result
	_ = _10_encryptionMaterialsOut
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_5_kmsEcdhKeyringDiscoveryConfiguration).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_9_encryptionMaterialsIn))
	_10_encryptionMaterialsOut = _out4
	if !((_10_encryptionMaterialsOut).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(97,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_10_encryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(98,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _11_expectedErrorMessage _dafny.Sequence
	_ = _11_expectedErrorMessage
	_11_expectedErrorMessage = m_ErrorMessages.Companion_Default___.KMS__ECDH__DISCOVERY__ENCRYPT__ERROR()
	if !(_dafny.Companion_Sequence_.Equal(((_10_encryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), _11_expectedErrorMessage)) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(101,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(105,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(107,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_senderArns _dafny.Sequence
	_ = _4_senderArns
	_4_senderArns = _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__S())
	var _5_recipientArns _dafny.Sequence
	_ = _5_recipientArns
	_5_recipientArns = _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__R())
	var _6_curveSpecs _dafny.Sequence
	_ = _6_curveSpecs
	_6_curveSpecs = _dafny.SeqOf(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_4_senderArns).Cardinality())
	_ = _hi0
	for _7_i := _dafny.Zero; _7_i.Cmp(_hi0) < 0; _7_i = _7_i.Plus(_dafny.One) {
		var _8_publicKeyResponse m_Wrappers.Result
		_ = _8_publicKeyResponse
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = (_3_kmsClient).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_((_5_recipientArns).Select((_7_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_None_()))
		_8_publicKeyResponse = _out2
		if !((_8_publicKeyResponse).Is_Success()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(121,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_8_publicKeyResponse).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
		_ = _let_tmp_rhs0
		var _9___v0 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
		_ = _9___v0
		var _10_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
		_ = _10_PublicKey
		var _11___v1 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
		_ = _11___v1
		var _12___v2 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
		_ = _12___v2
		var _13___v3 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
		_ = _13___v3
		var _14___v4 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
		_ = _14___v4
		var _15___v5 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
		_ = _15___v5
		var _16___v6 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
		_ = _16___v6
		if !((_10_PublicKey).Is_Some()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(123,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		_dafny.Print((_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("\nTest with sender: "), (_4_senderArns).Select((_7_i).Uint32()).(_dafny.Sequence)), _dafny.SeqOfString(" and recipient: ")), (_5_recipientArns).Select((_7_i).Uint32()).(_dafny.Sequence)), _dafny.SeqOfString("\n"))).SetString())
		var _17_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _17_valueOrError2
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_((_4_senderArns).Select((_7_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_None_(), (_10_PublicKey).Dtor_value().(_dafny.Sequence))), (_6_curveSpecs).Select((_7_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
		_17_valueOrError2 = _out3
		if !(!((_17_valueOrError2).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(126,28): " + (_17_valueOrError2).String())
		}
		var _18_kmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _18_kmsEcdhKeyring
		_18_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_17_valueOrError2).Extract())
		var _19_encryptionContext _dafny.Map
		_ = _19_encryptionContext
		var _out4 _dafny.Map
		_ = _out4
		_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
		_19_encryptionContext = _out4
		var _20_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
		_ = _20_algorithmSuiteId
		_20_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
		var _21_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
		_ = _21_suite
		_21_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_20_algorithmSuiteId)
		var _22_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _22_valueOrError3
		_22_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_20_algorithmSuiteId, _19_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
		if !(!((_22_valueOrError3).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(144,35): " + (_22_valueOrError3).String())
		}
		var _23_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
		_ = _23_encryptionMaterialsIn
		_23_encryptionMaterialsIn = (_22_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
		var _24_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _24_valueOrError4
		var _out5 m_Wrappers.Result
		_ = _out5
		_out5 = (_18_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_23_encryptionMaterialsIn))
		_24_valueOrError4 = _out5
		if !(!((_24_valueOrError4).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(154,36): " + (_24_valueOrError4).String())
		}
		var _25_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
		_ = _25_encryptionMaterialsOut
		_25_encryptionMaterialsOut = (_24_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
		var _26_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = _26_valueOrError5
		_26_valueOrError5 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_25_encryptionMaterialsOut).Dtor_materials())
		if !(!((_26_valueOrError5).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(158,15): " + (_26_valueOrError5).String())
		}
		var _27___v7 _dafny.Tuple
		_ = _27___v7
		_27___v7 = (_26_valueOrError5).Extract().(_dafny.Tuple)
		if !((_dafny.IntOfUint32((((_25_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(160,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _28_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
		_ = _28_edk
		_28_edk = (((_25_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
		var _29_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _29_valueOrError6
		_29_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_20_algorithmSuiteId, _19_encryptionContext, _dafny.SeqOf()))
		if !(!((_29_valueOrError6).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(163,35): " + (_29_valueOrError6).String())
		}
		var _30_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
		_ = _30_decryptionMaterialsIn
		_30_decryptionMaterialsIn = (_29_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
		var _31_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _31_valueOrError7
		var _out6 m_Wrappers.Result
		_ = _out6
		_out6 = (_18_kmsEcdhKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_30_decryptionMaterialsIn, _dafny.SeqOf(_28_edk)))
		_31_valueOrError7 = _out6
		if !(!((_31_valueOrError7).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(170,36): " + (_31_valueOrError7).String())
		}
		var _32_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
		_ = _32_decryptionMaterialsOut
		_32_decryptionMaterialsOut = (_31_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
		if !((((_25_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_32_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(177,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(183,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(185,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_senderArns _dafny.Sequence
	_ = _4_senderArns
	_4_senderArns = _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__S())
	var _5_recipientArns _dafny.Sequence
	_ = _5_recipientArns
	_5_recipientArns = _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__R())
	var _6_curveSpecs _dafny.Sequence
	_ = _6_curveSpecs
	_6_curveSpecs = _dafny.SeqOf(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_4_senderArns).Cardinality())
	_ = _hi0
	for _7_i := _dafny.Zero; _7_i.Cmp(_hi0) < 0; _7_i = _7_i.Plus(_dafny.One) {
		var _8_publicKeyResponse m_Wrappers.Result
		_ = _8_publicKeyResponse
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = (_3_kmsClient).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_((_5_recipientArns).Select((_7_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_None_()))
		_8_publicKeyResponse = _out2
		if !((_8_publicKeyResponse).Is_Success()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(199,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_8_publicKeyResponse).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
		_ = _let_tmp_rhs0
		var _9___v8 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
		_ = _9___v8
		var _10_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
		_ = _10_PublicKey
		var _11___v9 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
		_ = _11___v9
		var _12___v10 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
		_ = _12___v10
		var _13___v11 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
		_ = _13___v11
		var _14___v12 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
		_ = _14___v12
		var _15___v13 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
		_ = _15___v13
		var _16___v14 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
		_ = _16___v14
		if !((_10_PublicKey).Is_Some()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(201,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		_dafny.Print((_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("\nTest with sender: "), (_4_senderArns).Select((_7_i).Uint32()).(_dafny.Sequence)), _dafny.SeqOfString(" and recipient: ")), (_5_recipientArns).Select((_7_i).Uint32()).(_dafny.Sequence)), _dafny.SeqOfString("\n"))).SetString())
		var _17_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _17_valueOrError2
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_((_4_senderArns).Select((_7_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_None_(), (_10_PublicKey).Dtor_value().(_dafny.Sequence))), (_6_curveSpecs).Select((_7_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
		_17_valueOrError2 = _out3
		if !(!((_17_valueOrError2).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(204,28): " + (_17_valueOrError2).String())
		}
		var _18_kmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _18_kmsEcdhKeyring
		_18_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_17_valueOrError2).Extract())
		var _19_encryptionContext _dafny.Map
		_ = _19_encryptionContext
		var _out4 _dafny.Map
		_ = _out4
		_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
		_19_encryptionContext = _out4
		var _20_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
		_ = _20_materials
		var _out5 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
		_ = _out5
		_out5 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__DBE__ALG__SUITE__ID())
		_20_materials = _out5
		var _21_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _21_valueOrError3
		var _out6 m_Wrappers.Result
		_ = _out6
		_out6 = (_18_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_20_materials))
		_21_valueOrError3 = _out6
		if !(!((_21_valueOrError3).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(221,36): " + (_21_valueOrError3).String())
		}
		var _22_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
		_ = _22_encryptionMaterialsOut
		_22_encryptionMaterialsOut = (_21_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
		var _23_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = _23_valueOrError4
		_23_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_22_encryptionMaterialsOut).Dtor_materials())
		if !(!((_23_valueOrError4).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(225,15): " + (_23_valueOrError4).String())
		}
		var _24___v15 _dafny.Tuple
		_ = _24___v15
		_24___v15 = (_23_valueOrError4).Extract().(_dafny.Tuple)
		if !((_dafny.IntOfUint32((((_22_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(227,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _25_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
		_ = _25_edk
		_25_edk = (((_22_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
		var _26_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _26_valueOrError5
		_26_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(Companion_Default___.TEST__DBE__ALG__SUITE__ID(), _19_encryptionContext, _dafny.SeqOf()))
		if !(!((_26_valueOrError5).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(230,35): " + (_26_valueOrError5).String())
		}
		var _27_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
		_ = _27_decryptionMaterialsIn
		_27_decryptionMaterialsIn = (_26_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
		var _28_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _28_valueOrError6
		var _out7 m_Wrappers.Result
		_ = _out7
		_out7 = (_18_kmsEcdhKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_27_decryptionMaterialsIn, _dafny.SeqOf(_25_edk)))
		_28_valueOrError6 = _out7
		if !(!((_28_valueOrError6).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(237,36): " + (_28_valueOrError6).String())
		}
		var _29_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
		_ = _29_decryptionMaterialsOut
		_29_decryptionMaterialsOut = (_28_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
		if !((((_22_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_29_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(244,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhKeyringDiscoverySuccess() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(251,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(253,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_senderArns _dafny.Sequence
	_ = _4_senderArns
	_4_senderArns = _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__S())
	var _5_recipientArns _dafny.Sequence
	_ = _5_recipientArns
	_5_recipientArns = _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__R())
	var _6_curveSpecs _dafny.Sequence
	_ = _6_curveSpecs
	_6_curveSpecs = _dafny.SeqOf(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_4_senderArns).Cardinality())
	_ = _hi0
	for _7_i := _dafny.Zero; _7_i.Cmp(_hi0) < 0; _7_i = _7_i.Plus(_dafny.One) {
		var _8_publicKeyResponse m_Wrappers.Result
		_ = _8_publicKeyResponse
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = (_3_kmsClient).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_((_5_recipientArns).Select((_7_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_None_()))
		_8_publicKeyResponse = _out2
		if !((_8_publicKeyResponse).Is_Success()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(267,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_8_publicKeyResponse).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
		_ = _let_tmp_rhs0
		var _9___v16 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
		_ = _9___v16
		var _10_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
		_ = _10_PublicKey
		var _11___v17 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
		_ = _11___v17
		var _12___v18 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
		_ = _12___v18
		var _13___v19 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
		_ = _13___v19
		var _14___v20 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
		_ = _14___v20
		var _15___v21 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
		_ = _15___v21
		var _16___v22 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
		_ = _16___v22
		if !((_10_PublicKey).Is_Some()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(269,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _17_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _17_valueOrError2
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_((_4_senderArns).Select((_7_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_None_(), (_10_PublicKey).Dtor_value().(_dafny.Sequence))), (_6_curveSpecs).Select((_7_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
		_17_valueOrError2 = _out3
		if !(!((_17_valueOrError2).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(271,28): " + (_17_valueOrError2).String())
		}
		var _18_kmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _18_kmsEcdhKeyring
		_18_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_17_valueOrError2).Extract())
		var _19_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _19_valueOrError3
		var _out4 m_Wrappers.Result
		_ = _out4
		_out4 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPublicKeyDiscovery_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPublicKeyDiscoveryInput_.Create_KmsPublicKeyDiscoveryInput_((_5_recipientArns).Select((_7_i).Uint32()).(_dafny.Sequence))), (_6_curveSpecs).Select((_7_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
		_19_valueOrError3 = _out4
		if !(!((_19_valueOrError3).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(285,37): " + (_19_valueOrError3).String())
		}
		var _20_kmsEcdhKeyringDiscovery m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _20_kmsEcdhKeyringDiscovery
		_20_kmsEcdhKeyringDiscovery = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_19_valueOrError3).Extract())
		var _21_encryptionContext _dafny.Map
		_ = _21_encryptionContext
		var _out5 _dafny.Map
		_ = _out5
		_out5 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
		_21_encryptionContext = _out5
		var _22_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
		_ = _22_algorithmSuiteId
		_22_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
		var _23_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
		_ = _23_suite
		_23_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_22_algorithmSuiteId)
		var _24_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _24_valueOrError4
		_24_valueOrError4 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_22_algorithmSuiteId, _21_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
		if !(!((_24_valueOrError4).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(302,35): " + (_24_valueOrError4).String())
		}
		var _25_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
		_ = _25_encryptionMaterialsIn
		_25_encryptionMaterialsIn = (_24_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
		var _26_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _26_valueOrError5
		var _out6 m_Wrappers.Result
		_ = _out6
		_out6 = (_18_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_25_encryptionMaterialsIn))
		_26_valueOrError5 = _out6
		if !(!((_26_valueOrError5).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(312,36): " + (_26_valueOrError5).String())
		}
		var _27_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
		_ = _27_encryptionMaterialsOut
		_27_encryptionMaterialsOut = (_26_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
		var _28_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = _28_valueOrError6
		_28_valueOrError6 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_27_encryptionMaterialsOut).Dtor_materials())
		if !(!((_28_valueOrError6).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(316,15): " + (_28_valueOrError6).String())
		}
		var _29___v23 _dafny.Tuple
		_ = _29___v23
		_29___v23 = (_28_valueOrError6).Extract().(_dafny.Tuple)
		if !((_dafny.IntOfUint32((((_27_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(318,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _30_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
		_ = _30_edk
		_30_edk = (((_27_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
		var _31_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _31_valueOrError7
		_31_valueOrError7 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_22_algorithmSuiteId, _21_encryptionContext, _dafny.SeqOf()))
		if !(!((_31_valueOrError7).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(321,35): " + (_31_valueOrError7).String())
		}
		var _32_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
		_ = _32_decryptionMaterialsIn
		_32_decryptionMaterialsIn = (_31_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
		_dafny.Print((_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("\nDiscovery Test for: "), (_5_recipientArns).Select((_7_i).Uint32()).(_dafny.Sequence)), _dafny.SeqOfString("\n"))).SetString())
		var _33_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _33_valueOrError8
		var _out7 m_Wrappers.Result
		_ = _out7
		_out7 = (_20_kmsEcdhKeyringDiscovery).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_32_decryptionMaterialsIn, _dafny.SeqOf(_30_edk)))
		_33_valueOrError8 = _out7
		if !(!((_33_valueOrError8).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(329,36): " + (_33_valueOrError8).String())
		}
		var _34_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
		_ = _34_decryptionMaterialsOut
		_34_decryptionMaterialsOut = (_33_valueOrError8).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
		if !((((_27_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_34_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(336,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(343,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(344,22): " + (_2_valueOrError1).String())
	}
	var _3_primitives *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _3_primitives
	_3_primitives = (_2_valueOrError1).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
	_ = _4_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_3_primitives).GenerateECCKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(Companion_Default___.P256()))
	_4_valueOrError2 = _out2
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(346,28): " + (_4_valueOrError2).String())
	}
	var _5_recipientKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_recipientKeypair
	_5_recipientKeypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(352,21): " + (_6_valueOrError3).String())
	}
	var _7_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClient
	_7_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError3).Extract())
	var _8_publicKeyResponse m_Wrappers.Result
	_ = _8_publicKeyResponse
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_7_kmsClient).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_Wrappers.Companion_Option_.Create_None_()))
	_8_publicKeyResponse = _out4
	if !((_8_publicKeyResponse).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(359,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_8_publicKeyResponse).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
	_ = _let_tmp_rhs0
	var _9___v24 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
	_ = _9___v24
	var _10_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
	_ = _10_PublicKey
	var _11___v25 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
	_ = _11___v25
	var _12___v26 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
	_ = _12___v26
	var _13___v27 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
	_ = _13___v27
	var _14___v28 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
	_ = _14___v28
	var _15___v29 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
	_ = _15___v29
	var _16___v30 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
	_ = _16___v30
	if !((_10_PublicKey).Is_Some()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(362,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _17_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError4
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_Wrappers.Companion_Option_.Create_Some_((_10_PublicKey).Dtor_value().(_dafny.Sequence)), ((_5_recipientKeypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), _7_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_17_valueOrError4 = _out5
	if !(!((_17_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(364,26): " + (_17_valueOrError4).String())
	}
	var _18_kmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _18_kmsEcdhKeyring
	_18_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_17_valueOrError4).Extract())
	var _19_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError5
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(((_5_recipientKeypair).Dtor_privateKey()).Dtor_pem(), (_10_PublicKey).Dtor_value().(_dafny.Sequence))), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_19_valueOrError5 = _out6
	if !(!((_19_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(379,28): " + (_19_valueOrError5).String())
	}
	var _20_recipientKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _20_recipientKeyring
	_20_recipientKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_19_valueOrError5).Extract())
	var _21_encryptionContext _dafny.Map
	_ = _21_encryptionContext
	var _out7 _dafny.Map
	_ = _out7
	_out7 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_21_encryptionContext = _out7
	var _22_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _22_algorithmSuiteId
	_22_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _23_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	_ = _23_suite
	_23_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_22_algorithmSuiteId)
	var _24_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _24_valueOrError6
	_24_valueOrError6 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_22_algorithmSuiteId, _21_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_24_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(395,33): " + (_24_valueOrError6).String())
	}
	var _25_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _25_encryptionMaterialsIn
	_25_encryptionMaterialsIn = (_24_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _26_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _26_valueOrError7
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_18_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_25_encryptionMaterialsIn))
	_26_valueOrError7 = _out8
	if !(!((_26_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(405,34): " + (_26_valueOrError7).String())
	}
	var _27_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _27_encryptionMaterialsOut
	_27_encryptionMaterialsOut = (_26_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _28_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _28_valueOrError8
	_28_valueOrError8 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_27_encryptionMaterialsOut).Dtor_materials())
	if !(!((_28_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(409,13): " + (_28_valueOrError8).String())
	}
	var _29___v31 _dafny.Tuple
	_ = _29___v31
	_29___v31 = (_28_valueOrError8).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_27_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(411,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _30_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _30_edk
	_30_edk = (((_27_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _31_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _31_valueOrError9
	_31_valueOrError9 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_22_algorithmSuiteId, _21_encryptionContext, _dafny.SeqOf()))
	if !(!((_31_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(414,33): " + (_31_valueOrError9).String())
	}
	var _32_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _32_decryptionMaterialsIn
	_32_decryptionMaterialsIn = (_31_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _33_valueOrError10 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _33_valueOrError10
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_20_recipientKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_32_decryptionMaterialsIn, _dafny.SeqOf(_30_edk)))
	_33_valueOrError10 = _out9
	if !(!((_33_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(421,34): " + (_33_valueOrError10).String())
	}
	var _34_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _34_decryptionMaterialsOut
	_34_decryptionMaterialsOut = (_33_valueOrError10).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_27_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_34_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(428,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhKeyringWithDerPublicKeys() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(434,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(436,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.CURVES()).Cardinality())
	_ = _hi0
	for _4_i := _dafny.Zero; _4_i.Cmp(_hi0) < 0; _4_i = _4_i.Plus(_dafny.One) {
		var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _5_valueOrError2
		_5_valueOrError2 = m_Base64.Companion_Default___.Decode((Companion_Default___.DerKmsSenderPublicKeyStrings()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_5_valueOrError2).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(440,29): " + (_5_valueOrError2).String())
		}
		var _6_senderPublicKey _dafny.Sequence
		_ = _6_senderPublicKey
		_6_senderPublicKey = (_5_valueOrError2).Extract().(_dafny.Sequence)
		var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _7_valueOrError3
		_7_valueOrError3 = m_Base64.Companion_Default___.Decode((Companion_Default___.DerKmsRecipientPublicKeyStrings()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_7_valueOrError3).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(441,32): " + (_7_valueOrError3).String())
		}
		var _8_recipientPublicKey _dafny.Sequence
		_ = _8_recipientPublicKey
		_8_recipientPublicKey = (_7_valueOrError3).Extract().(_dafny.Sequence)
		var _9_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _9_valueOrError4
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_((Companion_Default___.SenderKmsKeys()).Select((_4_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_Some_(_6_senderPublicKey), _8_recipientPublicKey)), (Companion_Default___.CURVES()).Select((_4_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
		_9_valueOrError4 = _out2
		if !(!((_9_valueOrError4).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(443,34): " + (_9_valueOrError4).String())
		}
		var _10_senderKmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _10_senderKmsEcdhKeyring
		_10_senderKmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_9_valueOrError4).Extract())
		var _11_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _11_valueOrError5
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_((Companion_Default___.RecipientKmsKeys()).Select((_4_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_Some_(_8_recipientPublicKey), _6_senderPublicKey)), (Companion_Default___.CURVES()).Select((_4_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
		_11_valueOrError5 = _out3
		if !(!((_11_valueOrError5).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(458,37): " + (_11_valueOrError5).String())
		}
		var _12_recipientKmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _12_recipientKmsEcdhKeyring
		_12_recipientKmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_11_valueOrError5).Extract())
		var _13_encryptionContext _dafny.Map
		_ = _13_encryptionContext
		var _out4 _dafny.Map
		_ = _out4
		_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
		_13_encryptionContext = _out4
		var _14_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
		_ = _14_algorithmSuiteId
		_14_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
		var _15_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
		_ = _15_suite
		_15_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_14_algorithmSuiteId)
		var _16_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _16_valueOrError6
		_16_valueOrError6 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_14_algorithmSuiteId, _13_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
		if !(!((_16_valueOrError6).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(477,35): " + (_16_valueOrError6).String())
		}
		var _17_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
		_ = _17_encryptionMaterialsIn
		_17_encryptionMaterialsIn = (_16_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
		var _18_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _18_valueOrError7
		var _out5 m_Wrappers.Result
		_ = _out5
		_out5 = (_10_senderKmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_17_encryptionMaterialsIn))
		_18_valueOrError7 = _out5
		if !(!((_18_valueOrError7).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(487,36): " + (_18_valueOrError7).String())
		}
		var _19_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
		_ = _19_encryptionMaterialsOut
		_19_encryptionMaterialsOut = (_18_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
		var _20_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = _20_valueOrError8
		_20_valueOrError8 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_19_encryptionMaterialsOut).Dtor_materials())
		if !(!((_20_valueOrError8).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(491,15): " + (_20_valueOrError8).String())
		}
		var _21___v32 _dafny.Tuple
		_ = _21___v32
		_21___v32 = (_20_valueOrError8).Extract().(_dafny.Tuple)
		if !((_dafny.IntOfUint32((((_19_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(493,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _22_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
		_ = _22_edk
		_22_edk = (((_19_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
		var _23_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _23_valueOrError9
		_23_valueOrError9 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_14_algorithmSuiteId, _13_encryptionContext, _dafny.SeqOf()))
		if !(!((_23_valueOrError9).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(496,35): " + (_23_valueOrError9).String())
		}
		var _24_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
		_ = _24_decryptionMaterialsIn
		_24_decryptionMaterialsIn = (_23_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
		var _25_valueOrError10 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _25_valueOrError10
		var _out6 m_Wrappers.Result
		_ = _out6
		_out6 = (_12_recipientKmsEcdhKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_24_decryptionMaterialsIn, _dafny.SeqOf(_22_edk)))
		_25_valueOrError10 = _out6
		if !(!((_25_valueOrError10).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(503,36): " + (_25_valueOrError10).String())
		}
		var _26_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
		_ = _26_decryptionMaterialsOut
		_26_decryptionMaterialsOut = (_25_valueOrError10).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
		if !((((_19_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_26_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(510,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhRawEcdhKeyringWithDerPublicKeys() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(518,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(520,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _hi0 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.CURVES()).Cardinality())
	_ = _hi0
	for _4_i := _dafny.Zero; _4_i.Cmp(_hi0) < 0; _4_i = _4_i.Plus(_dafny.One) {
		var _5_senderKmsKey _dafny.Sequence
		_ = _5_senderKmsKey
		_5_senderKmsKey = (Companion_Default___.SenderKmsKeys()).Select((_4_i).Uint32()).(_dafny.Sequence)
		var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _6_valueOrError2
		_6_valueOrError2 = m_Base64.Companion_Default___.Decode((Companion_Default___.DerKmsSenderPublicKeyStrings()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_6_valueOrError2).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(525,29): " + (_6_valueOrError2).String())
		}
		var _7_senderPublicKey _dafny.Sequence
		_ = _7_senderPublicKey
		_7_senderPublicKey = (_6_valueOrError2).Extract().(_dafny.Sequence)
		var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
		_ = _8_valueOrError3
		_8_valueOrError3 = m_UTF8.Encode((Companion_Default___.RawEccPrivateKeys()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_8_valueOrError3).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(526,33): " + (_8_valueOrError3).String())
		}
		var _9_recipientPrivateKey _dafny.Sequence
		_ = _9_recipientPrivateKey
		_9_recipientPrivateKey = (_8_valueOrError3).Extract().(_dafny.Sequence)
		var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _10_valueOrError4
		_10_valueOrError4 = m_Base64.Companion_Default___.Decode((Companion_Default___.RawEccPublicKeysB64der()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_10_valueOrError4).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(527,32): " + (_10_valueOrError4).String())
		}
		var _11_recipientPublicKey _dafny.Sequence
		_ = _11_recipientPublicKey
		_11_recipientPublicKey = (_10_valueOrError4).Extract().(_dafny.Sequence)
		var _12_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _12_curve
		_12_curve = (Companion_Default___.CURVES()).Select((_4_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _13_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _13_valueOrError5
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_5_senderKmsKey, m_Wrappers.Companion_Option_.Create_Some_(_7_senderPublicKey), _11_recipientPublicKey)), _12_curve, _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
		_13_valueOrError5 = _out2
		if !(!((_13_valueOrError5).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(530,34): " + (_13_valueOrError5).String())
		}
		var _14_senderKmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _14_senderKmsEcdhKeyring
		_14_senderKmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_13_valueOrError5).Extract())
		var _15_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _15_valueOrError6
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_9_recipientPrivateKey, _7_senderPublicKey)), _12_curve))
		_15_valueOrError6 = _out3
		if !(!((_15_valueOrError6).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(545,33): " + (_15_valueOrError6).String())
		}
		var _16_recipientRawKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
		_ = _16_recipientRawKeyring
		_16_recipientRawKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_15_valueOrError6).Extract())
		var _17_encryptionContext _dafny.Map
		_ = _17_encryptionContext
		var _out4 _dafny.Map
		_ = _out4
		_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
		_17_encryptionContext = _out4
		var _18_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
		_ = _18_algorithmSuiteId
		_18_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
		var _19_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
		_ = _19_suite
		_19_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_18_algorithmSuiteId)
		var _20_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _20_valueOrError7
		_20_valueOrError7 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_18_algorithmSuiteId, _17_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
		if !(!((_20_valueOrError7).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(561,35): " + (_20_valueOrError7).String())
		}
		var _21_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
		_ = _21_encryptionMaterialsIn
		_21_encryptionMaterialsIn = (_20_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
		var _22_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _22_valueOrError8
		var _out5 m_Wrappers.Result
		_ = _out5
		_out5 = (_14_senderKmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_21_encryptionMaterialsIn))
		_22_valueOrError8 = _out5
		if !(!((_22_valueOrError8).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(571,36): " + (_22_valueOrError8).String())
		}
		var _23_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
		_ = _23_encryptionMaterialsOut
		_23_encryptionMaterialsOut = (_22_valueOrError8).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
		var _24_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = _24_valueOrError9
		_24_valueOrError9 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_23_encryptionMaterialsOut).Dtor_materials())
		if !(!((_24_valueOrError9).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(575,15): " + (_24_valueOrError9).String())
		}
		var _25___v33 _dafny.Tuple
		_ = _25___v33
		_25___v33 = (_24_valueOrError9).Extract().(_dafny.Tuple)
		if !((_dafny.IntOfUint32((((_23_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(577,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _26_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
		_ = _26_edk
		_26_edk = (((_23_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
		var _27_valueOrError10 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _27_valueOrError10
		_27_valueOrError10 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_18_algorithmSuiteId, _17_encryptionContext, _dafny.SeqOf()))
		if !(!((_27_valueOrError10).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(580,35): " + (_27_valueOrError10).String())
		}
		var _28_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
		_ = _28_decryptionMaterialsIn
		_28_decryptionMaterialsIn = (_27_valueOrError10).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
		var _29_valueOrError11 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _29_valueOrError11
		var _out6 m_Wrappers.Result
		_ = _out6
		_out6 = (_16_recipientRawKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_28_decryptionMaterialsIn, _dafny.SeqOf(_26_edk)))
		_29_valueOrError11 = _out6
		if !(!((_29_valueOrError11).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(587,36): " + (_29_valueOrError11).String())
		}
		var _30_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
		_ = _30_decryptionMaterialsOut
		_30_decryptionMaterialsOut = (_29_valueOrError11).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
		if !((((_23_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_30_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(594,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(603,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(605,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _4_valueOrError2
	_4_valueOrError2 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__256__PUBLIC__KEY__S())
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(607,27): " + (_4_valueOrError2).String())
	}
	var _5_senderPublicKey _dafny.Sequence
	_ = _5_senderPublicKey
	_5_senderPublicKey = (_4_valueOrError2).Extract().(_dafny.Sequence)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _6_valueOrError3
	_6_valueOrError3 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__256__PUBLIC__KEY__R())
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(608,30): " + (_6_valueOrError3).String())
	}
	var _7_recipientPublicKey _dafny.Sequence
	_ = _7_recipientPublicKey
	_7_recipientPublicKey = (_6_valueOrError3).Extract().(_dafny.Sequence)
	var _8_senderKmsEcdhKeyring m_Wrappers.Result
	_ = _8_senderKmsEcdhKeyring
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_Wrappers.Companion_Option_.Create_Some_(_5_senderPublicKey), _7_recipientPublicKey)), Companion_Default___.P384(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_8_senderKmsEcdhKeyring = _out2
	if !((_8_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(625,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(630,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(632,21): " + (_2_valueOrError1).String())
	}
	var _3_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _3_kmsClient
	_3_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_senderKmsKey256 _dafny.Sequence
	_ = _4_senderKmsKey256
	_4_senderKmsKey256 = m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S()
	var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _5_valueOrError2
	_5_valueOrError2 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__256__PUBLIC__KEY__S())
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(635,33): " + (_5_valueOrError2).String())
	}
	var _6_senderPublicKey256 _dafny.Sequence
	_ = _6_senderPublicKey256
	_6_senderPublicKey256 = (_5_valueOrError2).Extract().(_dafny.Sequence)
	var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _7_valueOrError3
	_7_valueOrError3 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P256__PUBLIC__R())
	if !(!((_7_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(636,33): " + (_7_valueOrError3).String())
	}
	var _8_recipientPublicKey256 _dafny.Sequence
	_ = _8_recipientPublicKey256
	_8_recipientPublicKey256 = (_7_valueOrError3).Extract().(_dafny.Sequence)
	var _9_senderKmsKey384 _dafny.Sequence
	_ = _9_senderKmsKey384
	_9_senderKmsKey384 = m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__S()
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _10_valueOrError4
	_10_valueOrError4 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__384__PUBLIC__KEY__S())
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(639,33): " + (_10_valueOrError4).String())
	}
	var _11_senderPublicKey384 _dafny.Sequence
	_ = _11_senderPublicKey384
	_11_senderPublicKey384 = (_10_valueOrError4).Extract().(_dafny.Sequence)
	var _12_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _12_valueOrError5
	_12_valueOrError5 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P384__PUBLIC__R())
	if !(!((_12_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(640,33): " + (_12_valueOrError5).String())
	}
	var _13_recipientPublicKey384 _dafny.Sequence
	_ = _13_recipientPublicKey384
	_13_recipientPublicKey384 = (_12_valueOrError5).Extract().(_dafny.Sequence)
	var _14_senderKmsKey521 _dafny.Sequence
	_ = _14_senderKmsKey521
	_14_senderKmsKey521 = m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__S()
	var _15_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _15_valueOrError6
	_15_valueOrError6 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__521__PUBLIC__KEY__S())
	if !(!((_15_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(643,33): " + (_15_valueOrError6).String())
	}
	var _16_senderPublicKey521 _dafny.Sequence
	_ = _16_senderPublicKey521
	_16_senderPublicKey521 = (_15_valueOrError6).Extract().(_dafny.Sequence)
	var _17_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _17_valueOrError7
	_17_valueOrError7 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P521__PUBLIC__R())
	if !(!((_17_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(644,33): " + (_17_valueOrError7).String())
	}
	var _18_recipientPublicKey521 _dafny.Sequence
	_ = _18_recipientPublicKey521
	_18_recipientPublicKey521 = (_17_valueOrError7).Extract().(_dafny.Sequence)
	var _19_senderKmsEcdhKeyring m_Wrappers.Result
	_ = _19_senderKmsEcdhKeyring
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_4_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_6_senderPublicKey256), _8_recipientPublicKey256)), Companion_Default___.P384(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out2
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(662,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_4_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_6_senderPublicKey256), _8_recipientPublicKey256)), Companion_Default___.P521(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out3
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_9_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_11_senderPublicKey384), _13_recipientPublicKey384)), Companion_Default___.P256(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out4
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(694,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_9_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_11_senderPublicKey384), _13_recipientPublicKey384)), Companion_Default___.P521(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out5
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_14_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_16_senderPublicKey521), _18_recipientPublicKey521)), Companion_Default___.P256(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out6
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(726,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_14_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_16_senderPublicKey521), _18_recipientPublicKey521)), Companion_Default___.P384(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out7
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_4_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_6_senderPublicKey256), _13_recipientPublicKey384)), Companion_Default___.P256(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out8
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(759,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_4_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_6_senderPublicKey256), _18_recipientPublicKey521)), Companion_Default___.P256(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out9
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(775,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_9_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_11_senderPublicKey384), _8_recipientPublicKey256)), Companion_Default___.P384(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out10
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(792,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_9_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_11_senderPublicKey384), _18_recipientPublicKey521)), Companion_Default___.P384(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out11
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(808,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out12 m_Wrappers.Result
	_ = _out12
	_out12 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_14_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_16_senderPublicKey521), _8_recipientPublicKey256)), Companion_Default___.P521(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out12
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(825,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out13 m_Wrappers.Result
	_ = _out13
	_out13 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_14_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_16_senderPublicKey521), _13_recipientPublicKey384)), Companion_Default___.P521(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out13
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(841,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out14 m_Wrappers.Result
	_ = _out14
	_out14 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_9_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_11_senderPublicKey384), _8_recipientPublicKey256)), Companion_Default___.P256(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out14
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(860,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out15 m_Wrappers.Result
	_ = _out15
	_out15 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_14_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_16_senderPublicKey521), _8_recipientPublicKey256)), Companion_Default___.P256(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out15
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(876,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out16 m_Wrappers.Result
	_ = _out16
	_out16 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_4_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_6_senderPublicKey256), _13_recipientPublicKey384)), Companion_Default___.P384(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out16
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(893,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out17 m_Wrappers.Result
	_ = _out17
	_out17 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_14_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_16_senderPublicKey521), _13_recipientPublicKey384)), Companion_Default___.P384(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out17
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(909,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out18 m_Wrappers.Result
	_ = _out18
	_out18 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_4_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_6_senderPublicKey256), _18_recipientPublicKey521)), Companion_Default___.P521(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out18
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(926,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out19 m_Wrappers.Result
	_ = _out19
	_out19 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_9_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_11_senderPublicKey384), _18_recipientPublicKey521)), Companion_Default___.P521(), _3_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_senderKmsEcdhKeyring = _out19
	if !((_19_senderKmsEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(942,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestLyingKmsKey() {
	var _0_senderKmsKey256 _dafny.Sequence
	_ = _0_senderKmsKey256
	_0_senderKmsKey256 = m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S()
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _1_valueOrError0
	_1_valueOrError0 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__256__PUBLIC__KEY__S())
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(948,33): " + (_1_valueOrError0).String())
	}
	var _2_senderPublicKey256 _dafny.Sequence
	_ = _2_senderPublicKey256
	_2_senderPublicKey256 = (_1_valueOrError0).Extract().(_dafny.Sequence)
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _3_valueOrError1
	_3_valueOrError1 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P256__PUBLIC__R())
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(949,33): " + (_3_valueOrError1).String())
	}
	var _4_recipientPublicKey256 _dafny.Sequence
	_ = _4_recipientPublicKey256
	_4_recipientPublicKey256 = (_3_valueOrError1).Extract().(_dafny.Sequence)
	var _5_senderKmsKey384 _dafny.Sequence
	_ = _5_senderKmsKey384
	_5_senderKmsKey384 = m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__S()
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _6_valueOrError2
	_6_valueOrError2 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__384__PUBLIC__KEY__S())
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(952,33): " + (_6_valueOrError2).String())
	}
	var _7_senderPublicKey384 _dafny.Sequence
	_ = _7_senderPublicKey384
	_7_senderPublicKey384 = (_6_valueOrError2).Extract().(_dafny.Sequence)
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _8_valueOrError3
	_8_valueOrError3 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P384__PUBLIC__R())
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(953,33): " + (_8_valueOrError3).String())
	}
	var _9_recipientPublicKey384 _dafny.Sequence
	_ = _9_recipientPublicKey384
	_9_recipientPublicKey384 = (_8_valueOrError3).Extract().(_dafny.Sequence)
	var _10_senderKmsKey521 _dafny.Sequence
	_ = _10_senderKmsKey521
	_10_senderKmsKey521 = m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__S()
	var _11_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _11_valueOrError4
	_11_valueOrError4 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.KMS__ECC__521__PUBLIC__KEY__S())
	if !(!((_11_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(956,33): " + (_11_valueOrError4).String())
	}
	var _12_senderPublicKey521 _dafny.Sequence
	_ = _12_senderPublicKey521
	_12_senderPublicKey521 = (_11_valueOrError4).Extract().(_dafny.Sequence)
	var _13_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _13_valueOrError5
	_13_valueOrError5 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P521__PUBLIC__R())
	if !(!((_13_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(957,33): " + (_13_valueOrError5).String())
	}
	var _14_recipientPublicKey521 _dafny.Sequence
	_ = _14_recipientPublicKey521
	_14_recipientPublicKey521 = (_13_valueOrError5).Extract().(_dafny.Sequence)
	var _15_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _15_valueOrError6
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_15_valueOrError6 = _out0
	if !(!((_15_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(959,15): " + (_15_valueOrError6).String())
	}
	var _16_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _16_mpl
	_16_mpl = (_15_valueOrError6).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _17_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError7
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_17_valueOrError7 = _out1
	if !(!((_17_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(961,21): " + (_17_valueOrError7).String())
	}
	var _18_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _18_kmsClient
	_18_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_17_valueOrError7).Extract())
	var _19_encryptionContext _dafny.Map
	_ = _19_encryptionContext
	var _out2 _dafny.Map
	_ = _out2
	_out2 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_19_encryptionContext = _out2
	var _20_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _20_algorithmSuiteId
	_20_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _21_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	_ = _21_suite
	_21_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_20_algorithmSuiteId)
	var _22_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _22_valueOrError8
	_22_valueOrError8 = (_16_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_20_algorithmSuiteId, _19_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_22_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(967,33): " + (_22_valueOrError8).String())
	}
	var _23_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _23_encryptionMaterialsIn
	_23_encryptionMaterialsIn = (_22_valueOrError8).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _24_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _24_valueOrError9
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_16_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_5_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_2_senderPublicKey256), _4_recipientPublicKey256)), Companion_Default___.P256(), _18_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_24_valueOrError9 = _out3
	if !(!((_24_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(985,26): " + (_24_valueOrError9).String())
	}
	var _25_kmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _25_kmsEcdhKeyring
	_25_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_24_valueOrError9).Extract())
	var _26_encryptionMaterialsOut m_Wrappers.Result
	_ = _26_encryptionMaterialsOut
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_25_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_23_encryptionMaterialsIn))
	_26_encryptionMaterialsOut = _out4
	if !((_26_encryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1002,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _27_valueOrError10 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _27_valueOrError10
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_16_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_10_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_2_senderPublicKey256), _4_recipientPublicKey256)), Companion_Default___.P256(), _18_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_27_valueOrError10 = _out5
	if !(!((_27_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1004,22): " + (_27_valueOrError10).String())
	}
	_25_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_27_valueOrError10).Extract())
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_25_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_23_encryptionMaterialsIn))
	_26_encryptionMaterialsOut = _out6
	if !((_26_encryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1021,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _28_valueOrError11 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _28_valueOrError11
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_16_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_0_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_7_senderPublicKey384), _9_recipientPublicKey384)), Companion_Default___.P384(), _18_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_28_valueOrError11 = _out7
	if !(!((_28_valueOrError11).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1024,22): " + (_28_valueOrError11).String())
	}
	_25_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_28_valueOrError11).Extract())
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_25_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_23_encryptionMaterialsIn))
	_26_encryptionMaterialsOut = _out8
	if !((_26_encryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1041,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _29_valueOrError12 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _29_valueOrError12
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_16_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_10_senderKmsKey521, m_Wrappers.Companion_Option_.Create_Some_(_7_senderPublicKey384), _9_recipientPublicKey384)), Companion_Default___.P384(), _18_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_29_valueOrError12 = _out9
	if !(!((_29_valueOrError12).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1043,22): " + (_29_valueOrError12).String())
	}
	_25_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_29_valueOrError12).Extract())
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_25_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_23_encryptionMaterialsIn))
	_26_encryptionMaterialsOut = _out10
	if !((_26_encryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1060,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _30_valueOrError13 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _30_valueOrError13
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_16_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_0_senderKmsKey256, m_Wrappers.Companion_Option_.Create_Some_(_12_senderPublicKey521), _14_recipientPublicKey521)), Companion_Default___.P521(), _18_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_30_valueOrError13 = _out11
	if !(!((_30_valueOrError13).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1063,22): " + (_30_valueOrError13).String())
	}
	_25_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_30_valueOrError13).Extract())
	var _out12 m_Wrappers.Result
	_ = _out12
	_out12 = (_25_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_23_encryptionMaterialsIn))
	_26_encryptionMaterialsOut = _out12
	if !((_26_encryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1080,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _31_valueOrError14 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _31_valueOrError14
	var _out13 m_Wrappers.Result
	_ = _out13
	_out13 = (_16_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_5_senderKmsKey384, m_Wrappers.Companion_Option_.Create_Some_(_12_senderPublicKey521), _14_recipientPublicKey521)), Companion_Default___.P521(), _18_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_31_valueOrError14 = _out13
	if !(!((_31_valueOrError14).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1082,22): " + (_31_valueOrError14).String())
	}
	_25_kmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_31_valueOrError14).Extract())
	var _out14 m_Wrappers.Result
	_ = _out14
	_out14 = (_25_kmsEcdhKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_23_encryptionMaterialsIn))
	_26_encryptionMaterialsOut = _out14
	if !((_26_encryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1099,4): " + (_dafny.SeqOfString("expectation violation")).String())
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
func (_static *CompanionStruct_Default___) CURVES() _dafny.Sequence {
	return _dafny.SeqOf(Companion_Default___.P256(), Companion_Default___.P384(), Companion_Default___.P521())
}
func (_static *CompanionStruct_Default___) TEST__DBE__ALG__SUITE__ID() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_DBE_(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384_())
}
func (_static *CompanionStruct_Default___) DerKmsSenderPublicKeyStrings() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__PUBLIC__KEY__S(), m_TestUtils.Companion_Default___.KMS__ECC__384__PUBLIC__KEY__S(), m_TestUtils.Companion_Default___.KMS__ECC__521__PUBLIC__KEY__S())
}
func (_static *CompanionStruct_Default___) DerKmsRecipientPublicKeyStrings() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__PUBLIC__KEY__R(), m_TestUtils.Companion_Default___.KMS__ECC__384__PUBLIC__KEY__R(), m_TestUtils.Companion_Default___.KMS__ECC__521__PUBLIC__KEY__R())
}
func (_static *CompanionStruct_Default___) SenderKmsKeys() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__S())
}
func (_static *CompanionStruct_Default___) RecipientKmsKeys() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__R(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__R())
}
func (_static *CompanionStruct_Default___) RawEccPrivateKeys() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.ECC__P256__PRIVATE(), m_TestUtils.Companion_Default___.ECC__P384__PRIVATE(), m_TestUtils.Companion_Default___.ECC__P521__PRIVATE())
}
func (_static *CompanionStruct_Default___) RawEccPublicKeysB64der() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.ECC__P256__PUBLIC(), m_TestUtils.Companion_Default___.ECC__P384__PUBLIC(), m_TestUtils.Companion_Default___.ECC__P521__PUBLIC())
}

// End of class Default__
