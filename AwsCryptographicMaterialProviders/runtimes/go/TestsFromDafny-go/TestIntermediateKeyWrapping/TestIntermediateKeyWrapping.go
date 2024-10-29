// Package TestIntermediateKeyWrapping
// Dafny module TestIntermediateKeyWrapping compiled into Go

package TestIntermediateKeyWrapping

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
	m_TestEcdhCalculation "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestEcdhCalculation"
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
var _ m_TestEcdhCalculation.Dummy__

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
	return "TestIntermediateKeyWrapping.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) IntermediateWrapUnwrapTest() {
	var _0_encCtx _dafny.Map
	_ = _0_encCtx
	_0_encCtx = _dafny.NewMapBuilder().ToMap()
	var _1_keyLen _dafny.Int
	_ = _1_keyLen
	_1_keyLen = _dafny.IntOfInt32((((Companion_Default___.TEST__ALG__SUITE()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength())
	var _2_tagLen _dafny.Int
	_ = _2_tagLen
	_2_tagLen = _dafny.IntOfInt32((((Companion_Default___.TEST__ALG__SUITE()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_tagLength())
	var _3_pdk _dafny.Sequence
	_ = _3_pdk
	_3_pdk = _dafny.SeqCreate((_1_keyLen).Uint32(), func(coer15 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg15 _dafny.Int) interface{} {
			return coer15(arg15)
		}
	}(func(_4___v2 _dafny.Int) uint8 {
		return uint8(0)
	}))
	var _5_testGenerateAndWrap *TestGenerateAndWrapKeyMaterial
	_ = _5_testGenerateAndWrap
	var _nw0 *TestGenerateAndWrapKeyMaterial = New_TestGenerateAndWrapKeyMaterial_()
	_ = _nw0
	_nw0.Ctor__()
	_5_testGenerateAndWrap = _nw0
	var _6_intermediateWrapOutput m_Wrappers.Result
	_ = _6_intermediateWrapOutput
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_IntermediateKeyWrapping.Companion_Default___.IntermediateWrap(_5_testGenerateAndWrap, _3_pdk, Companion_Default___.TEST__ALG__SUITE(), _0_encCtx)
	_6_intermediateWrapOutput = _out0
	if !((_6_intermediateWrapOutput).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(36,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_6_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateWrapOutput)).Dtor_wrappedMaterial()).Cardinality())).Cmp(((_1_keyLen).Plus(_2_tagLen)).Plus(_dafny.IntOfUint32((Companion_Default___.WRAPPED__MAT()).Cardinality()))) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(37,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((((_6_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateWrapOutput)).Dtor_wrappedMaterial()).Drop(((_1_keyLen).Plus(_2_tagLen)).Uint32()), Companion_Default___.WRAPPED__MAT())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(38,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _7_testUnwrap *TestUnwrapKeyMaterial
	_ = _7_testUnwrap
	var _nw1 *TestUnwrapKeyMaterial = New_TestUnwrapKeyMaterial_()
	_ = _nw1
	_nw1.Ctor__()
	_7_testUnwrap = _nw1
	var _8_intermediateUnwrapOutput m_Wrappers.Result
	_ = _8_intermediateUnwrapOutput
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_IntermediateKeyWrapping.Companion_Default___.IntermediateUnwrap(_7_testUnwrap, ((_6_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateWrapOutput)).Dtor_wrappedMaterial(), Companion_Default___.TEST__ALG__SUITE(), _0_encCtx)
	_8_intermediateUnwrapOutput = _out1
	if !((_8_intermediateUnwrapOutput).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(47,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_8_intermediateUnwrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateUnwrapOutput)).Dtor_plaintextDataKey(), _3_pdk)) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(48,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_6_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateWrapOutput)).Dtor_symmetricSigningKey(), ((_8_intermediateUnwrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateUnwrapOutput)).Dtor_symmetricSigningKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(49,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) IntermediateGenerateAndWrapUnwrapTest() {
	var _0_encCtx _dafny.Map
	_ = _0_encCtx
	_0_encCtx = _dafny.NewMapBuilder().ToMap()
	var _1_keyLen _dafny.Int
	_ = _1_keyLen
	_1_keyLen = _dafny.IntOfInt32((((Companion_Default___.TEST__ALG__SUITE()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength())
	var _2_tagLen _dafny.Int
	_ = _2_tagLen
	_2_tagLen = _dafny.IntOfInt32((((Companion_Default___.TEST__ALG__SUITE()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_tagLength())
	var _3_testGenerateAndWrap *TestGenerateAndWrapKeyMaterial
	_ = _3_testGenerateAndWrap
	var _nw0 *TestGenerateAndWrapKeyMaterial = New_TestGenerateAndWrapKeyMaterial_()
	_ = _nw0
	_nw0.Ctor__()
	_3_testGenerateAndWrap = _nw0
	var _4_intermediateWrapOutput m_Wrappers.Result
	_ = _4_intermediateWrapOutput
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_IntermediateKeyWrapping.Companion_Default___.IntermediateGenerateAndWrap(_3_testGenerateAndWrap, Companion_Default___.TEST__ALG__SUITE(), _0_encCtx)
	_4_intermediateWrapOutput = _out0
	if !((_4_intermediateWrapOutput).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(63,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32((((_4_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput)).Dtor_wrappedMaterial()).Cardinality())).Cmp(((_1_keyLen).Plus(_2_tagLen)).Plus(_dafny.IntOfUint32((Companion_Default___.WRAPPED__MAT()).Cardinality()))) == 0) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(64,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((((_4_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput)).Dtor_wrappedMaterial()).Drop(((_1_keyLen).Plus(_2_tagLen)).Uint32()), Companion_Default___.WRAPPED__MAT())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(65,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_testUnwrap *TestUnwrapKeyMaterial
	_ = _5_testUnwrap
	var _nw1 *TestUnwrapKeyMaterial = New_TestUnwrapKeyMaterial_()
	_ = _nw1
	_nw1.Ctor__()
	_5_testUnwrap = _nw1
	var _6_intermediateUnwrapOutput m_Wrappers.Result
	_ = _6_intermediateUnwrapOutput
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_IntermediateKeyWrapping.Companion_Default___.IntermediateUnwrap(_5_testUnwrap, ((_4_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput)).Dtor_wrappedMaterial(), Companion_Default___.TEST__ALG__SUITE(), _0_encCtx)
	_6_intermediateUnwrapOutput = _out1
	if !((_6_intermediateUnwrapOutput).Is_Success()) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(74,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_4_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput)).Dtor_plaintextDataKey(), ((_6_intermediateUnwrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateUnwrapOutput)).Dtor_plaintextDataKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(75,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(((_4_intermediateWrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput)).Dtor_symmetricSigningKey(), ((_6_intermediateUnwrapOutput).Dtor_value().(m_IntermediateKeyWrapping.IntermediateUnwrapOutput)).Dtor_symmetricSigningKey())) {
		panic("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(76,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TEST__ALG__SUITE() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AlgorithmSuites.Companion_Default___.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()
}
func (_static *CompanionStruct_Default___) PLAINTEXT__MAT() _dafny.Sequence {
	return _dafny.SeqCreate((_dafny.IntOfInt32((((Companion_Default___.TEST__ALG__SUITE()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength())).Uint32(), func(coer16 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg16 _dafny.Int) interface{} {
			return coer16(arg16)
		}
	}(func(_0___v0 _dafny.Int) uint8 {
		return uint8(1)
	}))
}
func (_static *CompanionStruct_Default___) WRAPPED__MAT() _dafny.Sequence {
	return _dafny.SeqCreate((_dafny.IntOfInt32((((Companion_Default___.TEST__ALG__SUITE()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength())).Uint32(), func(coer17 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg17 _dafny.Int) interface{} {
			return coer17(arg17)
		}
	}(func(_0___v1 _dafny.Int) uint8 {
		return uint8(2)
	}))
}

// End of class Default__

// Definition of datatype TestInfo
type TestInfo struct {
	Data_TestInfo_
}

func (_this TestInfo) Get_() Data_TestInfo_ {
	return _this.Data_TestInfo_
}

type Data_TestInfo_ interface {
	isTestInfo()
}

type CompanionStruct_TestInfo_ struct {
}

var Companion_TestInfo_ = CompanionStruct_TestInfo_{}

type TestInfo_TestInfo struct {
}

func (TestInfo_TestInfo) isTestInfo() {}

func (CompanionStruct_TestInfo_) Create_TestInfo_() TestInfo {
	return TestInfo{TestInfo_TestInfo{}}
}

func (_this TestInfo) Is_TestInfo() bool {
	_, ok := _this.Get_().(TestInfo_TestInfo)
	return ok
}

func (CompanionStruct_TestInfo_) Default() TestInfo {
	return Companion_TestInfo_.Create_TestInfo_()
}

func (_ CompanionStruct_TestInfo_) AllSingletonConstructors() _dafny.Iterator {
	i := -1
	return func() (interface{}, bool) {
		i++
		switch i {
		case 0:
			return Companion_TestInfo_.Create_TestInfo_(), true
		default:
			return TestInfo{}, false
		}
	}
}

func (_this TestInfo) String() string {
	switch _this.Get_().(type) {
	case nil:
		return "null"
	case TestInfo_TestInfo:
		{
			return "TestIntermediateKeyWrapping.TestInfo.TestInfo"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this TestInfo) Equals(other TestInfo) bool {
	switch _this.Get_().(type) {
	case TestInfo_TestInfo:
		{
			_, ok := other.Get_().(TestInfo_TestInfo)
			return ok
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this TestInfo) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(TestInfo)
	return ok && _this.Equals(typed)
}

func Type_TestInfo_() _dafny.TypeDescriptor {
	return type_TestInfo_{}
}

type type_TestInfo_ struct {
}

func (_this type_TestInfo_) Default() interface{} {
	return Companion_TestInfo_.Default()
}

func (_this type_TestInfo_) String() string {
	return "TestIntermediateKeyWrapping.TestInfo"
}
func (_this TestInfo) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = TestInfo{}

// End of datatype TestInfo

// Definition of class TestGenerateAndWrapKeyMaterial
type TestGenerateAndWrapKeyMaterial struct {
	dummy byte
}

func New_TestGenerateAndWrapKeyMaterial_() *TestGenerateAndWrapKeyMaterial {
	_this := TestGenerateAndWrapKeyMaterial{}

	return &_this
}

type CompanionStruct_TestGenerateAndWrapKeyMaterial_ struct {
}

var Companion_TestGenerateAndWrapKeyMaterial_ = CompanionStruct_TestGenerateAndWrapKeyMaterial_{}

func (_this *TestGenerateAndWrapKeyMaterial) Equals(other *TestGenerateAndWrapKeyMaterial) bool {
	return _this == other
}

func (_this *TestGenerateAndWrapKeyMaterial) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*TestGenerateAndWrapKeyMaterial)
	return ok && _this.Equals(other)
}

func (*TestGenerateAndWrapKeyMaterial) String() string {
	return "TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial"
}

func Type_TestGenerateAndWrapKeyMaterial_() _dafny.TypeDescriptor {
	return type_TestGenerateAndWrapKeyMaterial_{}
}

type type_TestGenerateAndWrapKeyMaterial_ struct {
}

func (_this type_TestGenerateAndWrapKeyMaterial_) Default() interface{} {
	return (*TestGenerateAndWrapKeyMaterial)(nil)
}

func (_this type_TestGenerateAndWrapKeyMaterial_) String() string {
	return "TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial"
}
func (_this *TestGenerateAndWrapKeyMaterial) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){m_MaterialWrapping.Companion_GenerateAndWrapMaterial_.TraitID_, m_Actions.Companion_ActionWithResult_.TraitID_, m_Actions.Companion_Action_.TraitID_}
}

var _ m_MaterialWrapping.GenerateAndWrapMaterial = &TestGenerateAndWrapKeyMaterial{}
var _ m_Actions.ActionWithResult = &TestGenerateAndWrapKeyMaterial{}
var _ m_Actions.Action = &TestGenerateAndWrapKeyMaterial{}
var _ _dafny.TraitOffspring = &TestGenerateAndWrapKeyMaterial{}

func (_this *TestGenerateAndWrapKeyMaterial) Ctor__() {
	{
	}
}
func (_this *TestGenerateAndWrapKeyMaterial) Invoke(input interface{}) interface{} {
	{
		var input m_MaterialWrapping.GenerateAndWrapInput = input.(m_MaterialWrapping.GenerateAndWrapInput)
		_ = input
		var res m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_MaterialWrapping.Companion_GenerateAndWrapOutput_.Default(Companion_TestInfo_.Default()))
		_ = res
		var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
		_ = _0_valueOrError0
		_0_valueOrError0 = m_Wrappers.Companion_Default___.Need(((input).Dtor_algorithmSuite()).Equals(Companion_Default___.TEST__ALG__SUITE()), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Unexpected input on TestGenerateAndWrapMaterial")))
		if (_0_valueOrError0).IsFailure() {
			res = (_0_valueOrError0).PropagateFailure()
			return res
		}
		res = m_Wrappers.Companion_Result_.Create_Success_(m_MaterialWrapping.Companion_GenerateAndWrapOutput_.Create_GenerateAndWrapOutput_(Companion_Default___.PLAINTEXT__MAT(), Companion_Default___.WRAPPED__MAT(), Companion_TestInfo_.Create_TestInfo_()))
		return res
		return res
	}
}

// End of class TestGenerateAndWrapKeyMaterial

// Definition of class TestUnwrapKeyMaterial
type TestUnwrapKeyMaterial struct {
	dummy byte
}

func New_TestUnwrapKeyMaterial_() *TestUnwrapKeyMaterial {
	_this := TestUnwrapKeyMaterial{}

	return &_this
}

type CompanionStruct_TestUnwrapKeyMaterial_ struct {
}

var Companion_TestUnwrapKeyMaterial_ = CompanionStruct_TestUnwrapKeyMaterial_{}

func (_this *TestUnwrapKeyMaterial) Equals(other *TestUnwrapKeyMaterial) bool {
	return _this == other
}

func (_this *TestUnwrapKeyMaterial) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*TestUnwrapKeyMaterial)
	return ok && _this.Equals(other)
}

func (*TestUnwrapKeyMaterial) String() string {
	return "TestIntermediateKeyWrapping.TestUnwrapKeyMaterial"
}

func Type_TestUnwrapKeyMaterial_() _dafny.TypeDescriptor {
	return type_TestUnwrapKeyMaterial_{}
}

type type_TestUnwrapKeyMaterial_ struct {
}

func (_this type_TestUnwrapKeyMaterial_) Default() interface{} {
	return (*TestUnwrapKeyMaterial)(nil)
}

func (_this type_TestUnwrapKeyMaterial_) String() string {
	return "TestIntermediateKeyWrapping.TestUnwrapKeyMaterial"
}
func (_this *TestUnwrapKeyMaterial) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){m_MaterialWrapping.Companion_UnwrapMaterial_.TraitID_, m_Actions.Companion_ActionWithResult_.TraitID_, m_Actions.Companion_Action_.TraitID_}
}

var _ m_MaterialWrapping.UnwrapMaterial = &TestUnwrapKeyMaterial{}
var _ m_Actions.ActionWithResult = &TestUnwrapKeyMaterial{}
var _ m_Actions.Action = &TestUnwrapKeyMaterial{}
var _ _dafny.TraitOffspring = &TestUnwrapKeyMaterial{}

func (_this *TestUnwrapKeyMaterial) Ctor__() {
	{
	}
}
func (_this *TestUnwrapKeyMaterial) Invoke(input interface{}) interface{} {
	{
		var input m_MaterialWrapping.UnwrapInput = input.(m_MaterialWrapping.UnwrapInput)
		_ = input
		var res m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_MaterialWrapping.Companion_UnwrapOutput_.Default(Companion_TestInfo_.Default()))
		_ = res
		var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
		_ = _0_valueOrError0
		_0_valueOrError0 = m_Wrappers.Companion_Default___.Need(_dafny.Companion_Sequence_.Equal((input).Dtor_wrappedMaterial(), Companion_Default___.WRAPPED__MAT()), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Unexpected input on TestUnwrapMaterial")))
		if (_0_valueOrError0).IsFailure() {
			res = (_0_valueOrError0).PropagateFailure()
			return res
		}
		var _1_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
		_ = _1_valueOrError1
		_1_valueOrError1 = m_Wrappers.Companion_Default___.Need(((input).Dtor_algorithmSuite()).Equals(Companion_Default___.TEST__ALG__SUITE()), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Unexpected input on TestUnwrapMaterial")))
		if (_1_valueOrError1).IsFailure() {
			res = (_1_valueOrError1).PropagateFailure()
			return res
		}
		res = m_Wrappers.Companion_Result_.Create_Success_(m_MaterialWrapping.Companion_UnwrapOutput_.Create_UnwrapOutput_(Companion_Default___.PLAINTEXT__MAT(), Companion_TestInfo_.Create_TestInfo_()))
		return res
		return res
	}
}

// End of class TestUnwrapKeyMaterial
