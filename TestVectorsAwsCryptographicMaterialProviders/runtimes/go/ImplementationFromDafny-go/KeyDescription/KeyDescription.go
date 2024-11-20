// Package KeyDescription
// Dafny module KeyDescription compiled into Go

package KeyDescription

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
	m_AwsCryptographyMaterialProvidersTestVectorKeysTypes "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AwsCryptographyMaterialProvidersTestVectorKeysTypes"
	m_JSONHelpers "github.com/aws/aws-cryptographic-material-providers-library/testvectors/JSONHelpers"
	m_MplManifestOptions "github.com/aws/aws-cryptographic-material-providers-library/testvectors/MplManifestOptions"
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
	return "KeyDescription.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) PrintErr(e _dafny.Sequence) _dafny.Tuple {
	var _hresult _dafny.Tuple = _dafny.TupleOf()
	_ = _hresult
	_dafny.Print((e).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_hresult = _dafny.TupleOf()
	return _hresult
	return _hresult
}
func (_static *CompanionStruct_Default___) PrintJSON(e _dafny.Sequence) _dafny.Tuple {
	var _hresult _dafny.Tuple = _dafny.TupleOf()
	_ = _hresult
	_dafny.Print(e)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_hresult = _dafny.TupleOf()
	return _hresult
	return _hresult
}
func (_static *CompanionStruct_Default___) ToKeyDescription(json m_JSON_Values.JSON) m_Wrappers.Result {
	if (json).Is_Array() {
		var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_dafny.One).Cmp(_dafny.IntOfUint32(((json).Dtor_arr()).Cardinality())) <= 0, _dafny.SeqOfString("Need at least one element in a JSON Array."))
		_ = _0_valueOrError0
		if (_0_valueOrError0).IsFailure() {
			return (_0_valueOrError0).PropagateFailure()
		} else {
			var _1_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier(((json).Dtor_arr()).UniqueElements(), true, func(_forall_var_0 m_JSON_Values.JSON) bool {
				var _2_c m_JSON_Values.JSON
				_2_c = interface{}(_forall_var_0).(m_JSON_Values.JSON)
				return !(_dafny.Companion_Sequence_.Contains((json).Dtor_arr(), _2_c)) || ((_2_c).Is_Object())
			}), _dafny.SeqOfString("No nested arrays."))
			_ = _1_valueOrError1
			if (_1_valueOrError1).IsFailure() {
				return (_1_valueOrError1).PropagateFailure()
			} else {
				return Companion_Default___.ToMultiKeyring(json, m_Wrappers.Companion_Option_.Create_Some_(((json).Dtor_arr()).Select(0).(m_JSON_Values.JSON)), ((json).Dtor_arr()).Drop(1))
			}
		}
	} else {
		var _3_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((json).Is_Object(), _dafny.SeqOfString("KeyDescription not an object"))
		_ = _3_valueOrError2
		if (_3_valueOrError2).IsFailure() {
			return (_3_valueOrError2).PropagateFailure()
		} else {
			var _4_obj _dafny.Sequence = (json).Dtor_obj()
			_ = _4_obj
			var _5_typString _dafny.Sequence = _dafny.SeqOfString("type")
			_ = _5_typString
			var _6_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_5_typString, _4_obj)
			_ = _6_valueOrError3
			if (_6_valueOrError3).IsFailure() {
				return (_6_valueOrError3).PropagateFailure()
			} else {
				var _7_typ _dafny.Sequence = (_6_valueOrError3).Extract().(_dafny.Sequence)
				_ = _7_typ
				var _8_valueOrError4 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(Companion_Default___.KeyDescriptionString_q(_7_typ), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported KeyDescription type:"), _7_typ))
				_ = _8_valueOrError4
				if (_8_valueOrError4).IsFailure() {
					return (_8_valueOrError4).PropagateFailure()
				} else {
					var _source0 _dafny.Sequence = _7_typ
					_ = _source0
					{
						if (_source0).Equals(_dafny.SeqOfString("aws-kms-mrk-aware-discovery")) {
							return Companion_Default___.ToAwsKmsMrkAwareDiscovery(_4_obj)
						}
					}
					{
						if (_source0).Equals(_dafny.SeqOfString("multi-keyring")) {
							var _9_generatorJson m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.Get(_dafny.SeqOfString("generator"), _4_obj)).ToOption()
							_ = _9_generatorJson
							var _10_valueOrError5 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetArray(_dafny.SeqOfString("childKeyrings"), _4_obj)
							_ = _10_valueOrError5
							if (_10_valueOrError5).IsFailure() {
								return (_10_valueOrError5).PropagateFailure()
							} else {
								var _11_childKeyringsJson _dafny.Sequence = (_10_valueOrError5).Extract().(_dafny.Sequence)
								_ = _11_childKeyringsJson
								return Companion_Default___.ToMultiKeyring(json, _9_generatorJson, _11_childKeyringsJson)
							}
						}
					}
					{
						if (_source0).Equals(_dafny.SeqOfString("required-encryption-context-cmm")) {
							var _12_valueOrError6 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Get(_dafny.SeqOfString("underlying"), _4_obj)
							_ = _12_valueOrError6
							if (_12_valueOrError6).IsFailure() {
								return (_12_valueOrError6).PropagateFailure()
							} else {
								var _13_u m_JSON_Values.JSON = (_12_valueOrError6).Extract().(m_JSON_Values.JSON)
								_ = _13_u
								var _14_valueOrError7 m_Wrappers.Result = Companion_Default___.ToKeyDescription(_13_u)
								_ = _14_valueOrError7
								if (_14_valueOrError7).IsFailure() {
									return (_14_valueOrError7).PropagateFailure()
								} else {
									var _15_underlying m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_14_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
									_ = _15_underlying
									var _16_requiredEncryptionContextStrings _dafny.Sequence = ((m_JSONHelpers.Companion_Default___.GetArrayString(_dafny.SeqOfString("requiredEncryptionContextKeys"), _4_obj)).ToOption()).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence)
									_ = _16_requiredEncryptionContextStrings
									var _17_valueOrError8 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeSeq(_16_requiredEncryptionContextStrings)
									_ = _17_valueOrError8
									if (_17_valueOrError8).IsFailure() {
										return (_17_valueOrError8).PropagateFailure()
									} else {
										var _18_requiredEncryptionContextKeys _dafny.Sequence = (_17_valueOrError8).Extract().(_dafny.Sequence)
										_ = _18_requiredEncryptionContextKeys
										return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_RequiredEncryptionContext_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RequiredEncryptionContextCMM_.Create_RequiredEncryptionContextCMM_(_15_underlying, _18_requiredEncryptionContextKeys)))
									}
								}
							}
						}
					}
					{
						if (_source0).Equals(_dafny.SeqOfString("raw-ecdh")) {
							return Companion_Default___.ToRawEcdh(_4_obj)
						}
					}
					{
						if (_source0).Equals(_dafny.SeqOfString("aws-kms-ecdh")) {
							return Companion_Default___.ToAwsKmsEcdh(_4_obj)
						}
					}
					{
						var _19_valueOrError9 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("key"), _4_obj)
						_ = _19_valueOrError9
						if (_19_valueOrError9).IsFailure() {
							return (_19_valueOrError9).PropagateFailure()
						} else {
							var _20_key _dafny.Sequence = (_19_valueOrError9).Extract().(_dafny.Sequence)
							_ = _20_key
							var _source1 _dafny.Sequence = _7_typ
							_ = _source1
							{
								if (_source1).Equals(_dafny.SeqOfString("static-material-keyring")) {
									return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_Static_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_StaticKeyring_.Create_StaticKeyring_(_20_key)))
								}
							}
							{
								if (_source1).Equals(_dafny.SeqOfString("aws-kms")) {
									return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_Kms_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KMSInfo_.Create_KMSInfo_(_20_key)))
								}
							}
							{
								if (_source1).Equals(_dafny.SeqOfString("aws-kms-mrk-aware")) {
									return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_KmsMrk_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KmsMrkAware_.Create_KmsMrkAware_(_20_key)))
								}
							}
							{
								if (_source1).Equals(_dafny.SeqOfString("aws-kms-rsa")) {
									return Companion_Default___.ToAwsKmsRsa(_20_key, _4_obj)
								}
							}
							{
								if (_source1).Equals(_dafny.SeqOfString("aws-kms-hierarchy")) {
									return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_Hierarchy_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_HierarchyKeyring_.Create_HierarchyKeyring_(_20_key)))
								}
							}
							{
								var _21_valueOrError10 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("encryption-algorithm"), _4_obj)
								_ = _21_valueOrError10
								if (_21_valueOrError10).IsFailure() {
									return (_21_valueOrError10).PropagateFailure()
								} else {
									var _22_algorithm _dafny.Sequence = (_21_valueOrError10).Extract().(_dafny.Sequence)
									_ = _22_algorithm
									var _23_valueOrError11 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(Companion_Default___.RawAlgorithmString_q(_22_algorithm), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported algorithm:"), _22_algorithm))
									_ = _23_valueOrError11
									if (_23_valueOrError11).IsFailure() {
										return (_23_valueOrError11).PropagateFailure()
									} else {
										var _source2 _dafny.Sequence = _22_algorithm
										_ = _source2
										{
											if (_source2).Equals(_dafny.SeqOfString("aes")) {
												return Companion_Default___.ToRawAes(_20_key, _4_obj)
											}
										}
										{
											return Companion_Default___.ToRawRsa(_20_key, _4_obj)
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToDiscoveryFilter(obj _dafny.Sequence) m_Wrappers.Option {
	var _0_valueOrError0 m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.GetObject(_dafny.SeqOfString("aws-kms-discovery-filter"), obj)).ToOption()
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_filter _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_filter
		var _2_valueOrError1 m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("partition"), _1_filter)).ToOption()
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_partition _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
			_ = _3_partition
			var _4_valueOrError2 m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.GetArrayString(_dafny.SeqOfString("account-ids"), _1_filter)).ToOption()
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				var _5_accountIds _dafny.Sequence = (_4_valueOrError2).Extract().(_dafny.Sequence)
				_ = _5_accountIds
				return m_Wrappers.Companion_Option_.Create_Some_(m_AwsCryptographyMaterialProvidersTypes.Companion_DiscoveryFilter_.Create_DiscoveryFilter_(_5_accountIds, _3_partition))
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToAwsKmsMrkAwareDiscovery(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("default-mrk-region"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_defaultMrkRegion _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_defaultMrkRegion
		var _2_filter m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetObject(_dafny.SeqOfString("aws-kms-discovery-filter"), obj)
		_ = _2_filter
		var _3_awsKmsDiscoveryFilter m_Wrappers.Option = Companion_Default___.ToDiscoveryFilter(obj)
		_ = _3_awsKmsDiscoveryFilter
		return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_KmsMrkDiscovery_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KmsMrkAwareDiscovery_.Create_KmsMrkAwareDiscovery_(_dafny.SeqOfString("aws-kms-mrk-aware-discovery"), _1_defaultMrkRegion, _3_awsKmsDiscoveryFilter)))
	}
}
func (_static *CompanionStruct_Default___) ToAwsKmsRsa(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("encryption-algorithm"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_encryptionAlgorithmString _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_encryptionAlgorithmString
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((Companion_Default___.String2EncryptionAlgorithmSpec()).Contains(_1_encryptionAlgorithmString), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported EncryptionAlgorithmSpec:"), _1_encryptionAlgorithmString))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_encryptionAlgorithm m_ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = (Companion_Default___.String2EncryptionAlgorithmSpec()).Get(_1_encryptionAlgorithmString).(m_ComAmazonawsKmsTypes.EncryptionAlgorithmSpec)
			_ = _3_encryptionAlgorithm
			return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_KmsRsa_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KmsRsaKeyring_.Create_KmsRsaKeyring_(key, _3_encryptionAlgorithm)))
		}
	}
}
func (_static *CompanionStruct_Default___) ToAwsKmsEcdh(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("ecc-curve"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_eccCurve _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_eccCurve
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((Companion_Default___.KmsKey2EccAlgorithmSpec()).Contains(_1_eccCurve), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported ECC Curve Spec:"), _1_eccCurve))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("schema"), obj)
			_ = _3_valueOrError2
			if (_3_valueOrError2).IsFailure() {
				return (_3_valueOrError2).PropagateFailure()
			} else {
				var _4_schema _dafny.Sequence = (_3_valueOrError2).Extract().(_dafny.Sequence)
				_ = _4_schema
				var _5_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender"), obj)
				_ = _5_valueOrError3
				if (_5_valueOrError3).IsFailure() {
					return (_5_valueOrError3).PropagateFailure()
				} else {
					var _6_sender _dafny.Sequence = (_5_valueOrError3).Extract().(_dafny.Sequence)
					_ = _6_sender
					var _7_valueOrError4 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient"), obj)
					_ = _7_valueOrError4
					if (_7_valueOrError4).IsFailure() {
						return (_7_valueOrError4).PropagateFailure()
					} else {
						var _8_recipient _dafny.Sequence = (_7_valueOrError4).Extract().(_dafny.Sequence)
						_ = _8_recipient
						var _9_valueOrError5 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender-public-key"), obj)
						_ = _9_valueOrError5
						if (_9_valueOrError5).IsFailure() {
							return (_9_valueOrError5).PropagateFailure()
						} else {
							var _10_senderPublicKey _dafny.Sequence = (_9_valueOrError5).Extract().(_dafny.Sequence)
							_ = _10_senderPublicKey
							var _11_valueOrError6 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient-public-key"), obj)
							_ = _11_valueOrError6
							if (_11_valueOrError6).IsFailure() {
								return (_11_valueOrError6).PropagateFailure()
							} else {
								var _12_recipientPublicKey _dafny.Sequence = (_11_valueOrError6).Extract().(_dafny.Sequence)
								_ = _12_recipientPublicKey
								return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_KmsECDH_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KmsEcdhKeyring_.Create_KmsEcdhKeyring_(_6_sender, _8_recipient, _10_senderPublicKey, _12_recipientPublicKey, _1_eccCurve, _4_schema)))
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToRawAes(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("provider-id"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_providerId _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_providerId
		return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_AES_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RawAES_.Create_RawAES_(key, _1_providerId)))
	}
}
func (_static *CompanionStruct_Default___) ToRawRsa(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("provider-id"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_providerId _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_providerId
		var _2_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("padding-algorithm"), obj)
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_paddingAlgorithm _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
			_ = _3_paddingAlgorithm
			var _4_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("padding-hash"), obj)
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				var _5_maybePaddingHash m_Wrappers.Option = (_4_valueOrError2).Extract().(m_Wrappers.Option)
				_ = _5_maybePaddingHash
				var _6_valueOrError3 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(!((_5_maybePaddingHash).Is_None()) || (_dafny.Companion_Sequence_.Equal(_3_paddingAlgorithm, _dafny.SeqOfString("pkcs1"))), _dafny.SeqOfString("oaep-mgf1 MUST define padding-hash"))
				_ = _6_valueOrError3
				if (_6_valueOrError3).IsFailure() {
					return (_6_valueOrError3).PropagateFailure()
				} else {
					var _7_paddingHash _dafny.Sequence = (_5_maybePaddingHash).UnwrapOr(_dafny.SeqOfString("sha1")).(_dafny.Sequence)
					_ = _7_paddingHash
					var _8_valueOrError4 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((Companion_Default___.String2PaddingAlgorithm()).Contains(_dafny.TupleOf(_3_paddingAlgorithm, _7_paddingHash)), _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported padding:"), _3_paddingAlgorithm), _dafny.SeqOfString(" hash:")), _7_paddingHash))
					_ = _8_valueOrError4
					if (_8_valueOrError4).IsFailure() {
						return (_8_valueOrError4).PropagateFailure()
					} else {
						return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_RSA_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RawRSA_.Create_RawRSA_(key, _1_providerId, (Companion_Default___.String2PaddingAlgorithm()).Get(_dafny.TupleOf(_3_paddingAlgorithm, _7_paddingHash)).(m_AwsCryptographyMaterialProvidersTypes.PaddingScheme))))
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToRawEcdh(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("provider-id"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_providerId _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_providerId
		var _2_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("ecc-curve"), obj)
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_ecc__curve _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
			_ = _3_ecc__curve
			var _4_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender"), obj)
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				var _5_sender _dafny.Sequence = (_4_valueOrError2).Extract().(_dafny.Sequence)
				_ = _5_sender
				var _6_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient"), obj)
				_ = _6_valueOrError3
				if (_6_valueOrError3).IsFailure() {
					return (_6_valueOrError3).PropagateFailure()
				} else {
					var _7_recipient _dafny.Sequence = (_6_valueOrError3).Extract().(_dafny.Sequence)
					_ = _7_recipient
					var _8_valueOrError4 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("schema"), obj)
					_ = _8_valueOrError4
					if (_8_valueOrError4).IsFailure() {
						return (_8_valueOrError4).PropagateFailure()
					} else {
						var _9_schema _dafny.Sequence = (_8_valueOrError4).Extract().(_dafny.Sequence)
						_ = _9_schema
						var _10_valueOrError5 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender-public-key"), obj)
						_ = _10_valueOrError5
						if (_10_valueOrError5).IsFailure() {
							return (_10_valueOrError5).PropagateFailure()
						} else {
							var _11_senderPublicKey _dafny.Sequence = (_10_valueOrError5).Extract().(_dafny.Sequence)
							_ = _11_senderPublicKey
							var _12_valueOrError6 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient-public-key"), obj)
							_ = _12_valueOrError6
							if (_12_valueOrError6).IsFailure() {
								return (_12_valueOrError6).PropagateFailure()
							} else {
								var _13_recipientPublicKey _dafny.Sequence = (_12_valueOrError6).Extract().(_dafny.Sequence)
								_ = _13_recipientPublicKey
								return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_ECDH_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RawEcdh_.Create_RawEcdh_(_5_sender, _7_recipient, _11_senderPublicKey, _13_recipientPublicKey, _1_providerId, _3_ecc__curve, _9_schema)))
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToMultiKeyring(json m_JSON_Values.JSON, generatorJson m_Wrappers.Option, childKeyringsJson _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(!((generatorJson).Is_Some()) || (((generatorJson).Dtor_value().(m_JSON_Values.JSON)).Is_Object()), _dafny.SeqOfString("Not an object"))
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_valueOrError1 m_Wrappers.Result = (func() m_Wrappers.Result {
			if (generatorJson).Is_Some() {
				return func(_pat_let0_0 m_Wrappers.Result) m_Wrappers.Result {
					return func(_2_valueOrError2 m_Wrappers.Result) m_Wrappers.Result {
						return (func() m_Wrappers.Result {
							if (_2_valueOrError2).IsFailure() {
								return (_2_valueOrError2).PropagateFailure()
							}
							return func(_pat_let1_0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) m_Wrappers.Result {
								return func(_3_g m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) m_Wrappers.Result {
									return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(_3_g))
								}(_pat_let1_0)
							}((_2_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription))
						})()
					}(_pat_let0_0)
				}(Companion_Default___.ToKeyDescription((generatorJson).Dtor_value().(m_JSON_Values.JSON)))
			}
			return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
		})()
		_ = _1_valueOrError1
		if (_1_valueOrError1).IsFailure() {
			return (_1_valueOrError1).PropagateFailure()
		} else {
			var _4_generator m_Wrappers.Option = (_1_valueOrError1).Extract().(m_Wrappers.Option)
			_ = _4_generator
			var _5_valueOrError3 m_Wrappers.Result = m_Seq.Companion_Default___.MapWithResult(func(coer6 func(m_JSON_Values.JSON) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
				return func(arg6 interface{}) m_Wrappers.Result {
					return coer6(arg6.(m_JSON_Values.JSON))
				}
			}((func(_6_childKeyringsJson _dafny.Sequence) func(m_JSON_Values.JSON) m_Wrappers.Result {
				return func(_7_c m_JSON_Values.JSON) m_Wrappers.Result {
					return Companion_Default___.ToKeyDescription(_7_c)
				}
			})(childKeyringsJson)), childKeyringsJson)
			_ = _5_valueOrError3
			if (_5_valueOrError3).IsFailure() {
				return (_5_valueOrError3).PropagateFailure()
			} else {
				var _8_childKeyrings _dafny.Sequence = (_5_valueOrError3).Extract().(_dafny.Sequence)
				_ = _8_childKeyrings
				return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_Multi_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_MultiKeyring_.Create_MultiKeyring_(_4_generator, _8_childKeyrings)))
			}
		}
	}
}
func (_static *CompanionStruct_Default___) KeyDescriptionString_q(s _dafny.Sequence) bool {
	return ((((((((((_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("static-material-keyring"))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms-mrk-aware")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms-mrk-aware-discovery")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("raw")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("raw-ecdh")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms-hierarchy")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms-rsa")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms-ecdh")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("required-encryption-context-cmm")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("multi-keyring")))
}
func (_static *CompanionStruct_Default___) RawAlgorithmString_q(s _dafny.Sequence) bool {
	return (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aes"))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("rsa")))
}
func (_static *CompanionStruct_Default___) KeyDescriptionVersion_q(v _dafny.Int) bool {
	return (((v).Cmp(_dafny.One) == 0) || ((v).Cmp(_dafny.IntOfInt64(2)) == 0)) || ((v).Cmp(_dafny.IntOfInt64(3)) == 0)
}
func (_static *CompanionStruct_Default___) ToJson(keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, outputVersion _dafny.Int) m_Wrappers.Result {
	var _source0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = keyDescription
	_ = _source0
	{
		if _source0.Is_Kms() {
			var _0_Kms m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Kms).Kms
			_ = _0_Kms
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("aws-kms"))), _dafny.TupleOf(_dafny.SeqOfString("key"), m_JSON_Values.Companion_JSON_.Create_String_((_0_Kms).Dtor_keyId())))))
		}
	}
	{
		if _source0.Is_KmsMrk() {
			var _1_KmsMrk m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrk).KmsMrk
			_ = _1_KmsMrk
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("aws-kms-mrk-aware"))), _dafny.TupleOf(_dafny.SeqOfString("key"), m_JSON_Values.Companion_JSON_.Create_String_((_1_KmsMrk).Dtor_keyId())))))
		}
	}
	{
		if _source0.Is_KmsMrkDiscovery() {
			var _2_KmsMrkDiscovery m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrkDiscovery).KmsMrkDiscovery
			_ = _2_KmsMrkDiscovery
			var _3_filter _dafny.Sequence = (func() _dafny.Sequence {
				if ((_2_KmsMrkDiscovery).Dtor_awsKmsDiscoveryFilter()).Is_Some() {
					return _dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("aws-kms-discovery-filter"), m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("partition"), m_JSON_Values.Companion_JSON_.Create_String_((((_2_KmsMrkDiscovery).Dtor_awsKmsDiscoveryFilter()).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DiscoveryFilter)).Dtor_partition())), _dafny.TupleOf(_dafny.SeqOfString("account-ids"), m_JSON_Values.Companion_JSON_.Create_Array_(m_Seq.Companion_Default___.Map(func(coer7 func(_dafny.Sequence) m_JSON_Values.JSON) func(interface{}) interface{} {
						return func(arg7 interface{}) interface{} {
							return coer7(arg7.(_dafny.Sequence))
						}
					}(func(_4_s _dafny.Sequence) m_JSON_Values.JSON {
						return m_JSON_Values.Companion_JSON_.Create_String_(_4_s)
					}), (((_2_KmsMrkDiscovery).Dtor_awsKmsDiscoveryFilter()).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DiscoveryFilter)).Dtor_accountIds())))))))
				}
				return _dafny.SeqOf()
			})()
			_ = _3_filter
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("aws-kms-mrk-aware-discovery"))), _dafny.TupleOf(_dafny.SeqOfString("default-mrk-region"), m_JSON_Values.Companion_JSON_.Create_String_((_2_KmsMrkDiscovery).Dtor_defaultMrkRegion()))), _3_filter)))
		}
	}
	{
		if _source0.Is_RSA() {
			var _5_RSA m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RSA).RSA
			_ = _5_RSA
			var _6_padding _dafny.Tuple = (Companion_Default___.PaddingAlgorithmString2String()).Get((_5_RSA).Dtor_padding()).(_dafny.Tuple)
			_ = _6_padding
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("raw"))), _dafny.TupleOf(_dafny.SeqOfString("key"), m_JSON_Values.Companion_JSON_.Create_String_((_5_RSA).Dtor_keyId())), _dafny.TupleOf(_dafny.SeqOfString("provider-id"), m_JSON_Values.Companion_JSON_.Create_String_((_5_RSA).Dtor_providerId())), _dafny.TupleOf(_dafny.SeqOfString("encryption-algorithm"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("rsa"))), _dafny.TupleOf(_dafny.SeqOfString("padding-algorithm"), m_JSON_Values.Companion_JSON_.Create_String_((*(_6_padding).IndexInt(0)).(_dafny.Sequence))), _dafny.TupleOf(_dafny.SeqOfString("padding-hash"), m_JSON_Values.Companion_JSON_.Create_String_((*(_6_padding).IndexInt(1)).(_dafny.Sequence))))))
		}
	}
	{
		if _source0.Is_AES() {
			var _7_AES m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_AES).AES
			_ = _7_AES
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("raw"))), _dafny.TupleOf(_dafny.SeqOfString("key"), m_JSON_Values.Companion_JSON_.Create_String_((_7_AES).Dtor_keyId())), _dafny.TupleOf(_dafny.SeqOfString("provider-id"), m_JSON_Values.Companion_JSON_.Create_String_((_7_AES).Dtor_providerId())), _dafny.TupleOf(_dafny.SeqOfString("encryption-algorithm"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("aes"))))))
		}
	}
	{
		if _source0.Is_ECDH() {
			var _8_ECDH m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH).ECDH
			_ = _8_ECDH
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("raw-ecdh"))), _dafny.TupleOf(_dafny.SeqOfString("sender"), m_JSON_Values.Companion_JSON_.Create_String_((_8_ECDH).Dtor_senderKeyId())), _dafny.TupleOf(_dafny.SeqOfString("recipient"), m_JSON_Values.Companion_JSON_.Create_String_((_8_ECDH).Dtor_recipientKeyId())), _dafny.TupleOf(_dafny.SeqOfString("sender-public-key"), m_JSON_Values.Companion_JSON_.Create_String_((_8_ECDH).Dtor_senderPublicKey())), _dafny.TupleOf(_dafny.SeqOfString("recipient-public-key"), m_JSON_Values.Companion_JSON_.Create_String_((_8_ECDH).Dtor_recipientPublicKey())), _dafny.TupleOf(_dafny.SeqOfString("provider-id"), m_JSON_Values.Companion_JSON_.Create_String_((_8_ECDH).Dtor_providerId())), _dafny.TupleOf(_dafny.SeqOfString("ecc-curve"), m_JSON_Values.Companion_JSON_.Create_String_((_8_ECDH).Dtor_curveSpec())), _dafny.TupleOf(_dafny.SeqOfString("schema"), m_JSON_Values.Companion_JSON_.Create_String_((_8_ECDH).Dtor_keyAgreementScheme())))))
		}
	}
	{
		if _source0.Is_Static() {
			var _9_Static m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static).Static
			_ = _9_Static
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("static-material-keyring"))), _dafny.TupleOf(_dafny.SeqOfString("key"), m_JSON_Values.Companion_JSON_.Create_String_((_9_Static).Dtor_keyId())))))
		}
	}
	{
		if _source0.Is_KmsRsa() {
			var _10_KmsRsa m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsRsa).KmsRsa
			_ = _10_KmsRsa
			var _11_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((Companion_Default___.EncryptionAlgorithmSpec2String()).Contains((_10_KmsRsa).Dtor_encryptionAlgorithm()), _dafny.SeqOfString("Unsupported encryptionAlgorithm"))
			_ = _11_valueOrError0
			if (_11_valueOrError0).IsFailure() {
				return (_11_valueOrError0).PropagateFailure()
			} else {
				var _12_encryptionAlgorithm _dafny.Sequence = (Companion_Default___.EncryptionAlgorithmSpec2String()).Get((_10_KmsRsa).Dtor_encryptionAlgorithm()).(_dafny.Sequence)
				_ = _12_encryptionAlgorithm
				return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("aws-kms-rsa"))), _dafny.TupleOf(_dafny.SeqOfString("key"), m_JSON_Values.Companion_JSON_.Create_String_((_10_KmsRsa).Dtor_keyId())), _dafny.TupleOf(_dafny.SeqOfString("encryption-algorithm"), m_JSON_Values.Companion_JSON_.Create_String_(_12_encryptionAlgorithm)))))
			}
		}
	}
	{
		if _source0.Is_KmsECDH() {
			var _13_KmsECDH m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsECDH).KmsECDH
			_ = _13_KmsECDH
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("aws-kms-ecdh"))), _dafny.TupleOf(_dafny.SeqOfString("sender"), m_JSON_Values.Companion_JSON_.Create_String_((_13_KmsECDH).Dtor_senderKeyId())), _dafny.TupleOf(_dafny.SeqOfString("recipient"), m_JSON_Values.Companion_JSON_.Create_String_((_13_KmsECDH).Dtor_recipientKeyId())), _dafny.TupleOf(_dafny.SeqOfString("sender-public-key"), m_JSON_Values.Companion_JSON_.Create_String_((_13_KmsECDH).Dtor_senderPublicKey())), _dafny.TupleOf(_dafny.SeqOfString("recipient-public-key"), m_JSON_Values.Companion_JSON_.Create_String_((_13_KmsECDH).Dtor_recipientPublicKey())), _dafny.TupleOf(_dafny.SeqOfString("ecc-curve"), m_JSON_Values.Companion_JSON_.Create_String_((_13_KmsECDH).Dtor_curveSpec())), _dafny.TupleOf(_dafny.SeqOfString("schema"), m_JSON_Values.Companion_JSON_.Create_String_((_13_KmsECDH).Dtor_keyAgreementScheme())))))
		}
	}
	{
		if _source0.Is_Hierarchy() {
			var _14_Hierarchy m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Hierarchy).Hierarchy
			_ = _14_Hierarchy
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("aws-kms-hierarchy"))), _dafny.TupleOf(_dafny.SeqOfString("key"), m_JSON_Values.Companion_JSON_.Create_String_((_14_Hierarchy).Dtor_keyId())))))
		}
	}
	{
		if _source0.Is_Multi() {
			var _15_MultiKeyring m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Multi).Multi
			_ = _15_MultiKeyring
			var _16_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((!(((_15_MultiKeyring).Dtor_generator()).Is_Some()) || (Companion_Default___.Keyring_q(((_15_MultiKeyring).Dtor_generator()).Dtor_value().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)))) && (_dafny.Quantifier(((_15_MultiKeyring).Dtor_childKeyrings()).UniqueElements(), true, func(_forall_var_0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) bool {
				var _17_c m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
				_17_c = interface{}(_forall_var_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
				return !(_dafny.Companion_Sequence_.Contains((_15_MultiKeyring).Dtor_childKeyrings(), _17_c)) || (Companion_Default___.Keyring_q(_17_c))
			})), _dafny.SeqOfString("CMMs not supported by Multi Keyrings"))
			_ = _16_valueOrError1
			if (_16_valueOrError1).IsFailure() {
				return (_16_valueOrError1).PropagateFailure()
			} else {
				var _source1 _dafny.Int = outputVersion
				_ = _source1
				{
					if (_source1).Cmp(_dafny.IntOfInt64(3)) == 0 {
						var _18_valueOrError2 m_Wrappers.Result = (func() m_Wrappers.Result {
							if ((_15_MultiKeyring).Dtor_generator()).Is_Some() {
								return func(_pat_let2_0 m_Wrappers.Result) m_Wrappers.Result {
									return func(_19_valueOrError3 m_Wrappers.Result) m_Wrappers.Result {
										return (func() m_Wrappers.Result {
											if (_19_valueOrError3).IsFailure() {
												return (_19_valueOrError3).PropagateFailure()
											}
											return func(_pat_let3_0 m_JSON_Values.JSON) m_Wrappers.Result {
												return func(_20_g m_JSON_Values.JSON) m_Wrappers.Result {
													return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(_20_g))
												}(_pat_let3_0)
											}((_19_valueOrError3).Extract().(m_JSON_Values.JSON))
										})()
									}(_pat_let2_0)
								}(Companion_Default___.ToJson(((_15_MultiKeyring).Dtor_generator()).Dtor_value().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription), outputVersion))
							}
							return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
						})()
						_ = _18_valueOrError2
						if (_18_valueOrError2).IsFailure() {
							return (_18_valueOrError2).PropagateFailure()
						} else {
							var _21_generator m_Wrappers.Option = (_18_valueOrError2).Extract().(m_Wrappers.Option)
							_ = _21_generator
							var _22_valueOrError4 m_Wrappers.Result = Companion_Default___.KeyDescriptionListToJson((_15_MultiKeyring).Dtor_childKeyrings(), outputVersion)
							_ = _22_valueOrError4
							if (_22_valueOrError4).IsFailure() {
								return (_22_valueOrError4).PropagateFailure()
							} else {
								var _23_childKeyrings _dafny.Sequence = (_22_valueOrError4).Extract().(_dafny.Sequence)
								_ = _23_childKeyrings
								return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("multi-keyring"))), _dafny.TupleOf(_dafny.SeqOfString("childKeyrings"), m_JSON_Values.Companion_JSON_.Create_Array_(_23_childKeyrings))), (func() _dafny.Sequence {
									if (_21_generator).Is_Some() {
										return _dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("generator"), (_21_generator).Dtor_value().(m_JSON_Values.JSON)))
									}
									return _dafny.SeqOf()
								})())))
							}
						}
					}
				}
				{
					var _24_valueOrError5 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(((_15_MultiKeyring).Dtor_generator()).Is_Some(), _dafny.SeqOfString("Generator required for v1 or v2"))
					_ = _24_valueOrError5
					if (_24_valueOrError5).IsFailure() {
						return (_24_valueOrError5).PropagateFailure()
					} else {
						var _25_keyrings _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(((_15_MultiKeyring).Dtor_generator()).Dtor_value().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)), (_15_MultiKeyring).Dtor_childKeyrings())
						_ = _25_keyrings
						var _26_valueOrError6 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier((_25_keyrings).UniqueElements(), true, func(_forall_var_1 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) bool {
							var _27_c m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
							_27_c = interface{}(_forall_var_1).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
							return !(_dafny.Companion_Sequence_.Contains(_25_keyrings, _27_c)) || (!((_27_c).Is_Multi()))
						}), _dafny.SeqOfString("Recursive structures not supported"))
						_ = _26_valueOrError6
						if (_26_valueOrError6).IsFailure() {
							return (_26_valueOrError6).PropagateFailure()
						} else {
							var _28_valueOrError7 m_Wrappers.Result = Companion_Default___.KeyDescriptionListToJson((_15_MultiKeyring).Dtor_childKeyrings(), outputVersion)
							_ = _28_valueOrError7
							if (_28_valueOrError7).IsFailure() {
								return (_28_valueOrError7).PropagateFailure()
							} else {
								var _29_keyrings _dafny.Sequence = (_28_valueOrError7).Extract().(_dafny.Sequence)
								_ = _29_keyrings
								return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Array_(_29_keyrings))
							}
						}
					}
				}
			}
		}
	}
	{
		var _30_RequiredEncryptionContext m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RequiredEncryptionContext).RequiredEncryptionContext
		_ = _30_RequiredEncryptionContext
		var _31_valueOrError8 m_Wrappers.Result = Companion_Default___.ToJson((_30_RequiredEncryptionContext).Dtor_underlying(), outputVersion)
		_ = _31_valueOrError8
		if (_31_valueOrError8).IsFailure() {
			return (_31_valueOrError8).PropagateFailure()
		} else {
			var _32_underlying m_JSON_Values.JSON = (_31_valueOrError8).Extract().(m_JSON_Values.JSON)
			_ = _32_underlying
			var _33_valueOrError9 m_Wrappers.Result = m_Seq.Companion_Default___.MapWithResult(func(coer8 func(_dafny.Sequence) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
				return func(arg8 interface{}) m_Wrappers.Result {
					return coer8(arg8.(_dafny.Sequence))
				}
			}(func(_34_key _dafny.Sequence) m_Wrappers.Result {
				return func(_pat_let4_0 m_Wrappers.Result) m_Wrappers.Result {
					return func(_35_valueOrError10 m_Wrappers.Result) m_Wrappers.Result {
						return (func() m_Wrappers.Result {
							if (_35_valueOrError10).IsFailure() {
								return (_35_valueOrError10).PropagateFailure()
							}
							return func(_pat_let5_0 _dafny.Sequence) m_Wrappers.Result {
								return func(_36_s _dafny.Sequence) m_Wrappers.Result {
									return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_String_(_36_s))
								}(_pat_let5_0)
							}((_35_valueOrError10).Extract().(_dafny.Sequence))
						})()
					}(_pat_let4_0)
				}(m_UTF8.Decode(_34_key))
			}), (_30_RequiredEncryptionContext).Dtor_requiredEncryptionContextKeys())
			_ = _33_valueOrError9
			if (_33_valueOrError9).IsFailure() {
				return (_33_valueOrError9).PropagateFailure()
			} else {
				var _37_requiredEncryptionContextKeys _dafny.Sequence = (_33_valueOrError9).Extract().(_dafny.Sequence)
				_ = _37_requiredEncryptionContextKeys
				return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Values.Companion_JSON_.Create_Object_(_dafny.SeqOf(_dafny.TupleOf(_dafny.SeqOfString("type"), m_JSON_Values.Companion_JSON_.Create_String_(_dafny.SeqOfString("required-encryption-context-cmm"))), _dafny.TupleOf(_dafny.SeqOfString("underlying"), _32_underlying), _dafny.TupleOf(_dafny.SeqOfString("requiredEncryptionContextKeys"), m_JSON_Values.Companion_JSON_.Create_Array_(_37_requiredEncryptionContextKeys)))))
			}
		}
	}
}
func (_static *CompanionStruct_Default___) Keyring_q(description m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) bool {
	return (((((((((((description).Is_Kms()) || ((description).Is_KmsMrk())) || ((description).Is_KmsMrkDiscovery())) || ((description).Is_RSA())) || ((description).Is_AES())) || ((description).Is_ECDH())) || ((description).Is_Static())) || ((description).Is_KmsRsa())) || ((description).Is_KmsECDH())) || ((description).Is_Hierarchy())) || ((description).Is_Multi())
}
func (_static *CompanionStruct_Default___) KeyDescriptionListToJson(childKeyrings _dafny.Sequence, outputVersion _dafny.Int) m_Wrappers.Result {
	if (_dafny.IntOfUint32((childKeyrings).Cardinality())).Sign() == 0 {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf())
	} else {
		var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.ToJson((childKeyrings).Select(0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription), outputVersion)
		_ = _0_valueOrError0
		if (_0_valueOrError0).IsFailure() {
			return (_0_valueOrError0).PropagateFailure()
		} else {
			var _1_json m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
			_ = _1_json
			var _2_valueOrError1 m_Wrappers.Result = Companion_Default___.KeyDescriptionListToJson((childKeyrings).Drop(1), outputVersion)
			_ = _2_valueOrError1
			if (_2_valueOrError1).IsFailure() {
				return (_2_valueOrError1).PropagateFailure()
			} else {
				var _3_rest _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
				_ = _3_rest
				return m_Wrappers.Companion_Result_.Create_Success_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_1_json), _3_rest))
			}
		}
	}
}
func (_static *CompanionStruct_Default___) Invert(m _dafny.Map) _dafny.Map {
	return func() _dafny.Map {
		var _coll0 = _dafny.NewMapBuilder()
		_ = _coll0
		for _iter5 := _dafny.Iterate((m).Keys().Elements()); ; {
			_compr_0, _ok5 := _iter5()
			if !_ok5 {
				break
			}
			var _0_k interface{}
			_0_k = interface{}(_compr_0).(interface{})
			if (m).Contains(_0_k) {
				_coll0.Add((m).Get(_0_k).(interface{}), _0_k)
			}
		}
		return _coll0.ToMap()
	}()
}
func (_static *CompanionStruct_Default___) KmsKey2EccAlgorithmSpec() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString("us-west-2-256-ecc"), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()).UpdateUnsafe(_dafny.SeqOfString("us-west-2-384-ecc"), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_()).UpdateUnsafe(_dafny.SeqOfString("us-west-2-521-ecc"), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_())
}
func (_static *CompanionStruct_Default___) EncryptionAlgorithmSpec2String() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_ComAmazonawsKmsTypes.Companion_EncryptionAlgorithmSpec_.Create_RSAES__OAEP__SHA__1_(), _dafny.SeqOfString("RSAES_OAEP_SHA_1")).UpdateUnsafe(m_ComAmazonawsKmsTypes.Companion_EncryptionAlgorithmSpec_.Create_RSAES__OAEP__SHA__256_(), _dafny.SeqOfString("RSAES_OAEP_SHA_256"))
}
func (_static *CompanionStruct_Default___) String2EncryptionAlgorithmSpec() _dafny.Map {
	return Companion_Default___.Invert(Companion_Default___.EncryptionAlgorithmSpec2String())
}
func (_static *CompanionStruct_Default___) PaddingAlgorithmString2String() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_PaddingScheme_.Create_PKCS1_(), _dafny.TupleOf(_dafny.SeqOfString("pkcs1"), _dafny.SeqOfString("sha1"))).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_PaddingScheme_.Create_OAEP__SHA1__MGF1_(), _dafny.TupleOf(_dafny.SeqOfString("oaep-mgf1"), _dafny.SeqOfString("sha1"))).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_PaddingScheme_.Create_OAEP__SHA256__MGF1_(), _dafny.TupleOf(_dafny.SeqOfString("oaep-mgf1"), _dafny.SeqOfString("sha256"))).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_PaddingScheme_.Create_OAEP__SHA384__MGF1_(), _dafny.TupleOf(_dafny.SeqOfString("oaep-mgf1"), _dafny.SeqOfString("sha384"))).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_PaddingScheme_.Create_OAEP__SHA512__MGF1_(), _dafny.TupleOf(_dafny.SeqOfString("oaep-mgf1"), _dafny.SeqOfString("sha512")))
}
func (_static *CompanionStruct_Default___) String2PaddingAlgorithm() _dafny.Map {
	return Companion_Default___.Invert(Companion_Default___.PaddingAlgorithmString2String())
}
func (_static *CompanionStruct_Default___) EccAlgorithmSpec2string() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_(), _dafny.SeqOfString("secp256r1")).UpdateUnsafe(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_(), _dafny.SeqOfString("secp384r1")).UpdateUnsafe(m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_(), _dafny.SeqOfString("secp521r1"))
}
func (_static *CompanionStruct_Default___) String2EccAlgorithmSpec() _dafny.Map {
	return Companion_Default___.Invert(Companion_Default___.EccAlgorithmSpec2string())
}
func (_static *CompanionStruct_Default___) Curve2EccAlgorithmSpec() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString("ecc-256"), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P256_()).UpdateUnsafe(_dafny.SeqOfString("ecc-384"), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P384_()).UpdateUnsafe(_dafny.SeqOfString("ecc-521"), m_AwsCryptographyPrimitivesTypes.Companion_ECDHCurveSpec_.Create_ECC__NIST__P521_())
}
func (_static *CompanionStruct_Default___) EccAlgorithmSpec2Spec() _dafny.Map {
	return Companion_Default___.Invert(Companion_Default___.Curve2EccAlgorithmSpec())
}

