// Package TestMultiKeyring
// Dafny module TestMultiKeyring compiled into Go

package TestMultiKeyring

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
	m_TestAwsKmsHierarchicalKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestAwsKmsHierarchicalKeyring"
	m_TestAwsKmsRsaKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestAwsKmsRsaKeyring"
	m_TestConfig "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestConfig"
	m_TestCreateKeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeyStore"
	m_TestCreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeys"
	m_TestDiscoveryGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestDiscoveryGetKeys"
	m_TestErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestErrorMessages"
	m_TestGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestGetKeys"
	m_TestLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLocalCMC"
	m_TestLyingBranchKey "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLyingBranchKey"
	m_TestRawAESKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestRawAESKeyring"
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
var _ m_TestAwsKmsHierarchicalKeyring.Dummy__
var _ m_TestAwsKmsRsaKeyring.Dummy__
var _ m_TestRawAESKeyring.Dummy__

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
	return "TestMultiKeyring.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) GetInputEncryptionMaterials(encryptionContext _dafny.Map) m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials {
	var res m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials{}
	_ = res
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(18,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _2_algorithmSuiteId
	_2_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _3_valueOrError1
	_3_valueOrError1 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_2_algorithmSuiteId, encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(21,33): " + (_3_valueOrError1).String())
	}
	var _4_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _4_encryptionMaterialsIn
	_4_encryptionMaterialsIn = (_3_valueOrError1).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	res = _4_encryptionMaterialsIn
	return res
	return res
}
func (_static *CompanionStruct_Default___) GetInputDecryptionMaterials(encryptionContext _dafny.Map) m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials {
	var res m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials{}
	_ = res
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(35,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _2_algorithmSuiteId
	_2_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _3_valueOrError1
	_3_valueOrError1 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_2_algorithmSuiteId, encryptionContext, _dafny.SeqOf()))
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(38,33): " + (_3_valueOrError1).String())
	}
	var _4_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _4_decryptionMaterialsIn
	_4_decryptionMaterialsIn = (_3_valueOrError1).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	res = _4_decryptionMaterialsIn
	return res
	return res
}
func (_static *CompanionStruct_Default___) TestHappyCase() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(51,15): " + (_0_valueOrError0).String())
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
	var _3_encryptionMaterials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _3_encryptionMaterials
	var _out2 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out2
	_out2 = Companion_Default___.GetInputEncryptionMaterials(_2_encryptionContext)
	_3_encryptionMaterials = _out2
	var _4_decryptionMaterials m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _4_decryptionMaterials
	var _out3 m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _out3
	_out3 = Companion_Default___.GetInputDecryptionMaterials(_2_encryptionContext)
	_4_decryptionMaterials = _out3
	var _5_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _5_rawAESKeyring
	var _out4 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out4
	_out4 = Companion_Default___.SetupRawAesKeyring(_2_encryptionContext)
	_5_rawAESKeyring = _out4
	var _6_expectedEncryptionMaterials m_Wrappers.Result
	_ = _6_expectedEncryptionMaterials
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_5_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_3_encryptionMaterials))
	_6_expectedEncryptionMaterials = _out5
	if !((_6_expectedEncryptionMaterials).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(63,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _7_expectedPlaintextDataKey m_Wrappers.Option
	_ = _7_expectedPlaintextDataKey
	_7_expectedPlaintextDataKey = (((_6_expectedEncryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)).Dtor_materials()).Dtor_plaintextDataKey()
	if !((_7_expectedPlaintextDataKey).Is_Some()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(65,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_staticKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _8_staticKeyring
	var _out6 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out6
	_out6 = Companion_Default___.SetupStaticKeyring(m_Wrappers.Companion_Option_.Create_Some_(((_6_expectedEncryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)).Dtor_materials()), m_Wrappers.Companion_Option_.Create_None_())
	_8_staticKeyring = _out6
	var _9_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError1
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_1_mpl).CreateMultiKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_8_staticKeyring), _dafny.SeqOf(_5_rawAESKeyring)))
	_9_valueOrError1 = _out7
	if !(!((_9_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(69,24): " + (_9_valueOrError1).String())
	}
	var _10_multiKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _10_multiKeyring
	_10_multiKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_9_valueOrError1).Extract())
	var _11_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _11_valueOrError2
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_10_multiKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_3_encryptionMaterials))
	_11_valueOrError2 = _out8
	if !(!((_11_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(74,34): " + (_11_valueOrError2).String())
	}
	var _12_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _12_encryptionMaterialsOut
	_12_encryptionMaterialsOut = (_11_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _13_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _13_valueOrError3
	_13_valueOrError3 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).Dtor_materials())
	if !(!((_13_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(76,13): " + (_13_valueOrError3).String())
	}
	var _14___v0 _dafny.Tuple
	_ = _14___v0
	_14___v0 = (_13_valueOrError3).Extract().(_dafny.Tuple)
	if !(_dafny.Companion_Sequence_.Equal((((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Dtor_value().(_dafny.Sequence), (_7_expectedPlaintextDataKey).Dtor_value().(_dafny.Sequence))) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(87,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.IntOfInt64(2)) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(101,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestChildKeyringFailureEncrypt() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(106,15): " + (_0_valueOrError0).String())
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
	var _3_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _3_rawAESKeyring
	var _out2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out2
	_out2 = Companion_Default___.SetupRawAesKeyring(_2_encryptionContext)
	_3_rawAESKeyring = _out2
	var _4_failingKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _4_failingKeyring
	var _out3 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out3
	_out3 = Companion_Default___.SetupFailingKeyring()
	_4_failingKeyring = _out3
	var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _5_valueOrError1
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateMultiKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_3_rawAESKeyring), _dafny.SeqOf(_4_failingKeyring)))
	_5_valueOrError1 = _out4
	if !(!((_5_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(116,24): " + (_5_valueOrError1).String())
	}
	var _6_multiKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_multiKeyring
	_6_multiKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_5_valueOrError1).Extract())
	var _7_encryptionMaterials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _7_encryptionMaterials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetInputEncryptionMaterials(_2_encryptionContext)
	_7_encryptionMaterials = _out5
	var _8_result m_Wrappers.Result
	_ = _8_result
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_6_multiKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_7_encryptionMaterials))
	_8_result = _out6
	if !((_8_result).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(124,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGeneratorKeyringFails() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(129,15): " + (_0_valueOrError0).String())
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
	var _3_failingKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _3_failingKeyring
	var _out2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out2
	_out2 = Companion_Default___.SetupFailingKeyring()
	_3_failingKeyring = _out2
	var _4_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _4_rawAESKeyring
	var _out3 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out3
	_out3 = Companion_Default___.SetupRawAesKeyring(_2_encryptionContext)
	_4_rawAESKeyring = _out3
	var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _5_valueOrError1
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateMultiKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_3_failingKeyring), _dafny.SeqOf(_4_rawAESKeyring)))
	_5_valueOrError1 = _out4
	if !(!((_5_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(142,24): " + (_5_valueOrError1).String())
	}
	var _6_multiKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_multiKeyring
	_6_multiKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_5_valueOrError1).Extract())
	var _7_encryptionMaterials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _7_encryptionMaterials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetInputEncryptionMaterials(_2_encryptionContext)
	_7_encryptionMaterials = _out5
	var _8_result m_Wrappers.Result
	_ = _8_result
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_6_multiKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_7_encryptionMaterials))
	_8_result = _out6
	if !((_8_result).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(150,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGeneratorKeyringDoesNotReturnPlaintextDataKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(155,15): " + (_0_valueOrError0).String())
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
	var _3_encryptionMaterials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _3_encryptionMaterials
	var _out2 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out2
	_out2 = Companion_Default___.GetInputEncryptionMaterials(_2_encryptionContext)
	_3_encryptionMaterials = _out2
	var _4_failingKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _4_failingKeyring
	var _out3 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out3
	_out3 = Companion_Default___.SetupStaticKeyring(m_Wrappers.Companion_Option_.Create_Some_(_3_encryptionMaterials), m_Wrappers.Companion_Option_.Create_None_())
	_4_failingKeyring = _out3
	var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _5_valueOrError1
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateMultiKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_4_failingKeyring), _dafny.SeqOf()))
	_5_valueOrError1 = _out4
	if !(!((_5_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(165,24): " + (_5_valueOrError1).String())
	}
	var _6_multiKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_multiKeyring
	_6_multiKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_5_valueOrError1).Extract())
	var _7_result m_Wrappers.Result
	_ = _7_result
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_6_multiKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_3_encryptionMaterials))
	_7_result = _out5
	if !((_7_result).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(171,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGeneratorAbleToDecrypt() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(176,15): " + (_0_valueOrError0).String())
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
	var _3_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _3_rawAESKeyring
	var _out2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out2
	_out2 = Companion_Default___.SetupRawAesKeyring(_2_encryptionContext)
	_3_rawAESKeyring = _out2
	var _4_inputEncryptionMaterials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _4_inputEncryptionMaterials
	var _out3 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out3
	_out3 = Companion_Default___.GetInputEncryptionMaterials(_2_encryptionContext)
	_4_inputEncryptionMaterials = _out3
	var _5_encryptionMaterials m_Wrappers.Result
	_ = _5_encryptionMaterials
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_3_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_4_inputEncryptionMaterials))
	_5_encryptionMaterials = _out4
	if !((_5_encryptionMaterials).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(190,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_inputDecryptionMaterials m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _6_inputDecryptionMaterials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetInputDecryptionMaterials(_2_encryptionContext)
	_6_inputDecryptionMaterials = _out5
	var _7_failingKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _7_failingKeyring
	var _out6 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out6
	_out6 = Companion_Default___.SetupFailingKeyring()
	_7_failingKeyring = _out6
	var _8_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError1
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_1_mpl).CreateMultiKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_3_rawAESKeyring), _dafny.SeqOf(_7_failingKeyring)))
	_8_valueOrError1 = _out7
	if !(!((_8_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(196,24): " + (_8_valueOrError1).String())
	}
	var _9_multiKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_multiKeyring
	_9_multiKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_8_valueOrError1).Extract())
	var _10_onDecryptInput m_AwsCryptographyMaterialProvidersTypes.OnDecryptInput
	_ = _10_onDecryptInput
	_10_onDecryptInput = m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_6_inputDecryptionMaterials, (((_5_encryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)).Dtor_materials()).Dtor_encryptedDataKeys())
	var _11_decryptionMaterials m_Wrappers.Result
	_ = _11_decryptionMaterials
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_9_multiKeyring).OnDecrypt(_10_onDecryptInput)
	_11_decryptionMaterials = _out8
	if !((_11_decryptionMaterials).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(206,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((((_11_decryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)).Dtor_materials()).Dtor_plaintextDataKey()).Equals((((_5_encryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(207,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGeneratorUnableToDecrypt() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(212,15): " + (_0_valueOrError0).String())
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
	var _3_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _3_rawAESKeyring
	var _out2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out2
	_out2 = Companion_Default___.SetupRawAesKeyring(_2_encryptionContext)
	_3_rawAESKeyring = _out2
	var _4_inputEncryptionMaterials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _4_inputEncryptionMaterials
	var _out3 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out3
	_out3 = Companion_Default___.GetInputEncryptionMaterials(_2_encryptionContext)
	_4_inputEncryptionMaterials = _out3
	var _5_encryptionMaterials m_Wrappers.Result
	_ = _5_encryptionMaterials
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_3_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_4_inputEncryptionMaterials))
	_5_encryptionMaterials = _out4
	if !((_5_encryptionMaterials).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(237,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_inputDecryptionMaterials m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _6_inputDecryptionMaterials
	var _out5 m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _out5
	_out5 = Companion_Default___.GetInputDecryptionMaterials(_2_encryptionContext)
	_6_inputDecryptionMaterials = _out5
	var _7_failingKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _7_failingKeyring
	var _out6 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out6
	_out6 = Companion_Default___.SetupFailingKeyring()
	_7_failingKeyring = _out6
	var _8_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError1
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_1_mpl).CreateMultiKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_7_failingKeyring), _dafny.SeqOf(_7_failingKeyring, _3_rawAESKeyring, _7_failingKeyring)))
	_8_valueOrError1 = _out7
	if !(!((_8_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(245,24): " + (_8_valueOrError1).String())
	}
	var _9_multiKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_multiKeyring
	_9_multiKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_8_valueOrError1).Extract())
	var _10_onDecryptInput m_AwsCryptographyMaterialProvidersTypes.OnDecryptInput
	_ = _10_onDecryptInput
	_10_onDecryptInput = m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_6_inputDecryptionMaterials, (((_5_encryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)).Dtor_materials()).Dtor_encryptedDataKeys())
	var _11_decryptionMaterials m_Wrappers.Result
	_ = _11_decryptionMaterials
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_9_multiKeyring).OnDecrypt(_10_onDecryptInput)
	_11_decryptionMaterials = _out8
	if !((_11_decryptionMaterials).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(265,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((((_11_decryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)).Dtor_materials()).Dtor_plaintextDataKey()).Equals((((_5_encryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(266,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestCollectFailuresDecrypt() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(272,15): " + (_0_valueOrError0).String())
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
	var _3_failingKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _3_failingKeyring
	var _out2 m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _out2
	_out2 = Companion_Default___.SetupFailingKeyring()
	_3_failingKeyring = _out2
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateMultiKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(m_Wrappers.Companion_Option_.Create_None_(), _dafny.SeqOf(_3_failingKeyring, _3_failingKeyring)))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(291,24): " + (_4_valueOrError1).String())
	}
	var _5_multiKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _5_multiKeyring
	_5_multiKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	_6_valueOrError2 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_()), _2_encryptionContext, _dafny.SeqOf()))
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(296,21): " + (_6_valueOrError2).String())
	}
	var _7_materials m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _7_materials
	_7_materials = (_6_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _8_result m_Wrappers.Result
	_ = _8_result
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_5_multiKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_7_materials, _dafny.SeqOf()))
	_8_result = _out4
	if !((_8_result).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(305,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) SetupRawAesKeyring(encryptionContext _dafny.Map) m_AwsCryptographyMaterialProvidersTypes.IKeyring {
	var res m_AwsCryptographyMaterialProvidersTypes.IKeyring = (m_AwsCryptographyMaterialProvidersTypes.IKeyring)(nil)
	_ = res
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(313,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_namespace _dafny.Sequence
	_ = _2_namespace
	var _3_name _dafny.Sequence
	_ = _3_name
	var _out1 _dafny.Sequence
	_ = _out1
	var _out2 _dafny.Sequence
	_ = _out2
	_out1, _out2 = m_TestUtils.Companion_Default___.NamespaceAndName(_dafny.Zero)
	_2_namespace = _out1
	_3_name = _out2
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer13 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg13 _dafny.Int) interface{} {
			return coer13(arg13)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(316,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	res = _6_rawAESKeyring
	return res
	return res
}
func (_static *CompanionStruct_Default___) SetupStaticKeyring(encryptionMaterials m_Wrappers.Option, decryptionMaterials m_Wrappers.Option) m_AwsCryptographyMaterialProvidersTypes.IKeyring {
	var res m_AwsCryptographyMaterialProvidersTypes.IKeyring = (m_AwsCryptographyMaterialProvidersTypes.IKeyring)(nil)
	_ = res
	var _nw0 *StaticKeyring = New_StaticKeyring_()
	_ = _nw0
	_nw0.Ctor__(encryptionMaterials, decryptionMaterials)
	res = _nw0
	return res
	return res
}
func (_static *CompanionStruct_Default___) SetupFailingKeyring() m_AwsCryptographyMaterialProvidersTypes.IKeyring {
	var res m_AwsCryptographyMaterialProvidersTypes.IKeyring = (m_AwsCryptographyMaterialProvidersTypes.IKeyring)(nil)
	_ = res
	var _nw0 *FailingKeyring = New_FailingKeyring_()
	_ = _nw0
	_nw0.Ctor__()
	res = _nw0
	return res
	return res
}

// End of class Default__

// Definition of class StaticKeyring
type StaticKeyring struct {
	_encryptionMaterials m_Wrappers.Option
	_decryptionMaterials m_Wrappers.Option
}

func New_StaticKeyring_() *StaticKeyring {
	_this := StaticKeyring{}

	_this._encryptionMaterials = m_Wrappers.Companion_Option_.Default()
	_this._decryptionMaterials = m_Wrappers.Companion_Option_.Default()
	return &_this
}

type CompanionStruct_StaticKeyring_ struct {
}

var Companion_StaticKeyring_ = CompanionStruct_StaticKeyring_{}

func (_this *StaticKeyring) Equals(other *StaticKeyring) bool {
	return _this == other
}

func (_this *StaticKeyring) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*StaticKeyring)
	return ok && _this.Equals(other)
}

func (*StaticKeyring) String() string {
	return "TestMultiKeyring.StaticKeyring"
}

func Type_StaticKeyring_() _dafny.TypeDescriptor {
	return type_StaticKeyring_{}
}

type type_StaticKeyring_ struct {
}

func (_this type_StaticKeyring_) Default() interface{} {
	return (*StaticKeyring)(nil)
}

func (_this type_StaticKeyring_) String() string {
	return "TestMultiKeyring.StaticKeyring"
}
func (_this *StaticKeyring) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.TraitID_}
}

