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
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations

# Module: MaterialProviders

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultMaterialProvidersConfig():
        return AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig_MaterialProvidersConfig()

    @staticmethod
    def MaterialProviders(config):
        res: Wrappers.Result = None
        d_1364_maybeCrypto_: Wrappers.Result
        out233_: Wrappers.Result
        out233_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_1364_maybeCrypto_ = out233_
        d_1365_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_1366_valueOrError0_: Wrappers.Result = None
        def lambda111_(d_1367_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1367_e_)

        d_1366_valueOrError0_ = (d_1364_maybeCrypto_).MapFailure(lambda111_)
        if (d_1366_valueOrError0_).IsFailure():
            res = (d_1366_valueOrError0_).PropagateFailure()
            return res
        d_1365_cryptoPrimitivesX_ = (d_1366_valueOrError0_).Extract()
        d_1368_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_1368_cryptoPrimitives_ = d_1365_cryptoPrimitivesX_
        d_1369_client_: MaterialProvidersClient
        nw72_ = MaterialProvidersClient()
        nw72_.ctor__(AwsCryptographyMaterialProvidersOperations.Config_Config(d_1368_cryptoPrimitives_))
        d_1369_client_ = nw72_
        res = Wrappers.Result_Success(d_1369_client_)
        return res
        return res

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class MaterialProvidersClient(AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient):
    def  __init__(self):
        self._i_config: AwsCryptographyMaterialProvidersOperations.Config = None
        pass

    def __dafnystr__(self) -> str:
        return "MaterialProviders.MaterialProvidersClient"
    def ctor__(self, config):
        (self)._i_config = config

    def CreateAwsKmsKeyring(self, input):
        output: Wrappers.Result = None
        out234_: Wrappers.Result
        out234_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsKeyring((self).config, input)
        output = out234_
        return output

    def CreateAwsKmsDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out235_: Wrappers.Result
        out235_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryKeyring((self).config, input)
        output = out235_
        return output

    def CreateAwsKmsMultiKeyring(self, input):
        output: Wrappers.Result = None
        out236_: Wrappers.Result
        out236_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMultiKeyring((self).config, input)
        output = out236_
        return output

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out237_: Wrappers.Result
        out237_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryMultiKeyring((self).config, input)
        output = out237_
        return output

    def CreateAwsKmsMrkKeyring(self, input):
        output: Wrappers.Result = None
        out238_: Wrappers.Result
        out238_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkKeyring((self).config, input)
        output = out238_
        return output

    def CreateAwsKmsMrkMultiKeyring(self, input):
        output: Wrappers.Result = None
        out239_: Wrappers.Result
        out239_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkMultiKeyring((self).config, input)
        output = out239_
        return output

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out240_: Wrappers.Result
        out240_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryKeyring((self).config, input)
        output = out240_
        return output

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out241_: Wrappers.Result
        out241_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryMultiKeyring((self).config, input)
        output = out241_
        return output

    def CreateAwsKmsHierarchicalKeyring(self, input):
        output: Wrappers.Result = None
        out242_: Wrappers.Result
        out242_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsHierarchicalKeyring((self).config, input)
        output = out242_
        return output

    def CreateMultiKeyring(self, input):
        output: Wrappers.Result = None
        out243_: Wrappers.Result
        out243_ = AwsCryptographyMaterialProvidersOperations.default__.CreateMultiKeyring((self).config, input)
        output = out243_
        return output

    def CreateRawAesKeyring(self, input):
        output: Wrappers.Result = None
        out244_: Wrappers.Result
        out244_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawAesKeyring((self).config, input)
        output = out244_
        return output

    def CreateRawRsaKeyring(self, input):
        output: Wrappers.Result = None
        out245_: Wrappers.Result
        out245_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawRsaKeyring((self).config, input)
        output = out245_
        return output

    def CreateAwsKmsRsaKeyring(self, input):
        output: Wrappers.Result = None
        out246_: Wrappers.Result
        out246_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsRsaKeyring((self).config, input)
        output = out246_
        return output

    def CreateDefaultCryptographicMaterialsManager(self, input):
        output: Wrappers.Result = None
        out247_: Wrappers.Result
        out247_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultCryptographicMaterialsManager((self).config, input)
        output = out247_
        return output

    def CreateRequiredEncryptionContextCMM(self, input):
        output: Wrappers.Result = None
        out248_: Wrappers.Result
        out248_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRequiredEncryptionContextCMM((self).config, input)
        output = out248_
        return output

    def CreateCryptographicMaterialsCache(self, input):
        output: Wrappers.Result = None
        out249_: Wrappers.Result
        out249_ = AwsCryptographyMaterialProvidersOperations.default__.CreateCryptographicMaterialsCache((self).config, input)
        output = out249_
        return output

    def CreateDefaultClientSupplier(self, input):
        output: Wrappers.Result = None
        out250_: Wrappers.Result
        out250_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier((self).config, input)
        output = out250_
        return output

    def InitializeEncryptionMaterials(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.InitializeEncryptionMaterials((self).config, input)

    def InitializeDecryptionMaterials(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.InitializeDecryptionMaterials((self).config, input)

    def ValidEncryptionMaterialsTransition(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidEncryptionMaterialsTransition((self).config, input)

    def ValidDecryptionMaterialsTransition(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidDecryptionMaterialsTransition((self).config, input)

    def EncryptionMaterialsHasPlaintextDataKey(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.EncryptionMaterialsHasPlaintextDataKey((self).config, input)

    def DecryptionMaterialsWithPlaintextDataKey(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.DecryptionMaterialsWithPlaintextDataKey((self).config, input)

    def GetAlgorithmSuiteInfo(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.GetAlgorithmSuiteInfo((self).config, input)

    def ValidAlgorithmSuiteInfo(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidAlgorithmSuiteInfo((self).config, input)

    def ValidateCommitmentPolicyOnEncrypt(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidateCommitmentPolicyOnEncrypt((self).config, input)

    def ValidateCommitmentPolicyOnDecrypt(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidateCommitmentPolicyOnDecrypt((self).config, input)

    @property
    def config(self):
        return self._i_config
