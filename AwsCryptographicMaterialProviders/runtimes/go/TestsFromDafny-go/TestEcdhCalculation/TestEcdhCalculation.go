// Package TestEcdhCalculation
// Dafny module TestEcdhCalculation compiled into Go

package TestEcdhCalculation

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
	m_TestMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestMultiKeyring"
	m_TestRawAESKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestRawAESKeyring"
	m_TestRawECDHKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestRawECDHKeyring"
	m_TestRawRSAKeying "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestRawRSAKeying"
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
var _ m_TestRawAESKeyring.Dummy__
var _ m_TestMultiKeyring.Dummy__
var _ m_TestRawRSAKeying.Dummy__

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
	return "TestEcdhCalculation.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestKmsDeriveSharedSecretOfflineCalculation() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(32,21): " + (_0_valueOrError0).String())
	}
	var _1_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_kmsClient
	_1_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(33,22): " + (_2_valueOrError1).String())
	}
	var _3_primitives *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _3_primitives
	_3_primitives = (_2_valueOrError1).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
	_ = _4_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_3_primitives).GenerateECCKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()))
	_4_valueOrError2 = _out2
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(35,19): " + (_4_valueOrError2).String())
	}
	var _5_keyPair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
	_ = _5_keyPair
	_5_keyPair = (_4_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
	if !(((_dafny.One).Cmp(_dafny.IntOfUint32((((_5_keyPair).Dtor_publicKey()).Dtor_der()).Cardinality())) <= 0) && ((_dafny.IntOfUint32((((_5_keyPair).Dtor_publicKey()).Dtor_der()).Cardinality())).Cmp(_dafny.IntOfInt64(8192)) <= 0)) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(41,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_kmsSharedSecret m_Wrappers.Result
	_ = _6_kmsSharedSecret
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_kmsClient).DeriveSharedSecret(m_ComAmazonawsKmsTypes.Companion_DeriveSharedSecretRequest_.Create_DeriveSharedSecretRequest_(Companion_Default___.SenderKmsKey(), m_ComAmazonawsKmsTypes.Companion_KeyAgreementAlgorithmSpec_.Create_ECDH_(), ((_5_keyPair).Dtor_publicKey()).Dtor_der(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_6_kmsSharedSecret = _out3
	if !((_6_kmsSharedSecret).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(50,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((((_6_kmsSharedSecret).Dtor_value().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse)).Dtor_SharedSecret()).Is_Some()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(51,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _7_publicKeyResponse m_Wrappers.Result
	_ = _7_publicKeyResponse
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_1_kmsClient).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_(Companion_Default___.SenderKmsKey(), m_Wrappers.Companion_Option_.Create_None_()))
	_7_publicKeyResponse = _out4
	if !((_7_publicKeyResponse).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(59,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_7_publicKeyResponse).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
	_ = _let_tmp_rhs0
	var _8___v0 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
	_ = _8___v0
	var _9_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
	_ = _9_PublicKey
	var _10___v1 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
	_ = _10___v1
	var _11___v2 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
	_ = _11___v2
	var _12___v3 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
	_ = _12___v3
	var _13___v4 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
	_ = _13___v4
	var _14___v5 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
	_ = _14___v5
	var _15___v6 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
	_ = _15___v6
	if !((_9_PublicKey).Is_Some()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(62,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _16_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretOutput_.Default())
	_ = _16_valueOrError3
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_3_primitives).DeriveSharedSecret(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretInput_.Create_DeriveSharedSecretInput_(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), (_5_keyPair).Dtor_privateKey(), m_AwsCryptographyPrimitivesTypes.Companion_ECCPublicKey_.Create_ECCPublicKey_((_9_PublicKey).Dtor_value().(_dafny.Sequence))))
	_16_valueOrError3 = _out5
	if !(!((_16_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(64,31): " + (_16_valueOrError3).String())
	}
	var _17_offlineSharedSecret m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
	_ = _17_offlineSharedSecret
	_17_offlineSharedSecret = (_16_valueOrError3).Extract().(m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput)
	if !(_dafny.Companion_Sequence_.Equal((((_6_kmsSharedSecret).Dtor_value().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse)).Dtor_SharedSecret()).Dtor_value().(_dafny.Sequence), (_17_offlineSharedSecret).Dtor_sharedSecret())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(72,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestKmsDeriveSharedSecretOfflineCalculationCurves() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(77,21): " + (_0_valueOrError0).String())
	}
	var _1_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_kmsClient
	_1_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(78,22): " + (_2_valueOrError1).String())
	}
	var _3_primitives *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _3_primitives
	_3_primitives = (_2_valueOrError1).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _hi0 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.SenderArns()).Cardinality())
	_ = _hi0
	for _4_i := _dafny.Zero; _4_i.Cmp(_hi0) < 0; _4_i = _4_i.Plus(_dafny.One) {
		var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairOutput_.Default())
		_ = _5_valueOrError2
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = (_3_primitives).GenerateECCKeyPair(m_AwsCryptographyPrimitivesTypes.Companion_GenerateECCKeyPairInput_.Create_GenerateECCKeyPairInput_((Companion_Default___.CurveSpecs()).Select((_4_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)))
		_5_valueOrError2 = _out2
		if !(!((_5_valueOrError2).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(82,21): " + (_5_valueOrError2).String())
		}
		var _6_keyPair m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
		_ = _6_keyPair
		_6_keyPair = (_5_valueOrError2).Extract().(m_AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput)
		if !(((_dafny.One).Cmp(_dafny.IntOfUint32((((_6_keyPair).Dtor_publicKey()).Dtor_der()).Cardinality())) <= 0) && ((_dafny.IntOfUint32((((_6_keyPair).Dtor_publicKey()).Dtor_der()).Cardinality())).Cmp(_dafny.IntOfInt64(8192)) <= 0)) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(87,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _7_kmsSharedSecret m_Wrappers.Result
		_ = _7_kmsSharedSecret
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = (_1_kmsClient).DeriveSharedSecret(m_ComAmazonawsKmsTypes.Companion_DeriveSharedSecretRequest_.Create_DeriveSharedSecretRequest_((Companion_Default___.SenderArns()).Select((_4_i).Uint32()).(_dafny.Sequence), m_ComAmazonawsKmsTypes.Companion_KeyAgreementAlgorithmSpec_.Create_ECDH_(), ((_6_keyPair).Dtor_publicKey()).Dtor_der(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
		_7_kmsSharedSecret = _out3
		if !((_7_kmsSharedSecret).Is_Success()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(96,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !((((_7_kmsSharedSecret).Dtor_value().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse)).Dtor_SharedSecret()).Is_Some()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(97,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _8_publicKeyResponse m_Wrappers.Result
		_ = _8_publicKeyResponse
		var _out4 m_Wrappers.Result
		_ = _out4
		_out4 = (_1_kmsClient).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_((Companion_Default___.SenderArns()).Select((_4_i).Uint32()).(_dafny.Sequence), m_Wrappers.Companion_Option_.Create_None_()))
		_8_publicKeyResponse = _out4
		if !((_8_publicKeyResponse).Is_Success()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(105,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_8_publicKeyResponse).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
		_ = _let_tmp_rhs0
		var _9___v7 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
		_ = _9___v7
		var _10_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
		_ = _10_PublicKey
		var _11___v8 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
		_ = _11___v8
		var _12___v9 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
		_ = _12___v9
		var _13___v10 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
		_ = _13___v10
		var _14___v11 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
		_ = _14___v11
		var _15___v12 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
		_ = _15___v12
		var _16___v13 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
		_ = _16___v13
		if !((_10_PublicKey).Is_Some()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(108,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _17_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretOutput_.Default())
		_ = _17_valueOrError3
		var _out5 m_Wrappers.Result
		_ = _out5
		_out5 = (_3_primitives).DeriveSharedSecret(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretInput_.Create_DeriveSharedSecretInput_((Companion_Default___.CurveSpecs()).Select((_4_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), (_6_keyPair).Dtor_privateKey(), m_AwsCryptographyPrimitivesTypes.Companion_ECCPublicKey_.Create_ECCPublicKey_((_10_PublicKey).Dtor_value().(_dafny.Sequence))))
		_17_valueOrError3 = _out5
		if !(!((_17_valueOrError3).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(110,33): " + (_17_valueOrError3).String())
		}
		var _18_offlineSharedSecret m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
		_ = _18_offlineSharedSecret
		_18_offlineSharedSecret = (_17_valueOrError3).Extract().(m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput)
		if !(_dafny.Companion_Sequence_.Equal((((_7_kmsSharedSecret).Dtor_value().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse)).Dtor_SharedSecret()).Dtor_value().(_dafny.Sequence), (_18_offlineSharedSecret).Dtor_sharedSecret())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(118,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) TestOfflineDeriveSharedSecretStaticKeys() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(125,21): " + (_0_valueOrError0).String())
	}
	var _1_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_kmsClient
	_1_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(126,22): " + (_2_valueOrError1).String())
	}
	var _3_primitives *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _3_primitives
	_3_primitives = (_2_valueOrError1).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _hi0 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.CurveSpecs()).Cardinality())
	_ = _hi0
	for _4_i := _dafny.Zero; _4_i.Cmp(_hi0) < 0; _4_i = _4_i.Plus(_dafny.One) {
		var _5_curve m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
		_ = _5_curve
		_5_curve = (Companion_Default___.CurveSpecs()).Select((_4_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
		var _6_senderArn _dafny.Sequence
		_ = _6_senderArn
		_6_senderArn = (Companion_Default___.SenderArns()).Select((_4_i).Uint32()).(_dafny.Sequence)
		var _7_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _7_valueOrError2
		_7_valueOrError2 = m_Base64.Companion_Default___.Decode((Companion_Default___.SenderArnPublicKeys()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_7_valueOrError2).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(132,29): " + (_7_valueOrError2).String())
		}
		var _8_senderPublicKey _dafny.Sequence
		_ = _8_senderPublicKey
		_8_senderPublicKey = (_7_valueOrError2).Extract().(_dafny.Sequence)
		var _9_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
		_ = _9_valueOrError3
		_9_valueOrError3 = m_UTF8.Encode((Companion_Default___.PrivateKeyReceivers()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_9_valueOrError3).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(133,33): " + (_9_valueOrError3).String())
		}
		var _10_recipientPrivateKey _dafny.Sequence
		_ = _10_recipientPrivateKey
		_10_recipientPrivateKey = (_9_valueOrError3).Extract().(_dafny.Sequence)
		var _11_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _11_valueOrError4
		_11_valueOrError4 = m_Base64.Companion_Default___.Decode((Companion_Default___.PublicKeyReceivers()).Select((_4_i).Uint32()).(_dafny.Sequence))
		if !(!((_11_valueOrError4).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(134,32): " + (_11_valueOrError4).String())
		}
		var _12_recipientPublicKey _dafny.Sequence
		_ = _12_recipientPublicKey
		_12_recipientPublicKey = (_11_valueOrError4).Extract().(_dafny.Sequence)
		var _13_kmsSharedSecret m_Wrappers.Result
		_ = _13_kmsSharedSecret
		var _out2 m_Wrappers.Result
		_ = _out2
		_out2 = (_1_kmsClient).DeriveSharedSecret(m_ComAmazonawsKmsTypes.Companion_DeriveSharedSecretRequest_.Create_DeriveSharedSecretRequest_(_6_senderArn, m_ComAmazonawsKmsTypes.Companion_KeyAgreementAlgorithmSpec_.Create_ECDH_(), _12_recipientPublicKey, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
		_13_kmsSharedSecret = _out2
		if !((_13_kmsSharedSecret).Is_Success()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(143,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !((((_13_kmsSharedSecret).Dtor_value().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse)).Dtor_SharedSecret()).Is_Some()) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(144,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		var _14_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretOutput_.Default())
		_ = _14_valueOrError5
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = (_3_primitives).DeriveSharedSecret(m_AwsCryptographyPrimitivesTypes.Companion_DeriveSharedSecretInput_.Create_DeriveSharedSecretInput_((Companion_Default___.CurveSpecs()).Select((_4_i).Uint32()).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec), m_AwsCryptographyPrimitivesTypes.Companion_ECCPrivateKey_.Create_ECCPrivateKey_(_10_recipientPrivateKey), m_AwsCryptographyPrimitivesTypes.Companion_ECCPublicKey_.Create_ECCPublicKey_(_8_senderPublicKey)))
		_14_valueOrError5 = _out3
		if !(!((_14_valueOrError5).IsFailure())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(146,33): " + (_14_valueOrError5).String())
		}
		var _15_offlineSharedSecret m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
		_ = _15_offlineSharedSecret
		_15_offlineSharedSecret = (_14_valueOrError5).Extract().(m_AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput)
		if !(_dafny.Companion_Sequence_.Equal((((_13_kmsSharedSecret).Dtor_value().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse)).Dtor_SharedSecret()).Dtor_value().(_dafny.Sequence), (_15_offlineSharedSecret).Dtor_sharedSecret())) {
			panic("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(155,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) SenderKmsKey() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9")
}
func (_static *CompanionStruct_Default___) SenderArns() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__384__KEY__ARN__S(), m_TestUtils.Companion_Default___.KMS__ECC__521__KEY__ARN__S())
}
func (_static *CompanionStruct_Default___) CurveSpecs() _dafny.Sequence {
	return _dafny.SeqOf(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_(), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_())
}
func (_static *CompanionStruct_Default___) SenderArnPublicKeys() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.KMS__ECC__256__PUBLIC__KEY__S(), m_TestUtils.Companion_Default___.KMS__ECC__384__PUBLIC__KEY__S(), m_TestUtils.Companion_Default___.KMS__ECC__521__PUBLIC__KEY__S())
}
func (_static *CompanionStruct_Default___) PrivateKeyReceivers() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.ECC__P256__PRIVATE(), m_TestUtils.Companion_Default___.ECC__P384__PRIVATE(), m_TestUtils.Companion_Default___.ECC__P521__PRIVATE())
}
func (_static *CompanionStruct_Default___) PublicKeyReceivers() _dafny.Sequence {
	return _dafny.SeqOf(m_TestUtils.Companion_Default___.ECC__P256__PUBLIC(), m_TestUtils.Companion_Default___.ECC__P384__PUBLIC(), m_TestUtils.Companion_Default___.ECC__P521__PUBLIC())
}
func (_static *CompanionStruct_Default___) RecipientKmsKey() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5")
}

// End of class Default__
