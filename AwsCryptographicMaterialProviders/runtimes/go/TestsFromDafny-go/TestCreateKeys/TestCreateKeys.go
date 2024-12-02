// Package TestCreateKeys
// Dafny module TestCreateKeys compiled into Go

package TestCreateKeys

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
	m_TestDiscoveryGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestDiscoveryGetKeys"
	m_TestGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestGetKeys"
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
	m_UUID "github.com/dafny-lang/DafnyStandardLibGo/UUID"
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
	return "TestCreateKeys.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestCreateBranchAndBeaconKeys() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(68,21): " + (_0_valueOrError0).String())
	}
	var _1_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_kmsClient
	_1_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(69,21): " + (_2_valueOrError1).String())
	}
	var _3_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _3_ddbClient
	_3_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _4_kmsConfig
	_4_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(m_Fixtures.Companion_Default___.KeyArn())
	var _5_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _5_keyStoreConfig
	_5_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), _4_kmsConfig, m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_3_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_1_kmsClient))
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_KeyStore.Companion_Default___.KeyStore(_5_keyStoreConfig)
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(82,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyOutput_.Default())
	_ = _8_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).CreateKey(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyInput_.Create_CreateKeyInput_(m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_8_valueOrError3 = _out3
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(84,23): " + (_8_valueOrError3).String())
	}
	var _9_branchKeyId m_AwsCryptographyKeyStoreTypes.CreateKeyOutput
	_ = _9_branchKeyId
	_9_branchKeyId = (_8_valueOrError3).Extract().(m_AwsCryptographyKeyStoreTypes.CreateKeyOutput)
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBeaconKeyOutput_.Default())
	_ = _10_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_7_keyStore).GetBeaconKey(m_AwsCryptographyKeyStoreTypes.Companion_GetBeaconKeyInput_.Create_GetBeaconKeyInput_((_9_branchKeyId).Dtor_branchKeyIdentifier()))
	_10_valueOrError4 = _out4
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(88,27): " + (_10_valueOrError4).String())
	}
	var _11_beaconKeyResult m_AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
	_ = _11_beaconKeyResult
	_11_beaconKeyResult = (_10_valueOrError4).Extract().(m_AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput)
	var _12_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _12_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_9_branchKeyId).Dtor_branchKeyIdentifier()))
	_12_valueOrError5 = _out5
	if !(!((_12_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(93,24): " + (_12_valueOrError5).String())
	}
	var _13_activeResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _13_activeResult
	_13_activeResult = (_12_valueOrError5).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _14_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _14_valueOrError6
	_14_valueOrError6 = m_UTF8.Decode(((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_14_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(98,28): " + (_14_valueOrError6).String())
	}
	var _15_branchKeyVersion _dafny.Sequence
	_ = _15_branchKeyVersion
	_15_branchKeyVersion = (_14_valueOrError6).Extract().(_dafny.Sequence)
	var _16_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionOutput_.Default())
	_ = _16_valueOrError7
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_7_keyStore).GetBranchKeyVersion(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionInput_.Create_GetBranchKeyVersionInput_((_9_branchKeyId).Dtor_branchKeyIdentifier(), _15_branchKeyVersion))
	_16_valueOrError7 = _out6
	if !(!((_16_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(99,25): " + (_16_valueOrError7).String())
	}
	var _17_versionResult m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
	_ = _17_versionResult
	_17_versionResult = (_16_valueOrError7).Extract().(m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput)
	m_CleanupItems.Companion_Default___.DeleteVersion((_9_branchKeyId).Dtor_branchKeyIdentifier(), _15_branchKeyVersion, _3_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteActive((_9_branchKeyId).Dtor_branchKeyIdentifier(), _3_ddbClient)
	if !((((_11_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_beaconKey()).Is_Some()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(111,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32(((((_11_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_beaconKey()).Dtor_value().(_dafny.Sequence)).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(112,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(113,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_17_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKey(), ((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(114,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.Companion_Sequence_.Equal(((_17_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), ((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier())) && (_dafny.Companion_Sequence_.Equal(((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), ((_11_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_beaconKeyIdentifier()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(115,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_17_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), ((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(118,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _18_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _18_valueOrError8
	_18_valueOrError8 = m_UUID.ToByteArray(((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier())
	if !(!((_18_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(125,22): " + (_18_valueOrError8).String())
	}
	var _19_idByteUUID _dafny.Sequence
	_ = _19_idByteUUID
	_19_idByteUUID = (_18_valueOrError8).Extract().(_dafny.Sequence)
	var _20_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _20_valueOrError9
	_20_valueOrError9 = m_UUID.FromByteArray(_19_idByteUUID)
	if !(!((_20_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(126,23): " + (_20_valueOrError9).String())
	}
	var _21_idRoundTrip _dafny.Sequence
	_ = _21_idRoundTrip
	_21_idRoundTrip = (_20_valueOrError9).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_21_idRoundTrip, ((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(127,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _22_valueOrError10 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _22_valueOrError10
	_22_valueOrError10 = m_UTF8.Decode(((_13_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_22_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(133,25): " + (_22_valueOrError10).String())
	}
	var _23_versionString _dafny.Sequence
	_ = _23_versionString
	_23_versionString = (_22_valueOrError10).Extract().(_dafny.Sequence)
	var _24_valueOrError11 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _24_valueOrError11
	_24_valueOrError11 = m_UUID.ToByteArray(_23_versionString)
	if !(!((_24_valueOrError11).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(134,27): " + (_24_valueOrError11).String())
	}
	var _25_versionByteUUID _dafny.Sequence
	_ = _25_versionByteUUID
	_25_versionByteUUID = (_24_valueOrError11).Extract().(_dafny.Sequence)
	var _26_valueOrError12 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _26_valueOrError12
	_26_valueOrError12 = m_UUID.FromByteArray(_25_versionByteUUID)
	if !(!((_26_valueOrError12).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(135,28): " + (_26_valueOrError12).String())
	}
	var _27_versionRoundTrip _dafny.Sequence
	_ = _27_versionRoundTrip
	_27_versionRoundTrip = (_26_valueOrError12).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_27_versionRoundTrip, _23_versionString)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(136,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestCreateOptions() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(142,21): " + (_0_valueOrError0).String())
	}
	var _1_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_kmsClient
	_1_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(143,21): " + (_2_valueOrError1).String())
	}
	var _3_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _3_ddbClient
	_3_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _4_kmsConfig
	_4_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(m_Fixtures.Companion_Default___.KeyArn())
	var _5_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _5_keyStoreConfig
	_5_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), _4_kmsConfig, m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_3_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_1_kmsClient))
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_KeyStore.Companion_Default___.KeyStore(_5_keyStoreConfig)
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(156,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _8_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_UUID.GenerateUUID()
	_8_valueOrError3 = _out3
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(159,14): " + (_8_valueOrError3).String())
	}
	var _9_id _dafny.Sequence
	_ = _9_id
	_9_id = (_8_valueOrError3).Extract().(_dafny.Sequence)
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptyMap)
	_ = _10_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_Fixtures.Companion_Default___.EncodeEncryptionContext(_dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString("some"), _dafny.SeqOfString("encryption")).UpdateUnsafe(_dafny.SeqOfString("context"), _dafny.SeqOfString("values")))
	_10_valueOrError4 = _out4
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(161,29): " + (_10_valueOrError4).String())
	}
	var _11_encryptionContext _dafny.Map
	_ = _11_encryptionContext
	_11_encryptionContext = (_10_valueOrError4).Extract().(_dafny.Map)
	var _12_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyOutput_.Default())
	_ = _12_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_7_keyStore).CreateKey(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyInput_.Create_CreateKeyInput_(m_Wrappers.Companion_Option_.Create_Some_(_9_id), m_Wrappers.Companion_Option_.Create_Some_(_11_encryptionContext)))
	_12_valueOrError5 = _out5
	if !(!((_12_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(166,23): " + (_12_valueOrError5).String())
	}
	var _13_branchKeyId m_AwsCryptographyKeyStoreTypes.CreateKeyOutput
	_ = _13_branchKeyId
	_13_branchKeyId = (_12_valueOrError5).Extract().(m_AwsCryptographyKeyStoreTypes.CreateKeyOutput)
	var _14_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBeaconKeyOutput_.Default())
	_ = _14_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_7_keyStore).GetBeaconKey(m_AwsCryptographyKeyStoreTypes.Companion_GetBeaconKeyInput_.Create_GetBeaconKeyInput_((_13_branchKeyId).Dtor_branchKeyIdentifier()))
	_14_valueOrError6 = _out6
	if !(!((_14_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(171,27): " + (_14_valueOrError6).String())
	}
	var _15_beaconKeyResult m_AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
	_ = _15_beaconKeyResult
	_15_beaconKeyResult = (_14_valueOrError6).Extract().(m_AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput)
	var _16_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _16_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_13_branchKeyId).Dtor_branchKeyIdentifier()))
	_16_valueOrError7 = _out7
	if !(!((_16_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(176,24): " + (_16_valueOrError7).String())
	}
	var _17_activeResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _17_activeResult
	_17_activeResult = (_16_valueOrError7).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _18_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _18_valueOrError8
	_18_valueOrError8 = m_UTF8.Decode(((_17_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_18_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(181,28): " + (_18_valueOrError8).String())
	}
	var _19_branchKeyVersion _dafny.Sequence
	_ = _19_branchKeyVersion
	_19_branchKeyVersion = (_18_valueOrError8).Extract().(_dafny.Sequence)
	var _20_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionOutput_.Default())
	_ = _20_valueOrError9
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_7_keyStore).GetBranchKeyVersion(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionInput_.Create_GetBranchKeyVersionInput_((_13_branchKeyId).Dtor_branchKeyIdentifier(), _19_branchKeyVersion))
	_20_valueOrError9 = _out8
	if !(!((_20_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(182,25): " + (_20_valueOrError9).String())
	}
	var _21_versionResult m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
	_ = _21_versionResult
	_21_versionResult = (_20_valueOrError9).Extract().(m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput)
	m_CleanupItems.Companion_Default___.DeleteVersion((_13_branchKeyId).Dtor_branchKeyIdentifier(), _19_branchKeyVersion, _3_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteActive((_13_branchKeyId).Dtor_branchKeyIdentifier(), _3_ddbClient)
	if !(((_dafny.Companion_Sequence_.Equal(_9_id, ((_21_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier())) && (_dafny.Companion_Sequence_.Equal(((_21_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), ((_17_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier()))) && (_dafny.Companion_Sequence_.Equal(((_17_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), ((_15_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_beaconKeyIdentifier()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(195,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((((_11_encryptionContext).Equals(((_21_versionResult).Dtor_branchKeyMaterials()).Dtor_encryptionContext())) && ((((_21_versionResult).Dtor_branchKeyMaterials()).Dtor_encryptionContext()).Equals(((_17_activeResult).Dtor_branchKeyMaterials()).Dtor_encryptionContext()))) && ((((_17_activeResult).Dtor_branchKeyMaterials()).Dtor_encryptionContext()).Equals(((_15_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_encryptionContext()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(200,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestCreateDuplicate() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(209,21): " + (_0_valueOrError0).String())
	}
	var _1_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_kmsClient
	_1_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(210,21): " + (_2_valueOrError1).String())
	}
	var _3_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _3_ddbClient
	_3_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _4_kmsConfig
	_4_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(m_Fixtures.Companion_Default___.KeyArn())
	var _5_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _5_keyStoreConfig
	_5_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), _4_kmsConfig, m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_3_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_1_kmsClient))
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_KeyStore.Companion_Default___.KeyStore(_5_keyStoreConfig)
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(223,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_attempt m_Wrappers.Result
	_ = _8_attempt
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).CreateKey(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyInput_.Create_CreateKeyInput_(m_Wrappers.Companion_Option_.Create_Some_(m_Fixtures.Companion_Default___.BranchKeyId()), m_Wrappers.Companion_Option_.Create_None_()))
	_8_attempt = _out3
	if !((_8_attempt).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(230,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) InsertingADuplicateWillFail() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(236,21): " + (_0_valueOrError0).String())
	}
	var _1_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _1_ddbClient
	_1_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_encryptionContext _dafny.Map
	_ = _2_encryptionContext
	_2_encryptionContext = m_Structure.Companion_Default___.DecryptOnlyBranchKeyEncryptionContext(m_Fixtures.Companion_Default___.BranchKeyId(), m_Fixtures.Companion_Default___.BranchKeyIdActiveVersion(), _dafny.SeqOfString(""), _dafny.SeqOfString(""), m_Fixtures.Companion_Default___.KeyArn(), _dafny.NewMapBuilder().ToMap())
	var _3_output m_Wrappers.Result
	_ = _3_output
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_DDBKeystoreOperations.Companion_Default___.WriteNewKeyToStore(m_Structure.Companion_Default___.ToAttributeMap(_2_encryptionContext, _dafny.SeqOf(uint8(1))), m_Structure.Companion_Default___.ToAttributeMap(m_Structure.Companion_Default___.ActiveBranchKeyEncryptionContext(_2_encryptionContext), _dafny.SeqOf(uint8(2))), m_Structure.Companion_Default___.ToAttributeMap(m_Structure.Companion_Default___.BeaconKeyEncryptionContext(_2_encryptionContext), _dafny.SeqOf(uint8(3))), m_Fixtures.Companion_Default___.BranchKeyStoreName(), _1_ddbClient)
	_3_output = _out1
	if !((_3_output).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(255,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) InsertingADuplicateWillWithADifferentVersionFail() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(261,21): " + (_0_valueOrError0).String())
	}
	var _1_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _1_ddbClient
	_1_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_encryptionContext _dafny.Map
	_ = _2_encryptionContext
	_2_encryptionContext = m_Structure.Companion_Default___.DecryptOnlyBranchKeyEncryptionContext(m_Fixtures.Companion_Default___.BranchKeyId(), _dafny.SeqOfString("!= branchKeyIdActiveVersion"), _dafny.SeqOfString(""), _dafny.SeqOfString(""), m_Fixtures.Companion_Default___.KeyArn(), _dafny.NewMapBuilder().ToMap())
	var _3_output m_Wrappers.Result
	_ = _3_output
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_DDBKeystoreOperations.Companion_Default___.WriteNewKeyToStore(m_Structure.Companion_Default___.ToAttributeMap(_2_encryptionContext, _dafny.SeqOf(uint8(1))), m_Structure.Companion_Default___.ToAttributeMap(m_Structure.Companion_Default___.ActiveBranchKeyEncryptionContext(_2_encryptionContext), _dafny.SeqOf(uint8(2))), m_Structure.Companion_Default___.ToAttributeMap(m_Structure.Companion_Default___.BeaconKeyEncryptionContext(_2_encryptionContext), _dafny.SeqOf(uint8(3))), m_Fixtures.Companion_Default___.BranchKeyStoreName(), _1_ddbClient)
	_3_output = _out1
	if !((_3_output).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(280,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
