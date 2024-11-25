// Package TestManifests
// Dafny module TestManifests compiled into Go

package TestManifests

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
	m_AllAlgorithmSuites "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllAlgorithmSuites"
	m_AllDefaultCmm "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllDefaultCmm"
	m_AllHierarchy "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllHierarchy"
	m_AllKms "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKms"
	m_AllKmsEcdh "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsEcdh"
	m_AllKmsMrkAware "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsMrkAware"
	m_AllKmsMrkAwareDiscovery "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsMrkAwareDiscovery"
	m_AllKmsRsa "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsRsa"
	m_AllMulti "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllMulti"
	m_AllRawAES "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawAES"
	m_AllRawECDH "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawECDH"
	m_AllRawRSA "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawRSA"
	m_AllRequiredEncryptionContextCmm "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRequiredEncryptionContextCmm"
	m_AwsCryptographyMaterialProvidersTestVectorKeysTypes "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AwsCryptographyMaterialProvidersTestVectorKeysTypes"
	m_CmmFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CmmFromKeyDescription"
	m_CompleteVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CompleteVectors"
	m_CreateStaticKeyStores "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyStores"
	m_CreateStaticKeyrings "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyrings"
	m_JSONHelpers "github.com/aws/aws-cryptographic-material-providers-library/testvectors/JSONHelpers"
	m_KeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyDescription"
	m_KeyMaterial "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyMaterial"
	m_KeyVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyVectors"
	m_KeyringFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyringFromKeyDescription"
	m_KeysVectorOperations "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeysVectorOperations"
	m_MplManifestOptions "github.com/aws/aws-cryptographic-material-providers-library/testvectors/MplManifestOptions"
	m_ParseJsonManifests "github.com/aws/aws-cryptographic-material-providers-library/testvectors/ParseJsonManifests"
	m_TestVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/TestVectors"
	m_WrappedMaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/testvectors/WrappedMaterialProviders"
	m_WriteJsonManifests "github.com/aws/aws-cryptographic-material-providers-library/testvectors/WriteJsonManifests"
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
	m_JSON_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_API"
	m_JSON_ConcreteSyntax_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_Spec"
	m_JSON_ConcreteSyntax_SpecProperties "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_SpecProperties"
	m_JSON_Deserializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer"
	m_JSON_Deserializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_ByteStrConversion"
	m_JSON_Deserializer_Uint16StrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_Uint16StrConversion"
	m_JSON_Errors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Errors"
	m_JSON_Grammar "github.com/dafny-lang/DafnyStandardLibGo/JSON_Grammar"
	m_JSON_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer"
	m_JSON_Serializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer_ByteStrConversion"
	m_JSON_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_Spec"
	m_JSON_Utils_Cursors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Cursors"
	m_JSON_Utils_Lexers_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Core"
	m_JSON_Utils_Lexers_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Strings"
	m_JSON_Utils_Parsers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Parsers"
	m_JSON_Utils_Seq "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Seq"
	m_JSON_Utils_Str "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str"
	m_JSON_Utils_Str_CharStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrConversion"
	m_JSON_Utils_Str_CharStrEscaping "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrEscaping"
	m_JSON_Utils_Vectors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Vectors"
	m_JSON_Utils_Views_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Core"
	m_JSON_Utils_Views_Writers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Writers"
	m_JSON_Values "github.com/dafny-lang/DafnyStandardLibGo/JSON_Values"
	m_JSON_ZeroCopy_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_API"
	m_JSON_ZeroCopy_Deserializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer"
	m_JSON_ZeroCopy_Deserializer_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_API"
	m_JSON_ZeroCopy_Deserializer_ArrayParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ArrayParams"
	m_JSON_ZeroCopy_Deserializer_Arrays "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Arrays"
	m_JSON_ZeroCopy_Deserializer_Constants "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Constants"
	m_JSON_ZeroCopy_Deserializer_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Core"
	m_JSON_ZeroCopy_Deserializer_Numbers "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Numbers"
	m_JSON_ZeroCopy_Deserializer_ObjectParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ObjectParams"
	m_JSON_ZeroCopy_Deserializer_Objects "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Objects"
	m_JSON_ZeroCopy_Deserializer_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Strings"
	m_JSON_ZeroCopy_Deserializer_Values "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Values"
	m_JSON_ZeroCopy_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Serializer"
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
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
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
var _ m_ComAmazonawsDynamodbTypes.Dummy__
var _ m_ComAmazonawsKmsTypes.Dummy__
var _ m_AwsCryptographyKeyStoreTypes.Dummy__
var _ m_AwsCryptographyMaterialProvidersTypes.Dummy__
var _ m_Base64.Dummy__
var _ m_AlgorithmSuites.Dummy__
var _ m_Materials.Dummy__
var _ m_Keyring.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m_MultiKeyring.Dummy__
var _ m_AwsArnParsing.Dummy__
var _ m_AwsKmsMrkAreUnique.Dummy__
var _ m_Actions.Dummy__
var _ m_AwsKmsMrkMatchForDecrypt.Dummy__
var _ m_AwsKmsUtils.Dummy__
var _ m_Constants.Dummy__
var _ m_MaterialWrapping.Dummy__
var _ m_CanonicalEncryptionContext.Dummy__
var _ m_IntermediateKeyWrapping.Dummy__
var _ m_EdkWrapping.Dummy__
var _ m_ErrorMessages.Dummy__
var _ m_AwsKmsKeyring.Dummy__
var _ m_StrictMultiKeyring.Dummy__
var _ m_AwsKmsDiscoveryKeyring.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__
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
var _ m_KeyStoreErrorMessages.Dummy__
var _ m_KmsArn.Dummy__
var _ m_Structure.Dummy__
var _ m_KMSKeystoreOperations.Dummy__
var _ m_DDBKeystoreOperations.Dummy__
var _ m_CreateKeys.Dummy__
var _ m_CreateKeyStoreTable.Dummy__
var _ m_GetKeys.Dummy__
var _ m_AwsCryptographyKeyStoreOperations.Dummy__
var _ m_KeyStore.Dummy__
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
var _ m_MplManifestOptions.Dummy__
var _ m_AllAlgorithmSuites.Dummy__
var _ m_WrappedMaterialProviders.Dummy__
var _ m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Dummy__
var _ m_JSON_Utils_Views_Core.Dummy__
var _ m_JSON_Utils_Views_Writers.Dummy__
var _ m_JSON_Utils_Lexers_Core.Dummy__
var _ m_JSON_Utils_Lexers_Strings.Dummy__
var _ m_JSON_Utils_Cursors.Dummy__
var _ m_JSON_Utils_Parsers.Dummy__
var _ m_JSON_Utils_Str_CharStrConversion.Dummy__
var _ m_JSON_Utils_Str_CharStrEscaping.Dummy__
var _ m_JSON_Utils_Str.Dummy__
var _ m_JSON_Utils_Seq.Dummy__
var _ m_JSON_Utils_Vectors.Dummy__
var _ m_JSON_Errors.Dummy__
var _ m_JSON_Values.Dummy__
var _ m_JSON_Spec.Dummy__
var _ m_JSON_Grammar.Dummy__
var _ m_JSON_Serializer_ByteStrConversion.Dummy__
var _ m_JSON_Serializer.Dummy__
var _ m_JSON_Deserializer_Uint16StrConversion.Dummy__
var _ m_JSON_Deserializer_ByteStrConversion.Dummy__
var _ m_JSON_Deserializer.Dummy__
var _ m_JSON_ConcreteSyntax_Spec.Dummy__
var _ m_JSON_ConcreteSyntax_SpecProperties.Dummy__
var _ m_JSON_ZeroCopy_Serializer.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Core.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Strings.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Numbers.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ObjectParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Objects.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ArrayParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Arrays.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Constants.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Values.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_API.Dummy__
var _ m_JSON_ZeroCopy_Deserializer.Dummy__
var _ m_JSON_ZeroCopy_API.Dummy__
var _ m_JSON_API.Dummy__
var _ m_JSONHelpers.Dummy__
var _ m_KeyDescription.Dummy__
var _ m_KeyMaterial.Dummy__
var _ m_CreateStaticKeyrings.Dummy__
var _ m_CreateStaticKeyStores.Dummy__
var _ m_KeyringFromKeyDescription.Dummy__
var _ m_CmmFromKeyDescription.Dummy__
var _ m_KeysVectorOperations.Dummy__
var _ m_KeyVectors.Dummy__
var _ m_TestVectors.Dummy__
var _ m_AllHierarchy.Dummy__
var _ m_AllKms.Dummy__
var _ m_AllKmsMrkAware.Dummy__
var _ m_AllKmsMrkAwareDiscovery.Dummy__
var _ m_AllKmsRsa.Dummy__
var _ m_AllKmsEcdh.Dummy__
var _ m_AllRawAES.Dummy__
var _ m_AllRawRSA.Dummy__
var _ m_AllRawECDH.Dummy__
var _ m_AllDefaultCmm.Dummy__
var _ m_AllRequiredEncryptionContextCmm.Dummy__
var _ m_AllMulti.Dummy__
var _ m_WriteJsonManifests.Dummy__
var _ m_CompleteVectors.Dummy__
var _ m_ParseJsonManifests.Dummy__

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
	return "TestManifests.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) StartEncrypt(op m_MplManifestOptions.ManifestOptions) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = output
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = Companion_Default___.GetManifest((op).Dtor_manifestPath(), _dafny.SeqOfString("manifest.json"))
	_0_valueOrError0 = _out0
	if (_0_valueOrError0).IsFailure() {
		output = (_0_valueOrError0).PropagateFailure()
		return output
	}
	var _1_encryptManifest ManifestData
	_ = _1_encryptManifest
	_1_encryptManifest = (_0_valueOrError0).Extract().(ManifestData)
	var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _2_valueOrError1
	_2_valueOrError1 = m_Wrappers.Companion_Default___.Need((_1_encryptManifest).Is_EncryptManifest(), _dafny.SeqOfString("Not a encrypt manifest"))
	if (_2_valueOrError1).IsFailure() {
		output = (_2_valueOrError1).PropagateFailure()
		return output
	}
	var _3_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _3_valueOrError2
	_3_valueOrError2 = m_ParseJsonManifests.Companion_Default___.BuildEncryptTestVector((_1_encryptManifest).Dtor_keys(), (_1_encryptManifest).Dtor_jsonTests())
	if (_3_valueOrError2).IsFailure() {
		output = (_3_valueOrError2).PropagateFailure()
		return output
	}
	var _4_encryptVectors _dafny.Sequence
	_ = _4_encryptVectors
	_4_encryptVectors = (_3_valueOrError2).Extract().(_dafny.Sequence)
	var _5_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _5_valueOrError3
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = Companion_Default___.ToEncryptTests((_1_encryptManifest).Dtor_keys(), _4_encryptVectors)
	_5_valueOrError3 = _out1
	if (_5_valueOrError3).IsFailure() {
		output = (_5_valueOrError3).PropagateFailure()
		return output
	}
	var _6_encryptTests _dafny.Sequence
	_ = _6_encryptTests
	_6_encryptTests = (_5_valueOrError3).Extract().(_dafny.Sequence)
	var _7_decryptVectors _dafny.Sequence
	_ = _7_decryptVectors
	var _out2 _dafny.Sequence
	_ = _out2
	_out2 = Companion_Default___.TestEncrypts(_6_encryptTests, (_1_encryptManifest).Dtor_keys())
	_7_decryptVectors = _out2
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _8_valueOrError4
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = m_CompleteVectors.Companion_Default___.WriteDecryptManifest(op, (_1_encryptManifest).Dtor_keys(), _7_decryptVectors)
	_8_valueOrError4 = _out3
	if (_8_valueOrError4).IsFailure() {
		output = (_8_valueOrError4).PropagateFailure()
		return output
	}
	var _9___v0 _dafny.Tuple
	_ = _9___v0
	_9___v0 = (_8_valueOrError4).Extract().(_dafny.Tuple)
	output = m_Wrappers.Companion_Result_.Create_Success_(_dafny.TupleOf())
	return output
}
func (_static *CompanionStruct_Default___) TestEncrypts(tests _dafny.Sequence, keys *m_KeyVectors.KeyVectorsClient) _dafny.Sequence {
	var output _dafny.Sequence = _dafny.EmptySeq
	_ = output
	var _0_hasFailure bool
	_ = _0_hasFailure
	_0_hasFailure = false
	_dafny.Print((_dafny.SeqOfString("\n=================== Starting ")).SetString())
	_dafny.Print(_dafny.IntOfUint32((tests).Cardinality()))
	_dafny.Print((_dafny.SeqOfString(" Encrypt Tests =================== \n\n")).SetString())
	var _1_decryptableTests _dafny.Sequence
	_ = _1_decryptableTests
	_1_decryptableTests = _dafny.SeqOf()
	var _hi0 _dafny.Int = _dafny.IntOfUint32((tests).Cardinality())
	_ = _hi0
	for _2_i := _dafny.Zero; _2_i.Cmp(_hi0) < 0; _2_i = _2_i.Plus(_dafny.One) {
		var _3_test m_TestVectors.EncryptTest
		_ = _3_test
		_3_test = (tests).Select((_2_i).Uint32()).(m_TestVectors.EncryptTest)
		var _4_pass bool
		_ = _4_pass
		var _5_maybeEncryptionMaterials m_Wrappers.Option
		_ = _5_maybeEncryptionMaterials
		var _out0 bool
		_ = _out0
		var _out1 m_Wrappers.Option
		_ = _out1
		_out0, _out1 = m_TestVectors.Companion_Default___.TestGetEncryptionMaterials(_3_test)
		// // fmt.Println(_out1)
		_4_pass = _out0
		_5_maybeEncryptionMaterials = _out1
		// // fmt.Println(_out1)
		if (_4_pass) && (!(((_3_test).Dtor_vector()).Is_NegativeEncryptKeyringVector())) {
			_1_decryptableTests = _dafny.Companion_Sequence_.Concatenate(_1_decryptableTests, _dafny.SeqOf(_dafny.TupleOf(_3_test, (_5_maybeEncryptionMaterials).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials))))
		} else if !(_4_pass) {
			_0_hasFailure = true
		}
	}
	_dafny.Print((_dafny.SeqOfString("\n=================== Completed ")).SetString())
	_dafny.Print(_dafny.IntOfUint32((tests).Cardinality()))
	_dafny.Print((_dafny.SeqOfString(" Encrypt Tests =================== \n\n")).SetString())
	if !(!(_0_hasFailure)) {
		panic("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(74,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _6_valueOrError0
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = Companion_Default___.ToDecryptTestVectors(keys, _1_decryptableTests)
	_6_valueOrError0 = _out2
	if !(!((_6_valueOrError0).IsFailure())) {
		panic("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(75,14): " + (_6_valueOrError0).String())
	}
	output = (_6_valueOrError0).Extract().(_dafny.Sequence)
	return output
}
func (_static *CompanionStruct_Default___) StartDecrypt(op m_MplManifestOptions.ManifestOptions) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = output
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = Companion_Default___.GetManifest((op).Dtor_manifestPath(), _dafny.SeqOfString("manifest.json"))
	_0_valueOrError0 = _out0
	if (_0_valueOrError0).IsFailure() {
		output = (_0_valueOrError0).PropagateFailure()
		return output
	}
	var _1_decryptManifest ManifestData
	_ = _1_decryptManifest
	_1_decryptManifest = (_0_valueOrError0).Extract().(ManifestData)
	var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _2_valueOrError1
	_2_valueOrError1 = m_Wrappers.Companion_Default___.Need((_1_decryptManifest).Is_DecryptManifest(), _dafny.SeqOfString("Not a encrypt manifest"))
	if (_2_valueOrError1).IsFailure() {
		output = (_2_valueOrError1).PropagateFailure()
		return output
	}
	var _3_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _3_valueOrError2
	_3_valueOrError2 = m_ParseJsonManifests.Companion_Default___.BuildDecryptTestVector((_1_decryptManifest).Dtor_keys(), (_1_decryptManifest).Dtor_jsonTests())
	if (_3_valueOrError2).IsFailure() {
		output = (_3_valueOrError2).PropagateFailure()
		return output
	}
	var _4_decryptVectors _dafny.Sequence
	_ = _4_decryptVectors
	_4_decryptVectors = (_3_valueOrError2).Extract().(_dafny.Sequence)
	var _5_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _5_valueOrError3
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = Companion_Default___.ToDecryptTests((_1_decryptManifest).Dtor_keys(), _4_decryptVectors)
	_5_valueOrError3 = _out1
	if (_5_valueOrError3).IsFailure() {
		output = (_5_valueOrError3).PropagateFailure()
		return output
	}
	var _6_decryptTests _dafny.Sequence
	_ = _6_decryptTests
	_6_decryptTests = (_5_valueOrError3).Extract().(_dafny.Sequence)
	Companion_Default___.TestDecrypts(_6_decryptTests)
	output = m_Wrappers.Companion_Result_.Create_Success_(_dafny.TupleOf())
	return output
}
func (_static *CompanionStruct_Default___) TestDecrypts(tests _dafny.Sequence) {
	_dafny.Print((_dafny.SeqOfString("\n=================== Starting ")).SetString())
	_dafny.Print(_dafny.IntOfUint32((tests).Cardinality()))
	_dafny.Print((_dafny.SeqOfString(" Decrypt Tests =================== \n\n")).SetString())
	var _0_hasFailure bool
	_ = _0_hasFailure
	_0_hasFailure = false
	var _hi0 _dafny.Int = _dafny.IntOfUint32((tests).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_pass bool
		_ = _2_pass
		var _out0 bool
		_ = _out0
		_out0 = m_TestVectors.Companion_Default___.TestDecryptMaterials((tests).Select((_1_i).Uint32()).(m_TestVectors.DecryptTest))
		_2_pass = _out0
		if !(_2_pass) {
			_0_hasFailure = true
		}
	}
	_dafny.Print((_dafny.SeqOfString("\n=================== Completed ")).SetString())
	_dafny.Print(_dafny.IntOfUint32((tests).Cardinality()))
	_dafny.Print((_dafny.SeqOfString(" Decrypt Tests =================== \n\n")).SetString())
	if !(!(_0_hasFailure)) {
		panic("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(113,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) ToEncryptTests(keys *m_KeyVectors.KeyVectorsClient, encryptVectors _dafny.Sequence) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = output
	var _0_encryptTests _dafny.Sequence
	_ = _0_encryptTests
	_0_encryptTests = _dafny.SeqOf()
	var _hi0 _dafny.Int = _dafny.IntOfUint32((encryptVectors).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _2_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_TestVectors.Companion_Default___.ToEncryptTest(keys, (encryptVectors).Select((_1_i).Uint32()).(m_TestVectors.EncryptTestVector))
		_2_valueOrError0 = _out0
		if (_2_valueOrError0).IsFailure() {
			output = (_2_valueOrError0).PropagateFailure()
			return output
		}
		var _3_test m_TestVectors.EncryptTest
		_ = _3_test
		_3_test = (_2_valueOrError0).Extract().(m_TestVectors.EncryptTest)
		_0_encryptTests = _dafny.Companion_Sequence_.Concatenate(_0_encryptTests, _dafny.SeqOf(_3_test))
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(_0_encryptTests)
	return output
	return output
}
func (_static *CompanionStruct_Default___) ToDecryptTestVectors(keys *m_KeyVectors.KeyVectorsClient, tests _dafny.Sequence) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = output
	var _0_successfulEncrypt _dafny.Sequence
	_ = _0_successfulEncrypt
	_0_successfulEncrypt = m_Seq.Companion_Default___.Filter(func(coer104 func(_dafny.Tuple) bool) func(interface{}) bool {
		return func(arg144 interface{}) bool {
			return coer104(arg144.(_dafny.Tuple))
		}
	}(func(_1_r _dafny.Tuple) bool {
		return ((((*(_1_r).IndexInt(0)).(m_TestVectors.EncryptTest)).Dtor_vector()).Is_PositiveEncryptKeyringVector()) || ((((*(_1_r).IndexInt(0)).(m_TestVectors.EncryptTest)).Dtor_vector()).Is_PositiveEncryptNegativeDecryptKeyringVector())
	}), tests)
	var _2_decryptTestVectors _dafny.Sequence
	_ = _2_decryptTestVectors
	_2_decryptTestVectors = _dafny.SeqOf()
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_successfulEncrypt).Cardinality())
	_ = _hi0
	for _3_i := _dafny.Zero; _3_i.Cmp(_hi0) < 0; _3_i = _3_i.Plus(_dafny.One) {
		var _4_vector m_TestVectors.DecryptTestVector
		_ = _4_vector
		_4_vector = m_TestVectors.Companion_Default___.EncryptTestToDecryptVector((*((_0_successfulEncrypt).Select((_3_i).Uint32()).(_dafny.Tuple)).IndexInt(0)).(m_TestVectors.EncryptTest), (*((_0_successfulEncrypt).Select((_3_i).Uint32()).(_dafny.Tuple)).IndexInt(1)).(m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials))
		_2_decryptTestVectors = _dafny.Companion_Sequence_.Concatenate(_2_decryptTestVectors, _dafny.SeqOf(_4_vector))
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(_2_decryptTestVectors)
	return output
}
func (_static *CompanionStruct_Default___) ToDecryptTests(keys *m_KeyVectors.KeyVectorsClient, vectors _dafny.Sequence) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = output
	var _0_decryptTests _dafny.Sequence
	_ = _0_decryptTests
	_0_decryptTests = _dafny.SeqOf()
	var _hi0 _dafny.Int = _dafny.IntOfUint32((vectors).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _2_valueOrError0
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_TestVectors.Companion_Default___.DecryptVectorToDecryptTest(keys, (vectors).Select((_1_i).Uint32()).(m_TestVectors.DecryptTestVector))
		_2_valueOrError0 = _out0
		if (_2_valueOrError0).IsFailure() {
			output = (_2_valueOrError0).PropagateFailure()
			return output
		}
		var _3_test m_TestVectors.DecryptTest
		_ = _3_test
		_3_test = (_2_valueOrError0).Extract().(m_TestVectors.DecryptTest)
		_0_decryptTests = _dafny.Companion_Sequence_.Concatenate(_0_decryptTests, _dafny.SeqOf(_3_test))
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(_0_decryptTests)
	return output
	return output
}
func (_static *CompanionStruct_Default___) GetManifest(manifestPath _dafny.Sequence, manifestFileName _dafny.Sequence) m_Wrappers.Result {
	var manifestData m_Wrappers.Result = m_Wrappers.Result{}
	_ = manifestData
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_FileIO.Companion_Default___.ReadBytesFromFile(_dafny.Companion_Sequence_.Concatenate(manifestPath, manifestFileName))
	_0_valueOrError0 = _out0
	if (_0_valueOrError0).IsFailure() {
		manifestData = (_0_valueOrError0).PropagateFailure()
		return manifestData
	}
	var _1_decryptManifestBv _dafny.Sequence
	_ = _1_decryptManifestBv
	_1_decryptManifestBv = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_decryptManifestBytes _dafny.Sequence
	_ = _2_decryptManifestBytes
	_2_decryptManifestBytes = m_JSONHelpers.Companion_Default___.BvToBytes(_1_decryptManifestBv)
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_JSON_Values.Companion_JSON_.Default())
	_ = _3_valueOrError1
	_3_valueOrError1 = (m_JSON_API.Companion_Default___.Deserialize(_2_decryptManifestBytes)).MapFailure(func(coer105 func(m_JSON_Errors.DeserializationError) _dafny.Sequence) func(interface{}) interface{} {
		return func(arg145 interface{}) interface{} {
			return coer105(arg145.(m_JSON_Errors.DeserializationError))
		}
	}(func(_4_e m_JSON_Errors.DeserializationError) _dafny.Sequence {
		return (_4_e).ToString()
	}))
	if (_3_valueOrError1).IsFailure() {
		manifestData = (_3_valueOrError1).PropagateFailure()
		return manifestData
	}
	var _5_manifestJson m_JSON_Values.JSON
	_ = _5_manifestJson
	_5_manifestJson = (_3_valueOrError1).Extract().(m_JSON_Values.JSON)
	var _6_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _6_valueOrError2
	_6_valueOrError2 = m_Wrappers.Companion_Default___.Need((_5_manifestJson).Is_Object(), _dafny.SeqOfString("Not a JSON object"))
	if (_6_valueOrError2).IsFailure() {
		manifestData = (_6_valueOrError2).PropagateFailure()
		return manifestData
	}
	var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _7_valueOrError3
	_7_valueOrError3 = m_JSONHelpers.Companion_Default___.GetObject(_dafny.SeqOfString("manifest"), (_5_manifestJson).Dtor_obj())
	if (_7_valueOrError3).IsFailure() {
		manifestData = (_7_valueOrError3).PropagateFailure()
		return manifestData
	}
	var _8_manifest _dafny.Sequence
	_ = _8_manifest
	_8_manifest = (_7_valueOrError3).Extract().(_dafny.Sequence)
	var _9_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.Zero)
	_ = _9_valueOrError4
	_9_valueOrError4 = m_JSONHelpers.Companion_Default___.GetNat(_dafny.SeqOfString("version"), _8_manifest)
	if (_9_valueOrError4).IsFailure() {
		manifestData = (_9_valueOrError4).PropagateFailure()
		return manifestData
	}
	var _10_version _dafny.Int
	_ = _10_version
	_10_version = (_9_valueOrError4).Extract().(_dafny.Int)
	var _11_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _11_valueOrError5
	_11_valueOrError5 = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("type"), _8_manifest)
	if (_11_valueOrError5).IsFailure() {
		manifestData = (_11_valueOrError5).PropagateFailure()
		return manifestData
	}
	var _12_typ _dafny.Sequence
	_ = _12_typ
	_12_typ = (_11_valueOrError5).Extract().(_dafny.Sequence)
	var _13_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _13_valueOrError6
	_13_valueOrError6 = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("keys"), (_5_manifestJson).Dtor_obj())
	if (_13_valueOrError6).IsFailure() {
		manifestData = (_13_valueOrError6).PropagateFailure()
		return manifestData
	}
	var _14_keyManifestUri _dafny.Sequence
	_ = _14_keyManifestUri
	_14_keyManifestUri = (_13_valueOrError6).Extract().(_dafny.Sequence)
	var _15_valueOrError7 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _15_valueOrError7
	_15_valueOrError7 = m_Wrappers.Companion_Default___.Need(_dafny.Companion_Sequence_.IsProperPrefixOf(_dafny.SeqOfString("file://"), _14_keyManifestUri), _dafny.SeqOfString("Unexpected URI prefix"))
	if (_15_valueOrError7).IsFailure() {
		manifestData = (_15_valueOrError7).PropagateFailure()
		return manifestData
	}
	var _16_keyManifestPath _dafny.Sequence
	_ = _16_keyManifestPath
	_16_keyManifestPath = _dafny.Companion_Sequence_.Concatenate(manifestPath, (_14_keyManifestUri).Drop(7))
	var _17_valueOrError8 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _17_valueOrError8
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = m_KeyVectors.Companion_Default___.KeyVectors(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyVectorsConfig_.Create_KeyVectorsConfig_(_16_keyManifestPath))
	_17_valueOrError8 = _out1
	if !(!((_17_valueOrError8).IsFailure())) {
		panic("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(222,16): " + (_17_valueOrError8).String())
	}
	var _18_keys *m_KeyVectors.KeyVectorsClient
	_ = _18_keys
	_18_keys = (_17_valueOrError8).Extract().(*m_KeyVectors.KeyVectorsClient)
	var _19_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _19_valueOrError9
	_19_valueOrError9 = m_JSONHelpers.Companion_Default___.GetObject(_dafny.SeqOfString("tests"), (_5_manifestJson).Dtor_obj())
	if (_19_valueOrError9).IsFailure() {
		manifestData = (_19_valueOrError9).PropagateFailure()
		return manifestData
	}
	var _20_jsonTests _dafny.Sequence
	_ = _20_jsonTests
	_20_jsonTests = (_19_valueOrError9).Extract().(_dafny.Sequence)
	var _source0 _dafny.Sequence = _12_typ
	_ = _source0
	{
		{
			if (_source0).Equals(_dafny.SeqOfString("awses-mpl-decrypt")) {
				var _21_valueOrError10 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_JSON_Values.Companion_JSON_.Default())
				_ = _21_valueOrError10
				_21_valueOrError10 = m_JSONHelpers.Companion_Default___.Get(_dafny.SeqOfString("client"), (_5_manifestJson).Dtor_obj())
				if (_21_valueOrError10).IsFailure() {
					manifestData = (_21_valueOrError10).PropagateFailure()
					return manifestData
				}
				var _22_client m_JSON_Values.JSON
				_ = _22_client
				_22_client = (_21_valueOrError10).Extract().(m_JSON_Values.JSON)
				manifestData = m_Wrappers.Companion_Result_.Create_Success_(Companion_ManifestData_.Create_DecryptManifest_(_10_version, _18_keys, _22_client, _20_jsonTests))
				goto Lmatch0
			}
		}
		{
			if (_source0).Equals(_dafny.SeqOfString("awses-mpl-encrypt")) {
				manifestData = m_Wrappers.Companion_Result_.Create_Success_(Companion_ManifestData_.Create_EncryptManifest_(_10_version, _18_keys, _20_jsonTests))
				goto Lmatch0
			}
		}
		{
			manifestData = m_Wrappers.Companion_Result_.Create_Failure_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported manifest type:"), _12_typ))
		}
		goto Lmatch0
	}
