// Package TestAwsKmsRsaKeyring
// Dafny module TestAwsKmsRsaKeyring compiled into Go

package TestAwsKmsRsaKeyring

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
var _ m_TestAwsKmsHierarchicalKeyring.Dummy__

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
	return "TestAwsKmsRsaKeyring.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestKmsRsaRoundtrip() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(21,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UTF8.Encode(m_TestUtils.Companion_Default___.KMS__RSA__PUBLIC__KEY())
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(23,21): " + (_2_valueOrError1).String())
	}
	var _3_publicKey _dafny.Sequence
	_ = _3_publicKey
	_3_publicKey = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError2
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_mpl).CreateDefaultClientSupplier(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateDefaultClientSupplierInput_.Create_CreateDefaultClientSupplierInput_())
	_4_valueOrError2 = _out1
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(25,26): " + (_4_valueOrError2).String())
	}
	var _5_clientSupplier m_AwsCryptographyMaterialProvidersTypes.IClientSupplier
	_ = _5_clientSupplier
	_5_clientSupplier = m_AwsCryptographyMaterialProvidersTypes.Companion_IClientSupplier_.CastTo_((_4_valueOrError2).Extract())
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError3
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_5_clientSupplier).GetClient(m_AwsCryptographyMaterialProvidersTypes.Companion_GetClientInput_.Create_GetClientInput_(_dafny.SeqOfString("us-west-2")))
	_6_valueOrError3 = _out2
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(26,21): " + (_6_valueOrError3).String())
	}
	var _7_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClient
	_7_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError3).Extract())
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError4
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateAwsKmsRsaKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsRsaKeyringInput_.Create_CreateAwsKmsRsaKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_3_publicKey), m_TestUtils.Companion_Default___.KMS__RSA__PRIVATE__KEY__ARN(), m_ComAmazonawsKmsTypes.Companion_EncryptionAlgorithmSpec_.Create_RSAES__OAEP__SHA__1_(), m_Wrappers.Companion_Option_.Create_Some_(_7_kmsClient), m_Wrappers.Companion_Option_.Create_None_()))
	_8_valueOrError4 = _out3
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(28,25): " + (_8_valueOrError4).String())
	}
	var _9_kmsRsaKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_kmsRsaKeyring
	_9_kmsRsaKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_8_valueOrError4).Extract())
	var _10_encryptionContext _dafny.Map
	_ = _10_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_10_encryptionContext = _out4
	var _11_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _11_algorithmSuiteId
	_11_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _12_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	_ = _12_suite
	_12_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_11_algorithmSuiteId)
	var _13_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _13_valueOrError5
	_13_valueOrError5 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_11_algorithmSuiteId, _10_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_13_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(40,33): " + (_13_valueOrError5).String())
	}
	var _14_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _14_encryptionMaterialsIn
	_14_encryptionMaterialsIn = (_13_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _15_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _15_valueOrError6
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_9_kmsRsaKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_14_encryptionMaterialsIn))
	_15_valueOrError6 = _out5
	if !(!((_15_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(50,34): " + (_15_valueOrError6).String())
	}
	var _16_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _16_encryptionMaterialsOut
	_16_encryptionMaterialsOut = (_15_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _17_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _17_valueOrError7
	_17_valueOrError7 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_16_encryptionMaterialsOut).Dtor_materials())
	if !(!((_17_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(54,13): " + (_17_valueOrError7).String())
	}
	var _18___v0 _dafny.Tuple
	_ = _18___v0
	_18___v0 = (_17_valueOrError7).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_16_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(56,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _19_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _19_edk
	_19_edk = (((_16_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _20_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _20_valueOrError8
	_20_valueOrError8 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_11_algorithmSuiteId, _10_encryptionContext, _dafny.SeqOf()))
	if !(!((_20_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(60,33): " + (_20_valueOrError8).String())
	}
	var _21_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _21_decryptionMaterialsIn
	_21_decryptionMaterialsIn = (_20_valueOrError8).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _22_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _22_valueOrError9
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_9_kmsRsaKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_21_decryptionMaterialsIn, _dafny.SeqOf(_19_edk)))
	_22_valueOrError9 = _out6
	if !(!((_22_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(67,34): " + (_22_valueOrError9).String())
	}
	var _23_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _23_decryptionMaterialsOut
	_23_decryptionMaterialsOut = (_22_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_16_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_23_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(74,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestKmsRsaWithAsymmetricSignatureFails() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(79,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UTF8.Encode(m_TestUtils.Companion_Default___.KMS__RSA__PUBLIC__KEY())
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(81,21): " + (_2_valueOrError1).String())
	}
	var _3_publicKey _dafny.Sequence
	_ = _3_publicKey
	_3_publicKey = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError2
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_mpl).CreateDefaultClientSupplier(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateDefaultClientSupplierInput_.Create_CreateDefaultClientSupplierInput_())
	_4_valueOrError2 = _out1
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(83,26): " + (_4_valueOrError2).String())
	}
	var _5_clientSupplier m_AwsCryptographyMaterialProvidersTypes.IClientSupplier
	_ = _5_clientSupplier
	_5_clientSupplier = m_AwsCryptographyMaterialProvidersTypes.Companion_IClientSupplier_.CastTo_((_4_valueOrError2).Extract())
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError3
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_5_clientSupplier).GetClient(m_AwsCryptographyMaterialProvidersTypes.Companion_GetClientInput_.Create_GetClientInput_(_dafny.SeqOfString("us-west-2")))
	_6_valueOrError3 = _out2
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(84,21): " + (_6_valueOrError3).String())
	}
	var _7_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClient
	_7_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError3).Extract())
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError4
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateAwsKmsRsaKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsRsaKeyringInput_.Create_CreateAwsKmsRsaKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(_3_publicKey), m_TestUtils.Companion_Default___.KMS__RSA__PRIVATE__KEY__ARN(), m_ComAmazonawsKmsTypes.Companion_EncryptionAlgorithmSpec_.Create_RSAES__OAEP__SHA__1_(), m_Wrappers.Companion_Option_.Create_Some_(_7_kmsClient), m_Wrappers.Companion_Option_.Create_None_()))
	_8_valueOrError4 = _out3
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(86,25): " + (_8_valueOrError4).String())
	}
	var _9_kmsRsaKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_kmsRsaKeyring
	_9_kmsRsaKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_8_valueOrError4).Extract())
	var _10_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _10_algorithmSuiteId
	_10_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_DBE_(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384_())
	var _11_suite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	_ = _11_suite
	_11_suite = m_AlgorithmSuites.Companion_Default___.GetSuite(_10_algorithmSuiteId)
	var _12_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError5
	_12_valueOrError5 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_10_algorithmSuiteId, _dafny.NewMapBuilder().ToMap(), _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOf(uint8(0), uint8(0), uint8(0), uint8(0), uint8(0))), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOf(uint8(0), uint8(0), uint8(0), uint8(0), uint8(0)))))
	if !(!((_12_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(96,33): " + (_12_valueOrError5).String())
	}
	var _13_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _13_encryptionMaterialsIn
	_13_encryptionMaterialsIn = (_12_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _14_encryptionMaterialsOutRes m_Wrappers.Result
	_ = _14_encryptionMaterialsOutRes
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_9_kmsRsaKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_13_encryptionMaterialsIn))
	_14_encryptionMaterialsOutRes = _out4
	if !((_14_encryptionMaterialsOutRes).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(110,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_14_encryptionMaterialsOutRes).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(111,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_14_encryptionMaterialsOutRes).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("AwsKmsRsaKeyring cannot be used with"), _dafny.SeqOfString(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(112,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _15_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _15_valueOrError6
	_15_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_10_algorithmSuiteId, (_13_encryptionMaterialsIn).Dtor_encryptionContext(), _dafny.SeqOf()))
	if !(!((_15_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(115,33): " + (_15_valueOrError6).String())
	}
	var _16_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _16_decryptionMaterialsIn
	_16_decryptionMaterialsIn = (_15_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _17_decryptionMaterialsOutRes m_Wrappers.Result
	_ = _17_decryptionMaterialsOutRes
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_9_kmsRsaKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_16_decryptionMaterialsIn, _dafny.SeqOf()))
	_17_decryptionMaterialsOutRes = _out5
	if !((_17_decryptionMaterialsOutRes).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(129,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_17_decryptionMaterialsOutRes).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(130,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_17_decryptionMaterialsOutRes).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("AwsKmsRsaKeyring cannot be used with"), _dafny.SeqOfString(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(131,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
