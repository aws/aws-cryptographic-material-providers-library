// Package KeyringFromKeyDescription
// Dafny module KeyringFromKeyDescription compiled into Go

package KeyringFromKeyDescription

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
	m_CreateStaticKeyStores "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyStores"
	m_CreateStaticKeyrings "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyrings"
	m_JSONHelpers "github.com/aws/aws-cryptographic-material-providers-library/testvectors/JSONHelpers"
	m_KeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyDescription"
	m_KeyMaterial "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyMaterial"
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
var _ m_KeyDescription.Dummy__
var _ m_KeyMaterial.Dummy__
var _ m_CreateStaticKeyrings.Dummy__
var _ m_CreateStaticKeyStores.Dummy__

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
	return "KeyringFromKeyDescription.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) GetKeyId(input m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) _dafny.Sequence {
	goto TAIL_CALL_START
TAIL_CALL_START:
	var _source0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = input
	_ = _source0
	{
		if _source0.Is_Kms() {
			var _0_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Kms).Kms
			_ = _0_i
			return (_0_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_KmsMrk() {
			var _1_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrk).KmsMrk
			_ = _1_i
			return (_1_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_KmsMrkDiscovery() {
			var _2_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrkDiscovery).KmsMrkDiscovery
			_ = _2_i
			return (_2_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_RSA() {
			var _3_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RSA).RSA
			_ = _3_i
			return (_3_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_AES() {
			var _4_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_AES).AES
			_ = _4_i
			return (_4_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_ECDH() {
			var _5_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH).ECDH
			_ = _5_i
			return (_5_i).Dtor_senderKeyId()
		}
	}
	{
		if _source0.Is_KmsECDH() {
			var _6_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsECDH).KmsECDH
			_ = _6_i
			return (_6_i).Dtor_senderKeyId()
		}
	}
	{
		if _source0.Is_Static() {
			var _7_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static).Static
			_ = _7_i
			return (_7_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_Hierarchy() {
			var _8_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Hierarchy).Hierarchy
			_ = _8_i
			return (_8_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_KmsRsa() {
			var _9_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsRsa).KmsRsa
			_ = _9_i
			return (_9_i).Dtor_keyId()
		}
	}
	{
		if _source0.Is_RequiredEncryptionContext() {
			var _10_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RequiredEncryptionContext).RequiredEncryptionContext
			_ = _10_i
			var _in0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_10_i).Dtor_underlying()
			_ = _in0
			input = _in0
			goto TAIL_CALL_START
		}
	}
	{
		return _dafny.SeqOfString("")
	}
}
func (_static *CompanionStruct_Default___) GetSenderKeyId(input m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) _dafny.Sequence {
	var _source0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = input
	_ = _source0
	{
		if _source0.Is_ECDH() {
			var _0_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH).ECDH
			_ = _0_i
			return (_0_i).Dtor_senderKeyId()
		}
	}
	{
		return _dafny.SeqOfString("")
	}
}
func (_static *CompanionStruct_Default___) GetRecipientKeyId(input m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) _dafny.Sequence {
	var _source0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = input
	_ = _source0
	{
		if _source0.Is_ECDH() {
			var _0_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH).ECDH
			_ = _0_i
			return (_0_i).Dtor_recipientKeyId()
		}
	}
	{
		if _source0.Is_KmsECDH() {
			var _1_i m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsECDH).KmsECDH
			_ = _1_i
			return (_1_i).Dtor_recipientKeyId()
		}
	}
	{
		return _dafny.SeqOfString("")
	}
}
func (_static *CompanionStruct_Default___) GetKeyMaterial(keys _dafny.Map, keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) m_Wrappers.Option {
	var _0_keyId _dafny.Sequence = Companion_Default___.GetKeyId(keyDescription)
	_ = _0_keyId
	if (keys).Contains(_0_keyId) {
		return m_Wrappers.Companion_Option_.Create_Some_((keys).Get(_0_keyId).(m_KeyMaterial.KeyMaterial))
	} else {
		return m_Wrappers.Companion_Option_.Create_None_()
	}
}
func (_static *CompanionStruct_Default___) GetSenderKeyMaterial(keys _dafny.Map, keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) m_Wrappers.Option {
	var _0_keyId _dafny.Sequence = Companion_Default___.GetSenderKeyId(keyDescription)
	_ = _0_keyId
	if (keys).Contains(_0_keyId) {
		return m_Wrappers.Companion_Option_.Create_Some_((keys).Get(_0_keyId).(m_KeyMaterial.KeyMaterial))
	} else {
		return m_Wrappers.Companion_Option_.Create_None_()
	}
}
func (_static *CompanionStruct_Default___) GetRecipientKeyMaterial(keys _dafny.Map, keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) m_Wrappers.Option {
	var _0_keyId _dafny.Sequence = Companion_Default___.GetRecipientKeyId(keyDescription)
	_ = _0_keyId
	if (keys).Contains(_0_keyId) {
		return m_Wrappers.Companion_Option_.Create_Some_((keys).Get(_0_keyId).(m_KeyMaterial.KeyMaterial))
	} else {
		return m_Wrappers.Companion_Option_.Create_None_()
	}
}
func (_static *CompanionStruct_Default___) ToKeyring(mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient, keys _dafny.Map, description m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_material m_Wrappers.Option
	_ = _0_material
	_0_material = Companion_Default___.GetKeyMaterial(keys, description)
	var _source0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = description
	_ = _source0
	{
		{
			if _source0.Is_Static() {
				var Static0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static).Static
				_ = Static0
				var _1_key _dafny.Sequence = Static0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring).KeyId
				_ = _1_key
				{
					var _2_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _2_valueOrError0
					_2_valueOrError0 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_StaticMaterial()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: StaticMaterial")))
					if (_2_valueOrError0).IsFailure() {
						output = (_2_valueOrError0).PropagateFailure()
						return output
					}
					var _3_encrypt m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
					_ = _3_encrypt
					_3_encrypt = m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptionMaterials_.Create_EncryptionMaterials_(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_algorithmSuite(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_encryptionContext(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_encryptedDataKeys(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_requiredEncryptionContextKeys(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_plaintextDataKey(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_signingKey(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_symmetricSigningKeys())
					var _4_decrypt m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
					_ = _4_decrypt
					_4_decrypt = m_AwsCryptographyMaterialProvidersTypes.Companion_DecryptionMaterials_.Create_DecryptionMaterials_(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_algorithmSuite(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_encryptionContext(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_requiredEncryptionContextKeys(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_plaintextDataKey(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_verificationKey(), m_Wrappers.Companion_Option_.Create_None_())
					var _5_keyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
					_ = _5_keyring
					var _out0 m_AwsCryptographyMaterialProvidersTypes.IKeyring
					_ = _out0
					_out0 = m_CreateStaticKeyrings.Companion_Default___.CreateStaticMaterialsKeyring(_3_encrypt, _4_decrypt)
					_5_keyring = _out0
					output = m_Wrappers.Companion_Result_.Create_Success_(_5_keyring)
					return output
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_Kms() {
				var Kms0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Kms).Kms
				_ = Kms0
				var _6_key _dafny.Sequence = Kms0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo_KMSInfo).KeyId
				_ = _6_key
				{
					var _7_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _7_valueOrError1
					_7_valueOrError1 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_KMS()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: KMS")))
					if (_7_valueOrError1).IsFailure() {
						output = (_7_valueOrError1).PropagateFailure()
						return output
					}
					var _8_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _8_valueOrError2
					var _out1 m_Wrappers.Result
					_ = _out1
					_out1 = Companion_Default___.GetKmsClient(mpl, ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier())
					_8_valueOrError2 = _out1
					if (_8_valueOrError2).IsFailure() {
						output = (_8_valueOrError2).PropagateFailure()
						return output
					}
					var _9_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
					_ = _9_kmsClient
					_9_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_8_valueOrError2).Extract())
					var _10_input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput
					_ = _10_input
					_10_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsKeyringInput_.Create_CreateAwsKmsKeyringInput_(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier(), _9_kmsClient, m_Wrappers.Companion_Option_.Create_None_())
					var _11_keyring m_Wrappers.Result
					_ = _11_keyring
					var _out2 m_Wrappers.Result
					_ = _out2
					_out2 = (mpl).CreateAwsKmsKeyring(_10_input)
					_11_keyring = _out2
					output = (_11_keyring).MapFailure(func(coer12 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
						return func(arg12 interface{}) interface{} {
							return coer12(arg12.(m_AwsCryptographyMaterialProvidersTypes.Error))
						}
					}(func(_12_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
						return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_12_e)
					}))
					return output
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_KmsMrk() {
				var KmsMrk0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrk).KmsMrk
				_ = KmsMrk0
				var _13_key _dafny.Sequence = KmsMrk0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware_KmsMrkAware).KeyId
				_ = _13_key
				{
					var _14_valueOrError3 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _14_valueOrError3
					_14_valueOrError3 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_KMS()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: KMS")))
					if (_14_valueOrError3).IsFailure() {
						output = (_14_valueOrError3).PropagateFailure()
						return output
					}
					var _15_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _15_valueOrError4
					var _out3 m_Wrappers.Result
					_ = _out3
					_out3 = Companion_Default___.GetKmsClient(mpl, ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier())
					_15_valueOrError4 = _out3
					if (_15_valueOrError4).IsFailure() {
						output = (_15_valueOrError4).PropagateFailure()
						return output
					}
					var _16_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
					_ = _16_kmsClient
					_16_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_15_valueOrError4).Extract())
					var _17_input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput
					_ = _17_input
					_17_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsMrkKeyringInput_.Create_CreateAwsKmsMrkKeyringInput_(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier(), _16_kmsClient, m_Wrappers.Companion_Option_.Create_None_())
					var _18_keyring m_Wrappers.Result
					_ = _18_keyring
					var _out4 m_Wrappers.Result
					_ = _out4
					_out4 = (mpl).CreateAwsKmsMrkKeyring(_17_input)
					_18_keyring = _out4
					output = (_18_keyring).MapFailure(func(coer13 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
						return func(arg13 interface{}) interface{} {
							return coer13(arg13.(m_AwsCryptographyMaterialProvidersTypes.Error))
						}
					}(func(_19_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
						return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_19_e)
					}))
					return output
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_KmsRsa() {
				var KmsRsa0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsRsa).KmsRsa
				_ = KmsRsa0
				var _20_key _dafny.Sequence = KmsRsa0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring_KmsRsaKeyring).KeyId
				_ = _20_key
				var _21_encryptionAlgorithm m_ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = KmsRsa0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring_KmsRsaKeyring).EncryptionAlgorithm
				_ = _21_encryptionAlgorithm
				{
					var _22_valueOrError5 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _22_valueOrError5
					_22_valueOrError5 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_KMSAsymetric()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: KMSAsymetric")))
					if (_22_valueOrError5).IsFailure() {
						output = (_22_valueOrError5).PropagateFailure()
						return output
					}
					var _23_valueOrError6 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _23_valueOrError6
					var _out5 m_Wrappers.Result
					_ = _out5
					_out5 = Companion_Default___.GetKmsClient(mpl, ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier())
					_23_valueOrError6 = _out5
					if (_23_valueOrError6).IsFailure() {
						output = (_23_valueOrError6).PropagateFailure()
						return output
					}
					var _24_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
					_ = _24_kmsClient
					_24_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_23_valueOrError6).Extract())
					var _25_input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput
					_ = _25_input
					_25_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsRsaKeyringInput_.Create_CreateAwsKmsRsaKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_publicKey()), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier(), _21_encryptionAlgorithm, m_Wrappers.Companion_Option_.Create_Some_(_24_kmsClient), m_Wrappers.Companion_Option_.Create_None_())
					var _26_keyring m_Wrappers.Result
					_ = _26_keyring
					var _out6 m_Wrappers.Result
					_ = _out6
					_out6 = (mpl).CreateAwsKmsRsaKeyring(_25_input)
					_26_keyring = _out6
					output = (_26_keyring).MapFailure(func(coer14 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
						return func(arg14 interface{}) interface{} {
							return coer14(arg14.(m_AwsCryptographyMaterialProvidersTypes.Error))
						}
					}(func(_27_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
						return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_27_e)
					}))
					return output
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_Hierarchy() {
				var Hierarchy0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Hierarchy).Hierarchy
				_ = Hierarchy0
				var _28_key _dafny.Sequence = Hierarchy0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring_HierarchyKeyring).KeyId
				_ = _28_key
				{
					var _29_valueOrError7 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _29_valueOrError7
					_29_valueOrError7 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_StaticKeyStoreInformation()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: StaticKeyStoreInformation")))
					if (_29_valueOrError7).IsFailure() {
						output = (_29_valueOrError7).PropagateFailure()
						return output
					}
					var _30_keyStore m_AwsCryptographyKeyStoreTypes.IKeyStoreClient
					_ = _30_keyStore
					var _out7 m_AwsCryptographyKeyStoreTypes.IKeyStoreClient
					_ = _out7
					_out7 = m_CreateStaticKeyStores.Companion_Default___.CreateStaticKeyStore((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial))
					_30_keyStore = _out7
					var _31_input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput
					_ = _31_input
					_31_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsHierarchicalKeyringInput_.Create_CreateAwsKmsHierarchicalKeyringInput_(m_Wrappers.Companion_Option_.Create_Some_(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier()), m_Wrappers.Companion_Option_.Create_None_(), _30_keyStore, int64(11), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
					var _32_keyring m_Wrappers.Result
					_ = _32_keyring
					var _out8 m_Wrappers.Result
					_ = _out8
					_out8 = (mpl).CreateAwsKmsHierarchicalKeyring(_31_input)
					_32_keyring = _out8
					output = (_32_keyring).MapFailure(func(coer15 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
						return func(arg15 interface{}) interface{} {
							return coer15(arg15.(m_AwsCryptographyMaterialProvidersTypes.Error))
						}
					}(func(_33_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
						return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_33_e)
					}))
					return output
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_KmsMrkDiscovery() {
				var KmsMrkDiscovery0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrkDiscovery).KmsMrkDiscovery
				_ = KmsMrkDiscovery0
				var _34_defaultMrkRegion _dafny.Sequence = KmsMrkDiscovery0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery).DefaultMrkRegion
				_ = _34_defaultMrkRegion
				var _35_awsKmsDiscoveryFilter m_Wrappers.Option = KmsMrkDiscovery0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery).AwsKmsDiscoveryFilter
				_ = _35_awsKmsDiscoveryFilter
				{
					var _36_valueOrError8 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _36_valueOrError8
					_36_valueOrError8 = m_Wrappers.Companion_Default___.Need((_0_material).Is_None(), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Discovery has not key")))
					if (_36_valueOrError8).IsFailure() {
						output = (_36_valueOrError8).PropagateFailure()
						return output
					}
					var _37_input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput
					_ = _37_input
					_37_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsMrkDiscoveryMultiKeyringInput_.Create_CreateAwsKmsMrkDiscoveryMultiKeyringInput_(_dafny.SeqOf(_34_defaultMrkRegion), _35_awsKmsDiscoveryFilter, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
					var _38_keyring m_Wrappers.Result
					_ = _38_keyring
					var _out9 m_Wrappers.Result
					_ = _out9
					_out9 = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(_37_input)
					_38_keyring = _out9
					output = (_38_keyring).MapFailure(func(coer16 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
						return func(arg16 interface{}) interface{} {
							return coer16(arg16.(m_AwsCryptographyMaterialProvidersTypes.Error))
						}
					}(func(_39_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
						return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_39_e)
					}))
					return output
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_AES() {
				var AES0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_AES).AES
				_ = AES0
				var _40_key _dafny.Sequence = AES0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES_RawAES).KeyId
				_ = _40_key
				var _41_providerId _dafny.Sequence = AES0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES_RawAES).ProviderId
				_ = _41_providerId
				{
					var _42_valueOrError9 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _42_valueOrError9
					_42_valueOrError9 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_Symetric()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: Symmetric")))
					if (_42_valueOrError9).IsFailure() {
						output = (_42_valueOrError9).PropagateFailure()
						return output
					}
					var _43_valueOrError10 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Default())
					_ = _43_valueOrError10
					var _source1 _dafny.Int = ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_bits()
					_ = _source1
					{
						{
							if (_source1).Cmp(_dafny.IntOfInt64(128)) == 0 {
								_43_valueOrError10 = m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES128__GCM__IV12__TAG16_())
								goto Lmatch1
							}
						}
						{
							if (_source1).Cmp(_dafny.IntOfInt64(192)) == 0 {
								_43_valueOrError10 = m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES192__GCM__IV12__TAG16_())
								goto Lmatch1
							}
						}
						{
							if (_source1).Cmp(_dafny.IntOfInt64(256)) == 0 {
								_43_valueOrError10 = m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_AesWrappingAlg_.Create_ALG__AES256__GCM__IV12__TAG16_())
								goto Lmatch1
							}
						}
						{
							_43_valueOrError10 = m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not a supported bit length")))
						}
						goto Lmatch1
					}
				Lmatch1:
					if (_43_valueOrError10).IsFailure() {
						output = (_43_valueOrError10).PropagateFailure()
						return output
					}
					var _44_wrappingAlg m_AwsCryptographyMaterialProvidersTypes.AesWrappingAlg
					_ = _44_wrappingAlg
					_44_wrappingAlg = (_43_valueOrError10).Extract().(m_AwsCryptographyMaterialProvidersTypes.AesWrappingAlg)
					var _45_input m_AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput
					_ = _45_input
					_45_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawAesKeyringInput_.Create_CreateRawAesKeyringInput_(_41_providerId, ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_keyIdentifier(), ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_wrappingKey(), _44_wrappingAlg)
					var _46_keyring m_Wrappers.Result
					_ = _46_keyring
					var _out10 m_Wrappers.Result
					_ = _out10
					_out10 = (mpl).CreateRawAesKeyring(_45_input)
					_46_keyring = _out10
					output = (_46_keyring).MapFailure(func(coer17 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
						return func(arg17 interface{}) interface{} {
							return coer17(arg17.(m_AwsCryptographyMaterialProvidersTypes.Error))
						}
					}(func(_47_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
						return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_47_e)
					}))
					return output
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_RSA() {
				var RSA0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RSA).RSA
				_ = RSA0
				var _48_key _dafny.Sequence = RSA0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA_RawRSA).KeyId
				_ = _48_key
				var _49_providerId _dafny.Sequence = RSA0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA_RawRSA).ProviderId
				_ = _49_providerId
				var _50_padding m_AwsCryptographyMaterialProvidersTypes.PaddingScheme = RSA0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA_RawRSA).Padding
				_ = _50_padding
				{
					var _51_valueOrError11 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _51_valueOrError11
					_51_valueOrError11 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && ((((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_PrivateRSA()) || (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_PublicRSA())), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: PrivateRSA or PublicRSA")))
					if (_51_valueOrError11).IsFailure() {
						output = (_51_valueOrError11).PropagateFailure()
						return output
					}
					var _source2 m_Wrappers.Option = _0_material
					_ = _source2
					{
						{
							if _source2.Is_Some() {
								var value0 m_KeyMaterial.KeyMaterial = _source2.Get_().(m_Wrappers.Option_Some).Value.(m_KeyMaterial.KeyMaterial)
								_ = value0
								if value0.Is_PrivateRSA() {
									var _52_decrypt bool = value0.Get_().(m_KeyMaterial.KeyMaterial_PrivateRSA).Decrypt
									_ = _52_decrypt
									var _53_material _dafny.Sequence = value0.Get_().(m_KeyMaterial.KeyMaterial_PrivateRSA).Material
									_ = _53_material
									var _54_keyIdentifier _dafny.Sequence = value0.Get_().(m_KeyMaterial.KeyMaterial_PrivateRSA).KeyIdentifier
									_ = _54_keyIdentifier
									{
										var _55_valueOrError12 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
										_ = _55_valueOrError12
										_55_valueOrError12 = m_Wrappers.Companion_Default___.Need(_52_decrypt, m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Private RSA keys only supports decrypt.")))
										if (_55_valueOrError12).IsFailure() {
											output = (_55_valueOrError12).PropagateFailure()
											return output
										}
										var _56_valueOrError13 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
										_ = _56_valueOrError13
										_56_valueOrError13 = (m_UTF8.Encode(_53_material)).MapFailure(func(coer18 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
											return func(arg18 interface{}) interface{} {
												return coer18(arg18.(_dafny.Sequence))
											}
										}(func(_57_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
											return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_57_e)
										}))
										if (_56_valueOrError13).IsFailure() {
											output = (_56_valueOrError13).PropagateFailure()
											return output
										}
										var _58_privateKeyPemBytes _dafny.Sequence
										_ = _58_privateKeyPemBytes
										_58_privateKeyPemBytes = (_56_valueOrError13).Extract().(_dafny.Sequence)
										var _59_input m_AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
										_ = _59_input
										_59_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawRsaKeyringInput_.Create_CreateRawRsaKeyringInput_(_49_providerId, _54_keyIdentifier, _50_padding, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_58_privateKeyPemBytes))
										var _60_keyring m_Wrappers.Result
										_ = _60_keyring
										var _out11 m_Wrappers.Result
										_ = _out11
										_out11 = (mpl).CreateRawRsaKeyring(_59_input)
										_60_keyring = _out11
										output = (_60_keyring).MapFailure(func(coer19 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
											return func(arg19 interface{}) interface{} {
												return coer19(arg19.(m_AwsCryptographyMaterialProvidersTypes.Error))
											}
										}(func(_61_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
											return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_61_e)
										}))
										return output
									}
									goto Lmatch2
								}
							}
						}
						{
							var value1 m_KeyMaterial.KeyMaterial = _source2.Get_().(m_Wrappers.Option_Some).Value.(m_KeyMaterial.KeyMaterial)
							_ = value1
							var _62_encrypt bool = value1.Get_().(m_KeyMaterial.KeyMaterial_PublicRSA).Encrypt
							_ = _62_encrypt
							var _63_material _dafny.Sequence = value1.Get_().(m_KeyMaterial.KeyMaterial_PublicRSA).Material
							_ = _63_material
							var _64_keyIdentifier _dafny.Sequence = value1.Get_().(m_KeyMaterial.KeyMaterial_PublicRSA).KeyIdentifier
							_ = _64_keyIdentifier
							{
								var _65_valueOrError14 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
								_ = _65_valueOrError14
								_65_valueOrError14 = m_Wrappers.Companion_Default___.Need(_62_encrypt, m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Public RSA keys only supports encrypt.")))
								if (_65_valueOrError14).IsFailure() {
									output = (_65_valueOrError14).PropagateFailure()
									return output
								}
								var _66_valueOrError15 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
								_ = _66_valueOrError15
								_66_valueOrError15 = (m_UTF8.Encode(_63_material)).MapFailure(func(coer20 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
									return func(arg20 interface{}) interface{} {
										return coer20(arg20.(_dafny.Sequence))
									}
								}(func(_67_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
									return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_67_e)
								}))
								if (_66_valueOrError15).IsFailure() {
									output = (_66_valueOrError15).PropagateFailure()
									return output
								}
								var _68_publicKeyPemBytes _dafny.Sequence
								_ = _68_publicKeyPemBytes
								_68_publicKeyPemBytes = (_66_valueOrError15).Extract().(_dafny.Sequence)
								var _69_input m_AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
								_ = _69_input
								_69_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawRsaKeyringInput_.Create_CreateRawRsaKeyringInput_(_49_providerId, _64_keyIdentifier, _50_padding, m_Wrappers.Companion_Option_.Create_Some_(_68_publicKeyPemBytes), m_Wrappers.Companion_Option_.Create_None_())
								var _70_keyring m_Wrappers.Result
								_ = _70_keyring
								var _out12 m_Wrappers.Result
								_ = _out12
								_out12 = (mpl).CreateRawRsaKeyring(_69_input)
								_70_keyring = _out12
								output = (_70_keyring).MapFailure(func(coer21 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
									return func(arg21 interface{}) interface{} {
										return coer21(arg21.(m_AwsCryptographyMaterialProvidersTypes.Error))
									}
								}(func(_71_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
									return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_71_e)
								}))
								return output
							}
						}
						goto Lmatch2
					}
				Lmatch2:
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_ECDH() {
				var ECDH0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH).ECDH
				_ = ECDH0
				var _72_senderKeyId _dafny.Sequence = ECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh).SenderKeyId
				_ = _72_senderKeyId
				var _73_recipientKeyId _dafny.Sequence = ECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh).RecipientKeyId
				_ = _73_recipientKeyId
				var _74_senderPublicKey _dafny.Sequence = ECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh).SenderPublicKey
				_ = _74_senderPublicKey
				var _75_recipientPublicKey _dafny.Sequence = ECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh).RecipientPublicKey
				_ = _75_recipientPublicKey
				var _76_providerId _dafny.Sequence = ECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh).ProviderId
				_ = _76_providerId
				var _77_curveSpec _dafny.Sequence = ECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh).CurveSpec
				_ = _77_curveSpec
				var _78_keyAgreementScheme _dafny.Sequence = ECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh).KeyAgreementScheme
				_ = _78_keyAgreementScheme
				{
					var _79_valueOrError16 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _79_valueOrError16
					_79_valueOrError16 = m_Wrappers.Companion_Default___.Need((m_KeyDescription.Companion_Default___.Curve2EccAlgorithmSpec()).Contains(_77_curveSpec), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Unknown curve spec")))
					if (_79_valueOrError16).IsFailure() {
						output = (_79_valueOrError16).PropagateFailure()
						return output
					}
					var _80_curveType m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
					_ = _80_curveType
					_80_curveType = (m_KeyDescription.Companion_Default___.Curve2EccAlgorithmSpec()).Get(_77_curveSpec).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
					var _81_primitives_q m_Wrappers.Result
					_ = _81_primitives_q
					var _out13 m_Wrappers.Result
					_ = _out13
					_out13 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
					_81_primitives_q = _out13
					var _82_valueOrError17 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _82_valueOrError17
					_82_valueOrError17 = (_81_primitives_q).MapFailure(func(coer22 func(m_AwsCryptographyPrimitivesTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
						return func(arg22 interface{}) interface{} {
							return coer22(arg22.(m_AwsCryptographyPrimitivesTypes.Error))
						}
					}(func(_83_e m_AwsCryptographyPrimitivesTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
						return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Unable to create primitives client"))
					}))
					if (_82_valueOrError17).IsFailure() {
						output = (_82_valueOrError17).PropagateFailure()
						return output
					}
					var _84_primitives *m_AtomicPrimitives.AtomicPrimitivesClient
					_ = _84_primitives
					_84_primitives = (_82_valueOrError17).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
					var _source3 _dafny.Sequence = _78_keyAgreementScheme
					_ = _source3
					{
						{
							if (_source3).Equals(_dafny.SeqOfString("static")) {
								{
									var _85_valueOrError18 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
									_ = _85_valueOrError18
									_85_valueOrError18 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_PrivateECDH()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: PrivateECDH")))
									if (_85_valueOrError18).IsFailure() {
										output = (_85_valueOrError18).PropagateFailure()
										return output
									}
									var _86_valueOrError19 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
									_ = _86_valueOrError19
									_86_valueOrError19 = (m_UTF8.Encode(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_senderMaterial())).MapFailure(func(coer23 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg23 interface{}) interface{} {
											return coer23(arg23.(_dafny.Sequence))
										}
									}(func(_87_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_87_e)
									}))
									if (_86_valueOrError19).IsFailure() {
										output = (_86_valueOrError19).PropagateFailure()
										return output
									}
									var _88_senderMaterial _dafny.Sequence
									_ = _88_senderMaterial
									_88_senderMaterial = (_86_valueOrError19).Extract().(_dafny.Sequence)
									var _89_valueOrError20 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
									_ = _89_valueOrError20
									_89_valueOrError20 = (m_UTF8.Encode(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientMaterial())).MapFailure(func(coer24 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg24 interface{}) interface{} {
											return coer24(arg24.(_dafny.Sequence))
										}
									}(func(_90_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_90_e)
									}))
									if (_89_valueOrError20).IsFailure() {
										output = (_89_valueOrError20).PropagateFailure()
										return output
									}
									var _91_recipientMaterial _dafny.Sequence
									_ = _91_recipientMaterial
									_91_recipientMaterial = (_89_valueOrError20).Extract().(_dafny.Sequence)
									var _92_valueOrError21 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
									_ = _92_valueOrError21
									_92_valueOrError21 = (m_Base64.Companion_Default___.Decode(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientPublicKey())).MapFailure(func(coer25 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg25 interface{}) interface{} {
											return coer25(arg25.(_dafny.Sequence))
										}
									}(func(_93_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_93_e)
									}))
									if (_92_valueOrError21).IsFailure() {
										output = (_92_valueOrError21).PropagateFailure()
										return output
									}
									var _94_recipientPublicKey _dafny.Sequence
									_ = _94_recipientPublicKey
									_94_recipientPublicKey = (_92_valueOrError21).Extract().(_dafny.Sequence)
									var _95_schema m_AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
									_ = _95_schema
									_95_schema = m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_RawPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_RawPrivateKeyToStaticPublicKeyInput_.Create_RawPrivateKeyToStaticPublicKeyInput_(_88_senderMaterial, _94_recipientPublicKey))
									var _96_input m_AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
									_ = _96_input
									_96_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(_95_schema, _80_curveType)
									var _97_keyring m_Wrappers.Result
									_ = _97_keyring
									var _out14 m_Wrappers.Result
									_ = _out14
									_out14 = (mpl).CreateRawEcdhKeyring(_96_input)
									_97_keyring = _out14
									output = (_97_keyring).MapFailure(func(coer26 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg26 interface{}) interface{} {
											return coer26(arg26.(m_AwsCryptographyMaterialProvidersTypes.Error))
										}
									}(func(_98_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_98_e)
									}))
									return output
								}
								goto Lmatch3
							}
						}
						{
							if (_source3).Equals(_dafny.SeqOfString("ephemeral")) {
								{
									var _99_recipientMaterial_q m_Wrappers.Option
									_ = _99_recipientMaterial_q
									_99_recipientMaterial_q = Companion_Default___.GetRecipientKeyMaterial(keys, description)
									var _100_valueOrError22 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
									_ = _100_valueOrError22
									_100_valueOrError22 = m_Wrappers.Companion_Default___.Need(((_99_recipientMaterial_q).Is_Some()) && (((_99_recipientMaterial_q).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_PrivateECDH()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: PrivateECDH")))
									if (_100_valueOrError22).IsFailure() {
										output = (_100_valueOrError22).PropagateFailure()
										return output
									}
									var _101_valueOrError23 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
									_ = _101_valueOrError23
									_101_valueOrError23 = (m_UTF8.Encode(((_99_recipientMaterial_q).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientMaterial())).MapFailure(func(coer27 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg27 interface{}) interface{} {
											return coer27(arg27.(_dafny.Sequence))
										}
									}(func(_102_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_102_e)
									}))
									if (_101_valueOrError23).IsFailure() {
										output = (_101_valueOrError23).PropagateFailure()
										return output
									}
									var _103_recipientMaterial _dafny.Sequence
									_ = _103_recipientMaterial
									_103_recipientMaterial = (_101_valueOrError23).Extract().(_dafny.Sequence)
									var _104_valueOrError24 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
									_ = _104_valueOrError24
									_104_valueOrError24 = (m_Base64.Companion_Default___.Decode(((_99_recipientMaterial_q).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientPublicKey())).MapFailure(func(coer28 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg28 interface{}) interface{} {
											return coer28(arg28.(_dafny.Sequence))
										}
									}(func(_105_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_105_e)
									}))
									if (_104_valueOrError24).IsFailure() {
										output = (_104_valueOrError24).PropagateFailure()
										return output
									}
									var _106_recipientPublicKey _dafny.Sequence
									_ = _106_recipientPublicKey
									_106_recipientPublicKey = (_104_valueOrError24).Extract().(_dafny.Sequence)
									var _107_schema m_AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
									_ = _107_schema
									_107_schema = m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_EphemeralPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_EphemeralPrivateKeyToStaticPublicKeyInput_.Create_EphemeralPrivateKeyToStaticPublicKeyInput_(_106_recipientPublicKey))
									var _108_input m_AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
									_ = _108_input
									_108_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(_107_schema, _80_curveType)
									var _109_keyring m_Wrappers.Result
									_ = _109_keyring
									var _out15 m_Wrappers.Result
									_ = _out15
									_out15 = (mpl).CreateRawEcdhKeyring(_108_input)
									_109_keyring = _out15
									output = (_109_keyring).MapFailure(func(coer29 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg29 interface{}) interface{} {
											return coer29(arg29.(m_AwsCryptographyMaterialProvidersTypes.Error))
										}
									}(func(_110_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_110_e)
									}))
									return output
								}
								goto Lmatch3
							}
						}
						{
							if (_source3).Equals(_dafny.SeqOfString("discovery")) {
								{
									var _111_recipientMaterial_q m_Wrappers.Option
									_ = _111_recipientMaterial_q
									_111_recipientMaterial_q = Companion_Default___.GetRecipientKeyMaterial(keys, description)
									var _112_valueOrError25 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
									_ = _112_valueOrError25
									_112_valueOrError25 = m_Wrappers.Companion_Default___.Need(((_111_recipientMaterial_q).Is_Some()) && (((_111_recipientMaterial_q).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_PrivateECDH()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: PrivateECDH")))
									if (_112_valueOrError25).IsFailure() {
										output = (_112_valueOrError25).PropagateFailure()
										return output
									}
									var _113_valueOrError26 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
									_ = _113_valueOrError26
									_113_valueOrError26 = (m_UTF8.Encode(((_111_recipientMaterial_q).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientMaterial())).MapFailure(func(coer30 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg30 interface{}) interface{} {
											return coer30(arg30.(_dafny.Sequence))
										}
									}(func(_114_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_114_e)
									}))
									if (_113_valueOrError26).IsFailure() {
										output = (_113_valueOrError26).PropagateFailure()
										return output
									}
									var _115_recipientMaterial _dafny.Sequence
									_ = _115_recipientMaterial
									_115_recipientMaterial = (_113_valueOrError26).Extract().(_dafny.Sequence)
									var _116_schema m_AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
									_ = _116_schema
									_116_schema = m_AwsCryptographyMaterialProvidersTypes.Companion_RawEcdhStaticConfigurations_.Create_PublicKeyDiscovery_(m_AwsCryptographyMaterialProvidersTypes.Companion_PublicKeyDiscoveryInput_.Create_PublicKeyDiscoveryInput_(_115_recipientMaterial))
									var _117_input m_AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
									_ = _117_input
									_117_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateRawEcdhKeyringInput_.Create_CreateRawEcdhKeyringInput_(_116_schema, _80_curveType)
									var _118_keyring m_Wrappers.Result
									_ = _118_keyring
									var _out16 m_Wrappers.Result
									_ = _out16
									_out16 = (mpl).CreateRawEcdhKeyring(_117_input)
									_118_keyring = _out16
									output = (_118_keyring).MapFailure(func(coer31 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg31 interface{}) interface{} {
											return coer31(arg31.(m_AwsCryptographyMaterialProvidersTypes.Error))
										}
									}(func(_119_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_119_e)
									}))
									return output
								}
								goto Lmatch3
							}
						}
						{
							{
								output = m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("key agreement schema not recognized")))
								return output
							}
						}
						goto Lmatch3
					}
				Lmatch3:
				}
				goto Lmatch0
			}
		}
		{
			if _source0.Is_KmsECDH() {
				var KmsECDH0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsECDH).KmsECDH
				_ = KmsECDH0
				var _120_senderKeyId _dafny.Sequence = KmsECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring).SenderKeyId
				_ = _120_senderKeyId
				var _121_recipientKeyId _dafny.Sequence = KmsECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring).RecipientKeyId
				_ = _121_recipientKeyId
				var _122_senderPublicKey _dafny.Sequence = KmsECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring).SenderPublicKey
				_ = _122_senderPublicKey
				var _123_recipientPublicKey _dafny.Sequence = KmsECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring).RecipientPublicKey
				_ = _123_recipientPublicKey
				var _124_curveSpec _dafny.Sequence = KmsECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring).CurveSpec
				_ = _124_curveSpec
				var _125_keyAgreementScheme _dafny.Sequence = KmsECDH0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring).KeyAgreementScheme
				_ = _125_keyAgreementScheme
				{
					var _126_valueOrError27 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _126_valueOrError27
					_126_valueOrError27 = m_Wrappers.Companion_Default___.Need((m_KeyDescription.Companion_Default___.KmsKey2EccAlgorithmSpec()).Contains(_124_curveSpec), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Unknown curve spec")))
					if (_126_valueOrError27).IsFailure() {
						output = (_126_valueOrError27).PropagateFailure()
						return output
					}
					var _127_curveType m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec
					_ = _127_curveType
					_127_curveType = (m_KeyDescription.Companion_Default___.KmsKey2EccAlgorithmSpec()).Get(_124_curveSpec).(m_AwsCryptographyPrimitivesTypes.ECDHCurveSpec)
					var _source4 _dafny.Sequence = _125_keyAgreementScheme
					_ = _source4
					{
						{
							if (_source4).Equals(_dafny.SeqOfString("static")) {
								{
									var _128_valueOrError28 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
									_ = _128_valueOrError28
									_128_valueOrError28 = m_Wrappers.Companion_Default___.Need(((_0_material).Is_Some()) && (((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_KMSEcdh()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: KmsEcdh")))
									if (_128_valueOrError28).IsFailure() {
										output = (_128_valueOrError28).PropagateFailure()
										return output
									}
									var _129_senderKmsKey _dafny.Sequence
									_ = _129_senderKmsKey
									_129_senderKmsKey = ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_senderMaterial()
									var _130_recipientKmsKey _dafny.Sequence
									_ = _130_recipientKmsKey
									_130_recipientKmsKey = ((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientMaterial()
									var _131_valueOrError29 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
									_ = _131_valueOrError29
									_131_valueOrError29 = m_Wrappers.Companion_Default___.Need((m_ComAmazonawsKmsTypes.Companion_Default___.IsValid__KeyIdType(_129_senderKmsKey)) && (m_ComAmazonawsKmsTypes.Companion_Default___.IsValid__KeyIdType(_130_recipientKmsKey)), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not a valid Kms Key Id")))
									if (_131_valueOrError29).IsFailure() {
										output = (_131_valueOrError29).PropagateFailure()
										return output
									}
									var _132_valueOrError30 m_Wrappers.Result = m_Wrappers.Result{}
									_ = _132_valueOrError30
									var _out17 m_Wrappers.Result
									_ = _out17
									_out17 = Companion_Default___.GetKmsClient(mpl, _129_senderKmsKey)
									_132_valueOrError30 = _out17
									if (_132_valueOrError30).IsFailure() {
										output = (_132_valueOrError30).PropagateFailure()
										return output
									}
									var _133_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
									_ = _133_kmsClient
									_133_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_132_valueOrError30).Extract())
									var _134_valueOrError31 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
									_ = _134_valueOrError31
									_134_valueOrError31 = (m_Base64.Companion_Default___.Decode(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_senderPublicKey())).MapFailure(func(coer32 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg32 interface{}) interface{} {
											return coer32(arg32.(_dafny.Sequence))
										}
									}(func(_135_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_135_e)
									}))
									if (_134_valueOrError31).IsFailure() {
										output = (_134_valueOrError31).PropagateFailure()
										return output
									}
									var _136_senderPublicKey _dafny.Sequence
									_ = _136_senderPublicKey
									_136_senderPublicKey = (_134_valueOrError31).Extract().(_dafny.Sequence)
									var _137_valueOrError32 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
									_ = _137_valueOrError32
									_137_valueOrError32 = (m_Base64.Companion_Default___.Decode(((_0_material).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientPublicKey())).MapFailure(func(coer33 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg33 interface{}) interface{} {
											return coer33(arg33.(_dafny.Sequence))
										}
									}(func(_138_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_138_e)
									}))
									if (_137_valueOrError32).IsFailure() {
										output = (_137_valueOrError32).PropagateFailure()
										return output
									}
									var _139_recipientPublicKey _dafny.Sequence
									_ = _139_recipientPublicKey
									_139_recipientPublicKey = (_137_valueOrError32).Extract().(_dafny.Sequence)
									var _140_schema m_AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations
									_ = _140_schema
									_140_schema = m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPrivateKeyToStaticPublicKey_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPrivateKeyToStaticPublicKeyInput_.Create_KmsPrivateKeyToStaticPublicKeyInput_(_129_senderKmsKey, m_Wrappers.Companion_Option_.Create_Some_(_136_senderPublicKey), _139_recipientPublicKey))
									var _141_input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput
									_ = _141_input
									_141_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(_140_schema, _127_curveType, _133_kmsClient, m_Wrappers.Companion_Option_.Create_None_())
									var _142_keyring m_Wrappers.Result
									_ = _142_keyring
									var _out18 m_Wrappers.Result
									_ = _out18
									_out18 = (mpl).CreateAwsKmsEcdhKeyring(_141_input)
									_142_keyring = _out18
									output = (_142_keyring).MapFailure(func(coer34 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg34 interface{}) interface{} {
											return coer34(arg34.(m_AwsCryptographyMaterialProvidersTypes.Error))
										}
									}(func(_143_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_143_e)
									}))
									return output
								}
								goto Lmatch4
							}
						}
						{
							if (_source4).Equals(_dafny.SeqOfString("discovery")) {
								{
									var _144_recipientMaterial_q m_Wrappers.Option
									_ = _144_recipientMaterial_q
									_144_recipientMaterial_q = Companion_Default___.GetRecipientKeyMaterial(keys, description)
									var _145_valueOrError33 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
									_ = _145_valueOrError33
									_145_valueOrError33 = m_Wrappers.Companion_Default___.Need(((_144_recipientMaterial_q).Is_Some()) && (((_144_recipientMaterial_q).Dtor_value().(m_KeyMaterial.KeyMaterial)).Is_KMSEcdh()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Not type: KmsEcdh")))
									if (_145_valueOrError33).IsFailure() {
										output = (_145_valueOrError33).PropagateFailure()
										return output
									}
									var _146_recipientKmsKey _dafny.Sequence
									_ = _146_recipientKmsKey
									_146_recipientKmsKey = ((_144_recipientMaterial_q).Dtor_value().(m_KeyMaterial.KeyMaterial)).Dtor_recipientMaterial()
									var _147_valueOrError34 m_Wrappers.Result = m_Wrappers.Result{}
									_ = _147_valueOrError34
									var _out19 m_Wrappers.Result
									_ = _out19
									_out19 = Companion_Default___.GetKmsClient(mpl, _146_recipientKmsKey)
									_147_valueOrError34 = _out19
									if (_147_valueOrError34).IsFailure() {
										output = (_147_valueOrError34).PropagateFailure()
										return output
									}
									var _148_kmsClient m_ComAmazonawsKmsTypes.IKMSClient
									_ = _148_kmsClient
									_148_kmsClient = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_147_valueOrError34).Extract())
									var _149_schema m_AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations
									_ = _149_schema
									_149_schema = m_AwsCryptographyMaterialProvidersTypes.Companion_KmsEcdhStaticConfigurations_.Create_KmsPublicKeyDiscovery_(m_AwsCryptographyMaterialProvidersTypes.Companion_KmsPublicKeyDiscoveryInput_.Create_KmsPublicKeyDiscoveryInput_(_146_recipientKmsKey))
									var _150_input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput
									_ = _150_input
									_150_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateAwsKmsEcdhKeyringInput_.Create_CreateAwsKmsEcdhKeyringInput_(_149_schema, _127_curveType, _148_kmsClient, m_Wrappers.Companion_Option_.Create_None_())
									var _151_keyring m_Wrappers.Result
									_ = _151_keyring
									var _out20 m_Wrappers.Result
									_ = _out20
									_out20 = (mpl).CreateAwsKmsEcdhKeyring(_150_input)
									_151_keyring = _out20
									output = (_151_keyring).MapFailure(func(coer35 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
										return func(arg35 interface{}) interface{} {
											return coer35(arg35.(m_AwsCryptographyMaterialProvidersTypes.Error))
										}
									}(func(_152_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
										return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_152_e)
									}))
									return output
								}
								goto Lmatch4
							}
						}
						{
							{
								output = m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("key agreement schema not recognized")))
								return output
							}
						}
						goto Lmatch4
					}
				Lmatch4:
				}
				goto Lmatch0
			}
		}
		{
			var _153_MultiKeyring m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Multi).Multi
			_ = _153_MultiKeyring
			{
				var _154_generator m_Wrappers.Option
				_ = _154_generator
				_154_generator = m_Wrappers.Companion_Option_.Create_None_()
				if ((_153_MultiKeyring).Dtor_generator()).Is_Some() {
					var _155_valueOrError35 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _155_valueOrError35
					_155_valueOrError35 = m_Wrappers.Companion_Default___.Need(m_KeyDescription.Companion_Default___.Keyring_q(((_153_MultiKeyring).Dtor_generator()).Dtor_value().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Only Keyring key descriptions are supported.")))
					if (_155_valueOrError35).IsFailure() {
						output = (_155_valueOrError35).PropagateFailure()
						return output
					}
					var _156_valueOrError36 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _156_valueOrError36
					var _out21 m_Wrappers.Result
					_ = _out21
					_out21 = Companion_Default___.ToKeyring(mpl, keys, ((_153_MultiKeyring).Dtor_generator()).Dtor_value().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription))
					_156_valueOrError36 = _out21
					if (_156_valueOrError36).IsFailure() {
						output = (_156_valueOrError36).PropagateFailure()
						return output
					}
					var _157_generator_k m_AwsCryptographyMaterialProvidersTypes.IKeyring
					_ = _157_generator_k
					_157_generator_k = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_156_valueOrError36).Extract())
					_154_generator = m_Wrappers.Companion_Option_.Create_Some_(_157_generator_k)
				}
				var _158_childKeyrings _dafny.Sequence
				_ = _158_childKeyrings
				_158_childKeyrings = _dafny.SeqOf()

				var _hi0 _dafny.Int = _dafny.IntOfUint32(((_153_MultiKeyring).Dtor_childKeyrings()).Cardinality())
				_ = _hi0
				for _159_i := _dafny.Zero; _159_i.Cmp(_hi0) < 0; _159_i = _159_i.Plus(_dafny.One) {
					var _160_child m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
					_ = _160_child
					_160_child = ((_153_MultiKeyring).Dtor_childKeyrings()).Select((_159_i).Uint32()).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
					var _161_valueOrError37 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
					_ = _161_valueOrError37
					_161_valueOrError37 = m_Wrappers.Companion_Default___.Need(m_KeyDescription.Companion_Default___.Keyring_q(_160_child), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Only Keyring key descriptions are supported.")))
					if (_161_valueOrError37).IsFailure() {
						output = (_161_valueOrError37).PropagateFailure()
						return output
					}
					var _162_valueOrError38 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _162_valueOrError38
					var _out22 m_Wrappers.Result
					_ = _out22
					_out22 = Companion_Default___.ToKeyring(mpl, keys, _160_child)
					_162_valueOrError38 = _out22
					if (_162_valueOrError38).IsFailure() {
						output = (_162_valueOrError38).PropagateFailure()
						return output
					}
					var _163_childKeyring m_AwsCryptographyMaterialProvidersTypes.IKeyring
					_ = _163_childKeyring
					_163_childKeyring = m_AwsCryptographyMaterialProvidersTypes.Companion_IKeyring_.CastTo_((_162_valueOrError38).Extract())
					_158_childKeyrings = _dafny.Companion_Sequence_.Concatenate(_158_childKeyrings, _dafny.SeqOf(_163_childKeyring))
				}
				var _164_input m_AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput
				_ = _164_input
				_164_input = m_AwsCryptographyMaterialProvidersTypes.Companion_CreateMultiKeyringInput_.Create_CreateMultiKeyringInput_(_154_generator, _158_childKeyrings)
				var _165_keyring m_Wrappers.Result
				_ = _165_keyring
				var _out23 m_Wrappers.Result
				_ = _out23
				_out23 = (mpl).CreateMultiKeyring(_164_input)
				_165_keyring = _out23
				output = (_165_keyring).MapFailure(func(coer36 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
					return func(arg36 interface{}) interface{} {
						return coer36(arg36.(m_AwsCryptographyMaterialProvidersTypes.Error))
					}
				}(func(_166_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
					return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_166_e)
				}))
				return output
			}
		}
		goto Lmatch0
	}
