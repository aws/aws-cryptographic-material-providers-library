// Package TestGetKeys
// Dafny module TestGetKeys compiled into Go

package TestGetKeys

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
	m_Fixtures "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/Fixtures"
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
	return "TestGetKeys.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestGetBeaconKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(23,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(24,21): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(37,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBeaconKeyOutput_.Default())
	_ = _8_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).GetBeaconKey(m_AwsCryptographyKeyStoreTypes.Companion_GetBeaconKeyInput_.Create_GetBeaconKeyInput_(m_Fixtures.Companion_Default___.BranchKeyId()))
	_8_valueOrError3 = _out3
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(39,27): " + (_8_valueOrError3).String())
	}
	var _9_beaconKeyResult m_AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
	_ = _9_beaconKeyResult
	_9_beaconKeyResult = (_8_valueOrError3).Extract().(m_AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_9_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_beaconKeyIdentifier(), m_Fixtures.Companion_Default___.BranchKeyId())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(43,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((((_9_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_beaconKey()).Is_Some()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(44,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32(((((_9_beaconKeyResult).Dtor_beaconKeyMaterials()).Dtor_beaconKey()).Dtor_value().(_dafny.Sequence)).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(45,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGetActiveKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(50,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(51,21): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(64,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _8_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.BranchKeyId()))
	_8_valueOrError3 = _out3
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(66,24): " + (_8_valueOrError3).String())
	}
	var _9_activeResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _9_activeResult
	_9_activeResult = (_8_valueOrError3).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_9_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.BranchKeyId())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(71,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_9_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), m_Fixtures.Companion_Default___.BranchKeyIdActiveVersionUtf8Bytes())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(72,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_9_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(73,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGetActiveMrkKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(78,21): " + (_0_valueOrError0).String())
	}
	var _1_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _1_ddbClient
	_1_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_eastKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _2_eastKeyStoreConfig
	_2_eastKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), m_Fixtures.Companion_Default___.KmsConfigEast(), m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_1_ddbClient), m_Wrappers.Companion_Option_.Create_None_())
	var _3_westKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _3_westKeyStoreConfig
	_3_westKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), m_Fixtures.Companion_Default___.KmsConfigWest(), m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_1_ddbClient), m_Wrappers.Companion_Option_.Create_None_())
	var _4_eastMrkKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _4_eastMrkKeyStoreConfig
	_4_eastMrkKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), m_Fixtures.Companion_Default___.KmsMrkConfigEast(), m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_1_ddbClient), m_Wrappers.Companion_Option_.Create_None_())
	var _5_westMrkKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _5_westMrkKeyStoreConfig
	_5_westMrkKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), m_Fixtures.Companion_Default___.KmsMrkConfigWest(), m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_1_ddbClient), m_Wrappers.Companion_Option_.Create_None_())
	var _6_apMrkKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _6_apMrkKeyStoreConfig
	_6_apMrkKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), m_Fixtures.Companion_Default___.KmsMrkConfigAP(), m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_1_ddbClient), m_Wrappers.Companion_Option_.Create_None_())
	var _7_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _7_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_KeyStore.Companion_Default___.KeyStore(_3_westKeyStoreConfig)
	_7_valueOrError1 = _out1
	if !(!((_7_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(127,24): " + (_7_valueOrError1).String())
	}
	var _8_westKeyStore *m_KeyStore.KeyStoreClient
	_ = _8_westKeyStore
	_8_westKeyStore = (_7_valueOrError1).Extract().(*m_KeyStore.KeyStoreClient)
	var _9_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _9_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_KeyStore.Companion_Default___.KeyStore(_2_eastKeyStoreConfig)
	_9_valueOrError2 = _out2
	if !(!((_9_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(128,24): " + (_9_valueOrError2).String())
	}
	var _10_eastKeyStore *m_KeyStore.KeyStoreClient
	_ = _10_eastKeyStore
	_10_eastKeyStore = (_9_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _11_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _11_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_KeyStore.Companion_Default___.KeyStore(_5_westMrkKeyStoreConfig)
	_11_valueOrError3 = _out3
	if !(!((_11_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(129,27): " + (_11_valueOrError3).String())
	}
	var _12_westMrkKeyStore *m_KeyStore.KeyStoreClient
	_ = _12_westMrkKeyStore
	_12_westMrkKeyStore = (_11_valueOrError3).Extract().(*m_KeyStore.KeyStoreClient)
	var _13_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _13_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_KeyStore.Companion_Default___.KeyStore(_4_eastMrkKeyStoreConfig)
	_13_valueOrError4 = _out4
	if !(!((_13_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(130,27): " + (_13_valueOrError4).String())
	}
	var _14_eastMrkKeyStore *m_KeyStore.KeyStoreClient
	_ = _14_eastMrkKeyStore
	_14_eastMrkKeyStore = (_13_valueOrError4).Extract().(*m_KeyStore.KeyStoreClient)
	var _15_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _15_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = m_KeyStore.Companion_Default___.KeyStore(_6_apMrkKeyStoreConfig)
	_15_valueOrError5 = _out5
	if !(!((_15_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(131,25): " + (_15_valueOrError5).String())
	}
	var _16_apMrkKeyStore *m_KeyStore.KeyStoreClient
	_ = _16_apMrkKeyStore
	_16_apMrkKeyStore = (_15_valueOrError5).Extract().(*m_KeyStore.KeyStoreClient)
	var _17_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _17_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_8_westKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.WestBranchKey()))
	_17_valueOrError6 = _out6
	if !(!((_17_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(135,24): " + (_17_valueOrError6).String())
	}
	var _18_activeResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _18_activeResult
	_18_activeResult = (_17_valueOrError6).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.WestBranchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(137,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(138,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _19_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _19_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_10_eastKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.EastBranchKey()))
	_19_valueOrError7 = _out7
	if !(!((_19_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(140,20): " + (_19_valueOrError7).String())
	}
	_18_activeResult = (_19_valueOrError7).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.EastBranchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(142,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(143,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _20_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _20_valueOrError8
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_12_westMrkKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.WestBranchKey()))
	_20_valueOrError8 = _out8
	if !(!((_20_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(145,20): " + (_20_valueOrError8).String())
	}
	_18_activeResult = (_20_valueOrError8).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.WestBranchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(147,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(148,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _21_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _21_valueOrError9
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_14_eastMrkKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.EastBranchKey()))
	_21_valueOrError9 = _out9
	if !(!((_21_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(150,20): " + (_21_valueOrError9).String())
	}
	_18_activeResult = (_21_valueOrError9).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.EastBranchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(152,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(153,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _22_valueOrError10 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _22_valueOrError10
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_12_westMrkKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.EastBranchKey()))
	_22_valueOrError10 = _out10
	if !(!((_22_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(157,20): " + (_22_valueOrError10).String())
	}
	_18_activeResult = (_22_valueOrError10).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.EastBranchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(159,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(160,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _23_valueOrError11 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _23_valueOrError11
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_14_eastMrkKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.WestBranchKey()))
	_23_valueOrError11 = _out11
	if !(!((_23_valueOrError11).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(162,20): " + (_23_valueOrError11).String())
	}
	_18_activeResult = (_23_valueOrError11).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal(((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.WestBranchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(164,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_18_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(165,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _24_badResult m_Wrappers.Result
	_ = _24_badResult
	var _out12 m_Wrappers.Result
	_ = _out12
	_out12 = (_8_westKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.EastBranchKey()))
	_24_badResult = _out12
	if !((_24_badResult).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(171,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_24_badResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)).Equals(m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.GET__KEY__ARN__DISAGREEMENT()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(172,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out13 m_Wrappers.Result
	_ = _out13
	_out13 = (_10_eastKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.WestBranchKey()))
	_24_badResult = _out13
	if !((_24_badResult).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(176,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_24_badResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)).Equals(m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.GET__KEY__ARN__DISAGREEMENT()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(177,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _out14 m_Wrappers.Result
	_ = _out14
	_out14 = (_16_apMrkKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.WestBranchKey()))
	_24_badResult = _out14
	if !((_24_badResult).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(183,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_24_badResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)).Is_ComAmazonawsKms()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(184,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((((_24_badResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)).Dtor_ComAmazonawsKms()).Is_Opaque()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(185,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGetBranchKeyVersion() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(191,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(192,21): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(205,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionOutput_.Default())
	_ = _8_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).GetBranchKeyVersion(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionInput_.Create_GetBranchKeyVersionInput_(m_Fixtures.Companion_Default___.BranchKeyId(), m_Fixtures.Companion_Default___.BranchKeyIdActiveVersion()))
	_8_valueOrError3 = _out3
	if !(!((_8_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(207,25): " + (_8_valueOrError3).String())
	}
	var _9_versionResult m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
	_ = _9_versionResult
	_9_versionResult = (_8_valueOrError3).Extract().(m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput)
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _10_valueOrError4
	_10_valueOrError4 = m_UTF8.Encode(m_Fixtures.Companion_Default___.BranchKeyIdActiveVersion())
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(213,21): " + (_10_valueOrError4).String())
	}
	var _11_testBytes _dafny.Sequence
	_ = _11_testBytes
	_11_testBytes = (_10_valueOrError4).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(((_9_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyIdentifier(), m_Fixtures.Companion_Default___.BranchKeyId())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(215,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.Companion_Sequence_.Equal(((_9_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), m_Fixtures.Companion_Default___.BranchKeyIdActiveVersionUtf8Bytes())) && (_dafny.Companion_Sequence_.Equal(m_Fixtures.Companion_Default___.BranchKeyIdActiveVersionUtf8Bytes(), _11_testBytes))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(216,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_9_versionResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(217,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGetActiveKeyWithIncorrectKmsKeyArn() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(222,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(223,21): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(236,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_activeResult m_Wrappers.Result
	_ = _8_activeResult
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.PostalHornBranchKeyId()))
	_8_activeResult = _out3
	if !((_8_activeResult).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(242,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_8_activeResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)).Equals(m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.GET__KEY__ARN__DISAGREEMENT()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(243,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGetActiveKeyWrongLogicalKeyStoreName() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(247,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(248,21): " + (_2_valueOrError1).String())
	}
	var _3_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _3_ddbClient
	_3_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _4_kmsConfig
	_4_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(m_Fixtures.Companion_Default___.KeyArn())
	var _5_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _5_keyStoreConfig
	_5_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), _4_kmsConfig, Companion_Default___.IncorrectLogicalName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_3_ddbClient), m_Wrappers.Companion_Option_.Create_Some_(_1_kmsClient))
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _6_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_KeyStore.Companion_Default___.KeyStore(_5_keyStoreConfig)
	_6_valueOrError2 = _out2
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(261,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_activeResult m_Wrappers.Result
	_ = _8_activeResult
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.BranchKeyId()))
	_8_activeResult = _out3
	if !((_8_activeResult).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(268,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _source0 m_AwsCryptographyKeyStoreTypes.Error = (_8_activeResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)
	_ = _source0
	{
		{
			if _source0.Is_ComAmazonawsKms() {
				var _9_nestedError m_ComAmazonawsKmsTypes.Error = _source0.Get_().(m_AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms).ComAmazonawsKms
				_ = _9_nestedError
				if !((_9_nestedError).Is_InvalidCiphertextException()) {
					panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(271,8): " + (_dafny.SeqOfString("expectation violation")).String())
				}
				goto Lmatch0
			}
		}
		{
			if !(false) {
				panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(272,16): " + (_dafny.SeqOfString("Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException.")).String())
			}
		}
		goto Lmatch0
	}
Lmatch0:
}
func (_static *CompanionStruct_Default___) TestGetActiveKeyDoesNotExistFails() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(278,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(279,21): " + (_2_valueOrError1).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(292,20): " + (_6_valueOrError2).String())
	}
	var _7_keyStore *m_KeyStore.KeyStoreClient
	_ = _7_keyStore
	_7_keyStore = (_6_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _8_activeResult m_Wrappers.Result
	_ = _8_activeResult
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(_dafny.SeqOfString("Robbie")))
	_8_activeResult = _out3
	if !((_8_activeResult).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(299,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_8_activeResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)).Equals(m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.NO__CORRESPONDING__BRANCH__KEY()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(300,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGetActiveKeyWithNoClients() {
	var _0_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _0_kmsConfig
	_0_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(m_Fixtures.Companion_Default___.KeyArn())
	var _1_keyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _1_keyStoreConfig
	_1_keyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), _0_kmsConfig, m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _2_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_KeyStore.Companion_Default___.KeyStore(_1_keyStoreConfig)
	_2_valueOrError0 = _out0
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(317,20): " + (_2_valueOrError0).String())
	}
	var _3_keyStore *m_KeyStore.KeyStoreClient
	_ = _3_keyStore
	_3_keyStore = (_2_valueOrError0).Extract().(*m_KeyStore.KeyStoreClient)
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _4_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_3_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_(m_Fixtures.Companion_Default___.BranchKeyId()))
	_4_valueOrError1 = _out1
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(319,24): " + (_4_valueOrError1).String())
	}
	var _5_activeResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _5_activeResult
	_5_activeResult = (_4_valueOrError1).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !((_dafny.IntOfUint32((((_5_activeResult).Dtor_branchKeyMaterials()).Dtor_branchKey()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) {
		panic("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(324,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) IncorrectLogicalName() _dafny.Sequence {
	return _dafny.SeqOfString("MySuperAwesomeTableName")
}

// End of class Default__
