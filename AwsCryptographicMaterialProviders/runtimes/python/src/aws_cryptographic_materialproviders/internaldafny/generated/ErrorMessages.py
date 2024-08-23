import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping

# Module: ErrorMessages

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IncorrectRawDataKeys(datakey, keyringName, keyProviderId):
        return (((((((_dafny.Seq("EncryptedDataKey ")) + (datakey)) + (_dafny.Seq(" did not match "))) + (keyringName)) + (_dafny.Seq(". "))) + (_dafny.Seq("Expected: keyProviderId: "))) + (keyProviderId)) + (_dafny.Seq(".\n"))

    @staticmethod
    def IncorrectDataKeys(encryptedDataKeys, material, errMsg):
        d_540_valueOrError0_ = default__.IncorrectDataKeysExpectedValues(encryptedDataKeys, material, errMsg)
        if (d_540_valueOrError0_).IsFailure():
            return (d_540_valueOrError0_).PropagateFailure()
        elif True:
            d_541_expectedValue_ = (d_540_valueOrError0_).Extract()
            return Wrappers.Result_Success((_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n")) + (d_541_expectedValue_))

    @staticmethod
    def IncorrectDataKeysExpectedValues(encryptedDataKeys, material, errMsg):
        while True:
            with _dafny.label():
                if (len(encryptedDataKeys)) == (0):
                    return Wrappers.Result_Success(errMsg)
                elif True:
                    d_542_encryptedDataKey_ = (encryptedDataKeys)[0]
                    def lambda57_(d_544_e_):
                        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_544_e_)

                    d_543_valueOrError0_ = (UTF8.default__.Decode((d_542_encryptedDataKey_).keyProviderId)).MapFailure(lambda57_)
                    if (d_543_valueOrError0_).IsFailure():
                        return (d_543_valueOrError0_).PropagateFailure()
                    elif True:
                        d_545_extractedKeyProviderId_ = (d_543_valueOrError0_).Extract()
                        def lambda58_(d_547_e_):
                            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_547_e_)

                        d_546_valueOrError1_ = (UTF8.default__.Decode((d_542_encryptedDataKey_).keyProviderInfo)).MapFailure(lambda58_)
                        if (d_546_valueOrError1_).IsFailure():
                            return (d_546_valueOrError1_).PropagateFailure()
                        elif True:
                            d_548_extractedKeyProviderInfo_ = (d_546_valueOrError1_).Extract()
                            if (d_545_extractedKeyProviderId_) != (_dafny.Seq("aws-kms-hierarchy")):
                                in2_ = _dafny.Seq((encryptedDataKeys)[1::])
                                in3_ = material
                                in4_ = (((((errMsg) + (_dafny.Seq("KeyProviderId: "))) + (d_545_extractedKeyProviderId_)) + (_dafny.Seq(", KeyProviderInfo: "))) + (d_548_extractedKeyProviderInfo_)) + (_dafny.Seq("\n"))
                                encryptedDataKeys = in2_
                                material = in3_
                                errMsg = in4_
                                raise _dafny.TailCall()
                            elif True:
                                d_549_valueOrError2_ = EdkWrapping.default__.GetProviderWrappedMaterial((d_542_encryptedDataKey_).ciphertext, material)
                                if (d_549_valueOrError2_).IsFailure():
                                    return (d_549_valueOrError2_).PropagateFailure()
                                elif True:
                                    d_550_providerWrappedMaterial_ = (d_549_valueOrError2_).Extract()
                                    d_551_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_ = (default__.SALT__LENGTH) + (default__.IV__LENGTH)
                                    d_552_EDK__CIPHERTEXT__VERSION__INDEX_ = (d_551_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_) + (default__.VERSION__LENGTH)
                                    d_553_valueOrError3_ = Wrappers.default__.Need((d_551_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_) < (d_552_EDK__CIPHERTEXT__VERSION__INDEX_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrong branch key version index.")))
                                    if (d_553_valueOrError3_).IsFailure():
                                        return (d_553_valueOrError3_).PropagateFailure()
                                    elif True:
                                        d_554_valueOrError4_ = Wrappers.default__.Need((len(d_550_providerWrappedMaterial_)) >= (d_552_EDK__CIPHERTEXT__VERSION__INDEX_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Incorrect ciphertext structure.")))
                                        if (d_554_valueOrError4_).IsFailure():
                                            return (d_554_valueOrError4_).PropagateFailure()
                                        elif True:
                                            d_555_branchKeyVersionUuid_ = _dafny.Seq((d_550_providerWrappedMaterial_)[d_551_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX_:d_552_EDK__CIPHERTEXT__VERSION__INDEX_:])
                                            def lambda59_(d_557_e_):
                                                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_557_e_)

                                            d_556_valueOrError5_ = (UUID.default__.FromByteArray(d_555_branchKeyVersionUuid_)).MapFailure(lambda59_)
                                            if (d_556_valueOrError5_).IsFailure():
                                                return (d_556_valueOrError5_).PropagateFailure()
                                            elif True:
                                                d_558_branchVersion_ = (d_556_valueOrError5_).Extract()
                                                in5_ = _dafny.Seq((encryptedDataKeys)[1::])
                                                in6_ = material
                                                in7_ = (((((((errMsg) + (_dafny.Seq("KeyProviderId: "))) + (d_545_extractedKeyProviderId_)) + (_dafny.Seq(", KeyProviderInfo: "))) + (d_548_extractedKeyProviderInfo_)) + (_dafny.Seq(", BranchKeyVersion: "))) + (d_558_branchVersion_)) + (_dafny.Seq("\n"))
                                                encryptedDataKeys = in5_
                                                material = in6_
                                                errMsg = in7_
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
