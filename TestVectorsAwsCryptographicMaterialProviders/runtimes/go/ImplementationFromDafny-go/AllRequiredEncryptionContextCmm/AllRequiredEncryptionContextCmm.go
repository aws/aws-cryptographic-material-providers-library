// Package AllRequiredEncryptionContextCmm
// Dafny module AllRequiredEncryptionContextCmm compiled into Go

package AllRequiredEncryptionContextCmm

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
	m_AllRawAES "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawAES"
	m_AllRawECDH "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawECDH"
	m_AllRawRSA "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawRSA"
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
	return "AllRequiredEncryptionContextCmm.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) A() _dafny.Sequence {
	return (m_UTF8.Encode(_dafny.SeqOfString("a"))).Dtor_value().(_dafny.Sequence)
}
func (_static *CompanionStruct_Default___) B() _dafny.Sequence {
	return (m_UTF8.Encode(_dafny.SeqOfString("b"))).Dtor_value().(_dafny.Sequence)
}
func (_static *CompanionStruct_Default___) RootEncryptionContext() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(Companion_Default___.A(), Companion_Default___.A()).UpdateUnsafe(Companion_Default___.B(), Companion_Default___.B())
}
func (_static *CompanionStruct_Default___) EncryptionContextsToTest() _dafny.Set {
	return _dafny.SetOf(Companion_Default___.RootEncryptionContext())
}
func (_static *CompanionStruct_Default___) C() _dafny.Sequence {
	return (m_UTF8.Encode(_dafny.SeqOfString("c"))).Dtor_value().(_dafny.Sequence)
}
func (_static *CompanionStruct_Default___) DisjointEncryptionContext() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(Companion_Default___.A(), Companion_Default___.C()).UpdateUnsafe(Companion_Default___.B(), Companion_Default___.C()).UpdateUnsafe(Companion_Default___.C(), Companion_Default___.C())
}
func (_static *CompanionStruct_Default___) SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter85 := _dafny.Iterate((Companion_Default___.EncryptionContextsToTest()).Elements()); ; {
			_compr_0, _ok85 := _iter85()
			if !_ok85 {
				break
			}
			var _0_encryptionContext _dafny.Map
			_0_encryptionContext = interface{}(_compr_0).(_dafny.Map)
			if (Companion_Default___.EncryptionContextsToTest()).Contains(_0_encryptionContext) {
				for _iter86 := _dafny.Iterate((func() _dafny.Set {
					var _coll1 = _dafny.NewBuilder()
					_ = _coll1
					for _iter87 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer74 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
						return func(arg94 interface{}, arg95 interface{}) bool {
							return coer74(arg94.(uint8), arg95.(uint8))
						}
					}(func(_1_a uint8, _2_b uint8) bool {
						return (_1_a) < (_2_b)
					})))).Elements()); ; {
						_compr_2, _ok87 := _iter87()
						if !_ok87 {
							break
						}
						var _3_s _dafny.Map
						_3_s = interface{}(_compr_2).(_dafny.Map)
						if ((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer75 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg96 interface{}, arg97 interface{}) bool {
								return coer75(arg96.(uint8), arg97.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Contains(_3_s)) && (((_3_s).Cardinality()).Sign() != 0) {
							_coll1.Add((_3_s).Keys())
						}
					}
					return _coll1.ToSet()
				}()).Elements()); ; {
					_compr_1, _ok86 := _iter86()
					if !_ok86 {
						break
					}
					var _4_requiredEncryptionContextKeys _dafny.Set
					_4_requiredEncryptionContextKeys = interface{}(_compr_1).(_dafny.Set)
					if (func() _dafny.Set {
						var _coll2 = _dafny.NewBuilder()
						_ = _coll2
						for _iter88 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer76 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg98 interface{}, arg99 interface{}) bool {
								return coer76(arg98.(uint8), arg99.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Elements()); ; {
							_compr_3, _ok88 := _iter88()
							if !_ok88 {
								break
							}
							var _5_s _dafny.Map
							_5_s = interface{}(_compr_3).(_dafny.Map)
							if ((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer77 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg100 interface{}, arg101 interface{}) bool {
									return coer77(arg100.(uint8), arg101.(uint8))
								}
							}(func(_1_a uint8, _2_b uint8) bool {
								return (_1_a) < (_2_b)
							})))).Contains(_5_s)) && (((_5_s).Cardinality()).Sign() != 0) {
								_coll2.Add((_5_s).Keys())
							}
						}
						return _coll2.ToSet()
					}()).Contains(_4_requiredEncryptionContextKeys) {
						for _iter89 := _dafny.Iterate((func() _dafny.Set {
							var _coll3 = _dafny.NewBuilder()
							_ = _coll3
							for _iter90 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer78 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg102 interface{}, arg103 interface{}) bool {
									return coer78(arg102.(uint8), arg103.(uint8))
								}
							}(func(_6_a uint8, _7_b uint8) bool {
								return (_6_a) < (_7_b)
							})))).Elements()); ; {
								_compr_5, _ok90 := _iter90()
								if !_ok90 {
									break
								}
								var _8_s _dafny.Map
								_8_s = interface{}(_compr_5).(_dafny.Map)
								if ((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer79 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg104 interface{}, arg105 interface{}) bool {
										return coer79(arg104.(uint8), arg105.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Contains(_8_s)) && ((((_8_s).Keys()).Intersection(_4_requiredEncryptionContextKeys)).Equals(_4_requiredEncryptionContextKeys)) {
									_coll3.Add(_8_s)
								}
							}
							return _coll3.ToSet()
						}()).Elements()); ; {
							_compr_4, _ok89 := _iter89()
							if !_ok89 {
								break
							}
							var _9_reproducedEncryptionContext _dafny.Map
							_9_reproducedEncryptionContext = interface{}(_compr_4).(_dafny.Map)
							if (func() _dafny.Set {
								var _coll4 = _dafny.NewBuilder()
								_ = _coll4
								for _iter91 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer80 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg106 interface{}, arg107 interface{}) bool {
										return coer80(arg106.(uint8), arg107.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Elements()); ; {
									_compr_6, _ok91 := _iter91()
									if !_ok91 {
										break
									}
									var _10_s _dafny.Map
									_10_s = interface{}(_compr_6).(_dafny.Map)
									if ((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer81 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg108 interface{}, arg109 interface{}) bool {
											return coer81(arg108.(uint8), arg109.(uint8))
										}
									}(func(_6_a uint8, _7_b uint8) bool {
										return (_6_a) < (_7_b)
									})))).Contains(_10_s)) && ((((_10_s).Keys()).Intersection(_4_requiredEncryptionContextKeys)).Equals(_4_requiredEncryptionContextKeys)) {
										_coll4.Add(_10_s)
									}
								}
								return _coll4.ToSet()
							}()).Contains(_9_reproducedEncryptionContext) {
								_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.SeqOfString("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), m_Wrappers.Companion_Option_.Create_None_(), _0_encryptionContext, m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(m_AllDefaultCmm.Companion_Default___.StaticAlgorithmSuite()), m_AllDefaultCmm.Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys)), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_RequiredEncryptionContext_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RequiredEncryptionContextCMM_.Create_RequiredEncryptionContextCMM_(m_AllDefaultCmm.Companion_Default___.RawAesKeyring(), m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys))), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_RequiredEncryptionContext_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RequiredEncryptionContextCMM_.Create_RequiredEncryptionContextCMM_(m_AllDefaultCmm.Companion_Default___.RawAesKeyring(), m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys))), m_Wrappers.Companion_Option_.Create_Some_(_9_reproducedEncryptionContext)))
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) FailureBadReproducedEncryptionContext() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter92 := _dafny.Iterate((Companion_Default___.EncryptionContextsToTest()).Elements()); ; {
			_compr_0, _ok92 := _iter92()
			if !_ok92 {
				break
			}
			var _0_encryptionContext _dafny.Map
			_0_encryptionContext = interface{}(_compr_0).(_dafny.Map)
			if (Companion_Default___.EncryptionContextsToTest()).Contains(_0_encryptionContext) {
				for _iter93 := _dafny.Iterate((func() _dafny.Set {
					var _coll1 = _dafny.NewBuilder()
					_ = _coll1
					for _iter94 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer82 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
						return func(arg110 interface{}, arg111 interface{}) bool {
							return coer82(arg110.(uint8), arg111.(uint8))
						}
					}(func(_1_a uint8, _2_b uint8) bool {
						return (_1_a) < (_2_b)
					})))).Elements()); ; {
						_compr_2, _ok94 := _iter94()
						if !_ok94 {
							break
						}
						var _3_s _dafny.Map
						_3_s = interface{}(_compr_2).(_dafny.Map)
						if ((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer83 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg112 interface{}, arg113 interface{}) bool {
								return coer83(arg112.(uint8), arg113.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Contains(_3_s)) && (((_3_s).Cardinality()).Sign() != 0) {
							_coll1.Add((_3_s).Keys())
						}
					}
					return _coll1.ToSet()
				}()).Elements()); ; {
					_compr_1, _ok93 := _iter93()
					if !_ok93 {
						break
					}
					var _4_requiredEncryptionContextKeys _dafny.Set
					_4_requiredEncryptionContextKeys = interface{}(_compr_1).(_dafny.Set)
					if (func() _dafny.Set {
						var _coll2 = _dafny.NewBuilder()
						_ = _coll2
						for _iter95 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer84 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg114 interface{}, arg115 interface{}) bool {
								return coer84(arg114.(uint8), arg115.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Elements()); ; {
							_compr_3, _ok95 := _iter95()
							if !_ok95 {
								break
							}
							var _5_s _dafny.Map
							_5_s = interface{}(_compr_3).(_dafny.Map)
							if ((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer85 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg116 interface{}, arg117 interface{}) bool {
									return coer85(arg116.(uint8), arg117.(uint8))
								}
							}(func(_1_a uint8, _2_b uint8) bool {
								return (_1_a) < (_2_b)
							})))).Contains(_5_s)) && (((_5_s).Cardinality()).Sign() != 0) {
								_coll2.Add((_5_s).Keys())
							}
						}
						return _coll2.ToSet()
					}()).Contains(_4_requiredEncryptionContextKeys) {
						for _iter96 := _dafny.Iterate((func() _dafny.Set {
							var _coll3 = _dafny.NewBuilder()
							_ = _coll3
							for _iter97 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer86 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg118 interface{}, arg119 interface{}) bool {
									return coer86(arg118.(uint8), arg119.(uint8))
								}
							}(func(_6_a uint8, _7_b uint8) bool {
								return (_6_a) < (_7_b)
							})))).Elements()); ; {
								_compr_5, _ok97 := _iter97()
								if !_ok97 {
									break
								}
								var _8_s _dafny.Map
								_8_s = interface{}(_compr_5).(_dafny.Map)
								if ((m_AllDefaultCmm.Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer87 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg120 interface{}, arg121 interface{}) bool {
										return coer87(arg120.(uint8), arg121.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Contains(_8_s)) && (!(_8_s).Equals(_dafny.NewMapBuilder().ToMap())) {
									_coll3.Add(_8_s)
								}
							}
							return _coll3.ToSet()
						}()).Elements()); ; {
							_compr_4, _ok96 := _iter96()
							if !_ok96 {
								break
							}
							var _9_incorrectEncryptionContext _dafny.Map
							_9_incorrectEncryptionContext = interface{}(_compr_4).(_dafny.Map)
							if (func() _dafny.Set {
								var _coll4 = _dafny.NewBuilder()
								_ = _coll4
								for _iter98 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer88 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg122 interface{}, arg123 interface{}) bool {
										return coer88(arg122.(uint8), arg123.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Elements()); ; {
									_compr_6, _ok98 := _iter98()
									if !_ok98 {
										break
									}
									var _10_s _dafny.Map
									_10_s = interface{}(_compr_6).(_dafny.Map)
									if ((m_AllDefaultCmm.Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer89 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg124 interface{}, arg125 interface{}) bool {
											return coer89(arg124.(uint8), arg125.(uint8))
										}
									}(func(_6_a uint8, _7_b uint8) bool {
										return (_6_a) < (_7_b)
									})))).Contains(_10_s)) && (!(_10_s).Equals(_dafny.NewMapBuilder().ToMap())) {
										_coll4.Add(_10_s)
									}
								}
								return _coll4.ToSet()
							}()).Contains(_9_incorrectEncryptionContext) {
								for _iter99 := _dafny.Iterate((func() _dafny.Set {
									var _coll5 = _dafny.NewBuilder()
									_ = _coll5
									for _iter100 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer90 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg126 interface{}, arg127 interface{}) bool {
											return coer90(arg126.(uint8), arg127.(uint8))
										}
									}(func(_11_a uint8, _12_b uint8) bool {
										return (_11_a) < (_12_b)
									})))).Elements()); ; {
										_compr_8, _ok100 := _iter100()
										if !_ok100 {
											break
										}
										var _13_s _dafny.Map
										_13_s = interface{}(_compr_8).(_dafny.Map)
										if (m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer91 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
											return func(arg128 interface{}, arg129 interface{}) bool {
												return coer91(arg128.(uint8), arg129.(uint8))
											}
										}(func(_11_a uint8, _12_b uint8) bool {
											return (_11_a) < (_12_b)
										})))).Contains(_13_s) {
											_coll5.Add((_13_s).Merge(_9_incorrectEncryptionContext))
										}
									}
									return _coll5.ToSet()
								}()).Elements()); ; {
									_compr_7, _ok99 := _iter99()
									if !_ok99 {
										break
									}
									var _14_reproducedEncryptionContext _dafny.Map
									_14_reproducedEncryptionContext = interface{}(_compr_7).(_dafny.Map)
									if (func() _dafny.Set {
										var _coll6 = _dafny.NewBuilder()
										_ = _coll6
										for _iter101 := _dafny.Iterate((m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer92 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
											return func(arg130 interface{}, arg131 interface{}) bool {
												return coer92(arg130.(uint8), arg131.(uint8))
											}
										}(func(_11_a uint8, _12_b uint8) bool {
											return (_11_a) < (_12_b)
										})))).Elements()); ; {
											_compr_9, _ok101 := _iter101()
											if !_ok101 {
												break
											}
											var _15_s _dafny.Map
											_15_s = interface{}(_compr_9).(_dafny.Map)
											if (m_AllDefaultCmm.Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer93 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
												return func(arg132 interface{}, arg133 interface{}) bool {
													return coer93(arg132.(uint8), arg133.(uint8))
												}
											}(func(_11_a uint8, _12_b uint8) bool {
												return (_11_a) < (_12_b)
											})))).Contains(_15_s) {
												_coll6.Add((_15_s).Merge(_9_incorrectEncryptionContext))
											}
										}
										return _coll6.ToSet()
									}()).Contains(_14_reproducedEncryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptNegativeDecryptKeyringVector_(_dafny.SeqOfString("Failure of reproducedEncryptionContext"), m_Wrappers.Companion_Option_.Create_None_(), _0_encryptionContext, m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(m_AllDefaultCmm.Companion_Default___.StaticAlgorithmSuite()), m_AllDefaultCmm.Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys)), _dafny.SeqOfString("The reproducedEncryptionContext is not correct"), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_RequiredEncryptionContext_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RequiredEncryptionContextCMM_.Create_RequiredEncryptionContextCMM_(m_AllDefaultCmm.Companion_Default___.RawAesKeyring(), m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys))), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_RequiredEncryptionContext_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RequiredEncryptionContextCMM_.Create_RequiredEncryptionContextCMM_(m_AllDefaultCmm.Companion_Default___.RawAesKeyring(), m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys))), m_Wrappers.Companion_Option_.Create_Some_(_14_reproducedEncryptionContext)))
									}
								}
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) Tests() _dafny.Set {
	return (Companion_Default___.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext()).Union(Companion_Default___.FailureBadReproducedEncryptionContext())
}

// End of class Default__
