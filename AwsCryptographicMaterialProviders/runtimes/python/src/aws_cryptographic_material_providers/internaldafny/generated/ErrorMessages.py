import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping

# Module: ErrorMessages

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IncorrectRawDataKeys(datakey, keyringName, keyProviderId):
        return (((((((_dafny.Seq("EncryptedDataKey ")) + (datakey)) + (_dafny.Seq(" did not match "))) + (keyringName)) + (_dafny.Seq(". "))) + (_dafny.Seq("Expected: keyProviderId: "))) + (keyProviderId)) + (_dafny.Seq(".\n"))

    @staticmethod
    def IncorrectDataKeys(encryptedDataKeys, material, errMsg):
        d_0_valueOrError0_ = default__.IncorrectDataKeysExpectedValues(encryptedDataKeys, material, errMsg)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_expectedValue_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success((_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n")) + (d_1_expectedValue_))

    @staticmethod
    def IncorrectDataKeysExpectedValues(encryptedDataKeys, material, errMsg):
        while True:
            with _dafny.label():
                if (len(encryptedDataKeys)) == (0):
                    return Wrappers.Result_Success(errMsg)
                elif True:
                    d_0_encryptedDataKey_ = (encryptedDataKeys)[0]
                    def lambda0_(d_2_e_):
                        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_2_e_)

                    d_1_valueOrError0_ = (UTF8.default__.Decode((d_0_encryptedDataKey_).keyProviderId)).MapFailure(lambda0_)
                    if (d_1_valueOrError0_).IsFailure():
                        return (d_1_valueOrError0_).PropagateFailure()
                    elif True:
                        d_3_extractedKeyProviderId_ = (d_1_valueOrError0_).Extract()
                        def lambda1_(d_5_e_):
                            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_5_e_)

                        d_4_valueOrError1_ = (UTF8.default__.Decode((d_0_encryptedDataKey_).keyProviderInfo)).MapFailure(lambda1_)
                        if (d_4_valueOrError1_).IsFailure():
                            return (d_4_valueOrError1_).PropagateFailure()
                        elif True:
                            d_6_extractedKeyProviderInfo_ = (d_4_valueOrError1_).Extract()
                            if (d_3_extractedKeyProviderId_) != (_dafny.Seq("aws-kms-hierarchy")):
                                in0_ = _dafny.Seq((encryptedDataKeys)[1::])
                                in1_ = material
                                in2_ = (((((errMsg) + (_dafny.Seq("KeyProviderId: "))) + (d_3_extractedKeyProviderId_)) + (_dafny.Seq(", KeyProviderInfo: "))) + (d_6_extractedKeyProviderInfo_)) + (_dafny.Seq("\n"))
                                encryptedDataKeys = in0_
                                material = in1_
                                errMsg = in2_
                                raise _dafny.TailCall()
                            elif True:
                                d_7_valueOrError2_ = EdkWrapping.default__.GetProviderWrappedMaterial((d_0_encryptedDataKey_).ciphertext, material)
                                if (d_7_valueOrError2_).IsFailure():
                                    return (d_7_valueOrError2_).PropagateFailure()
                                elif True:
                                    d_8_providerWrappedMaterial_ = (d_7_valueOrError2_).Extract()
                                    d_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_ = (default__.SALT__LENGTH) + (default__.IV__LENGTH)
                                    d_10_EDK__CIPHERTEXT__VERSION__INDEX_ = (d_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_) + (default__.VERSION__LENGTH)
                                    d_11_valueOrError3_ = Wrappers.default__.Need((d_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_) < (d_10_EDK__CIPHERTEXT__VERSION__INDEX_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrong branch key version index.")))
                                    if (d_11_valueOrError3_).IsFailure():
                                        return (d_11_valueOrError3_).PropagateFailure()
                                    elif True:
                                        d_12_valueOrError4_ = Wrappers.default__.Need((len(d_8_providerWrappedMaterial_)) >= (d_10_EDK__CIPHERTEXT__VERSION__INDEX_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Incorrect ciphertext structure.")))
                                        if (d_12_valueOrError4_).IsFailure():
                                            return (d_12_valueOrError4_).PropagateFailure()
                                        elif True:
                                            d_13_branchKeyVersionUuid_ = _dafny.Seq((d_8_providerWrappedMaterial_)[d_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_:d_10_EDK__CIPHERTEXT__VERSION__INDEX_:])
                                            def lambda2_(d_15_e_):
                                                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_15_e_)

                                            d_14_valueOrError5_ = (UUID.default__.FromByteArray(d_13_branchKeyVersionUuid_)).MapFailure(lambda2_)
                                            if (d_14_valueOrError5_).IsFailure():
                                                return (d_14_valueOrError5_).PropagateFailure()
                                            elif True:
                                                d_16_branchVersion_ = (d_14_valueOrError5_).Extract()
                                                in3_ = _dafny.Seq((encryptedDataKeys)[1::])
                                                in4_ = material
                                                in5_ = (((((((errMsg) + (_dafny.Seq("KeyProviderId: "))) + (d_3_extractedKeyProviderId_)) + (_dafny.Seq(", KeyProviderInfo: "))) + (d_6_extractedKeyProviderInfo_)) + (_dafny.Seq(", BranchKeyVersion: "))) + (d_16_branchVersion_)) + (_dafny.Seq("\n"))
                                                encryptedDataKeys = in3_
                                                material = in4_
                                                errMsg = in5_
                                                raise _dafny.TailCall()
                break

    @_dafny.classproperty
    def SALT__LENGTH(instance):
        return 16
    @_dafny.classproperty
    def IV__LENGTH(instance):
        return 12
    @_dafny.classproperty
    def VERSION__LENGTH(instance):
        return 16
    @_dafny.classproperty
    def KMS__ECDH__DISCOVERY__ENCRYPT__ERROR(instance):
        return _dafny.Seq("KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")
    @_dafny.classproperty
    def RAW__ECDH__DISCOVERY__ENCRYPT__ERROR(instance):
        return _dafny.Seq("PublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")
    @_dafny.classproperty
    def RAW__ECDH__EPHEMERAL__DECRYPT__ERROR(instance):
        return _dafny.Seq("EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt.")