Lmatch0:
	return output
}
func (_static *CompanionStruct_Default___) GetKmsClient(mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient, maybeKmsArn _dafny.Sequence) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_maybeClientSupplier m_Wrappers.Result
	_ = _0_maybeClientSupplier
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (mpl).CreateDefaultClientSupplier(m_AwsCryptographyMaterialProvidersTypes.Companion_CreateDefaultClientSupplierInput_.Create_CreateDefaultClientSupplierInput_())
	_0_maybeClientSupplier = _out0
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _1_valueOrError0
	_1_valueOrError0 = (_0_maybeClientSupplier).MapFailure(func(coer37 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
		return func(arg37 interface{}) interface{} {
			return coer37(arg37.(m_AwsCryptographyMaterialProvidersTypes.Error))
		}
	}(func(_2_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
		return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_2_e)
	}))
	if (_1_valueOrError0).IsFailure() {
		output = (_1_valueOrError0).PropagateFailure()
		return output
	}
	var _3_clientSupplier m_AwsCryptographyMaterialProvidersTypes.IClientSupplier
	_ = _3_clientSupplier
	_3_clientSupplier = m_AwsCryptographyMaterialProvidersTypes.Companion_IClientSupplier_.CastTo_((_1_valueOrError0).Extract())
	var _4_arn m_Wrappers.Result
	_ = _4_arn
	_4_arn = m_AwsArnParsing.Companion_Default___.IsAwsKmsIdentifierString(maybeKmsArn)
	var _5_region m_Wrappers.Option
	_ = _5_region
	if (_4_arn).Is_Success() {
		_5_region = m_AwsArnParsing.Companion_Default___.GetRegion((_4_arn).Dtor_value().(m_AwsArnParsing.AwsKmsIdentifier))
	} else {
		_5_region = m_Wrappers.Companion_Option_.Create_None_()
	}
	var _6_tmp m_Wrappers.Result
	_ = _6_tmp
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_3_clientSupplier).GetClient(m_AwsCryptographyMaterialProvidersTypes.Companion_GetClientInput_.Create_GetClientInput_((_5_region).UnwrapOr(_dafny.SeqOfString("")).(_dafny.Sequence)))
	_6_tmp = _out1
	output = (_6_tmp).MapFailure(func(coer38 func(m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
		return func(arg38 interface{}) interface{} {
			return coer38(arg38.(m_AwsCryptographyMaterialProvidersTypes.Error))
		}
	}(func(_7_e m_AwsCryptographyMaterialProvidersTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
		return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_AwsCryptographyMaterialProviders_(_7_e)
	}))
	return output
}
func (_static *CompanionStruct_Default___) GetEcdhPublicKey(client m_ComAmazonawsKmsTypes.IKMSClient, awsKmsKey _dafny.Sequence) m_Wrappers.Result {
	var res m_Wrappers.Result = m_Wrappers.Result{}
	_ = res
	var _0_getPublicKeyRequest m_ComAmazonawsKmsTypes.GetPublicKeyRequest
	_ = _0_getPublicKeyRequest
	_0_getPublicKeyRequest = m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_(awsKmsKey, m_Wrappers.Companion_Option_.Create_None_())
	var _1_maybePublicKeyResponse m_Wrappers.Result
	_ = _1_maybePublicKeyResponse
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (client).GetPublicKey(_0_getPublicKeyRequest)
	_1_maybePublicKeyResponse = _out0
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyResponse_.Default())
	_ = _2_valueOrError0
	_2_valueOrError0 = (_1_maybePublicKeyResponse).MapFailure(func(coer39 func(m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) func(interface{}) interface{} {
		return func(arg39 interface{}) interface{} {
			return coer39(arg39.(m_ComAmazonawsKmsTypes.Error))
		}
	}(func(_3_e m_ComAmazonawsKmsTypes.Error) m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error {
		return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_ComAmazonawsKms_(_3_e)
	}))
	if (_2_valueOrError0).IsFailure() {
		res = (_2_valueOrError0).PropagateFailure()
		return res
	}
	var _4_getPublicKeyResponse m_ComAmazonawsKmsTypes.GetPublicKeyResponse
	_ = _4_getPublicKeyResponse
	_4_getPublicKeyResponse = (_2_valueOrError0).Extract().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
	var _5_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _5_valueOrError1
	_5_valueOrError1 = m_Wrappers.Companion_Default___.Need(((((((_4_getPublicKeyResponse).Dtor_KeyId()).Is_Some()) && (_dafny.Companion_Sequence_.Equal(((_4_getPublicKeyResponse).Dtor_KeyId()).Dtor_value().(_dafny.Sequence), awsKmsKey))) && (((_4_getPublicKeyResponse).Dtor_KeyUsage()).Is_Some())) && ((((_4_getPublicKeyResponse).Dtor_KeyUsage()).Dtor_value().(m_ComAmazonawsKmsTypes.KeyUsageType)).Equals(m_ComAmazonawsKmsTypes.Companion_KeyUsageType_.Create_KEY__AGREEMENT_()))) && (((_4_getPublicKeyResponse).Dtor_PublicKey()).Is_Some()), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_Error_.Create_KeyVectorException_(_dafny.SeqOfString("Invalid response from KMS GetPublicKey")))
	if (_5_valueOrError1).IsFailure() {
		res = (_5_valueOrError1).PropagateFailure()
		return res
	}
	res = m_Wrappers.Companion_Result_.Create_Success_(((_4_getPublicKeyResponse).Dtor_PublicKey()).Dtor_value().(_dafny.Sequence))
	return res
	return res
}