// End of class Default__

// Definition of class KeyDescriptionVersion
type KeyDescriptionVersion struct {
}

func New_KeyDescriptionVersion_() *KeyDescriptionVersion {
	_this := KeyDescriptionVersion{}

	return &_this
}

type CompanionStruct_KeyDescriptionVersion_ struct {
}

var Companion_KeyDescriptionVersion_ = CompanionStruct_KeyDescriptionVersion_{}

func (*KeyDescriptionVersion) String() string {
	return "KeyDescription.KeyDescriptionVersion"
}
func (_this *CompanionStruct_KeyDescriptionVersion_) Witness() _dafny.Int {
	return _dafny.One
}

// End of class KeyDescriptionVersion

func Type_KeyDescriptionVersion_() _dafny.TypeDescriptor {
	return type_KeyDescriptionVersion_{}
}

type type_KeyDescriptionVersion_ struct {
}

func (_this type_KeyDescriptionVersion_) Default() interface{} {
	return Companion_KeyDescriptionVersion_.Witness()
}

func (_this type_KeyDescriptionVersion_) String() string {
	return "KeyDescription.KeyDescriptionVersion"
}
func (_this *CompanionStruct_KeyDescriptionVersion_) Is_(__source _dafny.Int) bool {
	var _0_v _dafny.Int = (__source)
	_ = _0_v
	return Companion_Default___.KeyDescriptionVersion_q(_0_v)
}