var _ m_AwsCryptographyMaterialProvidersTypes.IKeyring = &StaticKeyring{}
var _ _dafny.TraitOffspring = &StaticKeyring{}

func (_this *StaticKeyring) OnDecrypt(input m_AwsCryptographyMaterialProvidersTypes.OnDecryptInput) m_Wrappers.Result {
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.OnDecrypt(_this, input)
	return _out0
}
func (_this *StaticKeyring) OnEncrypt(input m_AwsCryptographyMaterialProvidersTypes.OnEncryptInput) m_Wrappers.Result {
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.OnEncrypt(_this, input)
	return _out0
}
func (_this *StaticKeyring) Ctor__(encryptionMaterials m_Wrappers.Option, decryptionMaterials m_Wrappers.Option) {
	{
		(_this)._encryptionMaterials = encryptionMaterials
		(_this)._decryptionMaterials = decryptionMaterials
	}
}
func (_this *StaticKeyring) OnEncrypt_k(input m_AwsCryptographyMaterialProvidersTypes.OnEncryptInput) m_Wrappers.Result {
	{
		var res m_Wrappers.Result = m_Wrappers.Result{}
		_ = res
		if ((_this).EncryptionMaterials()).Is_Some() {
			res = m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptOutput_.Create_OnEncryptOutput_(((_this).EncryptionMaterials()).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)))
			return res
		} else {
			var _0_exception m_AwsCryptographyMaterialProvidersTypes.Error
			_ = _0_exception
			_0_exception = m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Failure"))
			res = m_Wrappers.Companion_Result_.Create_Failure_(_0_exception)
			return res
		}
		return res
	}
}
func (_this *StaticKeyring) OnDecrypt_k(input m_AwsCryptographyMaterialProvidersTypes.OnDecryptInput) m_Wrappers.Result {
	{
		var res m_Wrappers.Result = m_Wrappers.Result{}
		_ = res
		if ((_this).DecryptionMaterials()).Is_Some() {
			res = m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptOutput_.Create_OnDecryptOutput_(((_this).DecryptionMaterials()).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)))
			return res
		} else {
			var _0_exception m_AwsCryptographyMaterialProvidersTypes.Error
			_ = _0_exception
			_0_exception = m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Failure"))
			res = m_Wrappers.Companion_Result_.Create_Failure_(_0_exception)
			return res
		}
		return res
	}
}
func (_this *StaticKeyring) EncryptionMaterials() m_Wrappers.Option {
	{
		return _this._encryptionMaterials
	}
}
func (_this *StaticKeyring) DecryptionMaterials() m_Wrappers.Option {
	{
		return _this._decryptionMaterials
	}
}