Lmatch0:
	return manifestData
}

// End of class Default__

// Definition of datatype ManifestData
type ManifestData struct {
	Data_ManifestData_
}

func (_this ManifestData) Get_() Data_ManifestData_ {
	return _this.Data_ManifestData_
}

type Data_ManifestData_ interface {
	isManifestData()
}

type CompanionStruct_ManifestData_ struct {
}

var Companion_ManifestData_ = CompanionStruct_ManifestData_{}

type ManifestData_DecryptManifest struct {
	Version   _dafny.Int
	Keys      *m_KeyVectors.KeyVectorsClient
	Client    m_JSON_Values.JSON
	JsonTests _dafny.Sequence
}

func (ManifestData_DecryptManifest) isManifestData() {}

func (CompanionStruct_ManifestData_) Create_DecryptManifest_(Version _dafny.Int, Keys *m_KeyVectors.KeyVectorsClient, Client m_JSON_Values.JSON, JsonTests _dafny.Sequence) ManifestData {
	return ManifestData{ManifestData_DecryptManifest{Version, Keys, Client, JsonTests}}
}

func (_this ManifestData) Is_DecryptManifest() bool {
	_, ok := _this.Get_().(ManifestData_DecryptManifest)
	return ok
}

type ManifestData_EncryptManifest struct {
	Version   _dafny.Int
	Keys      *m_KeyVectors.KeyVectorsClient
	JsonTests _dafny.Sequence
}

