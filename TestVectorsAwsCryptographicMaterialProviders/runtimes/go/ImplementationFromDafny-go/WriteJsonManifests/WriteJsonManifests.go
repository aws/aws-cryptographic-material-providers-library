// Package WriteJsonManifests
// Dafny module WriteJsonManifests compiled into Go

package WriteJsonManifests

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
	m_CreateStaticKeyStores "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyStores"
	m_CreateStaticKeyrings "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyrings"
	m_JSONHelpers "github.com/aws/aws-cryptographic-material-providers-library/testvectors/JSONHelpers"
	m_KeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyDescription"
	m_KeyMaterial "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyMaterial"
	m_KeyVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyVectors"
	m_KeyringFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyringFromKeyDescription"
	m_KeysVectorOperations "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeysVectorOperations"
	m_MplManifestOptions "github.com/aws/aws-cryptographic-material-providers-library/testvectors/MplManifestOptions"
	m_TestVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/TestVectors"
	m_WrappedMaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/testvectors/WrappedMaterialProviders"
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
	m_SortedSets "github.com/dafny-lang/DafnyStandardLibGo/SortedSets"
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
	return "WriteJsonManifests.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) EncryptionContextKeysToJson(keys m_Wrappers.Option) m_Wrappers.Result {
	if (keys).Is_Some() {
		var _0_valueOrError0 m_Wrappers.Result = m_Seq.Companion_Default___.MapWithResult(func(coer94 func(_dafny.Sequence) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
			return func(arg134 interface{}) m_Wrappers.Result {
				return coer94(arg134.(_dafny.Sequence))
			}
		}(func(_1_bytes _dafny.Sequence) m_Wrappers.Result {
			return func(_pat_let16_0 m_Wrappers.Result) m_Wrappers.Result {
				return func(_2_valueOrError1 m_Wrappers.Result) m_Wrappers.Result {
					return (func() m_Wrappers.Result {
						if (_2_valueOrError1).IsFailure() {
							return (_2_valueOrError1).PropagateFailure()
						}
						return func(_pat_let17_0 _dafny.Sequence) m_Wrappers.Result {
							return func(_3_key _dafny.Sequence) m_Wrappers.Result {
								return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_String_(_3_key))
							}(_pat_let17_0)
						}((_2_valueOrError1).Extract().(_dafny.Sequence))
					})()
				}(_pat_let16_0)
			}(m_UTF8.Decode(_1_bytes))
		}), (keys).Dtor_value().(_dafny.Sequence))
		_ = _0_valueOrError0
		if (_0_valueOrError0).IsFailure() {
			return (_0_valueOrError0).PropagateFailure()
		} else {
			var _4_tmp _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
			_ = _4_tmp
			return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("requiredEncryptionContextKeys"), m_JSON_Values.Companion_JSON_.Create_Array_(_4_tmp))))
		}
	} else {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf())
	}
}
func (_static *CompanionStruct_Default___) EncryptionContextToJson(key _dafny.Sequence, m _dafny.Map) m_Wrappers.Result {
	var _0_keys _dafny.Sequence = m_SortedSets.SetToSequence((m).Keys())
	_ = _0_keys
	var _1_valueOrError0 m_Wrappers.Result = m_Seq.Companion_Default___.MapWithResult(func(coer95 func(_dafny.Sequence) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
		return func(arg135 interface{}) m_Wrappers.Result {
			return coer95(arg135.(_dafny.Sequence))
		}
	}((func(_2_m _dafny.Map) func(_dafny.Sequence) m_Wrappers.Result {
		return func(_3_k _dafny.Sequence) m_Wrappers.Result {
			return func(_pat_let18_0 m_Wrappers.Result) m_Wrappers.Result {
				return func(_4_valueOrError1 m_Wrappers.Result) m_Wrappers.Result {
					return (func() m_Wrappers.Result {
						if (_4_valueOrError1).IsFailure() {
							return (_4_valueOrError1).PropagateFailure()
						}
						return func(_pat_let19_0 _dafny.Sequence) m_Wrappers.Result {
							return func(_5_key _dafny.Sequence) m_Wrappers.Result {
								return func(_pat_let20_0 m_Wrappers.Result) m_Wrappers.Result {
									return func(_6_valueOrError2 m_Wrappers.Result) m_Wrappers.Result {
										return (func() m_Wrappers.Result {
											if (_6_valueOrError2).IsFailure() {
												return (_6_valueOrError2).PropagateFailure()
											}
											return func(_pat_let21_0 _dafny.Sequence) m_Wrappers.Result {
												return func(_7_value _dafny.Sequence) m_Wrappers.Result {
													return m_Wrappers.Companion_Result_.Create_Success_(_dafny.TupleOf(_5_key, m_JSON_Values.Companion_JSON_.Create_String_(_7_value)))
												}(_pat_let21_0)
											}((_6_valueOrError2).Extract().(_dafny.Sequence))
										})()
									}(_pat_let20_0)
								}(m_UTF8.Decode((_2_m).Get(_3_k).(_dafny.Sequence)))
							}(_pat_let19_0)
						}((_4_valueOrError1).Extract().(_dafny.Sequence))
					})()
				}(_pat_let18_0)
			}(m_UTF8.Decode(_3_k))
		}
	})(m)), _0_keys)
	_ = _1_valueOrError0
	if (_1_valueOrError0).IsFailure() {
		return (_1_valueOrError0).PropagateFailure()
	} else {
		var _8_pairsBytes _dafny.Sequence = (_1_valueOrError0).Extract().(_dafny.Sequence)
		_ = _8_pairsBytes
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf(_dafny.TupleOf(key, m_JSON_Values.Companion_JSON_.Create_Object_(_8_pairsBytes))))
	}
}
func (_static *CompanionStruct_Default___) PrintJson(j m_JSON_Values.JSON) _dafny.Tuple {
	var _hresult _dafny.Tuple = _dafny.TupleOf()
	_ = _hresult
	_dafny.Print(j)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_hresult = _dafny.TupleOf()
	return _hresult
	return _hresult
}
func (_static *CompanionStruct_Default___) EncryptTestVectorToJson(test m_TestVectors.EncryptTestVector) m_Wrappers.Result {
	var _0_id _dafny.Sequence = m_AllAlgorithmSuites.Companion_Default___.ToHex((test).Dtor_algorithmSuite())
	_ = _0_id
	var _1_description _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate((test).Dtor_name(), _dafny.SeqOfString(" ")), _0_id)
	_ = _1_description
	var _2_valueOrError0 m_Wrappers.Result = Companion_Default___.EncryptionContextToJson(_dafny.SeqOfString("encryptionContext"), (test).Dtor_encryptionContext())
	_ = _2_valueOrError0
	if (_2_valueOrError0).IsFailure() {
		return (_2_valueOrError0).PropagateFailure()
	} else {
		var _3_encryptionContext _dafny.Sequence = (_2_valueOrError0).Extract().(_dafny.Sequence)
		_ = _3_encryptionContext
		var _4_maxPlaintextL _dafny.Sequence = (func() _dafny.Sequence {
			if ((test).Dtor_maxPlaintextLength()).Is_Some() {
				return _dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("maxPlaintextLength"), m_JSON_Values.Companion_JSON_.Create_Number_(m_JSON_Values.Companion_Default___.Int(_dafny.IntOfInt64(((test).Dtor_maxPlaintextLength()).Dtor_value().(int64))))))
			}
			return _dafny.SeqOf()
		})()
		_ = _4_maxPlaintextL
		var _5_valueOrError1 m_Wrappers.Result = Companion_Default___.EncryptionContextKeysToJson((test).Dtor_requiredEncryptionContextKeys())
		_ = _5_valueOrError1
		if (_5_valueOrError1).IsFailure() {
			return (_5_valueOrError1).PropagateFailure()
		} else {
			var _6_requiredEncryptionContextKeys _dafny.Sequence = (_5_valueOrError1).Extract().(_dafny.Sequence)
			_ = _6_requiredEncryptionContextKeys
			var _7_valueOrError2 m_Wrappers.Result = (func() m_Wrappers.Result {
				if (!((test).Is_NegativeEncryptKeyringVector())) && (((test).Dtor_reproducedEncryptionContext()).Is_Some()) {
					return Companion_Default___.EncryptionContextToJson(_dafny.SeqOfString("reproducedEncryptionContext"), ((test).Dtor_reproducedEncryptionContext()).Dtor_value().(_dafny.Map))
				}
				return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf())
			})()
			_ = _7_valueOrError2
			if (_7_valueOrError2).IsFailure() {
				return (_7_valueOrError2).PropagateFailure()
			} else {
				var _8_reproducedEc _dafny.Sequence = (_7_valueOrError2).Extract().(_dafny.Sequence)
				_ = _8_reproducedEc
				var _9_optionalValues _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_8_reproducedEc, _4_maxPlaintextL), _6_requiredEncryptionContextKeys), _3_encryptionContext)
				_ = _9_optionalValues
				var _source0 m_TestVectors.EncryptTestVector = test
				_ = _source0
				{
					if _source0.Is_PositiveEncryptKeyringVector() {
						var _10_valueOrError3 m_Wrappers.Result = m_KeyDescription.Companion_Default___.ToJson((test).Dtor_encryptDescription(), _dafny.IntOfInt64(3))
						_ = _10_valueOrError3
						if (_10_valueOrError3).IsFailure() {
							return (_10_valueOrError3).PropagateFailure()
						} else {
							var _11_encrypt m_JSON_Values.JSON = (_10_valueOrError3).Extract().(m_JSON_Values.JSON)
							_ = _11_encrypt
							var _12_valueOrError4 m_Wrappers.Result = m_KeyDescription.Companion_Default___.ToJson((test).Dtor_decryptDescription(), _dafny.IntOfInt64(3))
							_ = _12_valueOrError4
							if (_12_valueOrError4).IsFailure() {
								return (_12_valueOrError4).PropagateFailure()
							} else {
								var _13_decrypt m_JSON_Values.JSON = (_12_valueOrError4).Extract().(m_JSON_Values.JSON)
								_ = _13_decrypt
								return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("positive-keyring"))), _dafny.TupleOf(_dafny.SeqOfString("description"), m_JSON_Values.Companion_JSON_.Create_String_(_1_description)), _dafny.TupleOf(_dafny.SeqOfString("algorithmSuiteId"), m_JSON_Values.Companion_JSON_.Create_String_(_0_id)), _dafny.TupleOf(_dafny.SeqOfString("encryptKeyDescription"), _11_encrypt), _dafny.TupleOf(_dafny.SeqOfString("decryptKeyDescription"), _13_decrypt)), _9_optionalValues)))
							}
						}
					}
				}
				{
					if _source0.Is_PositiveEncryptNegativeDecryptKeyringVector() {
						var _14_valueOrError5 m_Wrappers.Result = m_KeyDescription.Companion_Default___.ToJson((test).Dtor_encryptDescription(), _dafny.IntOfInt64(3))
						_ = _14_valueOrError5
						if (_14_valueOrError5).IsFailure() {
							return (_14_valueOrError5).PropagateFailure()
						} else {
							var _15_encrypt m_JSON_Values.JSON = (_14_valueOrError5).Extract().(m_JSON_Values.JSON)
							_ = _15_encrypt
							var _16_valueOrError6 m_Wrappers.Result = m_KeyDescription.Companion_Default___.ToJson((test).Dtor_decryptDescription(), _dafny.IntOfInt64(3))
							_ = _16_valueOrError6
							if (_16_valueOrError6).IsFailure() {
								return (_16_valueOrError6).PropagateFailure()
							} else {
								var _17_decrypt m_JSON_Values.JSON = (_16_valueOrError6).Extract().(m_JSON_Values.JSON)
								_ = _17_decrypt
								return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("negative-decrypt-keyring"))), _dafny.TupleOf(_dafny.SeqOfString("description"), m_JSON_Values.Companion_JSON_.Create_String_(_1_description)), _dafny.TupleOf(_dafny.SeqOfString("decryptErrorDescription"), m_JSON_Values.Companion_JSON_.Create_String_((test).Dtor_decryptErrorDescription())), _dafny.TupleOf(_dafny.SeqOfString("algorithmSuiteId"), m_JSON_Values.Companion_JSON_.Create_String_(_0_id)), _dafny.TupleOf(_dafny.SeqOfString("encryptKeyDescription"), _15_encrypt), _dafny.TupleOf(_dafny.SeqOfString("decryptKeyDescription"), _17_decrypt)), _9_optionalValues)))
							}
						}
					}
				}
				{
					var _18_valueOrError7 m_Wrappers.Result = m_KeyDescription.Companion_Default___.ToJson((test).Dtor_keyDescription(), _dafny.IntOfInt64(3))
					_ = _18_valueOrError7
					if (_18_valueOrError7).IsFailure() {
						return (_18_valueOrError7).PropagateFailure()
					} else {
						var _19_keyDescription m_JSON_Values.JSON = (_18_valueOrError7).Extract().(m_JSON_Values.JSON)
						_ = _19_keyDescription
						return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("negative-encrypt-keyring"))), _dafny.TupleOf(_dafny.SeqOfString("description"), m_JSON_Values.Companion_JSON_.Create_String_(_1_description)), _dafny.TupleOf(_dafny.SeqOfString("errorDescription"), m_JSON_Values.Companion_JSON_.Create_String_((test).Dtor_errorDescription())), _dafny.TupleOf(_dafny.SeqOfString("algorithmSuiteId"), m_JSON_Values.Companion_JSON_.Create_String_(_0_id)), _dafny.TupleOf(_dafny.SeqOfString("keyDescription"), _19_keyDescription)), _9_optionalValues)))
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) OptionalBytes(key _dafny.Sequence, secret m_Wrappers.Option) _dafny.Sequence {
	if (secret).Is_Some() {
		var _0_base64 _dafny.Sequence = m_Base64.Companion_Default___.Encode((secret).Dtor_value().(_dafny.Sequence))
		_ = _0_base64
		return _dafny.SeqOf(_dafny.TupleOf(key, m_JSON_Values.Companion_JSON_.Create_String_(_0_base64)))
	} else {
		return _dafny.SeqOf()
	}
}
func (_static *CompanionStruct_Default___) EncryptedDataKey(encryptedDataKey m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_UTF8.Decode((encryptedDataKey).Dtor_keyProviderId())
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_keyProviderId _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_keyProviderId
		return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("keyProviderId"), m_JSON_Values.Companion_JSON_.Create_String_(_1_keyProviderId)), _dafny.TupleOf(_dafny.SeqOfString("keyProviderInfo"), m_JSON_Values.Companion_JSON_.Create_String_(m_Base64.Companion_Default___.Encode((encryptedDataKey).Dtor_keyProviderInfo()))), _dafny.TupleOf(_dafny.SeqOfString("ciphertext"), m_JSON_Values.Companion_JSON_.Create_String_(m_Base64.Companion_Default___.Encode((encryptedDataKey).Dtor_ciphertext()))))))
	}
}
func (_static *CompanionStruct_Default___) DecryptTestVectorToJson(test m_TestVectors.DecryptTestVector) m_Wrappers.Result {
	var _0_id _dafny.Sequence = m_AllAlgorithmSuites.Companion_Default___.ToHex((test).Dtor_algorithmSuite())
	_ = _0_id
	var _1_description _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate((test).Dtor_name(), _dafny.SeqOfString(" ")), _0_id)
	_ = _1_description
	var _2_valueOrError0 m_Wrappers.Result = Companion_Default___.EncryptionContextToJson(_dafny.SeqOfString("encryptionContext"), (test).Dtor_encryptionContext())
	_ = _2_valueOrError0
	if (_2_valueOrError0).IsFailure() {
		return (_2_valueOrError0).PropagateFailure()
	} else {
		var _3_encryptionContext _dafny.Sequence = (_2_valueOrError0).Extract().(_dafny.Sequence)
		_ = _3_encryptionContext
		var _4_valueOrError1 m_Wrappers.Result = (func() m_Wrappers.Result {
			if ((test).Dtor_reproducedEncryptionContext()).Is_Some() {
				return Companion_Default___.EncryptionContextToJson(_dafny.SeqOfString("reproducedEncryptionContext"), ((test).Dtor_reproducedEncryptionContext()).Dtor_value().(_dafny.Map))
			}
			return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf())
		})()
		_ = _4_valueOrError1
		if (_4_valueOrError1).IsFailure() {
			return (_4_valueOrError1).PropagateFailure()
		} else {
			var _5_reproducedEc _dafny.Sequence = (_4_valueOrError1).Extract().(_dafny.Sequence)
			_ = _5_reproducedEc
			var _6_valueOrError2 m_Wrappers.Result = m_KeyDescription.Companion_Default___.ToJson((test).Dtor_keyDescription(), _dafny.IntOfInt64(3))
			_ = _6_valueOrError2
			if (_6_valueOrError2).IsFailure() {
				return (_6_valueOrError2).PropagateFailure()
			} else {
				var _7_keyDescription m_JSON_Values.JSON = (_6_valueOrError2).Extract().(m_JSON_Values.JSON)
				_ = _7_keyDescription
				var _8_valueOrError3 m_Wrappers.Result = m_Seq.Companion_Default___.MapWithResult(func(coer96 func(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
					return func(arg136 interface{}) m_Wrappers.Result {
						return coer96(arg136.(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey))
					}
				}(func(_9_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey) m_Wrappers.Result {
					return Companion_Default___.EncryptedDataKey(_9_edk)
				}), (test).Dtor_encryptedDataKeys())
				_ = _8_valueOrError3
				if (_8_valueOrError3).IsFailure() {
					return (_8_valueOrError3).PropagateFailure()
				} else {
					var _10_encryptedDataKeys _dafny.Sequence = (_8_valueOrError3).Extract().(_dafny.Sequence)
					_ = _10_encryptedDataKeys
					var _source0 m_TestVectors.DecryptTestVector = test
					_ = _source0
					{
						if _source0.Is_PositiveDecryptKeyringTest() {
							var _11_plaintextDataKey _dafny.Sequence = Companion_Default___.OptionalBytes(_dafny.SeqOfString("plaintextDataKey"), ((test).Dtor_expectedResult()).Dtor_plaintextDataKey())
							_ = _11_plaintextDataKey
							var _12_symmetricSigningKey _dafny.Sequence = Companion_Default___.OptionalBytes(_dafny.SeqOfString("symmetricSigningKey"), ((test).Dtor_expectedResult()).Dtor_symmetricSigningKey())
							_ = _12_symmetricSigningKey
							var _13_valueOrError4 m_Wrappers.Result = Companion_Default___.EncryptionContextKeysToJson(m_Wrappers.Companion_Option_.Create_Some_(((test).Dtor_expectedResult()).Dtor_requiredEncryptionContextKeys()))
							_ = _13_valueOrError4
							if (_13_valueOrError4).IsFailure() {
								return (_13_valueOrError4).PropagateFailure()
							} else {
								var _14_requiredEncryptionContextKeys _dafny.Sequence = (_13_valueOrError4).Extract().(_dafny.Sequence)
								_ = _14_requiredEncryptionContextKeys
								return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("positive-keyring"))), _dafny.TupleOf(_dafny.SeqOfString("description"), m_JSON_Values.Companion_JSON_.Create_String_(_1_description)), _dafny.TupleOf(_dafny.SeqOfString("algorithmSuiteId"), m_JSON_Values.Companion_JSON_.Create_String_(_0_id)), _dafny.TupleOf(_dafny.SeqOfString("keyDescription"), _7_keyDescription), _dafny.TupleOf(_dafny.SeqOfString("encryptedDataKeys"), m_JSON_Values.Companion_JSON_.Create_Array_(_10_encryptedDataKeys)), _dafny.TupleOf(_dafny.SeqOfString("result"), m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_11_plaintextDataKey, _12_symmetricSigningKey), _14_requiredEncryptionContextKeys)))), _5_reproducedEc), _3_encryptionContext)))
							}
						}
					}
					{
						return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("negative-keyring"))), _dafny.TupleOf(_dafny.SeqOfString("description"), m_JSON_Values.Companion_JSON_.Create_String_(_1_description)), _dafny.TupleOf(_dafny.SeqOfString("errorDescription"), m_JSON_Values.Companion_JSON_.Create_String_((test).Dtor_errorDescription())), _dafny.TupleOf(_dafny.SeqOfString("algorithmSuiteId"), m_JSON_Values.Companion_JSON_.Create_String_(_0_id)), _dafny.TupleOf(_dafny.SeqOfString("keyDescription"), _7_keyDescription), _dafny.TupleOf(_dafny.SeqOfString("encryptedDataKeys"), m_JSON_Values.Companion_JSON_.Create_Array_(_10_encryptedDataKeys))), _5_reproducedEc), _3_encryptionContext)))
					}
				}
			}
		}
	}
}

// End of class Default__