// End of class StaticKeyring

// Definition of class FailingKeyring
type FailingKeyring struct {
	dummy byte
}

func New_FailingKeyring_() *FailingKeyring {
	_this := FailingKeyring{}

	return &_this
}

type CompanionStruct_FailingKeyring_ struct {
}

var Companion_FailingKeyring_ = CompanionStruct_FailingKeyring_{}

func (_this *FailingKeyring) Equals(other *FailingKeyring) bool {
	return _this == other
}

func (_this *FailingKeyring) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*FailingKeyring)
	return ok && _this.Equals(other)
}

func (*FailingKeyring) String() string {
	return "TestMultiKeyring.FailingKeyring"
}

func Type_FailingKeyring_() _dafny.TypeDescriptor {
	return type_FailingKeyring_{}
}

type type_FailingKeyring_ struct {
}

func (_this type_FailingKeyring_) Default() interface{} {
	return (*FailingKeyring)(nil)
}

func (_this type_FailingKeyring_) String() string {
	return "TestMultiKeyring.FailingKeyring"
}
func (_this *FailingKeyring) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.TraitID_}
}

var _ m_AwsCryptographyMaterialProvidersTypes.IKeyring = &FailingKeyring{}
var _ _dafny.TraitOffspring = &FailingKeyring{}

