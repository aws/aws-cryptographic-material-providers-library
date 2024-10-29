// Package TestRawECDHKeyring
// Dafny module TestRawECDHKeyring compiled into Go

package TestRawECDHKeyring

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
	m_TestLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLocalCMC"
	m_TestLyingBranchKey "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLyingBranchKey"
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
	return "TestRawECDHKeyring.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestRawEcdhDiscoveryOnEncryptFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(30,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(31,22): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(33,19): " + (_4_valueOrError2).String())
	}
	var _5_keypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_keypair
	_5_keypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_PublicKeyDiscovery_(m_AwsCryptographyMaterialProvidersTypes.Companion_PublicKeyDiscoveryInput_.Create_PublicKeyDiscoveryInput_(((_5_keypair).Dtor_privateKey()).Dtor_pem())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(39,19): " + (_6_valueOrError3).String())
	}
	var _7_keyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _7_keyring
	_7_keyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_6_valueOrError3).Extract())
	var _8_encryptionContext _dafny.Map
	_ = _8_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_8_encryptionContext = _out4
	var _9_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _9_algorithmSuiteId
	_9_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError4
	_10_valueOrError4 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_9_algorithmSuiteId, _8_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(51,33): " + (_10_valueOrError4).String())
	}
	var _11_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _11_encryptionMaterialsIn
	_11_encryptionMaterialsIn = (_10_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _12_encryptionMaterialsOut m_Wrappers.Result
	_ = _12_encryptionMaterialsOut
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_7_keyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_11_encryptionMaterialsIn))
	_12_encryptionMaterialsOut = _out5
	if !((_12_encryptionMaterialsOut).IsFailure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(65,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_12_encryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(66,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _13_expectedErrorMessage _dafny.Sequence
	_ = _13_expectedErrorMessage
	_13_expectedErrorMessage = m_ErrorMessages.Companion_Default___.RAW__ECDH__DISCOVERY__ENCRYPT__ERROR()
	if !(_dafny.Companion_Sequence_.Equal(((_12_encryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), _13_expectedErrorMessage)) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(69,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRawEcdhEphemeralOnDecryptFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(73,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(74,22): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(76,19): " + (_4_valueOrError2).String())
	}
	var _5_keypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_keypair
	_5_keypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_EphemeralPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_EphemeralPrivateKeyToStaticPublicKeyInput_.Create_EphemeralPrivateKeyToStaticPublicKeyInput_(((_5_keypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(82,19): " + (_6_valueOrError3).String())
	}
	var _7_keyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _7_keyring
	_7_keyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_6_valueOrError3).Extract())
	var _8_encryptionContext _dafny.Map
	_ = _8_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_8_encryptionContext = _out4
	var _9_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _9_algorithmSuiteId
	_9_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError4
	_10_valueOrError4 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_9_algorithmSuiteId, _dafny.NewMapBuilder().ToMap(), _dafny.SeqOf()))
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(96,33): " + (_10_valueOrError4).String())
	}
	var _11_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _11_decryptionMaterialsIn
	_11_decryptionMaterialsIn = (_10_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _12_decryptionMaterialsOutRes m_Wrappers.Result
	_ = _12_decryptionMaterialsOutRes
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_7_keyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_11_decryptionMaterialsIn, _dafny.SeqOf()))
	_12_decryptionMaterialsOutRes = _out5
	if !((_12_decryptionMaterialsOutRes).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(110,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_12_decryptionMaterialsOutRes).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(111,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_12_decryptionMaterialsOutRes).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), m_ErrorMessages.Companion_Default___.RAW__ECDH__EPHEMERAL__DECRYPT__ERROR())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(113,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(117,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(118,22): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(120,19): " + (_4_valueOrError2).String())
	}
	var _5_keypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_keypair
	_5_keypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_EphemeralPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_EphemeralPrivateKeyToStaticPublicKeyInput_.Create_EphemeralPrivateKeyToStaticPublicKeyInput_(((_5_keypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(126,19): " + (_6_valueOrError3).String())
	}
	var _7_keyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _7_keyring
	_7_keyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_6_valueOrError3).Extract())
	var _8_encryptionContext _dafny.Map
	_ = _8_encryptionContext
	var _out4 _dafny.Map
	_ = _out4
	_out4 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_8_encryptionContext = _out4
	var _9_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _9_algorithmSuiteId
	_9_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError4
	_10_valueOrError4 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_9_algorithmSuiteId, _8_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(140,33): " + (_10_valueOrError4).String())
	}
	var _11_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _11_encryptionMaterialsIn
	_11_encryptionMaterialsIn = (_10_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _12_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_7_keyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_11_encryptionMaterialsIn))
	_12_valueOrError5 = _out5
	if !(!((_12_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(150,34): " + (_12_valueOrError5).String())
	}
	var _13_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _13_encryptionMaterialsOut
	_13_encryptionMaterialsOut = (_12_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _14_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _14_valueOrError6
	_14_valueOrError6 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_13_encryptionMaterialsOut).Dtor_materials())
	if !(!((_14_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(154,13): " + (_14_valueOrError6).String())
	}
	var _15___v0 _dafny.Tuple
	_ = _15___v0
	_15___v0 = (_14_valueOrError6).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_13_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(156,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _16_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _16_edk
	_16_edk = (((_13_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _17_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError7
	_17_valueOrError7 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_9_algorithmSuiteId, _8_encryptionContext, _dafny.SeqOf()))
	if !(!((_17_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(159,33): " + (_17_valueOrError7).String())
	}
	var _18_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _18_decryptionMaterialsIn
	_18_decryptionMaterialsIn = (_17_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _19_decryptionMaterialsOut m_Wrappers.Result
	_ = _19_decryptionMaterialsOut
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_7_keyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_18_decryptionMaterialsIn, _dafny.SeqOf(_16_edk)))
	_19_decryptionMaterialsOut = _out6
	if !((_19_decryptionMaterialsOut).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(173,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_19_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_AwsCryptographicMaterialProvidersException()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(174,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _20_expectedErrorMessage _dafny.Sequence
	_ = _20_expectedErrorMessage
	_20_expectedErrorMessage = m_ErrorMessages.Companion_Default___.RAW__ECDH__EPHEMERAL__DECRYPT__ERROR()
	if !(_dafny.Companion_Sequence_.Equal(((_19_decryptionMaterialsOut).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Dtor_message(), _20_expectedErrorMessage)) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(177,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRawEcdhKeyringStaticSuccess() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(181,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(182,22): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(184,25): " + (_4_valueOrError2).String())
	}
	var _5_senderKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_senderKeypair
	_5_senderKeypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_3_primitives).GenerateECCKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(Companion_Default___.P256()))
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(190,28): " + (_6_valueOrError3).String())
	}
	var _7_recipientKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _7_recipientKeypair
	_7_recipientKeypair = (_6_valueOrError3).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(((_5_senderKeypair).Dtor_privateKey()).Dtor_pem(), ((_7_recipientKeypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_8_valueOrError4 = _out4
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(196,19): " + (_8_valueOrError4).String())
	}
	var _9_keyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_keyring
	_9_keyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_8_valueOrError4).Extract())
	var _10_encryptionContext _dafny.Map
	_ = _10_encryptionContext
	var _out5 _dafny.Map
	_ = _out5
	_out5 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_10_encryptionContext = _out5
	var _11_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _11_algorithmSuiteId
	_11_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _12_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError5
	_12_valueOrError5 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_11_algorithmSuiteId, _10_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_12_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(211,33): " + (_12_valueOrError5).String())
	}
	var _13_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _13_encryptionMaterialsIn
	_13_encryptionMaterialsIn = (_12_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _14_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_9_keyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_13_encryptionMaterialsIn))
	_14_valueOrError6 = _out6
	if !(!((_14_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(221,34): " + (_14_valueOrError6).String())
	}
	var _15_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _15_encryptionMaterialsOut
	_15_encryptionMaterialsOut = (_14_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _16_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _16_valueOrError7
	_16_valueOrError7 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_15_encryptionMaterialsOut).Dtor_materials())
	if !(!((_16_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(225,13): " + (_16_valueOrError7).String())
	}
	var _17___v1 _dafny.Tuple
	_ = _17___v1
	_17___v1 = (_16_valueOrError7).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_15_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(227,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _18_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _18_edk
	_18_edk = (((_15_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _19_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError8
	_19_valueOrError8 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_11_algorithmSuiteId, _10_encryptionContext, _dafny.SeqOf()))
	if !(!((_19_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(230,33): " + (_19_valueOrError8).String())
	}
	var _20_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _20_decryptionMaterialsIn
	_20_decryptionMaterialsIn = (_19_valueOrError8).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _21_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _21_valueOrError9
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_9_keyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_20_decryptionMaterialsIn, _dafny.SeqOf(_18_edk)))
	_21_valueOrError9 = _out7
	if !(!((_21_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(237,34): " + (_21_valueOrError9).String())
	}
	var _22_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _22_decryptionMaterialsOut
	_22_decryptionMaterialsOut = (_21_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_15_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_22_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(244,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestTwoRawEcdhKeyringStaticSuccess() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(250,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(251,22): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(253,25): " + (_4_valueOrError2).String())
	}
	var _5_senderKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_senderKeypair
	_5_senderKeypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_3_primitives).GenerateECCKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(Companion_Default___.P256()))
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(259,28): " + (_6_valueOrError3).String())
	}
	var _7_recipientKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _7_recipientKeypair
	_7_recipientKeypair = (_6_valueOrError3).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(((_5_senderKeypair).Dtor_privateKey()).Dtor_pem(), ((_7_recipientKeypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_8_valueOrError4 = _out4
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(265,25): " + (_8_valueOrError4).String())
	}
	var _9_senderKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_senderKeyring
	_9_senderKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_8_valueOrError4).Extract())
	var _10_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(((_7_recipientKeypair).Dtor_privateKey()).Dtor_pem(), ((_5_senderKeypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_10_valueOrError5 = _out5
	if !(!((_10_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(277,28): " + (_10_valueOrError5).String())
	}
	var _11_recipientKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _11_recipientKeyring
	_11_recipientKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_10_valueOrError5).Extract())
	var _12_encryptionContext _dafny.Map
	_ = _12_encryptionContext
	var _out6 _dafny.Map
	_ = _out6
	_out6 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_12_encryptionContext = _out6
	var _13_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _13_algorithmSuiteId
	_13_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _14_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError6
	_14_valueOrError6 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_13_algorithmSuiteId, _12_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_14_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(292,33): " + (_14_valueOrError6).String())
	}
	var _15_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _15_encryptionMaterialsIn
	_15_encryptionMaterialsIn = (_14_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _16_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _16_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_9_senderKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_15_encryptionMaterialsIn))
	_16_valueOrError7 = _out7
	if !(!((_16_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(302,34): " + (_16_valueOrError7).String())
	}
	var _17_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _17_encryptionMaterialsOut
	_17_encryptionMaterialsOut = (_16_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _18_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _18_valueOrError8
	_18_valueOrError8 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_17_encryptionMaterialsOut).Dtor_materials())
	if !(!((_18_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(306,13): " + (_18_valueOrError8).String())
	}
	var _19___v2 _dafny.Tuple
	_ = _19___v2
	_19___v2 = (_18_valueOrError8).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_17_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(308,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _20_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _20_edk
	_20_edk = (((_17_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _21_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _21_valueOrError9
	_21_valueOrError9 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_13_algorithmSuiteId, _12_encryptionContext, _dafny.SeqOf()))
	if !(!((_21_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(311,33): " + (_21_valueOrError9).String())
	}
	var _22_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _22_decryptionMaterialsIn
	_22_decryptionMaterialsIn = (_21_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _23_valueOrError10 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _23_valueOrError10
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_11_recipientKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_22_decryptionMaterialsIn, _dafny.SeqOf(_20_edk)))
	_23_valueOrError10 = _out8
	if !(!((_23_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(318,34): " + (_23_valueOrError10).String())
	}
	var _24_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _24_decryptionMaterialsOut
	_24_decryptionMaterialsOut = (_23_valueOrError10).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_17_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_24_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(325,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestTwoEcdhKeyringStaticSuccess() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(331,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(332,22): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(334,25): " + (_4_valueOrError2).String())
	}
	var _5_senderKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_senderKeypair
	_5_senderKeypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(340,21): " + (_6_valueOrError3).String())
	}
	var _7_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _7_kmsClient
	_7_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_6_valueOrError3).Extract())
	var _8_publicKeyResponse m_Wrappers.Result
	_ = _8_publicKeyResponse
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_7_kmsClient).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__R(), m_Wrappers.Companion_Option_.Create_None_()))
	_8_publicKeyResponse = _out4
	if !((_8_publicKeyResponse).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(347,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_8_publicKeyResponse).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
	_ = _let_tmp_rhs0
	var _9___v3 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
	_ = _9___v3
	var _10_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
	_ = _10_PublicKey
	var _11___v4 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
	_ = _11___v4
	var _12___v5 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
	_ = _12___v5
	var _13___v6 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
	_ = _13___v6
	var _14___v7 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
	_ = _14___v7
	var _15___v8 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
	_ = _15___v8
	var _16___v9 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
	_ = _16___v9
	if !((_10_PublicKey).Is_Some()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(350,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _17_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError4
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(((_5_senderKeypair).Dtor_privateKey()).Dtor_pem(), (_10_PublicKey).Dtor_value().(_dafny.Sequence))), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_17_valueOrError4 = _out5
	if !(!((_17_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(352,25): " + (_17_valueOrError4).String())
	}
	var _18_senderKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _18_senderKeyring
	_18_senderKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_17_valueOrError4).Extract())
	var _19_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError5
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_1_mpl).CreateAwsKmsEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__R(), m_Wrappers.Companion_Option_.Create_None_(), ((_5_senderKeypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), _7_kmsClient, m_Wrappers.Companion_Option_.Create_None_()))
	_19_valueOrError5 = _out6
	if !(!((_19_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(364,35): " + (_19_valueOrError5).String())
	}
	var _20_recipientKmsEcdhKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _20_recipientKmsEcdhKeyring
	_20_recipientKmsEcdhKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_19_valueOrError5).Extract())
	var _21_encryptionContext _dafny.Map
	_ = _21_encryptionContext
	var _out7 _dafny.Map
	_ = _out7
	_out7 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_21_encryptionContext = _out7
	var _22_algorithmSuiteId m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
	_ = _22_algorithmSuiteId
	_22_algorithmSuiteId = m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_())
	var _23_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _23_valueOrError6
	_23_valueOrError6 = (_1_mpl).InitializeEncryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeEncryptionMaterialsInput_.Create_InitializeEncryptionMaterialsInput_(_22_algorithmSuiteId, _21_encryptionContext, _dafny.SeqOf(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	if !(!((_23_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(381,33): " + (_23_valueOrError6).String())
	}
	var _24_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _24_encryptionMaterialsIn
	_24_encryptionMaterialsIn = (_23_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	var _25_valueOrError7 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _25_valueOrError7
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_18_senderKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_24_encryptionMaterialsIn))
	_25_valueOrError7 = _out8
	if !(!((_25_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(391,34): " + (_25_valueOrError7).String())
	}
	var _26_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _26_encryptionMaterialsOut
	_26_encryptionMaterialsOut = (_25_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _27_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _27_valueOrError8
	_27_valueOrError8 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_26_encryptionMaterialsOut).Dtor_materials())
	if !(!((_27_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(395,13): " + (_27_valueOrError8).String())
	}
	var _28___v10 _dafny.Tuple
	_ = _28___v10
	_28___v10 = (_27_valueOrError8).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_26_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(397,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _29_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _29_edk
	_29_edk = (((_26_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _30_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _30_valueOrError9
	_30_valueOrError9 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(_22_algorithmSuiteId, _21_encryptionContext, _dafny.SeqOf()))
	if !(!((_30_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(400,33): " + (_30_valueOrError9).String())
	}
	var _31_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _31_decryptionMaterialsIn
	_31_decryptionMaterialsIn = (_30_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _32_valueOrError10 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _32_valueOrError10
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_20_recipientKmsEcdhKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_31_decryptionMaterialsIn, _dafny.SeqOf(_29_edk)))
	_32_valueOrError10 = _out9
	if !(!((_32_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(407,34): " + (_32_valueOrError10).String())
	}
	var _33_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _33_decryptionMaterialsOut
	_33_decryptionMaterialsOut = (_32_valueOrError10).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_26_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_33_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(414,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(420,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(421,22): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(423,25): " + (_4_valueOrError2).String())
	}
	var _5_senderKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_senderKeypair
	_5_senderKeypair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
	_ = _6_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_3_primitives).GenerateECCKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(Companion_Default___.P256()))
	_6_valueOrError3 = _out3
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(429,28): " + (_6_valueOrError3).String())
	}
	var _7_recipientKeypair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _7_recipientKeypair
	_7_recipientKeypair = (_6_valueOrError3).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _8_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(((_5_senderKeypair).Dtor_privateKey()).Dtor_pem(), ((_7_recipientKeypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_8_valueOrError4 = _out4
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(435,25): " + (_8_valueOrError4).String())
	}
	var _9_senderKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _9_senderKeyring
	_9_senderKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_8_valueOrError4).Extract())
	var _10_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _10_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(((_7_recipientKeypair).Dtor_privateKey()).Dtor_pem(), ((_5_senderKeypair).Dtor_publicKey()).Dtor_der())), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_10_valueOrError5 = _out5
	if !(!((_10_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(447,28): " + (_10_valueOrError5).String())
	}
	var _11_recipientKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
	_ = _11_recipientKeyring
	_11_recipientKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_10_valueOrError5).Extract())
	var _12_encryptionContext _dafny.Map
	_ = _12_encryptionContext
	var _out6 _dafny.Map
	_ = _out6
	_out6 = m_TestUtils.Companion_Default___.SmallEncryptionContext(m_TestUtils.Companion_SmallEncryptionContextVariation_.Create_A_())
	_12_encryptionContext = _out6
	var _13_materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _13_materials
	var _out7 m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _out7
	_out7 = Companion_Default___.GetTestMaterials(Companion_Default___.TEST__DBE__ALG__SUITE__ID())
	_13_materials = _out7
	var _14_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError6
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_9_senderKeyring).OnEncrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnEncryptInput_.Create_OnEncryptInput_(_13_materials))
	_14_valueOrError6 = _out8
	if !(!((_14_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(463,34): " + (_14_valueOrError6).String())
	}
	var _15_encryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
	_ = _15_encryptionMaterialsOut
	_15_encryptionMaterialsOut = (_14_valueOrError6).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnEncryptOutput)
	var _16_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _16_valueOrError7
	_16_valueOrError7 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_15_encryptionMaterialsOut).Dtor_materials())
	if !(!((_16_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(467,13): " + (_16_valueOrError7).String())
	}
	var _17___v11 _dafny.Tuple
	_ = _17___v11
	_17___v11 = (_16_valueOrError7).Extract().(_dafny.Tuple)
	if !((_dafny.IntOfUint32((((_15_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(469,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _18_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	_ = _18_edk
	_18_edk = (((_15_encryptionMaterialsOut).Dtor_materials()).Dtor_encryptedDataKeys()).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
	var _19_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _19_valueOrError8
	_19_valueOrError8 = (_1_mpl).InitializeDecryptionMaterials(m_AwsCryptographyMaterialProvidersTypes.Companion_InitializeDecryptionMaterialsInput_.Create_InitializeDecryptionMaterialsInput_(Companion_Default___.TEST__DBE__ALG__SUITE__ID(), _12_encryptionContext, _dafny.SeqOf()))
	if !(!((_19_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(472,33): " + (_19_valueOrError8).String())
	}
	var _20_decryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
	_ = _20_decryptionMaterialsIn
	_20_decryptionMaterialsIn = (_19_valueOrError8).Extract().(m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials)
	var _21_valueOrError9 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _21_valueOrError9
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_11_recipientKeyring).OnDecrypt(m_AwsCryptographyMaterialProvidersTypes.Companion_OnDecryptInput_.Create_OnDecryptInput_(_20_decryptionMaterialsIn, _dafny.SeqOf(_18_edk)))
	_21_valueOrError9 = _out9
	if !(!((_21_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(479,34): " + (_21_valueOrError9).String())
	}
	var _22_decryptionMaterialsOut m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
	_ = _22_decryptionMaterialsOut
	_22_decryptionMaterialsOut = (_21_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTypes.OnDecryptOutput)
	if !((((_15_encryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey()).Equals(((_22_decryptionMaterialsOut).Dtor_materials()).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(486,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(492,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P256__PRIVATE())
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(494,28): " + (_2_valueOrError1).String())
	}
	var _3_senderPrivateKey _dafny.Sequence
	_ = _3_senderPrivateKey
	_3_senderPrivateKey = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _4_valueOrError2
	_4_valueOrError2 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P256__PRIVATE__R())
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(495,31): " + (_4_valueOrError2).String())
	}
	var _5_recipientPrivateKey _dafny.Sequence
	_ = _5_recipientPrivateKey
	_5_recipientPrivateKey = (_4_valueOrError2).Extract().(_dafny.Sequence)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _6_valueOrError3
	_6_valueOrError3 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P256__PUBLIC__R())
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(496,30): " + (_6_valueOrError3).String())
	}
	var _7_recipientPublicKey _dafny.Sequence
	_ = _7_recipientPublicKey
	_7_recipientPublicKey = (_6_valueOrError3).Extract().(_dafny.Sequence)
	var _8_rawEcdhKeyring m_Wrappers.Result
	_ = _8_rawEcdhKeyring
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_3_senderPrivateKey, _7_recipientPublicKey)), Companion_Default___.P384()))
	_8_rawEcdhKeyring = _out1
	if !((_8_rawEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(509,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionCombinationsFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_MaterialProviders.Companion_Default___.MaterialProviders(m_MaterialProviders.Companion_Default___.DefaultMaterialProvidersConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(514,15): " + (_0_valueOrError0).String())
	}
	var _1_mpl *m_MaterialProviders.MaterialProvidersClient
	_ = _1_mpl
	_1_mpl = (_0_valueOrError0).Extract().(*m_MaterialProviders.MaterialProvidersClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P256__PRIVATE())
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(516,31): " + (_2_valueOrError1).String())
	}
	var _3_senderPrivateKey256 _dafny.Sequence
	_ = _3_senderPrivateKey256
	_3_senderPrivateKey256 = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _4_valueOrError2
	_4_valueOrError2 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P256__PRIVATE__R())
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(517,34): " + (_4_valueOrError2).String())
	}
	var _5_recipientPrivateKey256 _dafny.Sequence
	_ = _5_recipientPrivateKey256
	_5_recipientPrivateKey256 = (_4_valueOrError2).Extract().(_dafny.Sequence)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _6_valueOrError3
	_6_valueOrError3 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P256__PUBLIC__R())
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(518,33): " + (_6_valueOrError3).String())
	}
	var _7_recipientPublicKey256 _dafny.Sequence
	_ = _7_recipientPublicKey256
	_7_recipientPublicKey256 = (_6_valueOrError3).Extract().(_dafny.Sequence)
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _8_valueOrError4
	_8_valueOrError4 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P384__PRIVATE())
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(520,31): " + (_8_valueOrError4).String())
	}
	var _9_senderPrivateKey384 _dafny.Sequence
	_ = _9_senderPrivateKey384
	_9_senderPrivateKey384 = (_8_valueOrError4).Extract().(_dafny.Sequence)
	var _10_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _10_valueOrError5
	_10_valueOrError5 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P384__PRIVATE__R())
	if !(!((_10_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(521,34): " + (_10_valueOrError5).String())
	}
	var _11_recipientPrivateKey384 _dafny.Sequence
	_ = _11_recipientPrivateKey384
	_11_recipientPrivateKey384 = (_10_valueOrError5).Extract().(_dafny.Sequence)
	var _12_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _12_valueOrError6
	_12_valueOrError6 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P384__PUBLIC__R())
	if !(!((_12_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(522,33): " + (_12_valueOrError6).String())
	}
	var _13_recipientPublicKey384 _dafny.Sequence
	_ = _13_recipientPublicKey384
	_13_recipientPublicKey384 = (_12_valueOrError6).Extract().(_dafny.Sequence)
	var _14_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _14_valueOrError7
	_14_valueOrError7 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P521__PRIVATE())
	if !(!((_14_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(524,31): " + (_14_valueOrError7).String())
	}
	var _15_senderPrivateKey521 _dafny.Sequence
	_ = _15_senderPrivateKey521
	_15_senderPrivateKey521 = (_14_valueOrError7).Extract().(_dafny.Sequence)
	var _16_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _16_valueOrError8
	_16_valueOrError8 = m_UTF8.Encode(m_TestUtils.Companion_Default___.ECC__P521__PRIVATE__R())
	if !(!((_16_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(525,34): " + (_16_valueOrError8).String())
	}
	var _17_recipientPrivateKey521 _dafny.Sequence
	_ = _17_recipientPrivateKey521
	_17_recipientPrivateKey521 = (_16_valueOrError8).Extract().(_dafny.Sequence)
	var _18_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _18_valueOrError9
	_18_valueOrError9 = m_Base64.Companion_Default___.Decode(m_TestUtils.Companion_Default___.ECC__P521__PUBLIC__R())
	if !(!((_18_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(526,33): " + (_18_valueOrError9).String())
	}
	var _19_recipientPublicKey521 _dafny.Sequence
	_ = _19_recipientPublicKey521
	_19_recipientPublicKey521 = (_18_valueOrError9).Extract().(_dafny.Sequence)
	var _20_rawEcdhKeyring m_Wrappers.Result
	_ = _20_rawEcdhKeyring
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_3_senderPrivateKey256, _7_recipientPublicKey256)), Companion_Default___.P384()))
	_20_rawEcdhKeyring = _out1
	if !((_20_rawEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(542,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_3_senderPrivateKey256, _7_recipientPublicKey256)), Companion_Default___.P521()))
	_20_rawEcdhKeyring = _out2
	if !((_20_rawEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(555,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_9_senderPrivateKey384, _13_recipientPublicKey384)), Companion_Default___.P256()))
	_20_rawEcdhKeyring = _out3
	if !((_20_rawEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(569,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_9_senderPrivateKey384, _13_recipientPublicKey384)), Companion_Default___.P521()))
	_20_rawEcdhKeyring = _out4
	if !((_20_rawEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(582,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_15_senderPrivateKey521, _19_recipientPublicKey521)), Companion_Default___.P256()))
	_20_rawEcdhKeyring = _out5
	if !((_20_rawEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(596,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_15_senderPrivateKey521, _19_recipientPublicKey521)), Companion_Default___.P384()))
	_20_rawEcdhKeyring = _out6
	if !((_20_rawEcdhKeyring).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(609,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _21_rawEcdhKeyringT2 m_Wrappers.Result
	_ = _21_rawEcdhKeyringT2
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_3_senderPrivateKey256, _13_recipientPublicKey384)), Companion_Default___.P256()))
	_21_rawEcdhKeyringT2 = _out7
	if !((_21_rawEcdhKeyringT2).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(623,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_3_senderPrivateKey256, _19_recipientPublicKey521)), Companion_Default___.P256()))
	_21_rawEcdhKeyringT2 = _out8
	if !((_21_rawEcdhKeyringT2).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(636,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_9_senderPrivateKey384, _7_recipientPublicKey256)), Companion_Default___.P384()))
	_21_rawEcdhKeyringT2 = _out9
	if !((_21_rawEcdhKeyringT2).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(649,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_9_senderPrivateKey384, _19_recipientPublicKey521)), Companion_Default___.P384()))
	_21_rawEcdhKeyringT2 = _out10
	if !((_21_rawEcdhKeyringT2).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(662,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_15_senderPrivateKey521, _7_recipientPublicKey256)), Companion_Default___.P521()))
	_21_rawEcdhKeyringT2 = _out11
	if !((_21_rawEcdhKeyringT2).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(675,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out12 m_Wrappers.Result
	_ = _out12
	_out12 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_15_senderPrivateKey521, _13_recipientPublicKey384)), Companion_Default___.P521()))
	_21_rawEcdhKeyringT2 = _out12
	if !((_21_rawEcdhKeyringT2).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(688,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _22_rawEcdhKeyringT3 m_Wrappers.Result
	_ = _22_rawEcdhKeyringT3
	var _out13 m_Wrappers.Result
	_ = _out13
	_out13 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_9_senderPrivateKey384, _7_recipientPublicKey256)), Companion_Default___.P256()))
	_22_rawEcdhKeyringT3 = _out13
	if !((_22_rawEcdhKeyringT3).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(703,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out14 m_Wrappers.Result
	_ = _out14
	_out14 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_15_senderPrivateKey521, _7_recipientPublicKey256)), Companion_Default___.P256()))
	_22_rawEcdhKeyringT3 = _out14
	if !((_22_rawEcdhKeyringT3).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(716,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out15 m_Wrappers.Result
	_ = _out15
	_out15 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_3_senderPrivateKey256, _13_recipientPublicKey384)), Companion_Default___.P384()))
	_22_rawEcdhKeyringT3 = _out15
	if !((_22_rawEcdhKeyringT3).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(729,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out16 m_Wrappers.Result
	_ = _out16
	_out16 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_15_senderPrivateKey521, _13_recipientPublicKey384)), Companion_Default___.P384()))
	_22_rawEcdhKeyringT3 = _out16
	if !((_22_rawEcdhKeyringT3).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(742,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out17 m_Wrappers.Result
	_ = _out17
	_out17 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_3_senderPrivateKey256, _19_recipientPublicKey521)), Companion_Default___.P521()))
	_22_rawEcdhKeyringT3 = _out17
	if !((_22_rawEcdhKeyringT3).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(755,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out18 m_Wrappers.Result
	_ = _out18
	_out18 = (_1_mpl).CreateRawEcdhKeyring(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_9_senderPrivateKey384, _19_recipientPublicKey521)), Companion_Default___.P521()))
	_22_rawEcdhKeyringT3 = _out18
	if !((_22_rawEcdhKeyringT3).Is_Failure()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(768,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(773,15): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(778,33): " + (_4_valueOrError1).String())
	}
	var _5_encryptionMaterialsIn m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
	_ = _5_encryptionMaterialsIn
	_5_encryptionMaterialsIn = (_4_valueOrError1).Extract().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials)
	out = _5_encryptionMaterialsIn
	return out
	return out
}
func (_static *CompanionStruct_Default___) P256() m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()
}
func (_static *CompanionStruct_Default___) TEST__DBE__ALG__SUITE__ID() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_DBE_(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384_())
}
func (_static *CompanionStruct_Default___) P384() m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_()
}
func (_static *CompanionStruct_Default___) P521() m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec {
	return m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_()
}

// End of class Default__
