// Package TestVersionKey
// Dafny module TestVersionKey compiled into Go

package TestVersionKey

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
	m_TestCreateKeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeyStore"
	m_TestCreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestCreateKeys"
	m_TestDiscoveryGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestDiscoveryGetKeys"
	m_TestGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestGetKeys"
	m_TestLyingBranchKey "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestLyingBranchKey"
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
var _ m_TestCreateKeys.Dummy__
var _ m_TestCreateKeyStore.Dummy__
var _ m_TestLyingBranchKey.Dummy__

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
	return "TestVersionKey.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestVersionKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(27,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(28,21): " + (_2_valueOrError1).String())
	}
	var _3_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _3_ddbClient
	_3_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _4_kmsConfig
	_4_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(m_Fixtures.Companion_Default___.KeyArn())
	if !(m_ComAmazonawsDynamodbTypes.Companion_Default___.IsValid__TableName(m_Fixtures.Companion_Default___.BranchKeyStoreName())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(30,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
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
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(42,20): " + (_6_valueOrError2).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(47,23): " + (_8_valueOrError3).String())
	}
	var _9_branchKeyId m_AwsCryptographyKeyStoreTypes.CreateKeyOutput
	_ = _9_branchKeyId
	_9_branchKeyId = (_8_valueOrError3).Extract().(m_AwsCryptographyKeyStoreTypes.CreateKeyOutput)
	var _10_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _10_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_9_branchKeyId).Dtor_branchKeyIdentifier()))
	_10_valueOrError4 = _out4
	if !(!((_10_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(52,27): " + (_10_valueOrError4).String())
	}
	var _11_oldActiveResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _11_oldActiveResult
	_11_oldActiveResult = (_10_valueOrError4).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _12_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _12_valueOrError5
	_12_valueOrError5 = m_UTF8.Decode(((_11_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_12_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(57,28): " + (_12_valueOrError5).String())
	}
	var _13_oldActiveVersion _dafny.Sequence
	_ = _13_oldActiveVersion
	_13_oldActiveVersion = (_12_valueOrError5).Extract().(_dafny.Sequence)
	var _14_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_VersionKeyOutput_.Default())
	_ = _14_valueOrError6
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_7_keyStore).VersionKey(m_AwsCryptographyKeyStoreTypes.Companion_VersionKeyInput_.Create_VersionKeyInput_((_9_branchKeyId).Dtor_branchKeyIdentifier()))
	_14_valueOrError6 = _out5
	if !(!((_14_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(59,28): " + (_14_valueOrError6).String())
	}
	var _15_versionKeyResult m_AwsCryptographyKeyStoreTypes.VersionKeyOutput
	_ = _15_versionKeyResult
	_15_versionKeyResult = (_14_valueOrError6).Extract().(m_AwsCryptographyKeyStoreTypes.VersionKeyOutput)
	var _16_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionOutput_.Default())
	_ = _16_valueOrError7
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_7_keyStore).GetBranchKeyVersion(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionInput_.Create_GetBranchKeyVersionInput_((_9_branchKeyId).Dtor_branchKeyIdentifier(), _13_oldActiveVersion))
	_16_valueOrError7 = _out6
	if !(!((_16_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(64,37): " + (_16_valueOrError7).String())
	}
	var _17_getBranchKeyVersionResult m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
	_ = _17_getBranchKeyVersionResult
	_17_getBranchKeyVersionResult = (_16_valueOrError7).Extract().(m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput)
	var _18_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _18_valueOrError8
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_9_branchKeyId).Dtor_branchKeyIdentifier()))
	_18_valueOrError8 = _out7
	if !(!((_18_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(72,27): " + (_18_valueOrError8).String())
	}
	var _19_newActiveResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _19_newActiveResult
	_19_newActiveResult = (_18_valueOrError8).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _20_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _20_valueOrError9
	_20_valueOrError9 = m_UTF8.Decode(((_19_newActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_20_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(77,28): " + (_20_valueOrError9).String())
	}
	var _21_newActiveVersion _dafny.Sequence
	_ = _21_newActiveVersion
	_21_newActiveVersion = (_20_valueOrError9).Extract().(_dafny.Sequence)
	m_CleanupItems.Companion_Default___.DeleteVersion((_9_branchKeyId).Dtor_branchKeyIdentifier(), _21_newActiveVersion, _3_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteVersion((_9_branchKeyId).Dtor_branchKeyIdentifier(), _13_oldActiveVersion, _3_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteActive((_9_branchKeyId).Dtor_branchKeyIdentifier(), _3_ddbClient)
	if !(_dafny.Companion_Sequence_.Equal(((_17_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), ((_11_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(87,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_17_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKey(), ((_11_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(88,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(!_dafny.Companion_Sequence_.Equal(((_17_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), ((_19_newActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(90,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(!_dafny.Companion_Sequence_.Equal(((_17_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKey(), ((_19_newActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(91,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestVersionKeyWithEC() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(96,21): " + (_0_valueOrError0).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(97,21): " + (_2_valueOrError1).String())
	}
	var _3_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _3_ddbClient
	_3_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_2_valueOrError1).Extract())
	var _4_kmsConfig m_AwsCryptographyKeyStoreTypes.KMSConfiguration
	_ = _4_kmsConfig
	_4_kmsConfig = m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(m_Fixtures.Companion_Default___.KeyArn())
	if !(m_ComAmazonawsDynamodbTypes.Companion_Default___.IsValid__TableName(m_Fixtures.Companion_Default___.BranchKeyStoreName())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(99,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
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
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(111,20): " + (_6_valueOrError2).String())
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
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(116,14): " + (_8_valueOrError3).String())
	}
	var _9_id _dafny.Sequence
	_ = _9_id
	_9_id = (_8_valueOrError3).Extract().(_dafny.Sequence)
	var _10_customEC _dafny.Map
	_ = _10_customEC
	_10_customEC = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString("some"), _dafny.SeqOfString("encryption")).UpdateUnsafe(_dafny.SeqOfString("context"), _dafny.SeqOfString("values"))
	var _11_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptyMap)
	_ = _11_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_Fixtures.Companion_Default___.EncodeEncryptionContext(_10_customEC)
	_11_valueOrError4 = _out4
	if !(!((_11_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(122,29): " + (_11_valueOrError4).String())
	}
	var _12_encryptionContext _dafny.Map
	_ = _12_encryptionContext
	_12_encryptionContext = (_11_valueOrError4).Extract().(_dafny.Map)
	var _13_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyOutput_.Default())
	_ = _13_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_7_keyStore).CreateKey(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyInput_.Create_CreateKeyInput_(m_Wrappers.Companion_Option_.Create_Some_(_9_id), m_Wrappers.Companion_Option_.Create_Some_(_12_encryptionContext)))
	_13_valueOrError5 = _out5
	if !(!((_13_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(124,23): " + (_13_valueOrError5).String())
	}
	var _14_branchKeyId m_AwsCryptographyKeyStoreTypes.CreateKeyOutput
	_ = _14_branchKeyId
	_14_branchKeyId = (_13_valueOrError5).Extract().(m_AwsCryptographyKeyStoreTypes.CreateKeyOutput)
	if !(_dafny.Companion_Sequence_.Equal((_14_branchKeyId).Dtor_branchKeyIdentifier(), _9_id)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(129,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _15_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _15_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_14_branchKeyId).Dtor_branchKeyIdentifier()))
	_15_valueOrError6 = _out6
	if !(!((_15_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(131,27): " + (_15_valueOrError6).String())
	}
	var _16_oldActiveResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _16_oldActiveResult
	_16_oldActiveResult = (_15_valueOrError6).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _17_mat m_AwsCryptographyKeyStoreTypes.BranchKeyMaterials
	_ = _17_mat
	_17_mat = (_16_oldActiveResult).Dtor_branchKeyMaterials()
	if !(_dafny.Companion_Sequence_.Equal((_17_mat).Dtor_branchKeyIdentifier(), _9_id)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(136,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _18_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptyMap)
	_ = _18_valueOrError7
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = m_Fixtures.Companion_Default___.DecodeEncryptionContext((_17_mat).Dtor_encryptionContext())
	_18_valueOrError7 = _out7
	if !(!((_18_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(137,17): " + (_18_valueOrError7).String())
	}
	var _19_matEC _dafny.Map
	_ = _19_matEC
	_19_matEC = (_18_valueOrError7).Extract().(_dafny.Map)
	if !((_19_matEC).Equals(_10_customEC)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(138,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _20_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _20_valueOrError8
	_20_valueOrError8 = m_UTF8.Decode(((_16_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_20_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(140,28): " + (_20_valueOrError8).String())
	}
	var _21_oldActiveVersion _dafny.Sequence
	_ = _21_oldActiveVersion
	_21_oldActiveVersion = (_20_valueOrError8).Extract().(_dafny.Sequence)
	var _22_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_VersionKeyOutput_.Default())
	_ = _22_valueOrError9
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_7_keyStore).VersionKey(m_AwsCryptographyKeyStoreTypes.Companion_VersionKeyInput_.Create_VersionKeyInput_((_14_branchKeyId).Dtor_branchKeyIdentifier()))
	_22_valueOrError9 = _out8
	if !(!((_22_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(142,28): " + (_22_valueOrError9).String())
	}
	var _23_versionKeyResult m_AwsCryptographyKeyStoreTypes.VersionKeyOutput
	_ = _23_versionKeyResult
	_23_versionKeyResult = (_22_valueOrError9).Extract().(m_AwsCryptographyKeyStoreTypes.VersionKeyOutput)
	var _24_valueOrError10 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionOutput_.Default())
	_ = _24_valueOrError10
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_7_keyStore).GetBranchKeyVersion(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionInput_.Create_GetBranchKeyVersionInput_((_14_branchKeyId).Dtor_branchKeyIdentifier(), _21_oldActiveVersion))
	_24_valueOrError10 = _out9
	if !(!((_24_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(147,37): " + (_24_valueOrError10).String())
	}
	var _25_getBranchKeyVersionResult m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
	_ = _25_getBranchKeyVersionResult
	_25_getBranchKeyVersionResult = (_24_valueOrError10).Extract().(m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput)
	var _26_mat2 m_AwsCryptographyKeyStoreTypes.BranchKeyMaterials
	_ = _26_mat2
	_26_mat2 = (_25_getBranchKeyVersionResult).Dtor_branchKeyMaterials()
	if !(_dafny.Companion_Sequence_.Equal((_17_mat).Dtor_branchKeyIdentifier(), _9_id)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(155,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _27_valueOrError11 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptyMap)
	_ = _27_valueOrError11
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = m_Fixtures.Companion_Default___.DecodeEncryptionContext((_17_mat).Dtor_encryptionContext())
	_27_valueOrError11 = _out10
	if !(!((_27_valueOrError11).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(156,18): " + (_27_valueOrError11).String())
	}
	var _28_mat2EC _dafny.Map
	_ = _28_mat2EC
	_28_mat2EC = (_27_valueOrError11).Extract().(_dafny.Map)
	if !((_28_mat2EC).Equals(_10_customEC)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(157,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_26_mat2).Dtor_branchKeyVersion(), (_17_mat).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(158,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _29_valueOrError12 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _29_valueOrError12
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_7_keyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_14_branchKeyId).Dtor_branchKeyIdentifier()))
	_29_valueOrError12 = _out11
	if !(!((_29_valueOrError12).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(160,27): " + (_29_valueOrError12).String())
	}
	var _30_newActiveResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _30_newActiveResult
	_30_newActiveResult = (_29_valueOrError12).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _31_mat3 m_AwsCryptographyKeyStoreTypes.BranchKeyMaterials
	_ = _31_mat3
	_31_mat3 = (_30_newActiveResult).Dtor_branchKeyMaterials()
	if !(_dafny.Companion_Sequence_.Equal((_17_mat).Dtor_branchKeyIdentifier(), _9_id)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(165,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _32_valueOrError13 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptyMap)
	_ = _32_valueOrError13
	var _out12 m_Wrappers.Result
	_ = _out12
	_out12 = m_Fixtures.Companion_Default___.DecodeEncryptionContext((_17_mat).Dtor_encryptionContext())
	_32_valueOrError13 = _out12
	if !(!((_32_valueOrError13).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(166,18): " + (_32_valueOrError13).String())
	}
	var _33_mat3EC _dafny.Map
	_ = _33_mat3EC
	_33_mat3EC = (_32_valueOrError13).Extract().(_dafny.Map)
	if !((_33_mat3EC).Equals(_10_customEC)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(167,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(!_dafny.Companion_Sequence_.Equal((_31_mat3).Dtor_branchKeyVersion(), (_17_mat).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(168,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _34_valueOrError14 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _34_valueOrError14
	_34_valueOrError14 = m_UTF8.Decode(((_30_newActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_34_valueOrError14).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(170,28): " + (_34_valueOrError14).String())
	}
	var _35_newActiveVersion _dafny.Sequence
	_ = _35_newActiveVersion
	_35_newActiveVersion = (_34_valueOrError14).Extract().(_dafny.Sequence)
	if !(!_dafny.Companion_Sequence_.Equal(_35_newActiveVersion, _21_oldActiveVersion)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(172,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	m_CleanupItems.Companion_Default___.DeleteVersion((_14_branchKeyId).Dtor_branchKeyIdentifier(), _35_newActiveVersion, _3_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteVersion((_14_branchKeyId).Dtor_branchKeyIdentifier(), _21_oldActiveVersion, _3_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteActive((_14_branchKeyId).Dtor_branchKeyIdentifier(), _3_ddbClient)
	if !(_dafny.Companion_Sequence_.Equal(((_25_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), ((_16_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(182,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_25_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKey(), ((_16_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(183,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(!_dafny.Companion_Sequence_.Equal(((_25_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), ((_30_newActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(185,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(!_dafny.Companion_Sequence_.Equal(((_25_getBranchKeyVersionResult).Dtor_branchKeyMaterials()).Dtor_branchKey(), ((_30_newActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(186,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_19_matEC).Equals(_10_customEC)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(193,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_28_mat2EC).Equals(_10_customEC)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(194,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_33_mat3EC).Equals(_10_customEC)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(195,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestMrkVersionKey() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(200,21): " + (_0_valueOrError0).String())
	}
	var _1_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _1_ddbClient
	_1_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_eastKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _2_eastKeyStoreConfig
	_2_eastKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_(m_Fixtures.Companion_Default___.BranchKeyStoreName(), m_Fixtures.Companion_Default___.KmsMrkConfigEast(), m_Fixtures.Companion_Default___.LogicalKeyStoreName(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_1_ddbClient), m_Wrappers.Companion_Option_.Create_None_())
	var _3_westKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _3_westKeyStoreConfig
	var _4_dt__update__tmp_h0 m_AwsCryptographyKeyStoreTypes.KeyStoreConfig = _2_eastKeyStoreConfig
	_ = _4_dt__update__tmp_h0
	var _5_dt__update_hkmsConfiguration_h0 m_AwsCryptographyKeyStoreTypes.KMSConfiguration = m_Fixtures.Companion_Default___.KmsMrkConfigWest()
	_ = _5_dt__update_hkmsConfiguration_h0
	_3_westKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_((_4_dt__update__tmp_h0).Dtor_ddbTableName(), _5_dt__update_hkmsConfiguration_h0, (_4_dt__update__tmp_h0).Dtor_logicalKeyStoreName(), (_4_dt__update__tmp_h0).Dtor_id(), (_4_dt__update__tmp_h0).Dtor_grantTokens(), (_4_dt__update__tmp_h0).Dtor_ddbClient(), (_4_dt__update__tmp_h0).Dtor_kmsClient())
	var _6_eastSrkKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _6_eastSrkKeyStoreConfig
	var _7_dt__update__tmp_h1 m_AwsCryptographyKeyStoreTypes.KeyStoreConfig = _2_eastKeyStoreConfig
	_ = _7_dt__update__tmp_h1
	var _8_dt__update_hkmsConfiguration_h1 m_AwsCryptographyKeyStoreTypes.KMSConfiguration = m_Fixtures.Companion_Default___.KmsSrkConfigEast()
	_ = _8_dt__update_hkmsConfiguration_h1
	_6_eastSrkKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_((_7_dt__update__tmp_h1).Dtor_ddbTableName(), _8_dt__update_hkmsConfiguration_h1, (_7_dt__update__tmp_h1).Dtor_logicalKeyStoreName(), (_7_dt__update__tmp_h1).Dtor_id(), (_7_dt__update__tmp_h1).Dtor_grantTokens(), (_7_dt__update__tmp_h1).Dtor_ddbClient(), (_7_dt__update__tmp_h1).Dtor_kmsClient())
	var _9_westSrkKeyStoreConfig m_AwsCryptographyKeyStoreTypes.KeyStoreConfig
	_ = _9_westSrkKeyStoreConfig
	var _10_dt__update__tmp_h2 m_AwsCryptographyKeyStoreTypes.KeyStoreConfig = _2_eastKeyStoreConfig
	_ = _10_dt__update__tmp_h2
	var _11_dt__update_hkmsConfiguration_h2 m_AwsCryptographyKeyStoreTypes.KMSConfiguration = m_Fixtures.Companion_Default___.KmsSrkConfigWest()
	_ = _11_dt__update_hkmsConfiguration_h2
	_9_westSrkKeyStoreConfig = m_AwsCryptographyKeyStoreTypes.Companion_KeyStoreConfig_.Create_KeyStoreConfig_((_10_dt__update__tmp_h2).Dtor_ddbTableName(), _11_dt__update_hkmsConfiguration_h2, (_10_dt__update__tmp_h2).Dtor_logicalKeyStoreName(), (_10_dt__update__tmp_h2).Dtor_id(), (_10_dt__update__tmp_h2).Dtor_grantTokens(), (_10_dt__update__tmp_h2).Dtor_ddbClient(), (_10_dt__update__tmp_h2).Dtor_kmsClient())
	var _12_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _12_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_KeyStore.Companion_Default___.KeyStore(_2_eastKeyStoreConfig)
	_12_valueOrError1 = _out1
	if !(!((_12_valueOrError1).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(215,24): " + (_12_valueOrError1).String())
	}
	var _13_eastKeyStore *m_KeyStore.KeyStoreClient
	_ = _13_eastKeyStore
	_13_eastKeyStore = (_12_valueOrError1).Extract().(*m_KeyStore.KeyStoreClient)
	var _14_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _14_valueOrError2
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = m_KeyStore.Companion_Default___.KeyStore(_3_westKeyStoreConfig)
	_14_valueOrError2 = _out2
	if !(!((_14_valueOrError2).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(216,24): " + (_14_valueOrError2).String())
	}
	var _15_westKeyStore *m_KeyStore.KeyStoreClient
	_ = _15_westKeyStore
	_15_westKeyStore = (_14_valueOrError2).Extract().(*m_KeyStore.KeyStoreClient)
	var _16_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _16_valueOrError3
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_KeyStore.Companion_Default___.KeyStore(_6_eastSrkKeyStoreConfig)
	_16_valueOrError3 = _out3
	if !(!((_16_valueOrError3).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(217,27): " + (_16_valueOrError3).String())
	}
	var _17_eastSrkKeyStore *m_KeyStore.KeyStoreClient
	_ = _17_eastSrkKeyStore
	_17_eastSrkKeyStore = (_16_valueOrError3).Extract().(*m_KeyStore.KeyStoreClient)
	var _18_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _18_valueOrError4
	var _out4 m_Wrappers.Result
	_ = _out4
	_out4 = m_KeyStore.Companion_Default___.KeyStore(_9_westSrkKeyStoreConfig)
	_18_valueOrError4 = _out4
	if !(!((_18_valueOrError4).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(218,27): " + (_18_valueOrError4).String())
	}
	var _19_westSrkKeyStore *m_KeyStore.KeyStoreClient
	_ = _19_westSrkKeyStore
	_19_westSrkKeyStore = (_18_valueOrError4).Extract().(*m_KeyStore.KeyStoreClient)
	var _20_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyOutput_.Default())
	_ = _20_valueOrError5
	var _out5 m_Wrappers.Result
	_ = _out5
	_out5 = (_15_westKeyStore).CreateKey(m_AwsCryptographyKeyStoreTypes.Companion_CreateKeyInput_.Create_CreateKeyInput_(m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_20_valueOrError5 = _out5
	if !(!((_20_valueOrError5).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(223,23): " + (_20_valueOrError5).String())
	}
	var _21_branchKeyId m_AwsCryptographyKeyStoreTypes.CreateKeyOutput
	_ = _21_branchKeyId
	_21_branchKeyId = (_20_valueOrError5).Extract().(m_AwsCryptographyKeyStoreTypes.CreateKeyOutput)
	var _22_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _22_valueOrError6
	var _out6 m_Wrappers.Result
	_ = _out6
	_out6 = (_15_westKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_21_branchKeyId).Dtor_branchKeyIdentifier()))
	_22_valueOrError6 = _out6
	if !(!((_22_valueOrError6).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(228,27): " + (_22_valueOrError6).String())
	}
	var _23_oldActiveResult m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _23_oldActiveResult
	_23_oldActiveResult = (_22_valueOrError6).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _24_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _24_valueOrError7
	_24_valueOrError7 = m_UTF8.Decode(((_23_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_24_valueOrError7).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(233,28): " + (_24_valueOrError7).String())
	}
	var _25_oldActiveVersion _dafny.Sequence
	_ = _25_oldActiveVersion
	_25_oldActiveVersion = (_24_valueOrError7).Extract().(_dafny.Sequence)
	var _26_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_VersionKeyOutput_.Default())
	_ = _26_valueOrError8
	var _out7 m_Wrappers.Result
	_ = _out7
	_out7 = (_13_eastKeyStore).VersionKey(m_AwsCryptographyKeyStoreTypes.Companion_VersionKeyInput_.Create_VersionKeyInput_((_21_branchKeyId).Dtor_branchKeyIdentifier()))
	_26_valueOrError8 = _out7
	if !(!((_26_valueOrError8).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(236,28): " + (_26_valueOrError8).String())
	}
	var _27_versionKeyResult m_AwsCryptographyKeyStoreTypes.VersionKeyOutput
	_ = _27_versionKeyResult
	_27_versionKeyResult = (_26_valueOrError8).Extract().(m_AwsCryptographyKeyStoreTypes.VersionKeyOutput)
	var _28_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionOutput_.Default())
	_ = _28_valueOrError9
	var _out8 m_Wrappers.Result
	_ = _out8
	_out8 = (_15_westKeyStore).GetBranchKeyVersion(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionInput_.Create_GetBranchKeyVersionInput_((_21_branchKeyId).Dtor_branchKeyIdentifier(), _25_oldActiveVersion))
	_28_valueOrError9 = _out8
	if !(!((_28_valueOrError9).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(241,41): " + (_28_valueOrError9).String())
	}
	var _29_getBranchKeyVersionResultWest m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
	_ = _29_getBranchKeyVersionResultWest
	_29_getBranchKeyVersionResultWest = (_28_valueOrError9).Extract().(m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput)
	var _30_valueOrError10 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionOutput_.Default())
	_ = _30_valueOrError10
	var _out9 m_Wrappers.Result
	_ = _out9
	_out9 = (_13_eastKeyStore).GetBranchKeyVersion(m_AwsCryptographyKeyStoreTypes.Companion_GetBranchKeyVersionInput_.Create_GetBranchKeyVersionInput_((_21_branchKeyId).Dtor_branchKeyIdentifier(), _25_oldActiveVersion))
	_30_valueOrError10 = _out9
	if !(!((_30_valueOrError10).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(249,41): " + (_30_valueOrError10).String())
	}
	var _31_getBranchKeyVersionResultEast m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
	_ = _31_getBranchKeyVersionResultEast
	_31_getBranchKeyVersionResultEast = (_30_valueOrError10).Extract().(m_AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput)
	if !((_29_getBranchKeyVersionResultWest).Equals(_31_getBranchKeyVersionResultEast)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(257,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _32_valueOrError11 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _32_valueOrError11
	var _out10 m_Wrappers.Result
	_ = _out10
	_out10 = (_15_westKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_21_branchKeyId).Dtor_branchKeyIdentifier()))
	_32_valueOrError11 = _out10
	if !(!((_32_valueOrError11).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(259,31): " + (_32_valueOrError11).String())
	}
	var _33_newActiveResultWest m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _33_newActiveResultWest
	_33_newActiveResultWest = (_32_valueOrError11).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	var _34_valueOrError12 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _34_valueOrError12
	var _out11 m_Wrappers.Result
	_ = _out11
	_out11 = (_13_eastKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_21_branchKeyId).Dtor_branchKeyIdentifier()))
	_34_valueOrError12 = _out11
	if !(!((_34_valueOrError12).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(263,31): " + (_34_valueOrError12).String())
	}
	var _35_newActiveResultEast m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _35_newActiveResultEast
	_35_newActiveResultEast = (_34_valueOrError12).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !((_33_newActiveResultWest).Equals(_35_newActiveResultEast)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(268,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _36_valueOrError13 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyOutput_.Default())
	_ = _36_valueOrError13
	var _out12 m_Wrappers.Result
	_ = _out12
	_out12 = (_19_westSrkKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_21_branchKeyId).Dtor_branchKeyIdentifier()))
	_36_valueOrError13 = _out12
	if !(!((_36_valueOrError13).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(274,34): " + (_36_valueOrError13).String())
	}
	var _37_newActiveResultSrkWest m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
	_ = _37_newActiveResultSrkWest
	_37_newActiveResultSrkWest = (_36_valueOrError13).Extract().(m_AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput)
	if !((_37_newActiveResultSrkWest).Equals(_35_newActiveResultEast)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(279,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _38_newActiveResultSrkEastResult m_Wrappers.Result
	_ = _38_newActiveResultSrkEastResult
	var _out13 m_Wrappers.Result
	_ = _out13
	_out13 = (_17_eastSrkKeyStore).GetActiveBranchKey(m_AwsCryptographyKeyStoreTypes.Companion_GetActiveBranchKeyInput_.Create_GetActiveBranchKeyInput_((_21_branchKeyId).Dtor_branchKeyIdentifier()))
	_38_newActiveResultSrkEastResult = _out13
	if !((_38_newActiveResultSrkEastResult).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(285,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_38_newActiveResultSrkEastResult).Dtor_error().(m_AwsCryptographyKeyStoreTypes.Error)).Equals(m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.GET__KEY__ARN__DISAGREEMENT()))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(286,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _39_valueOrError14 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _39_valueOrError14
	_39_valueOrError14 = m_UTF8.Decode(((_33_newActiveResultWest).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_39_valueOrError14).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(289,32): " + (_39_valueOrError14).String())
	}
	var _40_newActiveVersionWest _dafny.Sequence
	_ = _40_newActiveVersionWest
	_40_newActiveVersionWest = (_39_valueOrError14).Extract().(_dafny.Sequence)
	var _41_valueOrError15 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _41_valueOrError15
	_41_valueOrError15 = m_UTF8.Decode(((_35_newActiveResultEast).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())
	if !(!((_41_valueOrError15).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(290,32): " + (_41_valueOrError15).String())
	}
	var _42_newActiveVersionEast _dafny.Sequence
	_ = _42_newActiveVersionEast
	_42_newActiveVersionEast = (_41_valueOrError15).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_40_newActiveVersionWest, _42_newActiveVersionEast)) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(291,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	m_CleanupItems.Companion_Default___.DeleteVersion((_21_branchKeyId).Dtor_branchKeyIdentifier(), _42_newActiveVersionEast, _1_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteVersion((_21_branchKeyId).Dtor_branchKeyIdentifier(), _25_oldActiveVersion, _1_ddbClient)
	m_CleanupItems.Companion_Default___.DeleteActive((_21_branchKeyId).Dtor_branchKeyIdentifier(), _1_ddbClient)
	if !(_dafny.Companion_Sequence_.Equal(((_31_getBranchKeyVersionResultEast).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), ((_23_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(301,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_31_getBranchKeyVersionResultEast).Dtor_branchKeyMaterials()).Dtor_branchKey(), ((_23_oldActiveResult).Dtor_branchKeyMaterials()).Dtor_branchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(302,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(!_dafny.Companion_Sequence_.Equal(((_31_getBranchKeyVersionResultEast).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion(), ((_35_newActiveResultEast).Dtor_branchKeyMaterials()).Dtor_branchKeyVersion())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(304,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(!_dafny.Companion_Sequence_.Equal(((_31_getBranchKeyVersionResultEast).Dtor_branchKeyMaterials()).Dtor_branchKey(), ((_35_newActiveResultEast).Dtor_branchKeyMaterials()).Dtor_branchKey())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(305,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) InsertingADuplicateVersionWillFail() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(316,21): " + (_0_valueOrError0).String())
	}
	var _1_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _1_ddbClient
	_1_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_0_valueOrError0).Extract())
	if !((_dafny.IntOfUint32((m_Fixtures.Companion_Default___.BranchKeyId()).Cardinality())).Sign() == 1) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(318,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((m_Fixtures.Companion_Default___.BranchKeyIdActiveVersion()).Cardinality())).Sign() == 1) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(319,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _2_customEncryptionContext _dafny.Map
	_ = _2_customEncryptionContext
	_2_customEncryptionContext = _dafny.NewMapBuilder().ToMap()
	if !(_dafny.Quantifier((_2_customEncryptionContext).Keys().Elements(), true, func(_forall_var_0 _dafny.Sequence) bool {
		var _3_k _dafny.Sequence
		_3_k = interface{}(_forall_var_0).(_dafny.Sequence)
		return !((_2_customEncryptionContext).Contains(_3_k)) || (m_ComAmazonawsDynamodbTypes.Companion_Default___.IsValid__AttributeName(_dafny.Companion_Sequence_.Concatenate(m_Structure.Companion_Default___.ENCRYPTION__CONTEXT__PREFIX(), _3_k)))
	})) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(321,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _4_encryptionContext _dafny.Map
	_ = _4_encryptionContext
	_4_encryptionContext = m_Structure.Companion_Default___.DecryptOnlyBranchKeyEncryptionContext(m_Fixtures.Companion_Default___.BranchKeyId(), m_Fixtures.Companion_Default___.BranchKeyIdActiveVersion(), _dafny.SeqOfString(""), _dafny.SeqOfString(""), m_Fixtures.Companion_Default___.KeyArn(), _dafny.NewMapBuilder().ToMap())
	if !(m_ComAmazonawsDynamodbTypes.Companion_Default___.IsValid__TableName(m_Fixtures.Companion_Default___.BranchKeyStoreName())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(332,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_myBranchKeyStoreName _dafny.Sequence
	_ = _5_myBranchKeyStoreName
	_5_myBranchKeyStoreName = m_Fixtures.Companion_Default___.BranchKeyStoreName()
	var _6_versionBranchKeyItem _dafny.Map
	_ = _6_versionBranchKeyItem
	_6_versionBranchKeyItem = m_Structure.Companion_Default___.ToAttributeMap(_4_encryptionContext, _dafny.SeqOf(uint8(1)))
	var _7_activeBranchKeyItem _dafny.Map
	_ = _7_activeBranchKeyItem
	_7_activeBranchKeyItem = m_Structure.Companion_Default___.ToAttributeMap(m_Structure.Companion_Default___.ActiveBranchKeyEncryptionContext(_4_encryptionContext), _dafny.SeqOf(uint8(2)))
	if !(((_7_activeBranchKeyItem).Get(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Equals((_6_versionBranchKeyItem).Get(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(336,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_7_activeBranchKeyItem).Get(m_Structure.Companion_Default___.BRANCH__KEY__ACTIVE__VERSION__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Equals((_6_versionBranchKeyItem).Get(m_Structure.Companion_Default___.TYPE__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(337,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_output m_Wrappers.Result
	_ = _8_output
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_DDBKeystoreOperations.Companion_Default___.WriteNewBranchKeyVersionToKeystore(_6_versionBranchKeyItem, _7_activeBranchKeyItem, _5_myBranchKeyStoreName, _1_ddbClient)
	_8_output = _out1
	if !((_8_output).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(346,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) VersioningANonexistentBranchKeyWillFail() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(352,21): " + (_0_valueOrError0).String())
	}
	var _1_ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _1_ddbClient
	_1_ddbClient = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_encryptionContext _dafny.Map
	_ = _2_encryptionContext
	_2_encryptionContext = m_Structure.Companion_Default___.DecryptOnlyBranchKeyEncryptionContext(_dafny.SeqOfString("!= branchKeyId"), m_Fixtures.Companion_Default___.BranchKeyIdActiveVersion(), _dafny.SeqOfString(""), _dafny.SeqOfString(""), m_Fixtures.Companion_Default___.KeyArn(), _dafny.NewMapBuilder().ToMap())
	var _3_versionBranchKeyItem _dafny.Map
	_ = _3_versionBranchKeyItem
	_3_versionBranchKeyItem = m_Structure.Companion_Default___.ToAttributeMap(_2_encryptionContext, _dafny.SeqOf(uint8(1)))
	var _4_activeBranchKeyItem _dafny.Map
	_ = _4_activeBranchKeyItem
	_4_activeBranchKeyItem = m_Structure.Companion_Default___.ToAttributeMap(m_Structure.Companion_Default___.ActiveBranchKeyEncryptionContext(_2_encryptionContext), _dafny.SeqOf(uint8(2)))
	if !(((_4_activeBranchKeyItem).Get(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Equals((_3_versionBranchKeyItem).Get(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(365,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_4_activeBranchKeyItem).Get(m_Structure.Companion_Default___.BRANCH__KEY__ACTIVE__VERSION__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Equals((_3_versionBranchKeyItem).Get(m_Structure.Companion_Default___.TYPE__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue))) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(366,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_ComAmazonawsDynamodbTypes.Companion_Default___.IsValid__TableName(m_Fixtures.Companion_Default___.BranchKeyStoreName())) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(367,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_myBranchKeyStoreName _dafny.Sequence
	_ = _5_myBranchKeyStoreName
	_5_myBranchKeyStoreName = m_Fixtures.Companion_Default___.BranchKeyStoreName()
	var _6_output m_Wrappers.Result
	_ = _6_output
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_DDBKeystoreOperations.Companion_Default___.WriteNewBranchKeyVersionToKeystore(_3_versionBranchKeyItem, _4_activeBranchKeyItem, _5_myBranchKeyStoreName, _1_ddbClient)
	_6_output = _out1
	if !((_6_output).Is_Failure()) {
		panic("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(377,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
