// Dafny program the_program compiled into Go
package main

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
	m_TestDefaultClientProvider "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestDefaultClientProvider"
	m_TestDiscoveryGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestDiscoveryGetKeys"
	m_TestEcdhCalculation "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestEcdhCalculation"
	m_TestErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestErrorMessages"
	m_TestGetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestGetKeys"
	m_TestIntermediateKeyWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/test/TestIntermediateKeyWrapping"
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
var _ m_TestIntermediateKeyWrapping.Dummy__
var _ m_TestDefaultClientProvider.Dummy__
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
	return "_module.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Test____Main____(__noArgsParameter _dafny.Sequence) {
	var _0_success bool
	_ = _0_success
	_0_success = true
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetBeaconKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _1_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_1_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetBeaconKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetActiveKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _2_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_2_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetActiveKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetActiveMrkKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _3_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_3_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetActiveMrkKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetBranchKeyVersion: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _4_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_4_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetBranchKeyVersion()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetActiveKeyWithIncorrectKmsKeyArn: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _5_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_5_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetActiveKeyWithIncorrectKmsKeyArn()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetActiveKeyWrongLogicalKeyStoreName: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _6_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_6_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetActiveKeyWrongLogicalKeyStoreName()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetActiveKeyDoesNotExistFails: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _7_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_7_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetActiveKeyDoesNotExistFails()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestGetKeys.TestGetActiveKeyWithNoClients: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _8_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_8_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestGetKeys.Companion_Default___.TestGetActiveKeyWithNoClients()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestDiscoveryGetKeys.TestGetBeaconKeyForTwoKmsArnsSuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _9_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_9_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestDiscoveryGetKeys.Companion_Default___.TestGetBeaconKeyForTwoKmsArnsSuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestDiscoveryGetKeys.TestGetActiveKeyForTwoKmsArnsSuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _10_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_10_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestDiscoveryGetKeys.Companion_Default___.TestGetActiveKeyForTwoKmsArnsSuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestDiscoveryGetKeys.TestGetBranchKeyVersionForTwoKmsArnsSuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _11_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_11_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestDiscoveryGetKeys.Companion_Default___.TestGetBranchKeyVersionForTwoKmsArnsSuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestDiscoveryGetKeys.TestGetKeysForMrk: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _12_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_12_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestDiscoveryGetKeys.Companion_Default___.TestGetKeysForMrk()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestCreateKeys.TestCreateBranchAndBeaconKeys: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _13_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_13_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestCreateKeys.Companion_Default___.TestCreateBranchAndBeaconKeys()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestCreateKeys.TestCreateOptions: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _14_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_14_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestCreateKeys.Companion_Default___.TestCreateOptions()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestCreateKeys.TestCreateDuplicate: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _15_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_15_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestCreateKeys.Companion_Default___.TestCreateDuplicate()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestCreateKeys.InsertingADuplicateWillFail: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _16_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_16_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestCreateKeys.Companion_Default___.InsertingADuplicateWillFail()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestCreateKeys.InsertingADuplicateWillWithADifferentVersionFail: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _17_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_17_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestCreateKeys.Companion_Default___.InsertingADuplicateWillWithADifferentVersionFail()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestCreateKeyStore.TestCreateKeyStore: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _18_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_18_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestCreateKeyStore.Companion_Default___.TestCreateKeyStore()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestLyingBranchKey.TestGetActiveKeyForLyingBranchKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _19_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_19_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestLyingBranchKey.Companion_Default___.TestGetActiveKeyForLyingBranchKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestLyingBranchKey.TestGetBranchKeyVersionForLyingBranchKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _20_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_20_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestLyingBranchKey.Companion_Default___.TestGetBranchKeyVersionForLyingBranchKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestLyingBranchKey.TestGetBeaconKeyForLyingBranchKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _21_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_21_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestLyingBranchKey.Companion_Default___.TestGetBeaconKeyForLyingBranchKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestLyingBranchKey.TestVersionKeyForLyingBranchKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _22_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_22_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestLyingBranchKey.Companion_Default___.TestVersionKeyForLyingBranchKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestVersionKey.TestVersionKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _23_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_23_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestVersionKey.Companion_Default___.TestVersionKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestVersionKey.TestVersionKeyWithEC: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _24_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_24_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestVersionKey.Companion_Default___.TestVersionKeyWithEC()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestVersionKey.TestMrkVersionKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _25_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_25_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestVersionKey.Companion_Default___.TestMrkVersionKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestVersionKey.InsertingADuplicateVersionWillFail: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _26_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_26_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestVersionKey.Companion_Default___.InsertingADuplicateVersionWillFail()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestVersionKey.VersioningANonexistentBranchKeyWillFail: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _27_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_27_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestVersionKey.Companion_Default___.VersioningANonexistentBranchKeyWillFail()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestConfig.TestInvalidKmsKeyArnConfig: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _28_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_28_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestConfig.Companion_Default___.TestInvalidKmsKeyArnConfig()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestConfig.TestInvalidKmsKeyArnAliasConfig: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _29_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_29_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestConfig.Companion_Default___.TestInvalidKmsKeyArnAliasConfig()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestConfig.TestValidConfig: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _30_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_30_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestConfig.Companion_Default___.TestValidConfig()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestConfig.TestValidConfigNoClients: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _31_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_31_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestConfig.Companion_Default___.TestValidConfigNoClients()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestErrorMessages.TestIncorrectRawDataKeys: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _32_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_32_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestErrorMessages.Companion_Default___.TestIncorrectRawDataKeys()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestErrorMessages.TestIncorrectDataKeys: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _33_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_33_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestErrorMessages.Companion_Default___.TestIncorrectDataKeys()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestStormTracker.StormTrackerBasics: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _34_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_34_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestStormTracker.Companion_Default___.StormTrackerBasics()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestStormTracker.StormTrackerFanOut: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _35_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_35_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestStormTracker.Companion_Default___.StormTrackerFanOut()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestStormTracker.StormTrackerTTL: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _36_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_36_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestStormTracker.Companion_Default___.StormTrackerTTL()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestStormTracker.StormTrackerGraceInterval: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _37_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_37_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestStormTracker.Companion_Default___.StormTrackerGraceInterval()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestStormTracker.StormTrackerGracePeriod: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _38_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_38_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestStormTracker.Companion_Default___.StormTrackerGracePeriod()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestLocalCMC.LocalCMCBasics: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _39_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_39_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestLocalCMC.Companion_Default___.LocalCMCBasics()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestRawEcdhDiscoveryOnEncryptFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _40_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_40_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestRawEcdhDiscoveryOnEncryptFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestRawEcdhEphemeralOnDecryptFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _41_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_41_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestRawEcdhEphemeralOnDecryptFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _42_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_42_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestRawEcdhKeyringStaticSuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _43_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_43_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestRawEcdhKeyringStaticSuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestTwoRawEcdhKeyringStaticSuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _44_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_44_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestTwoRawEcdhKeyringStaticSuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestTwoEcdhKeyringStaticSuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _45_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_45_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestTwoEcdhKeyringStaticSuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _46_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_46_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _47_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_47_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawECDHKeyring.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionCombinationsFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _48_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_48_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawECDHKeyring.Companion_Default___.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionCombinationsFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEncryptedDataKeyFilter.TestFailsNonKeyResource: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _49_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_49_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEncryptedDataKeyFilter.Companion_Default___.TestFailsNonKeyResource()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEncryptedDataKeyFilter.TestMatchesKeyringsConfiguration: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _50_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_50_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEncryptedDataKeyFilter.Companion_Default___.TestMatchesKeyringsConfiguration()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhConfigurationFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _51_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_51_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhConfigurationFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _52_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_52_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _53_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_53_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringDiscoverySuccess: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _54_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_54_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhKeyringDiscoverySuccess()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _55_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_55_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringWithDerPublicKeys: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _56_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_56_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhKeyringWithDerPublicKeys()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhRawEcdhKeyringWithDerPublicKeys: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _57_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_57_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhRawEcdhKeyringWithDerPublicKeys()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _58_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_58_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _59_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_59_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsEcdhKeyring.TestLyingKmsKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _60_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_60_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsEcdhKeyring.Companion_Default___.TestLyingKmsKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestHierarchyClientESDKSuite: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _61_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_61_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestHierarchyClientESDKSuite()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestHierarchyClientDBESuite: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _62_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_62_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestHierarchyClientDBESuite()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestBranchKeyIdSupplier: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _63_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_63_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestBranchKeyIdSupplier()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestInvalidDataKeyError: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _64_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_64_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestInvalidDataKeyError()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestSharedCacheWithSamePartitionIdAndSameLogicalKeyStoreName: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _65_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_65_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestSharedCacheWithSamePartitionIdAndSameLogicalKeyStoreName()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestSharedCacheWithDifferentUnspecifiedPartitionIdAndSameLogicalKeyStoreName: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _66_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_66_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestSharedCacheWithDifferentUnspecifiedPartitionIdAndSameLogicalKeyStoreName()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestSharedCacheWithDifferentSpecifiedPartitionIdAndSameLogicalKeyStoreName: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _67_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_67_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestSharedCacheWithDifferentSpecifiedPartitionIdAndSameLogicalKeyStoreName()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsHierarchicalKeyring.TestSharedCacheWithSamePartitionIdAndDifferentLogicalKeyStoreName: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _68_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_68_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsHierarchicalKeyring.Companion_Default___.TestSharedCacheWithSamePartitionIdAndDifferentLogicalKeyStoreName()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsRsaKeyring.TestKmsRsaRoundtrip: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _69_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_69_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsRsaKeyring.Companion_Default___.TestKmsRsaRoundtrip()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestAwsKmsRsaKeyring.TestKmsRsaWithAsymmetricSignatureFails: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _70_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_70_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestAwsKmsRsaKeyring.Companion_Default___.TestKmsRsaWithAsymmetricSignatureFails()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawAESKeyring.TestOnEncryptOnDecryptGenerateDataKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _71_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_71_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawAESKeyring.Companion_Default___.TestOnEncryptOnDecryptGenerateDataKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawAESKeyring.TestOnEncryptOnDecryptSuppliedDataKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _72_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_72_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawAESKeyring.Companion_Default___.TestOnEncryptOnDecryptSuppliedDataKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawAESKeyring.TestOnDecryptKeyNameMismatch: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _73_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_73_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawAESKeyring.Companion_Default___.TestOnDecryptKeyNameMismatch()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawAESKeyring.TestOnDecryptBadAndGoodEdkSucceeds: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _74_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_74_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawAESKeyring.Companion_Default___.TestOnDecryptBadAndGoodEdkSucceeds()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawAESKeyring.TestOnDecryptNoEDKs: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _75_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_75_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawAESKeyring.Companion_Default___.TestOnDecryptNoEDKs()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawAESKeyring.TestOnEncryptUnserializableEC: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _76_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_76_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawAESKeyring.Companion_Default___.TestOnEncryptUnserializableEC()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawAESKeyring.TestOnDecryptUnserializableEC: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _77_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_77_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawAESKeyring.Companion_Default___.TestOnDecryptUnserializableEC()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestMultiKeyring.TestHappyCase: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _78_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_78_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestMultiKeyring.Companion_Default___.TestHappyCase()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestMultiKeyring.TestChildKeyringFailureEncrypt: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _79_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_79_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestMultiKeyring.Companion_Default___.TestChildKeyringFailureEncrypt()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestMultiKeyring.TestGeneratorKeyringFails: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _80_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_80_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestMultiKeyring.Companion_Default___.TestGeneratorKeyringFails()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestMultiKeyring.TestGeneratorKeyringDoesNotReturnPlaintextDataKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _81_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_81_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestMultiKeyring.Companion_Default___.TestGeneratorKeyringDoesNotReturnPlaintextDataKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestMultiKeyring.TestGeneratorAbleToDecrypt: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _82_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_82_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestMultiKeyring.Companion_Default___.TestGeneratorAbleToDecrypt()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestMultiKeyring.TestGeneratorUnableToDecrypt: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _83_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_83_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestMultiKeyring.Companion_Default___.TestGeneratorUnableToDecrypt()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestMultiKeyring.TestCollectFailuresDecrypt: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _84_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_84_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestMultiKeyring.Companion_Default___.TestCollectFailuresDecrypt()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawRSAKeying.TestOnEncryptOnDecryptSuppliedDataKey: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _85_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_85_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawRSAKeying.Companion_Default___.TestOnEncryptOnDecryptSuppliedDataKey()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawRSAKeying.TestOnDecryptKeyNameMismatch: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _86_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_86_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawRSAKeying.Companion_Default___.TestOnDecryptKeyNameMismatch()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawRSAKeying.TestOnDecryptFailure: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _87_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_87_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawRSAKeying.Companion_Default___.TestOnDecryptFailure()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestRawRSAKeying.TestOnDecryptBadAndGoodEdkSucceeds: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _88_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_88_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestRawRSAKeying.Companion_Default___.TestOnDecryptBadAndGoodEdkSucceeds()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestEcdhCalculation.TestKmsDeriveSharedSecretOfflineCalculation: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _89_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_89_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestEcdhCalculation.Companion_Default___.TestKmsDeriveSharedSecretOfflineCalculation()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestEcdhCalculation.TestKmsDeriveSharedSecretOfflineCalculationCurves: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _90_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_90_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestEcdhCalculation.Companion_Default___.TestKmsDeriveSharedSecretOfflineCalculationCurves()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestEcdhCalculation.TestOfflineDeriveSharedSecretStaticKeys: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _91_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_91_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestEcdhCalculation.Companion_Default___.TestOfflineDeriveSharedSecretStaticKeys()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestIntermediateKeyWrapping.IntermediateWrapUnwrapTest: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _92_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_92_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestIntermediateKeyWrapping.Companion_Default___.IntermediateWrapUnwrapTest()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestIntermediateKeyWrapping.IntermediateGenerateAndWrapUnwrapTest: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _93_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_93_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestIntermediateKeyWrapping.Companion_Default___.IntermediateGenerateAndWrapUnwrapTest()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	_dafny.Print((_dafny.SeqOfString("TestDefaultClientProvider.GetUsWestTwo: ")).SetString())
	func() {
		defer func() {
			if r := recover(); r != nil {
				var _94_haltMessage = _dafny.SeqOfString(r.(string))
				{
					_dafny.Print((_dafny.SeqOfString("FAILED\n	")).SetString())
					_dafny.Print((_94_haltMessage).SetString())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_0_success = false
				}
			}
		}()
		{
			m_TestDefaultClientProvider.Companion_Default___.GetUsWestTwo()
			{
				_dafny.Print((_dafny.SeqOfString("PASSED\n")).SetString())
			}
		}
	}()
	if !(_0_success) {
		panic("<stdin>(1,0): " + (_dafny.SeqOfString("Test failures occurred: see above.\n")).String())
	}
}

// End of class Default__
func main() {
	defer _dafny.CatchHalt()
	Companion_Default___.Test____Main____(_dafny.FromMainArguments(os.Args))
}
