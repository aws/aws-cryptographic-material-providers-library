// Package AllDefaultCmm
// Dafny module AllDefaultCmm compiled into Go

package AllDefaultCmm

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb/ComAmazonawsDynamodbTypes"
	m_Com_Amazonaws_Dynamodb "github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb/Com_Amazonaws_Dynamodb"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms/ComAmazonawsKmsTypes"
	m_Com_Amazonaws_Kms "github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms/Com_Amazonaws_Kms"
	m_AlgorithmSuites "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AlgorithmSuites"
	m_AwsArnParsing "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsArnParsing"
	m_AwsCryptographyKeyStoreOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyKeyStoreOperations"
	m_AwsCryptographyKeyStoreTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyKeyStoreTypes"
	m_AwsCryptographyMaterialProvidersOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyMaterialProvidersOperations"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsDiscoveryKeyring"
	m_AwsKmsEcdhKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsEcdhKeyring"
	m_AwsKmsHierarchicalKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsHierarchicalKeyring"
	m_AwsKmsKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsKeyring"
	m_AwsKmsMrkAreUnique "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkAreUnique"
	m_AwsKmsMrkDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkDiscoveryKeyring"
	m_AwsKmsMrkKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkKeyring"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsRsaKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsRsaKeyring"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsUtils"
	m_CMM "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CMM"
	m_CacheConstants "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CacheConstants"
	m_CanonicalEncryptionContext "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CanonicalEncryptionContext"
	m_Commitment "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Commitment"
	m_Constants "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Constants"
	m_CreateKeyStoreTable "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CreateKeyStoreTable"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DDBKeystoreOperations"
	m_DefaultCMM "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DefaultCMM"
	m_DefaultClientSupplier "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DefaultClientSupplier"
	m_Defaults "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Defaults"
	m_DiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DiscoveryMultiKeyring"
	m_EcdhEdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/EcdhEdkWrapping"
	m_EdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/EdkWrapping"
	m_ErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/ErrorMessages"
	m_GetKeys "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/GetKeys"
	m_IntermediateKeyWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/IntermediateKeyWrapping"
	m_KMSKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KMSKeystoreOperations"
	m_KeyStore "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KeyStore"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KeyStoreErrorMessages"
	m_Keyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Keyring"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KmsArn"
	m_LocalCMC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/LocalCMC"
	m_MaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MaterialProviders"
	m_MaterialWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MaterialWrapping"
	m_Materials "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Materials"
	m_MrkAwareDiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MrkAwareDiscoveryMultiKeyring"
	m_MrkAwareStrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MrkAwareStrictMultiKeyring"
	m_MultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MultiKeyring"
	m_RawAESKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RawAESKeyring"
	m_RawECDHKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RawECDHKeyring"
	m_RawRSAKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RawRSAKeyring"
	m_RequiredEncryptionContextCMM "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RequiredEncryptionContextCMM"
	m_StormTracker "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/StormTracker"
	m_StormTrackingCMC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/StormTrackingCMC"
	m_StrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/StrictMultiKeyring"
	m_Structure "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Structure"
	m_SynchronizedLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/SynchronizedLocalCMC"
	m_Utils "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Utils"
	m_AtomicPrimitives "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/AtomicPrimitives"
	m_AwsCryptographyPrimitivesOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/AwsCryptographyPrimitivesOperations"
	m_AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/AwsCryptographyPrimitivesTypes"
	m_Digest "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/Digest"
	m_HKDF "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/HKDF"
	m_KdfCtr "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/KdfCtr"
	m_Random "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/Random"
	m_WrappedHKDF "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/WrappedHKDF"
	m_WrappedHMAC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/WrappedHMAC"
	m_Actions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Actions"
	m_Base64 "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Base64"
	m_Base64Lemmas "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Base64Lemmas"
	m_BoundedInts "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/BoundedInts"
	m_DivInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternals"
	m_DivInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternalsNonlinear"
	m_DivMod "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivMod"
	m_FileIO "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FileIO"
	m_FloatCompare "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FloatCompare"
	m_Functions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Functions"
	m_GeneralInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GeneralInternals"
	m_GetOpt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GetOpt"
	m_HexStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/HexStrings"
	m_JSON_API "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_API"
	m_JSON_ConcreteSyntax_Spec "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ConcreteSyntax_Spec"
	m_JSON_ConcreteSyntax_SpecProperties "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ConcreteSyntax_SpecProperties"
	m_JSON_Deserializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Deserializer"
	m_JSON_Deserializer_ByteStrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Deserializer_ByteStrConversion"
	m_JSON_Deserializer_Uint16StrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Deserializer_Uint16StrConversion"
	m_JSON_Errors "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Errors"
	m_JSON_Grammar "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Grammar"
	m_JSON_Serializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Serializer"
	m_JSON_Serializer_ByteStrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Serializer_ByteStrConversion"
	m_JSON_Spec "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Spec"
	m_JSON_Utils_Cursors "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Cursors"
	m_JSON_Utils_Lexers_Core "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Lexers_Core"
	m_JSON_Utils_Lexers_Strings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Lexers_Strings"
	m_JSON_Utils_Parsers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Parsers"
	m_JSON_Utils_Seq "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Seq"
	m_JSON_Utils_Str "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Str"
	m_JSON_Utils_Str_CharStrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Str_CharStrConversion"
	m_JSON_Utils_Str_CharStrEscaping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Str_CharStrEscaping"
	m_JSON_Utils_Vectors "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Vectors"
	m_JSON_Utils_Views_Core "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Views_Core"
	m_JSON_Utils_Views_Writers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Views_Writers"
	m_JSON_Values "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Values"
	m_JSON_ZeroCopy_API "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_API"
	m_JSON_ZeroCopy_Deserializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer"
	m_JSON_ZeroCopy_Deserializer_API "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_API"
	m_JSON_ZeroCopy_Deserializer_ArrayParams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_ArrayParams"
	m_JSON_ZeroCopy_Deserializer_Arrays "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Arrays"
	m_JSON_ZeroCopy_Deserializer_Constants "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Constants"
	m_JSON_ZeroCopy_Deserializer_Core "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Core"
	m_JSON_ZeroCopy_Deserializer_Numbers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Numbers"
	m_JSON_ZeroCopy_Deserializer_ObjectParams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_ObjectParams"
	m_JSON_ZeroCopy_Deserializer_Objects "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Objects"
	m_JSON_ZeroCopy_Deserializer_Strings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Strings"
	m_JSON_ZeroCopy_Deserializer_Values "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Values"
	m_JSON_ZeroCopy_Serializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Serializer"
	m_Logarithm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Logarithm"
	m__Math "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Math_"
	m_ModInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternals"
	m_ModInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternalsNonlinear"
	m_Mul "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Mul"
	m_MulInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternals"
	m_MulInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternalsNonlinear"
	m_Power "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Power"
	m_Relations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Relations"
	m_Seq "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq"
	m_Seq_MergeSort "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq_MergeSort"
	m_SortedSets "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/SortedSets"
	m_Sorting "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Sorting"
	m_StandardLibrary "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary"
	m_StandardLibraryInterop "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibraryInterop"
	m_StandardLibrary_MemoryMath "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_MemoryMath"
	m_StandardLibrary_Sequence "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_Sequence"
	m_StandardLibrary_String "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_UInt"
	m_Streams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Streams"
	m_UTF8 "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/UTF8"
	m_UnicodeStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/UnicodeStrings"
	m__Unicode "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Unicode_"
	m_Utf16EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf8EncodingForm"
	m_Wrappers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Wrappers"
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
	m_EncryptionContextUtils "github.com/aws/aws-cryptographic-material-providers-library/testvectors/EncryptionContextUtils"
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
)

