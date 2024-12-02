// Package TestRawAESKeyring
// Dafny module TestRawAESKeyring compiled into Go

package TestRawAESKeyring

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
var _ m_TestAwsKmsRsaKeyring.Dummy__

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
	return "TestRawAESKeyring.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestOnEncryptOnDecryptGenerateDataKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(20,15): " + (_0_valueOrError0).String())
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
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer2 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg2 _dafny.Int) interface{} {
			return coer2(arg2)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(23,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _7_encryptionContext _dafny.Map
	_ = _7_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_7_encryptionContext = _out4
	var _8_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _8_algorithmSuiteId
	_8_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError2
	_9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_9_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(32,33): " + (_9_valueOrError2).String())
	}
	var _10_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _10_encryptionMaterialsIn
	_10_encryptionMaterialsIn = (_9_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _11_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _11_valueOrError3
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_6_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_10_encryptionMaterialsIn))
	_11_valueOrError3 = _out5
	if !(!((_11_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(42,34): " + (_11_valueOrError3).String())
	}
	var _12_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _12_encryptionMaterialsOut
	_12_encryptionMaterialsOut = (_11_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _13_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _13_valueOrError4
	_13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).Dtor_materials())
	if !(!((_13_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(57,13): " + (_13_valueOrError4).String())
	}
	var _14___v0 _dafny.Tuple
	_ = _14___v0
	_14___v0 = (_13_valueOrError4).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(64,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _15_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _15_edk
	_15_edk = (((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _16_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _16_valueOrError5
	_16_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf()))
	if !(!((_16_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(68,33): " + (_16_valueOrError5).String())
	}
	var _17_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _17_decryptionMaterialsIn
	_17_decryptionMaterialsIn = (_16_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _18_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _18_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_6_rawAESKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_17_decryptionMaterialsIn, _dafny.SeqOf(_15_edk)))
	_18_valueOrError6 = _out6
	if !(!((_18_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(75,34): " + (_18_valueOrError6).String())
	}
	var _19_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _19_decryptionMaterialsOut
	_19_decryptionMaterialsOut = (_18_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(86,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestOnEncryptOnDecryptSuppliedDataKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(93,15): " + (_0_valueOrError0).String())
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
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer3 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg3 _dafny.Int) interface{} {
			return coer3(arg3)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(96,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _7_encryptionContext _dafny.Map
	_ = _7_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_7_encryptionContext = _out4
	var _8_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _8_algorithmSuiteId
	_8_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError2
	_9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_9_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(105,33): " + (_9_valueOrError2).String())
	}
	var _10_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _10_encryptionMaterialsIn
	_10_encryptionMaterialsIn = (_9_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _11_pdk _dafny.Sequence
	_ = _11_pdk
	_11_pdk = _dafny.SeqCreate(32, func(coer4 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg4 _dafny.Int) interface{} {
			return coer4(arg4)
		}
	}(func(_12_i _dafny.Int) uint8 {
		return uint8(0)
	}))
	var _13_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _13_valueOrError3
	var _pat_let_tv0 = _11_pdk
	_ = _pat_let_tv0
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_6_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(func(_pat_let9_0 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials) m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials {
		return func(_14_dt__update__tmp_h0 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials) m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials {
			return func(_pat_let10_0 m_Wrappers.Option) m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials {
				return func(_15_dt__update_hplaintextDataKey_h0 m_Wrappers.Option) m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials {
					return m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_((_14_dt__update__tmp_h0).Dtor_algorithmSuite(), (_14_dt__update__tmp_h0).Dtor_encryptionContext(), (_14_dt__update__tmp_h0).Dtor_encryptedDataKeys(), (_14_dt__update__tmp_h0).Dtor_requiredEncryptionContextKeys(), _15_dt__update_hplaintextDataKey_h0, (_14_dt__update__tmp_h0).Dtor_signingKey(), (_14_dt__update__tmp_h0).Dtor_symmetricSigningKeys())
				}(_pat_let10_0)
			}(m_Wrappers.Companion_Option_.Create_Some_(_pat_let_tv0))
		}(_pat_let9_0)
	}(_10_encryptionMaterialsIn)))
	_13_valueOrError3 = _out5
	if !(!((_13_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(120,34): " + (_13_valueOrError3).String())
	}
	var _16_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _16_encryptionMaterialsOut
	_16_encryptionMaterialsOut = (_13_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _17_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _17_valueOrError4
	_17_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_16_encryptionMaterialsOut).Dtor_materials())
	if !(!((_17_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(124,13): " + (_17_valueOrError4).String())
	}
	var _18___v1 _dafny.Tuple
	_ = _18___v1
	_18___v1 = (_17_valueOrError4).Extract().(_dafny.Tuple)
	var _19_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _19_edk
	_19_edk = (((_16_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _20_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _20_valueOrError5
	_20_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf()))
	if !(!((_20_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(128,33): " + (_20_valueOrError5).String())
	}
	var _21_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _21_decryptionMaterialsIn
	_21_decryptionMaterialsIn = (_20_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _22_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _22_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_6_rawAESKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_21_decryptionMaterialsIn, _dafny.SeqOf(_19_edk)))
	_22_valueOrError6 = _out6
	if !(!((_22_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(136,34): " + (_22_valueOrError6).String())
	}
	var _23_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _23_decryptionMaterialsOut
	_23_decryptionMaterialsOut = (_22_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_23_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(m_Wrappers.Companion_Option_.Create_Some_(_11_pdk))) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(148,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestOnDecryptKeyNameMismatch() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(154,15): " + (_0_valueOrError0).String())
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
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer5 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg5 _dafny.Int) interface{} {
			return coer5(arg5)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(157,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _7_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _7_valueOrError2
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _dafny.SeqOfString("mismatched"), _dafny.SeqCreate(32, func(coer6 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg6 _dafny.Int) interface{} {
			return coer6(arg6)
		}
	}(func(_8_i _dafny.Int) uint8 {
		return uint8(1)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_7_valueOrError2 = _out4
	if !(!((_7_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(164,32): " + (_7_valueOrError2).String())
	}
	var _9_mismatchedAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_mismatchedAESKeyring
	_9_mismatchedAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_7_valueOrError2).Extract())
	var _10_encryptionContext _dafny.Map
	_ = _10_encryptionContext
	var _out5 _dafny.Map
	_ = _out5
	_out5 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_10_encryptionContext = _out5
	var _11_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _11_algorithmSuiteId
	_11_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _12_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError3
	_12_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_11_algorithmSuiteId, _10_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_12_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(174,33): " + (_12_valueOrError3).String())
	}
	var _13_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _13_encryptionMaterialsIn
	_13_encryptionMaterialsIn = (_12_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _14_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError4
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_6_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_13_encryptionMaterialsIn))
	_14_valueOrError4 = _out6
	if !(!((_14_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(184,34): " + (_14_valueOrError4).String())
	}
	var _15_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _15_encryptionMaterialsOut
	_15_encryptionMaterialsOut = (_14_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _16_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _16_valueOrError5
	_16_valueOrError5 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_15_encryptionMaterialsOut).Dtor_materials())
	if !(!((_16_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(188,13): " + (_16_valueOrError5).String())
	}
	var _17___v2 _dafny.Tuple
	_ = _17___v2
	_17___v2 = (_16_valueOrError5).Extract().(_dafny.Tuple)
	var _18_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _18_edk
	_18_edk = (((_15_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _19_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError6
	_19_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_11_algorithmSuiteId, _10_encryptionContext, _dafny.SeqOf()))
	if !(!((_19_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(192,33): " + (_19_valueOrError6).String())
	}
	var _20_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _20_decryptionMaterialsIn
	_20_decryptionMaterialsIn = (_19_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _21_decryptionMaterialsOut m_Wrappers.Result
	_ = _21_decryptionMaterialsOut
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_9_mismatchedAESKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_20_decryptionMaterialsIn, _dafny.SeqOf(_18_edk)))
	_21_decryptionMaterialsOut = _out7
	if !((_21_decryptionMaterialsOut).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(205,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_21_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_CollectionOfErrors()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_21_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_list()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(207,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((((_21_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_list()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(208,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((((_21_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_list()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), m_ErrorMessages.Companion_Default___.IncorrectRawDataKeys(_dafny.SeqOfString("0"), _dafny.SeqOfString("AESKeyring"), _2_namespace))) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(209,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestOnDecryptBadAndGoodEdkSucceeds() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,15): " + (_0_valueOrError0).String())
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
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer7 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg7 _dafny.Int) interface{} {
			return coer7(arg7)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(218,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _7_encryptionContext _dafny.Map
	_ = _7_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_7_encryptionContext = _out4
	var _8_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _8_algorithmSuiteId
	_8_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError2
	_9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_9_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(227,33): " + (_9_valueOrError2).String())
	}
	var _10_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _10_encryptionMaterialsIn
	_10_encryptionMaterialsIn = (_9_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _11_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _11_valueOrError3
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_6_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_10_encryptionMaterialsIn))
	_11_valueOrError3 = _out5
	if !(!((_11_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(237,34): " + (_11_valueOrError3).String())
	}
	var _12_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _12_encryptionMaterialsOut
	_12_encryptionMaterialsOut = (_11_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _13_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _13_valueOrError4
	_13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).Dtor_materials())
	if !(!((_13_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(241,13): " + (_13_valueOrError4).String())
	}
	var _14___v3 _dafny.Tuple
	_ = _14___v3
	_14___v3 = (_13_valueOrError4).Extract().(_dafny.Tuple)
	var _15_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _15_edk
	_15_edk = (((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _16_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _16_valueOrError5
	_16_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf()))
	if !(!((_16_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(245,33): " + (_16_valueOrError5).String())
	}
	var _17_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _17_decryptionMaterialsIn
	_17_decryptionMaterialsIn = (_16_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _18_fakeEdk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _18_fakeEdk
	_18_fakeEdk = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptedDataKey_.Create_EncryptedDataKey_((_15_edk).Dtor_keyProviderId(), (_15_edk).Dtor_keyProviderInfo(), _dafny.SeqCreate((_dafny.IntOfUint32(((_15_edk).Dtor_ciphertext()).Cardinality())).Uint32(), func(coer8 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg8 _dafny.Int) interface{} {
			return coer8(arg8)
		}
	}(func(_19_i _dafny.Int) uint8 {
		return uint8(0)
	})))
	var _20_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _20_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_6_rawAESKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_17_decryptionMaterialsIn, _dafny.SeqOf(_18_fakeEdk, _15_edk)))
	_20_valueOrError6 = _out6
	if !(!((_20_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(258,34): " + (_20_valueOrError6).String())
	}
	var _21_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _21_decryptionMaterialsOut
	_21_decryptionMaterialsOut = (_20_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_21_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(265,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestOnDecryptNoEDKs() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,15): " + (_0_valueOrError0).String())
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
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer9 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg9 _dafny.Int) interface{} {
			return coer9(arg9)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(274,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _7_encryptionContext _dafny.Map
	_ = _7_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_7_encryptionContext = _out4
	var _8_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _8_algorithmSuiteId
	_8_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError2
	_9_valueOrError2 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf()))
	if !(!((_9_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(283,33): " + (_9_valueOrError2).String())
	}
	var _10_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _10_decryptionMaterialsIn
	_10_decryptionMaterialsIn = (_9_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _11_decryptionMaterialsOut m_Wrappers.Result
	_ = _11_decryptionMaterialsOut
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_6_rawAESKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_10_decryptionMaterialsIn, _dafny.SeqOf()))
	_11_decryptionMaterialsOut = _out5
	if !((_11_decryptionMaterialsOut).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(296,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestOnEncryptUnserializableEC() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,15): " + (_0_valueOrError0).String())
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
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer10 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg10 _dafny.Int) interface{} {
			return coer10(arg10)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(308,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _7_unserializableEncryptionContext _dafny.Map
	_ = _7_unserializableEncryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = Companion_Default___.GenerateUnserializableEncryptionContext()
	_7_unserializableEncryptionContext = _out4
	var _8_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _8_algorithmSuiteId
	_8_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError2
	_9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_8_algorithmSuiteId, _7_unserializableEncryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_9_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(317,33): " + (_9_valueOrError2).String())
	}
	var _10_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _10_encryptionMaterialsIn
	_10_encryptionMaterialsIn = (_9_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _11_encryptionMaterialsOut m_Wrappers.Result
	_ = _11_encryptionMaterialsOut
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_6_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_10_encryptionMaterialsIn))
	_11_encryptionMaterialsOut = _out5
	if !((_11_encryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(329,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestOnDecryptUnserializableEC() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,15): " + (_0_valueOrError0).String())
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
	_out3 = (_1_mpl).CreateRawAesKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_2_namespace, _3_name, _dafny.SeqCreate(32, func(coer11 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg11 _dafny.Int) interface{} {
			return coer11(arg11)
		}
	}(func(_5_i _dafny.Int) uint8 {
		return uint8(0)
	})), m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_()))
	_4_valueOrError1 = _out3
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(342,25): " + (_4_valueOrError1).String())
	}
	var _6_rawAESKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _6_rawAESKeyring
	_6_rawAESKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_4_valueOrError1).Extract())
	var _7_encryptionContext _dafny.Map
	_ = _7_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_7_encryptionContext = _out4
	var _8_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _8_algorithmSuiteId
	_8_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError2
	_9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_8_algorithmSuiteId, _7_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_9_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(351,33): " + (_9_valueOrError2).String())
	}
	var _10_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _10_encryptionMaterialsIn
	_10_encryptionMaterialsIn = (_9_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _11_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _11_valueOrError3
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_6_rawAESKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_10_encryptionMaterialsIn))
	_11_valueOrError3 = _out5
	if !(!((_11_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(361,34): " + (_11_valueOrError3).String())
	}
	var _12_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _12_encryptionMaterialsOut
	_12_encryptionMaterialsOut = (_11_valueOrError3).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _13_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _13_valueOrError4
	_13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).Dtor_materials())
	if !(!((_13_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(364,13): " + (_13_valueOrError4).String())
	}
	var _14___v4 _dafny.Tuple
	_ = _14___v4
	_14___v4 = (_13_valueOrError4).Extract().(_dafny.Tuple)
	var _15_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _15_edk
	_15_edk = (((_12_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _16_unserializableEncryptionContext _dafny.Map
	_ = _16_unserializableEncryptionContext
	var _out6 _dafny.Map
	_ = _out6
	_out6 = Companion_Default___.GenerateUnserializableEncryptionContext()
	_16_unserializableEncryptionContext = _out6
	var _17_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError5
	_17_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_8_algorithmSuiteId, _16_unserializableEncryptionContext, _dafny.SeqOf()))
	if !(!((_17_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(369,33): " + (_17_valueOrError5).String())
	}
	var _18_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _18_decryptionMaterialsIn
	_18_decryptionMaterialsIn = (_17_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _19_decryptionMaterialsOut m_Wrappers.Result
	_ = _19_decryptionMaterialsOut
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_6_rawAESKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_18_decryptionMaterialsIn, _dafny.SeqOf(_15_edk)))
	_19_decryptionMaterialsOut = _out7
	if !((_19_decryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(382,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) GenerateUnserializableEncryptionContext() _dafny.Map {
	var encCtx _dafny.Map = _dafny.EmptyMap
	_ = encCtx
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UTF8.Encode(_dafny.SeqOfString("keyA"))
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(387,16): " + (_0_valueOrError0).String())
	}
	var _1_keyA _dafny.Sequence
	_ = _1_keyA
	_1_keyA = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_invalidVal _dafny.Sequence
	_ = _2_invalidVal
	_2_invalidVal = _dafny.SeqCreate(65536, func(coer12 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg12 _dafny.Int) interface{} {
			return coer12(arg12)
		}
	}(func(_3___v5 _dafny.Int) uint8 {
		return uint8(0)
	}))
	encCtx = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_1_keyA, _2_invalidVal)
	return encCtx
	return encCtx
}

// End of class Default__