// End of class Default__

// Definition of datatype KeyringInfo
type KeyringInfo struct {
	Data_KeyringInfo_
}

func (_this KeyringInfo) Get_() Data_KeyringInfo_ {
	return _this.Data_KeyringInfo_
}

type Data_KeyringInfo_ interface {
	isKeyringInfo()
}

type CompanionStruct_KeyringInfo_ struct {
}

var Companion_KeyringInfo_ = CompanionStruct_KeyringInfo_{}

type KeyringInfo_KeyringInfo struct {
	Description m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
	Material    m_Wrappers.Option
}

func (KeyringInfo_KeyringInfo) isKeyringInfo() {}

func (CompanionStruct_KeyringInfo_) Create_KeyringInfo_(Description m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, Material m_Wrappers.Option) KeyringInfo {
	return KeyringInfo{KeyringInfo_KeyringInfo{Description, Material}}
}

func (_this KeyringInfo) Is_KeyringInfo() bool {
	_, ok := _this.Get_().(KeyringInfo_KeyringInfo)
	return ok
}

func (CompanionStruct_KeyringInfo_) Default() KeyringInfo {
	return Companion_KeyringInfo_.Create_KeyringInfo_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Default(), m_Wrappers.Companion_Option_.Default())
}

func (_this KeyringInfo) Dtor_description() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	return _this.Get_().(KeyringInfo_KeyringInfo).Description
}

