// Package AllDefaultCmm
// Dafny module AllDefaultCmm compiled into Go

package AllDefaultCmm

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
	return "AllDefaultCmm.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) SubSets(ec _dafny.Map, keys _dafny.Sequence) _dafny.Set {
	if ((ec).Cardinality()).Sign() == 0 {
		return _dafny.SetOf(_dafny.NewMapBuilder().ToMap())
	} else {
		var _0_subsets _dafny.Set = Companion_Default___.SubSets((ec).Subtract(_dafny.SetOf((keys).Select(0).(_dafny.Sequence))), (keys).Drop(1))
		_ = _0_subsets
		return (_0_subsets).Union(func() _dafny.Set {
			var _coll0 = _dafny.NewBuilder()
			_ = _coll0
			for _iter67 := _dafny.Iterate((_0_subsets).Elements()); ; {
				_compr_0, _ok67 := _iter67()
				if !_ok67 {
					break
				}
				var _1_s _dafny.Map
				_1_s = interface{}(_compr_0).(_dafny.Map)
				if (_0_subsets).Contains(_1_s) {
					_coll0.Add((_1_s).Merge(_dafny.NewMapBuilder().ToMap().UpdateUnsafe((keys).Select(0).(_dafny.Sequence), (ec).Get((keys).Select(0).(_dafny.Sequence)).(_dafny.Sequence))))
				}
			}
			return _coll0.ToSet()
		}())
	}
}
func (_static *CompanionStruct_Default___) AesKey() _dafny.Sequence {
	return (m_AllRawAES.Companion_Default___.AesPersistentKeyNames()).Select(((_dafny.IntOfUint32((m_AllRawAES.Companion_Default___.AesPersistentKeyNames()).Cardinality())).Minus(_dafny.One)).Uint32()).(_dafny.Sequence)
}
func (_static *CompanionStruct_Default___) RawAesKeyring() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_AES_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RawAES_.Create_RawAES_(Companion_Default___.AesKey(), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("aws-raw-vectors-persistent-"), Companion_Default___.AesKey())))
}
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
func (_static *CompanionStruct_Default___) StaticAlgorithmSuite() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AlgorithmSuites.Companion_Default___.GetESDKSuite(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF_())
}
func (_static *CompanionStruct_Default___) SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter68 := _dafny.Iterate((Companion_Default___.EncryptionContextsToTest()).Elements()); ; {
			_compr_0, _ok68 := _iter68()
			if !_ok68 {
				break
			}
			var _0_encryptionContext _dafny.Map
			_0_encryptionContext = interface{}(_compr_0).(_dafny.Map)
			if (Companion_Default___.EncryptionContextsToTest()).Contains(_0_encryptionContext) {
				for _iter69 := _dafny.Iterate((func() _dafny.Set {
					var _coll1 = _dafny.NewBuilder()
					_ = _coll1
					for _iter70 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer54 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
						return func(arg54 interface{}, arg55 interface{}) bool {
							return coer54(arg54.(uint8), arg55.(uint8))
						}
					}(func(_1_a uint8, _2_b uint8) bool {
						return (_1_a) < (_2_b)
					})))).Elements()); ; {
						_compr_2, _ok70 := _iter70()
						if !_ok70 {
							break
						}
						var _3_s _dafny.Map
						_3_s = interface{}(_compr_2).(_dafny.Map)
						if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer55 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg56 interface{}, arg57 interface{}) bool {
								return coer55(arg56.(uint8), arg57.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Contains(_3_s) {
							_coll1.Add((_3_s).Keys())
						}
					}
					return _coll1.ToSet()
				}()).Elements()); ; {
					_compr_1, _ok69 := _iter69()
					if !_ok69 {
						break
					}
					var _4_requiredEncryptionContextKeys _dafny.Set
					_4_requiredEncryptionContextKeys = interface{}(_compr_1).(_dafny.Set)
					if (func() _dafny.Set {
						var _coll2 = _dafny.NewBuilder()
						_ = _coll2
						for _iter71 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer56 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg58 interface{}, arg59 interface{}) bool {
								return coer56(arg58.(uint8), arg59.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Elements()); ; {
							_compr_3, _ok71 := _iter71()
							if !_ok71 {
								break
							}
							var _5_s _dafny.Map
							_5_s = interface{}(_compr_3).(_dafny.Map)
							if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer57 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg60 interface{}, arg61 interface{}) bool {
									return coer57(arg60.(uint8), arg61.(uint8))
								}
							}(func(_1_a uint8, _2_b uint8) bool {
								return (_1_a) < (_2_b)
							})))).Contains(_5_s) {
								_coll2.Add((_5_s).Keys())
							}
						}
						return _coll2.ToSet()
					}()).Contains(_4_requiredEncryptionContextKeys) {
						for _iter72 := _dafny.Iterate((func() _dafny.Set {
							var _coll3 = _dafny.NewBuilder()
							_ = _coll3
							for _iter73 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer58 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg62 interface{}, arg63 interface{}) bool {
									return coer58(arg62.(uint8), arg63.(uint8))
								}
							}(func(_6_a uint8, _7_b uint8) bool {
								return (_6_a) < (_7_b)
							})))).Elements()); ; {
								_compr_5, _ok73 := _iter73()
								if !_ok73 {
									break
								}
								var _8_s _dafny.Map
								_8_s = interface{}(_compr_5).(_dafny.Map)
								if ((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer59 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg64 interface{}, arg65 interface{}) bool {
										return coer59(arg64.(uint8), arg65.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Contains(_8_s)) && ((((_8_s).Keys()).Intersection(_4_requiredEncryptionContextKeys)).Equals(_4_requiredEncryptionContextKeys)) {
									_coll3.Add(_8_s)
								}
							}
							return _coll3.ToSet()
						}()).Elements()); ; {
							_compr_4, _ok72 := _iter72()
							if !_ok72 {
								break
							}
							var _9_reproducedEncryptionContext _dafny.Map
							_9_reproducedEncryptionContext = interface{}(_compr_4).(_dafny.Map)
							if (func() _dafny.Set {
								var _coll4 = _dafny.NewBuilder()
								_ = _coll4
								for _iter74 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer60 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg66 interface{}, arg67 interface{}) bool {
										return coer60(arg66.(uint8), arg67.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Elements()); ; {
									_compr_6, _ok74 := _iter74()
									if !_ok74 {
										break
									}
									var _10_s _dafny.Map
									_10_s = interface{}(_compr_6).(_dafny.Map)
									if ((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer61 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg68 interface{}, arg69 interface{}) bool {
											return coer61(arg68.(uint8), arg69.(uint8))
										}
									}(func(_6_a uint8, _7_b uint8) bool {
										return (_6_a) < (_7_b)
									})))).Contains(_10_s)) && ((((_10_s).Keys()).Intersection(_4_requiredEncryptionContextKeys)).Equals(_4_requiredEncryptionContextKeys)) {
										_coll4.Add(_10_s)
									}
								}
								return _coll4.ToSet()
							}()).Contains(_9_reproducedEncryptionContext) {
								_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.SeqOfString("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), m_Wrappers.Companion_Option_.Create_None_(), _0_encryptionContext, m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys)), Companion_Default___.RawAesKeyring(), Companion_Default___.RawAesKeyring(), m_Wrappers.Companion_Option_.Create_Some_(_9_reproducedEncryptionContext)))
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
		for _iter75 := _dafny.Iterate((Companion_Default___.EncryptionContextsToTest()).Elements()); ; {
			_compr_0, _ok75 := _iter75()
			if !_ok75 {
				break
			}
			var _0_encryptionContext _dafny.Map
			_0_encryptionContext = interface{}(_compr_0).(_dafny.Map)
			if (Companion_Default___.EncryptionContextsToTest()).Contains(_0_encryptionContext) {
				for _iter76 := _dafny.Iterate((func() _dafny.Set {
					var _coll1 = _dafny.NewBuilder()
					_ = _coll1
					for _iter77 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer62 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
						return func(arg70 interface{}, arg71 interface{}) bool {
							return coer62(arg70.(uint8), arg71.(uint8))
						}
					}(func(_1_a uint8, _2_b uint8) bool {
						return (_1_a) < (_2_b)
					})))).Elements()); ; {
						_compr_2, _ok77 := _iter77()
						if !_ok77 {
							break
						}
						var _3_s _dafny.Map
						_3_s = interface{}(_compr_2).(_dafny.Map)
						if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer63 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg72 interface{}, arg73 interface{}) bool {
								return coer63(arg72.(uint8), arg73.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Contains(_3_s) {
							_coll1.Add((_3_s).Keys())
						}
					}
					return _coll1.ToSet()
				}()).Elements()); ; {
					_compr_1, _ok76 := _iter76()
					if !_ok76 {
						break
					}
					var _4_requiredEncryptionContextKeys _dafny.Set
					_4_requiredEncryptionContextKeys = interface{}(_compr_1).(_dafny.Set)
					if (func() _dafny.Set {
						var _coll2 = _dafny.NewBuilder()
						_ = _coll2
						for _iter78 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer64 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg74 interface{}, arg75 interface{}) bool {
								return coer64(arg74.(uint8), arg75.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Elements()); ; {
							_compr_3, _ok78 := _iter78()
							if !_ok78 {
								break
							}
							var _5_s _dafny.Map
							_5_s = interface{}(_compr_3).(_dafny.Map)
							if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer65 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg76 interface{}, arg77 interface{}) bool {
									return coer65(arg76.(uint8), arg77.(uint8))
								}
							}(func(_1_a uint8, _2_b uint8) bool {
								return (_1_a) < (_2_b)
							})))).Contains(_5_s) {
								_coll2.Add((_5_s).Keys())
							}
						}
						return _coll2.ToSet()
					}()).Contains(_4_requiredEncryptionContextKeys) {
						for _iter79 := _dafny.Iterate((func() _dafny.Set {
							var _coll3 = _dafny.NewBuilder()
							_ = _coll3
							for _iter80 := _dafny.Iterate((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer66 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg78 interface{}, arg79 interface{}) bool {
									return coer66(arg78.(uint8), arg79.(uint8))
								}
							}(func(_6_a uint8, _7_b uint8) bool {
								return (_6_a) < (_7_b)
							})))).Elements()); ; {
								_compr_5, _ok80 := _iter80()
								if !_ok80 {
									break
								}
								var _8_s _dafny.Map
								_8_s = interface{}(_compr_5).(_dafny.Map)
								if ((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer67 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg80 interface{}, arg81 interface{}) bool {
										return coer67(arg80.(uint8), arg81.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Contains(_8_s)) && (!(_8_s).Equals(_dafny.NewMapBuilder().ToMap())) {
									_coll3.Add(_8_s)
								}
							}
							return _coll3.ToSet()
						}()).Elements()); ; {
							_compr_4, _ok79 := _iter79()
							if !_ok79 {
								break
							}
							var _9_incorrectEncryptionContext _dafny.Map
							_9_incorrectEncryptionContext = interface{}(_compr_4).(_dafny.Map)
							if (func() _dafny.Set {
								var _coll4 = _dafny.NewBuilder()
								_ = _coll4
								for _iter81 := _dafny.Iterate((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer68 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg82 interface{}, arg83 interface{}) bool {
										return coer68(arg82.(uint8), arg83.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Elements()); ; {
									_compr_6, _ok81 := _iter81()
									if !_ok81 {
										break
									}
									var _10_s _dafny.Map
									_10_s = interface{}(_compr_6).(_dafny.Map)
									if ((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer69 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg84 interface{}, arg85 interface{}) bool {
											return coer69(arg84.(uint8), arg85.(uint8))
										}
									}(func(_6_a uint8, _7_b uint8) bool {
										return (_6_a) < (_7_b)
									})))).Contains(_10_s)) && (!(_10_s).Equals(_dafny.NewMapBuilder().ToMap())) {
										_coll4.Add(_10_s)
									}
								}
								return _coll4.ToSet()
							}()).Contains(_9_incorrectEncryptionContext) {
								for _iter82 := _dafny.Iterate((func() _dafny.Set {
									var _coll5 = _dafny.NewBuilder()
									_ = _coll5
									for _iter83 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer70 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg86 interface{}, arg87 interface{}) bool {
											return coer70(arg86.(uint8), arg87.(uint8))
										}
									}(func(_11_a uint8, _12_b uint8) bool {
										return (_11_a) < (_12_b)
									})))).Elements()); ; {
										_compr_8, _ok83 := _iter83()
										if !_ok83 {
											break
										}
										var _13_s _dafny.Map
										_13_s = interface{}(_compr_8).(_dafny.Map)
										if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer71 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
											return func(arg88 interface{}, arg89 interface{}) bool {
												return coer71(arg88.(uint8), arg89.(uint8))
											}
										}(func(_11_a uint8, _12_b uint8) bool {
											return (_11_a) < (_12_b)
										})))).Contains(_13_s) {
											_coll5.Add((_13_s).Merge(_9_incorrectEncryptionContext))
										}
									}
									return _coll5.ToSet()
								}()).Elements()); ; {
									_compr_7, _ok82 := _iter82()
									if !_ok82 {
										break
									}
									var _14_reproducedEncryptionContext _dafny.Map
									_14_reproducedEncryptionContext = interface{}(_compr_7).(_dafny.Map)
									if (func() _dafny.Set {
										var _coll6 = _dafny.NewBuilder()
										_ = _coll6
										for _iter84 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer72 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
											return func(arg90 interface{}, arg91 interface{}) bool {
												return coer72(arg90.(uint8), arg91.(uint8))
											}
										}(func(_11_a uint8, _12_b uint8) bool {
											return (_11_a) < (_12_b)
										})))).Elements()); ; {
											_compr_9, _ok84 := _iter84()
											if !_ok84 {
												break
											}
											var _15_s _dafny.Map
											_15_s = interface{}(_compr_9).(_dafny.Map)
											if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer73 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
												return func(arg92 interface{}, arg93 interface{}) bool {
													return coer73(arg92.(uint8), arg93.(uint8))
												}
											}(func(_11_a uint8, _12_b uint8) bool {
												return (_11_a) < (_12_b)
											})))).Contains(_15_s) {
												_coll6.Add((_15_s).Merge(_9_incorrectEncryptionContext))
											}
										}
										return _coll6.ToSet()
									}()).Contains(_14_reproducedEncryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptNegativeDecryptKeyringVector_(_dafny.SeqOfString("Failure of reproducedEncryptionContext"), m_Wrappers.Companion_Option_.Create_None_(), _0_encryptionContext, m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_SortedSets.SetToSequence(_4_requiredEncryptionContextKeys)), _dafny.SeqOfString("The reproducedEncryptionContext is not correct"), Companion_Default___.RawAesKeyring(), Companion_Default___.RawAesKeyring(), m_Wrappers.Companion_Option_.Create_Some_(_14_reproducedEncryptionContext)))
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
func (_static *CompanionStruct_Default___) StaticPlaintextDataKey() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_Static_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_StaticKeyring_.Create_StaticKeyring_(_dafny.SeqOfString("static-plaintext-data-key")))
}
func (_static *CompanionStruct_Default___) StaticNotPlaintextDataKey() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_Static_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_StaticKeyring_.Create_StaticKeyring_(_dafny.SeqOfString("no-plaintext-data-key")))
}
func (_static *CompanionStruct_Default___) Tests() _dafny.Set {
	return (((_dafny.SetOf()).Union(_dafny.SetOf(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.SeqOfString("Simplest possible happy path"), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap(), m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), Companion_Default___.StaticPlaintextDataKey(), Companion_Default___.StaticPlaintextDataKey(), m_Wrappers.Companion_Option_.Create_None_()), m_TestVectors.Companion_EncryptTestVector_.Create_NegativeEncryptKeyringVector_(_dafny.SeqOfString("Missing plaintext data key on decrypt"), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap(), m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _dafny.SeqOfString("No plaintext data key on encrypt fails"), Companion_Default___.StaticNotPlaintextDataKey()), m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptNegativeDecryptKeyringVector_(_dafny.SeqOfString("Missing plaintext data key on decrypt"), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap(), m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _dafny.SeqOfString("No plaintext data key on encrypt fails"), Companion_Default___.StaticPlaintextDataKey(), Companion_Default___.StaticNotPlaintextDataKey(), m_Wrappers.Companion_Option_.Create_None_())))).Union(Companion_Default___.FailureBadReproducedEncryptionContext())).Union(Companion_Default___.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext())
}

// End of class Default__