func (ManifestData_EncryptManifest) isManifestData() {}

func (CompanionStruct_ManifestData_) Create_EncryptManifest_(Version _dafny.Int, Keys *m_KeyVectors.KeyVectorsClient, JsonTests _dafny.Sequence) ManifestData {
	return ManifestData{ManifestData_EncryptManifest{Version, Keys, JsonTests}}
}

func (_this ManifestData) Is_EncryptManifest() bool {
	_, ok := _this.Get_().(ManifestData_EncryptManifest)
	return ok
}

func (CompanionStruct_ManifestData_) Default() ManifestData {
	return Companion_ManifestData_.Create_DecryptManifest_(_dafny.Zero, (*m_KeyVectors.KeyVectorsClient)(nil), m_JSON_Values.Companion_JSON_.Default(), _dafny.EmptySeq)
}

func (_this ManifestData) Dtor_version() _dafny.Int {
	switch data := _this.Get_().(type) {
	case ManifestData_DecryptManifest:
		return data.Version
	default:
		return data.(ManifestData_EncryptManifest).Version
	}
}

func (_this ManifestData) Dtor_keys() *m_KeyVectors.KeyVectorsClient {
	switch data := _this.Get_().(type) {
	case ManifestData_DecryptManifest:
		return data.Keys
	default:
		return data.(ManifestData_EncryptManifest).Keys
	}
}