func (_this KeyringInfo) Dtor_material() m_Wrappers.Option {
	return _this.Get_().(KeyringInfo_KeyringInfo).Material
}

func (_this KeyringInfo) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KeyringInfo_KeyringInfo:
		{
			return "KeyringFromKeyDescription.KeyringInfo.KeyringInfo" + "(" + _dafny.String(data.Description) + ", " + _dafny.String(data.Material) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KeyringInfo) Equals(other KeyringInfo) bool {
	switch data1 := _this.Get_().(type) {
	case KeyringInfo_KeyringInfo:
		{
			data2, ok := other.Get_().(KeyringInfo_KeyringInfo)
			return ok && data1.Description.Equals(data2.Description) && data1.Material.Equals(data2.Material)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KeyringInfo) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KeyringInfo)
	return ok && _this.Equals(typed)
}

func Type_KeyringInfo_() _dafny.TypeDescriptor {
	return type_KeyringInfo_{}
}

type type_KeyringInfo_ struct {
}

func (_this type_KeyringInfo_) Default() interface{} {
	return Companion_KeyringInfo_.Default()
}

func (_this type_KeyringInfo_) String() string {
	return "KeyringFromKeyDescription.KeyringInfo"
}
func (_this KeyringInfo) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KeyringInfo{}

// End of datatype KeyringInfo