var _ = os.Args
var _ _dafny.Dummy__
var _ m__System.Dummy__
var _ m_Wrappers.Dummy__
var _ m_BoundedInts.Dummy__
var _ m_StandardLibrary_UInt.Dummy__
var _ m_StandardLibrary_MemoryMath.Dummy__
var _ m_StandardLibrary_Sequence.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
var _ m_Random.Dummy__
var _ m_Digest.Dummy__
var _ m_WrappedHMAC.Dummy__
var _ m_HKDF.Dummy__
var _ m_WrappedHKDF.Dummy__
var _ m_KdfCtr.Dummy__
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
var _ m_Actions.Dummy__
var _ m_CanonicalEncryptionContext.Dummy__
var _ m_MaterialWrapping.Dummy__
var _ m_IntermediateKeyWrapping.Dummy__
var _ m_EdkWrapping.Dummy__
var _ m_ErrorMessages.Dummy__
var _ m_RawAESKeyring.Dummy__
var _ m_AwsArnParsing.Dummy__
var _ m_Constants.Dummy__
var _ m_EcdhEdkWrapping.Dummy__
var _ m_RawECDHKeyring.Dummy__
var _ m_RawRSAKeyring.Dummy__
var _ m_AwsKmsMrkMatchForDecrypt.Dummy__
var _ m_AwsKmsUtils.Dummy__
var _ m_AwsKmsKeyring.Dummy__
var _ m_AwsKmsDiscoveryKeyring.Dummy__
var _ m_AwsKmsEcdhKeyring.Dummy__
var _ m_FileIO.Dummy__
var _ m_LocalCMC.Dummy__
var _ m_SynchronizedLocalCMC.Dummy__
var _ m_StormTracker.Dummy__
var _ m_StormTrackingCMC.Dummy__
var _ m_CacheConstants.Dummy__
var _ m_AwsKmsHierarchicalKeyring.Dummy__
var _ m_AwsKmsMrkDiscoveryKeyring.Dummy__
var _ m_AwsKmsMrkKeyring.Dummy__
var _ m_AwsKmsRsaKeyring.Dummy__
var _ m_MultiKeyring.Dummy__
var _ m_AwsKmsMrkAreUnique.Dummy__
var _ m_StrictMultiKeyring.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__
var _ m_DiscoveryMultiKeyring.Dummy__
var _ m_MrkAwareDiscoveryMultiKeyring.Dummy__
var _ m_MrkAwareStrictMultiKeyring.Dummy__
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
var _ m_EncryptionContextUtils.Dummy__
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
			for _iter117 := _dafny.Iterate((_0_subsets).Elements()); ; {
				_compr_0, _ok117 := _iter117()
				if !_ok117 {
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
		for _iter118 := _dafny.Iterate((Companion_Default___.EncryptionContextsToTest()).Elements()); ; {
			_compr_0, _ok118 := _iter118()
			if !_ok118 {
				break
			}
			var _0_encryptionContext _dafny.Map
			_0_encryptionContext = interface{}(_compr_0).(_dafny.Map)
			if (Companion_Default___.EncryptionContextsToTest()).Contains(_0_encryptionContext) {
				for _iter119 := _dafny.Iterate((func() _dafny.Set {
					var _coll1 = _dafny.NewBuilder()
					_ = _coll1
					for _iter120 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer52 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
						return func(arg52 interface{}, arg53 interface{}) bool {
							return coer52(arg52.(uint8), arg53.(uint8))
						}
					}(func(_1_a uint8, _2_b uint8) bool {
						return (_1_a) < (_2_b)
					})))).Elements()); ; {
						_compr_2, _ok120 := _iter120()
						if !_ok120 {
							break
						}
						var _3_s _dafny.Map
						_3_s = interface{}(_compr_2).(_dafny.Map)
						if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer53 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg54 interface{}, arg55 interface{}) bool {
								return coer53(arg54.(uint8), arg55.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Contains(_3_s) {
							_coll1.Add((_3_s).Keys())
						}
					}
					return _coll1.ToSet()
				}()).Elements()); ; {
					_compr_1, _ok119 := _iter119()
					if !_ok119 {
						break
					}
					var _4_requiredEncryptionContextKeys _dafny.Set
					_4_requiredEncryptionContextKeys = interface{}(_compr_1).(_dafny.Set)
					if (func() _dafny.Set {
						var _coll2 = _dafny.NewBuilder()
						_ = _coll2
						for _iter121 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer54 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg56 interface{}, arg57 interface{}) bool {
								return coer54(arg56.(uint8), arg57.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Elements()); ; {
							_compr_3, _ok121 := _iter121()
							if !_ok121 {
								break
							}
							var _5_s _dafny.Map
							_5_s = interface{}(_compr_3).(_dafny.Map)
							if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer55 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg58 interface{}, arg59 interface{}) bool {
									return coer55(arg58.(uint8), arg59.(uint8))
								}
							}(func(_1_a uint8, _2_b uint8) bool {
								return (_1_a) < (_2_b)
							})))).Contains(_5_s) {
								_coll2.Add((_5_s).Keys())
							}
						}
						return _coll2.ToSet()
					}()).Contains(_4_requiredEncryptionContextKeys) {
						for _iter122 := _dafny.Iterate((func() _dafny.Set {
							var _coll3 = _dafny.NewBuilder()
							_ = _coll3
							for _iter123 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer56 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg60 interface{}, arg61 interface{}) bool {
									return coer56(arg60.(uint8), arg61.(uint8))
								}
							}(func(_6_a uint8, _7_b uint8) bool {
								return (_6_a) < (_7_b)
							})))).Elements()); ; {
								_compr_5, _ok123 := _iter123()
								if !_ok123 {
									break
								}
								var _8_s _dafny.Map
								_8_s = interface{}(_compr_5).(_dafny.Map)
								if ((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer57 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg62 interface{}, arg63 interface{}) bool {
										return coer57(arg62.(uint8), arg63.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Contains(_8_s)) && ((((_8_s).Keys()).Intersection(_4_requiredEncryptionContextKeys)).Equals(_4_requiredEncryptionContextKeys)) {
									_coll3.Add(_8_s)
								}
							}
							return _coll3.ToSet()
						}()).Elements()); ; {
							_compr_4, _ok122 := _iter122()
							if !_ok122 {
								break
							}
							var _9_reproducedEncryptionContext _dafny.Map
							_9_reproducedEncryptionContext = interface{}(_compr_4).(_dafny.Map)
							if (func() _dafny.Set {
								var _coll4 = _dafny.NewBuilder()
								_ = _coll4
								for _iter124 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer58 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg64 interface{}, arg65 interface{}) bool {
										return coer58(arg64.(uint8), arg65.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Elements()); ; {
									_compr_6, _ok124 := _iter124()
									if !_ok124 {
										break
									}
									var _10_s _dafny.Map
									_10_s = interface{}(_compr_6).(_dafny.Map)
									if ((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer59 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg66 interface{}, arg67 interface{}) bool {
											return coer59(arg66.(uint8), arg67.(uint8))
										}
									}(func(_6_a uint8, _7_b uint8) bool {
										return (_6_a) < (_7_b)
									})))).Contains(_10_s)) && ((((_10_s).Keys()).Intersection(_4_requiredEncryptionContextKeys)).Equals(_4_requiredEncryptionContextKeys)) {
										_coll4.Add(_10_s)
									}
								}
								return _coll4.ToSet()
							}()).Contains(_9_reproducedEncryptionContext) {
								_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.SeqOfString("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), m_Wrappers.Companion_Option_.Create_None_(), _0_encryptionContext, m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_SortedSets.SetToOrderedSequence2(_4_requiredEncryptionContextKeys, func(coer60 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg68 interface{}, arg69 interface{}) bool {
										return coer60(arg68.(uint8), arg69.(uint8))
									}
								}(func(_11_a uint8, _12_b uint8) bool {
									return (_11_a) < (_12_b)
								}))), Companion_Default___.RawAesKeyring(), Companion_Default___.RawAesKeyring(), m_Wrappers.Companion_Option_.Create_Some_(_9_reproducedEncryptionContext)))
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
		for _iter125 := _dafny.Iterate((Companion_Default___.EncryptionContextsToTest()).Elements()); ; {
			_compr_0, _ok125 := _iter125()
			if !_ok125 {
				break
			}
			var _0_encryptionContext _dafny.Map
			_0_encryptionContext = interface{}(_compr_0).(_dafny.Map)
			if (Companion_Default___.EncryptionContextsToTest()).Contains(_0_encryptionContext) {
				for _iter126 := _dafny.Iterate((func() _dafny.Set {
					var _coll1 = _dafny.NewBuilder()
					_ = _coll1
					for _iter127 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer61 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
						return func(arg70 interface{}, arg71 interface{}) bool {
							return coer61(arg70.(uint8), arg71.(uint8))
						}
					}(func(_1_a uint8, _2_b uint8) bool {
						return (_1_a) < (_2_b)
					})))).Elements()); ; {
						_compr_2, _ok127 := _iter127()
						if !_ok127 {
							break
						}
						var _3_s _dafny.Map
						_3_s = interface{}(_compr_2).(_dafny.Map)
						if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer62 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg72 interface{}, arg73 interface{}) bool {
								return coer62(arg72.(uint8), arg73.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Contains(_3_s) {
							_coll1.Add((_3_s).Keys())
						}
					}
					return _coll1.ToSet()
				}()).Elements()); ; {
					_compr_1, _ok126 := _iter126()
					if !_ok126 {
						break
					}
					var _4_requiredEncryptionContextKeys _dafny.Set
					_4_requiredEncryptionContextKeys = interface{}(_compr_1).(_dafny.Set)
					if (func() _dafny.Set {
						var _coll2 = _dafny.NewBuilder()
						_ = _coll2
						for _iter128 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer63 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
							return func(arg74 interface{}, arg75 interface{}) bool {
								return coer63(arg74.(uint8), arg75.(uint8))
							}
						}(func(_1_a uint8, _2_b uint8) bool {
							return (_1_a) < (_2_b)
						})))).Elements()); ; {
							_compr_3, _ok128 := _iter128()
							if !_ok128 {
								break
							}
							var _5_s _dafny.Map
							_5_s = interface{}(_compr_3).(_dafny.Map)
							if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer64 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg76 interface{}, arg77 interface{}) bool {
									return coer64(arg76.(uint8), arg77.(uint8))
								}
							}(func(_1_a uint8, _2_b uint8) bool {
								return (_1_a) < (_2_b)
							})))).Contains(_5_s) {
								_coll2.Add((_5_s).Keys())
							}
						}
						return _coll2.ToSet()
					}()).Contains(_4_requiredEncryptionContextKeys) {
						for _iter129 := _dafny.Iterate((func() _dafny.Set {
							var _coll3 = _dafny.NewBuilder()
							_ = _coll3
							for _iter130 := _dafny.Iterate((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer65 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
								return func(arg78 interface{}, arg79 interface{}) bool {
									return coer65(arg78.(uint8), arg79.(uint8))
								}
							}(func(_6_a uint8, _7_b uint8) bool {
								return (_6_a) < (_7_b)
							})))).Elements()); ; {
								_compr_5, _ok130 := _iter130()
								if !_ok130 {
									break
								}
								var _8_s _dafny.Map
								_8_s = interface{}(_compr_5).(_dafny.Map)
								if ((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer66 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg80 interface{}, arg81 interface{}) bool {
										return coer66(arg80.(uint8), arg81.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Contains(_8_s)) && (!(_8_s).Equals(_dafny.NewMapBuilder().ToMap())) {
									_coll3.Add(_8_s)
								}
							}
							return _coll3.ToSet()
						}()).Elements()); ; {
							_compr_4, _ok129 := _iter129()
							if !_ok129 {
								break
							}
							var _9_incorrectEncryptionContext _dafny.Map
							_9_incorrectEncryptionContext = interface{}(_compr_4).(_dafny.Map)
							if (func() _dafny.Set {
								var _coll4 = _dafny.NewBuilder()
								_ = _coll4
								for _iter131 := _dafny.Iterate((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer67 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
									return func(arg82 interface{}, arg83 interface{}) bool {
										return coer67(arg82.(uint8), arg83.(uint8))
									}
								}(func(_6_a uint8, _7_b uint8) bool {
									return (_6_a) < (_7_b)
								})))).Elements()); ; {
									_compr_6, _ok131 := _iter131()
									if !_ok131 {
										break
									}
									var _10_s _dafny.Map
									_10_s = interface{}(_compr_6).(_dafny.Map)
									if ((Companion_Default___.SubSets(Companion_Default___.DisjointEncryptionContext(), m_SortedSets.SetToOrderedSequence2((Companion_Default___.DisjointEncryptionContext()).Keys(), func(coer68 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg84 interface{}, arg85 interface{}) bool {
											return coer68(arg84.(uint8), arg85.(uint8))
										}
									}(func(_6_a uint8, _7_b uint8) bool {
										return (_6_a) < (_7_b)
									})))).Contains(_10_s)) && (!(_10_s).Equals(_dafny.NewMapBuilder().ToMap())) {
										_coll4.Add(_10_s)
									}
								}
								return _coll4.ToSet()
							}()).Contains(_9_incorrectEncryptionContext) {
								for _iter132 := _dafny.Iterate((func() _dafny.Set {
									var _coll5 = _dafny.NewBuilder()
									_ = _coll5
									for _iter133 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer69 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
										return func(arg86 interface{}, arg87 interface{}) bool {
											return coer69(arg86.(uint8), arg87.(uint8))
										}
									}(func(_11_a uint8, _12_b uint8) bool {
										return (_11_a) < (_12_b)
									})))).Elements()); ; {
										_compr_8, _ok133 := _iter133()
										if !_ok133 {
											break
										}
										var _13_s _dafny.Map
										_13_s = interface{}(_compr_8).(_dafny.Map)
										if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer70 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
											return func(arg88 interface{}, arg89 interface{}) bool {
												return coer70(arg88.(uint8), arg89.(uint8))
											}
										}(func(_11_a uint8, _12_b uint8) bool {
											return (_11_a) < (_12_b)
										})))).Contains(_13_s) {
											_coll5.Add((_13_s).Merge(_9_incorrectEncryptionContext))
										}
									}
									return _coll5.ToSet()
								}()).Elements()); ; {
									_compr_7, _ok132 := _iter132()
									if !_ok132 {
										break
									}
									var _14_reproducedEncryptionContext _dafny.Map
									_14_reproducedEncryptionContext = interface{}(_compr_7).(_dafny.Map)
									if (func() _dafny.Set {
										var _coll6 = _dafny.NewBuilder()
										_ = _coll6
										for _iter134 := _dafny.Iterate((Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer71 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
											return func(arg90 interface{}, arg91 interface{}) bool {
												return coer71(arg90.(uint8), arg91.(uint8))
											}
										}(func(_11_a uint8, _12_b uint8) bool {
											return (_11_a) < (_12_b)
										})))).Elements()); ; {
											_compr_9, _ok134 := _iter134()
											if !_ok134 {
												break
											}
											var _15_s _dafny.Map
											_15_s = interface{}(_compr_9).(_dafny.Map)
											if (Companion_Default___.SubSets(_0_encryptionContext, m_SortedSets.SetToOrderedSequence2((_0_encryptionContext).Keys(), func(coer72 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
												return func(arg92 interface{}, arg93 interface{}) bool {
													return coer72(arg92.(uint8), arg93.(uint8))
												}
											}(func(_11_a uint8, _12_b uint8) bool {
												return (_11_a) < (_12_b)
											})))).Contains(_15_s) {
												_coll6.Add((_15_s).Merge(_9_incorrectEncryptionContext))
											}
										}
										return _coll6.ToSet()
									}()).Contains(_14_reproducedEncryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptNegativeDecryptKeyringVector_(_dafny.SeqOfString("Failure of reproducedEncryptionContext"), m_Wrappers.Companion_Option_.Create_None_(), _0_encryptionContext, m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_SortedSets.SetToOrderedSequence2(_4_requiredEncryptionContextKeys, func(coer73 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
											return func(arg94 interface{}, arg95 interface{}) bool {
												return coer73(arg94.(uint8), arg95.(uint8))
											}
										}(func(_16_a uint8, _17_b uint8) bool {
											return (_16_a) < (_17_b)
										}))), _dafny.SeqOfString("The reproducedEncryptionContext is not correct"), Companion_Default___.RawAesKeyring(), Companion_Default___.RawAesKeyring(), m_Wrappers.Companion_Option_.Create_Some_(_14_reproducedEncryptionContext)))
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
func (_static *CompanionStruct_Default___) D() _dafny.Sequence {
	return _dafny.SeqOf(uint8(240), uint8(144), uint8(128), uint8(130))
}
func (_static *CompanionStruct_Default___) StaticNotPlaintextDataKey() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	return m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_Static_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_StaticKeyring_.Create_StaticKeyring_(_dafny.SeqOfString("no-plaintext-data-key")))
}
func (_static *CompanionStruct_Default___) Tests() _dafny.Set {
	return (((_dafny.SetOf()).Union(_dafny.SetOf(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.SeqOfString("Simplest possible happy path"), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap(), m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), Companion_Default___.StaticPlaintextDataKey(), Companion_Default___.StaticPlaintextDataKey(), m_Wrappers.Companion_Option_.Create_None_()), m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.SeqOfString("SurrogatePair Encryption Context Test"), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap().UpdateUnsafe(Companion_Default___.D(), Companion_Default___.D()), m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), Companion_Default___.RawAesKeyring(), Companion_Default___.RawAesKeyring(), m_Wrappers.Companion_Option_.Create_None_()), m_TestVectors.Companion_EncryptTestVector_.Create_NegativeEncryptKeyringVector_(_dafny.SeqOfString("Missing plaintext data key on decrypt"), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap(), m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _dafny.SeqOfString("No plaintext data key on encrypt fails"), Companion_Default___.StaticNotPlaintextDataKey()), m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptNegativeDecryptKeyringVector_(_dafny.SeqOfString("Missing plaintext data key on decrypt"), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap(), m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(Companion_Default___.StaticAlgorithmSuite()), Companion_Default___.StaticAlgorithmSuite(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _dafny.SeqOfString("No plaintext data key on encrypt fails"), Companion_Default___.StaticPlaintextDataKey(), Companion_Default___.StaticNotPlaintextDataKey(), m_Wrappers.Companion_Option_.Create_None_())))).Union(Companion_Default___.FailureBadReproducedEncryptionContext())).Union(Companion_Default___.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext())
}

// End of class Default__