func (_this ManifestData) Dtor_client() m_JSON_Values.JSON {
	return _this.Get_().(ManifestData_DecryptManifest).Client
}

func (_this ManifestData) Dtor_jsonTests() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case ManifestData_DecryptManifest:
		return data.JsonTests
	default:
		return data.(ManifestData_EncryptManifest).JsonTests
	}
}

func (_this ManifestData) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case ManifestData_DecryptManifest:
		{
			return "TestManifests.ManifestData.DecryptManifest" + "(" + _dafny.String(data.Version) + ", " + _dafny.String(data.Keys) + ", " + _dafny.String(data.Client) + ", " + _dafny.String(data.JsonTests) + ")"
		}
	case ManifestData_EncryptManifest:
		{
			return "TestManifests.ManifestData.EncryptManifest" + "(" + _dafny.String(data.Version) + ", " + _dafny.String(data.Keys) + ", " + _dafny.String(data.JsonTests) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this ManifestData) Equals(other ManifestData) bool {
	switch data1 := _this.Get_().(type) {
	case ManifestData_DecryptManifest:
		{
			data2, ok := other.Get_().(ManifestData_DecryptManifest)
			return ok && data1.Version.Cmp(data2.Version) == 0 && data1.Keys == data2.Keys && data1.Client.Equals(data2.Client) && data1.JsonTests.Equals(data2.JsonTests)
		}
	case ManifestData_EncryptManifest:
		{
			data2, ok := other.Get_().(ManifestData_EncryptManifest)
			return ok && data1.Version.Cmp(data2.Version) == 0 && data1.Keys == data2.Keys && data1.JsonTests.Equals(data2.JsonTests)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this ManifestData) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(ManifestData)
	return ok && _this.Equals(typed)
}

func Type_ManifestData_() _dafny.TypeDescriptor {
	return type_ManifestData_{}
}

type type_ManifestData_ struct {
}

func (_this type_ManifestData_) Default() interface{} {
	return Companion_ManifestData_.Default()
}

func (_this type_ManifestData_) String() string {
	return "TestManifests.ManifestData"
}
func (_this ManifestData) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = ManifestData{}

// End of datatype ManifestData