func (_this *FailingKeyring) OnDecrypt(input m_AwsCryptographyMaterialProvidersTypes.OnDecryptInput) m_Wrappers.Result {
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.OnDecrypt(_this, input)
	return _out1
}
func (_this *FailingKeyring) OnEncrypt(input m_AwsCryptographyMaterialProvidersTypes.OnEncryptInput) m_Wrappers.Result {
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.OnEncrypt(_this, input)
	return _out1
}
func (_this *FailingKeyring) Ctor__() {
	{
	}
}
func (_this *FailingKeyring) OnEncrypt_k(input m_AwsCryptographyMaterialProvidersTypes.OnEncryptInput) m_Wrappers.Result {
	{
		var res m_Wrappers.Result = m_Wrappers.Result{}
		_ = res
		var _0_exception m_AwsCryptographyMaterialProvidersTypes.Error
		_ = _0_exception
		_0_exception = m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Failure"))
		res = m_Wrappers.Companion_Result_.Create_Failure_(_0_exception)
		return res
		return res
	}
}
func (_this *FailingKeyring) OnDecrypt_k(input m_AwsCryptographyMaterialProvidersTypes.OnDecryptInput) m_Wrappers.Result {
	{
		var res m_Wrappers.Result = m_Wrappers.Result{}
		_ = res
		var _0_exception m_AwsCryptographyMaterialProvidersTypes.Error
		_ = _0_exception
		_0_exception = m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Failure"))
		res = m_Wrappers.Companion_Result_.Create_Failure_(_0_exception)
		return res
		return res
	}
}

// End of class FailingKeyring
