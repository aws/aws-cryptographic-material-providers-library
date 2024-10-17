import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
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
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
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
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
import TestLyingBranchKey as TestLyingBranchKey
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys
import TestVersionKey as TestVersionKey

# Module: TestUtils

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateInvalidEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_0_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(115,46): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_validUTF8char_: _dafny.Seq
        d_1_validUTF8char_ = (d_0_valueOrError0_).Extract()
        d_2_key_: _dafny.Seq
        d_2_key_ = _dafny.Seq([])
        while (len(d_2_key_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT):
            d_2_key_ = (d_2_key_) + (d_1_validUTF8char_)
        encCtx = _dafny.Map({d_2_key_: _dafny.Seq([0])})
        return encCtx

    @staticmethod
    def GenerateLargeValidEncryptionContext():
        r: _dafny.Map = _dafny.Map({})
        d_0_numMaxPairs_: int
        d_0_numMaxPairs_ = 9361
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(135,15): " + _dafny.string_of(d_1_valueOrError0_))
        d_2_val_: _dafny.Seq
        d_2_val_ = (d_1_valueOrError0_).Extract()
        d_3_encCtx_: _dafny.Map
        d_3_encCtx_ = _dafny.Map({})
        d_4_i_: int
        d_4_i_ = 0
        while ((len(d_3_encCtx_)) < (d_0_numMaxPairs_)) and ((d_4_i_) < (65536)):
            d_5_key_: _dafny.Seq
            d_5_key_ = StandardLibrary_UInt.default__.UInt16ToSeq(d_4_i_)
            if UTF8.default__.ValidUTF8Seq(d_5_key_):
                d_3_encCtx_ = (d_3_encCtx_).set(d_5_key_, d_2_val_)
            d_4_i_ = (d_4_i_) + (1)
        r = d_3_encCtx_
        return r
        return r

    @staticmethod
    def SmallEncryptionContext(v):
        encryptionContext: _dafny.Map = _dafny.Map({})
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_0_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(163,16): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_keyA_: _dafny.Seq
        d_1_keyA_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_2_valueOrError1_ = UTF8.default__.Encode(_dafny.Seq("valA"))
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(164,16): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_valA_: _dafny.Seq
        d_3_valA_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_4_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("keyB"))
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(165,16): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_keyB_: _dafny.Seq
        d_5_keyB_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_6_valueOrError3_ = UTF8.default__.Encode(_dafny.Seq("valB"))
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(166,16): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_valB_: _dafny.Seq
        d_7_valB_ = (d_6_valueOrError3_).Extract()
        source0_ = v
        with _dafny.label("match0"):
            if True:
                if source0_.is_Empty:
                    encryptionContext = _dafny.Map({})
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_A:
                    encryptionContext = _dafny.Map({d_1_keyA_: d_3_valA_})
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_AB:
                    encryptionContext = _dafny.Map({d_1_keyA_: d_3_valA_, d_5_keyB_: d_7_valB_})
                    raise _dafny.Break("match0")
            if True:
                encryptionContext = _dafny.Map({d_5_keyB_: d_7_valB_, d_1_keyA_: d_3_valA_})
            pass
        return encryptionContext

    @staticmethod
    def GenerateMockEncryptedDataKey(keyProviderId, keyProviderInfo):
        edk: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey.default()()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_0_valueOrError0_ = UTF8.default__.Encode(keyProviderId)
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(186,32): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_encodedkeyProviderId_: _dafny.Seq
        d_1_encodedkeyProviderId_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_2_valueOrError1_ = UTF8.default__.Encode(keyProviderInfo)
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(187,34): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_encodedKeyProviderInfo_: _dafny.Seq
        d_3_encodedKeyProviderInfo_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_4_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("fakeCiphertext"))
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(188,26): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_fakeCiphertext_: _dafny.Seq
        d_5_fakeCiphertext_ = (d_4_valueOrError2_).Extract()
        edk = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(d_1_encodedkeyProviderId_, d_3_encodedKeyProviderInfo_, d_5_fakeCiphertext_)
        return edk
        return edk

    @staticmethod
    def NamespaceAndName(n):
        namespace: _dafny.Seq = _dafny.Seq("")
        name: _dafny.Seq = _dafny.Seq("")
        d_0_s_: _dafny.Seq
        d_0_s_ = (_dafny.Seq("child")) + (_dafny.Seq([_dafny.plus_char(chr(n), '0')]))
        namespace = (d_0_s_) + (_dafny.Seq(" Namespace"))
        name = (d_0_s_) + (_dafny.Seq(" Name"))
        return namespace, name

    @_dafny.classproperty
    def KMS__RSA__PUBLIC__KEY(instance):
        return ((((((((_dafny.Seq("-----BEGIN PUBLIC KEY-----\n")) + (_dafny.Seq("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA27Uc/fBaMVhxCE/SpCMQ\n"))) + (_dafny.Seq("oSBRSzQJw+o2hBaA+FiPGtiJ/aPy7sn18aCkelaSj4kwoC79b/arNHlkjc7OJFsN\n"))) + (_dafny.Seq("/GoFKgNvaiY4lOeJqEiWQGSSgHtsJLdbO2u4OOSxh8qIRAMKbMgQDVX4FR/PLKeK\n"))) + (_dafny.Seq("fc2aCDvcNSpAM++8NlNmv7+xQBJydr5ce91eISbHkFRkK3/bAM+1iddupoRw4Wo2\n"))) + (_dafny.Seq("r3avzrg5xBHmzR7u1FTab22Op3Hgb2dBLZH43wNKAceVwKqKA8UNAxashFON7xK9\n"))) + (_dafny.Seq("yy4kfOL0Z/nhxRKe4jRZ/5v508qIzgzCksYy7Y3QbMejAtiYnr7s5/d5KWw0swou\n"))) + (_dafny.Seq("twIDAQAB\n"))) + (_dafny.Seq("-----END PUBLIC KEY-----"))
    @_dafny.classproperty
    def KMS__RSA__PRIVATE__KEY__ARN(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297")
    @_dafny.classproperty
    def SHARED__TEST__KEY__ARN(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
    @_dafny.classproperty
    def ACCOUNT__IDS(instance):
        return _dafny.Seq([_dafny.Seq("658956600833")])
    @_dafny.classproperty
    def PARTITION(instance):
        return _dafny.Seq("aws")
    @_dafny.classproperty
    def KMS__ECC__256__KEY__ARN__S(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9")
    @_dafny.classproperty
    def KMS__ECC__256__KEY__ARN__R(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5")
    @_dafny.classproperty
    def KMS__ECC__384__KEY__ARN__S(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/7f35a704-f4fb-469d-98b1-62a1fa2cc44e")
    @_dafny.classproperty
    def KMS__ECC__384__KEY__ARN__R(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/29f0bef9-1677-4e74-b67e-acefab1295ff")
    @_dafny.classproperty
    def KMS__ECC__521__KEY__ARN__S(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/41b502e3-cc9d-442f-bd7b-d67faed0f22e")
    @_dafny.classproperty
    def KMS__ECC__521__KEY__ARN__R(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/c45f1043-53bb-4f37-adc5-4d25d4a84f9d")
    @_dafny.classproperty
    def KMS__ECC__256__PUBLIC__KEY__S(instance):
        return _dafny.Seq("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE18m54QsLUnhWU7gT8hkAceNbZ/WBGNUUSPCeIKqOyX5psiqyC1TXPOJXqKKaVv5Mg91WV9UjpboblOhNU35nRw==")
    @_dafny.classproperty
    def KMS__ECC__256__PUBLIC__KEY__R(instance):
        return _dafny.Seq("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9istdPCuX9nF8EmA4tioe/k0TCa2M9VeBW1N9n0sxPA6uPVOfLtE4+KuYxAGT0dYoK6CY93nowUy1yS+R7A+wA==")
    @_dafny.classproperty
    def KMS__ECC__384__PUBLIC__KEY__S(instance):
        return _dafny.Seq("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEfQ0OHFvwskFVjQwfqV7jpo62I6uyGY+5SPRZb6CuJ96bVreLZXh485BcPv09O/DWnpTBm8LL+YcfsqM3ECvi2ee3bDGpH6xIdr28uvyG75t5wqBjYYtZQFDf/ydfG9mm")
    @_dafny.classproperty
    def KMS__ECC__384__PUBLIC__KEY__R(instance):
        return _dafny.Seq("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEWgGNWQ+vEwlMxyMQkSsOAYGfT6IlgEkcanEOSjbeEpEnh8JHEiBHQ6QaROxJ7c3nEkbjbi0m+7ejBEGtkiqaY5Dsv5u1iV4fc/2v1RzPba1ZtudEmM16Eyy9LHswdJ7v")
    @_dafny.classproperty
    def KMS__ECC__521__PUBLIC__KEY__S(instance):
        return _dafny.Seq("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAz86qnfp3s0cl+73PQhlUstfdg9EZDA/jtLjBTWYp/1EB7RHNm8q5hMg5kBfjRDUFhbRBMlUV1xBOTgqzoSWj4oAABnQKiXXGGyu6PMN4D9nVMDsOpJ1pWU7rQexWDahBrK+5hx3beFXUpvvFRQrGAt2icUXm18VO6Qwbp0da9jyGDSY=")
    @_dafny.classproperty
    def KMS__ECC__521__PUBLIC__KEY__R(instance):
        return _dafny.Seq("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAxLxcjtYfqc4+4oJZY0gGv2Ehu++CnVFea6uwXgEgLifq4eDSSVmQYvU8majsufpBXQwVjnDlQ7pGRw1j6K4FaLAAgYuMrmrwKtx/ZZtkbXzCwrqJY+sfCk8U5m89DX331cdBAhR2uVSPL2d5hp8up5v+EBpNArtdC5lZMx2ZrwKKYuQ=")
    @_dafny.classproperty
    def ECC__P256__PRIVATE(instance):
        return ((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n"))) + (_dafny.Seq("22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n"))) + (_dafny.Seq("7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))
    @_dafny.classproperty
    def ECC__P256__PUBLIC(instance):
        return _dafny.Seq("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEp1IMe0q5R4TyJ9zHGX3N3BCLPPlxX+yb4XLldcFhCxmfAI7sJyoxNInpRMEmOR2M1ghe+9xbyWlhmBmBoUm2vA==")
    @_dafny.classproperty
    def ECC__P256__PRIVATE__R(instance):
        return ((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgxpnoWJBwDUkwvLHA\n"))) + (_dafny.Seq("YZgRRby9FdJtxAMvAcPPW6iaD+2hRANCAASihMmHeVwzccmYmFKPO5rlR+M3MBRH\n"))) + (_dafny.Seq("zdCaw8TGxfX25tCKkhQUm6kUlPqaCzirEYPbUt3wK8XJ6jF5iRzuGxad\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----\n"))
    @_dafny.classproperty
    def ECC__P256__PUBLIC__R(instance):
        return _dafny.Seq("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEooTJh3lcM3HJmJhSjzua5UfjNzAUR83QmsPExsX19ubQipIUFJupFJT6mgs4qxGD21Ld8CvFyeoxeYkc7hsWnQ==")
    @_dafny.classproperty
    def ECC__P384__PRIVATE(instance):
        return (((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n"))) + (_dafny.Seq("6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n"))) + (_dafny.Seq("GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n"))) + (_dafny.Seq("b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))
    @_dafny.classproperty
    def ECC__P384__PUBLIC(instance):
        return _dafny.Seq("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEGsj1ugd2lRilhQWwx90nrjIYmNhiDxvrQRB5jGd0FGhuqjZ0MV0vkKUfeSFskFmYyJ8g5NrqXm9U4rz9FGGsvnSEvDKwRTO6CwbCSKsRokUNRDxSKQS7+JprXjpmuarf")
    @_dafny.classproperty
    def ECC__P384__PRIVATE__R(instance):
        return (((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDBX0BpijAta/CndWCkA\n"))) + (_dafny.Seq("hl4fu2mIlnsh8umliaBBDHjA2T/3eeYWid5m96Bs2QxYIn6hZANiAAR/qhoNylqV\n"))) + (_dafny.Seq("2084hlZEXr8XWj9DuZ0WHgJ/rniicwqxXEFwPCkeh7VvpO7+tN8HxUoWpPLSdkCK\n"))) + (_dafny.Seq("nWeq6senikNb4RNp3Na43wPyF2SjQI/uzujHjlrVrea2zvJP7rsLdAI=\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----\n"))
    @_dafny.classproperty
    def ECC__P384__PUBLIC__R(instance):
        return _dafny.Seq("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEf6oaDcpaldtPOIZWRF6/F1o/Q7mdFh4Cf654onMKsVxBcDwpHoe1b6Tu/rTfB8VKFqTy0nZAip1nqurHp4pDW+ETadzWuN8D8hdko0CP7s7ox45a1a3mts7yT+67C3QC")
    @_dafny.classproperty
    def ECC__P521__PRIVATE(instance):
        return (((((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n"))) + (_dafny.Seq("xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n"))) + (_dafny.Seq("oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n"))) + (_dafny.Seq("I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n"))) + (_dafny.Seq("C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n"))) + (_dafny.Seq("Qg==\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))
    @_dafny.classproperty
    def ECC__P521__PUBLIC(instance):
        return _dafny.Seq("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQB3jJzJGnYdp5HrVE3A7yhOFgnHU3SBSmg6sLTCG6v8uTeBCO+zsWMCj+yHRgQvZ/xpHDSFsekfdc3NwCHfWu1azkBffh4rZ25Qci9btzepFoVHwt7q8tdU/HZDVvi21ZJl/Ad/rOlWhEFimvkmAXpj1dOWiYVNMWmhfzIbCxsCi6T6UI=")
    @_dafny.classproperty
    def ECC__P521__PRIVATE__R(instance):
        return (((((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIAGQrViOzSEfLFHdlp\n"))) + (_dafny.Seq("rFcl/iWrPt7vWyga71fnLOzj4nTWBJ/Pua+xOVfTGjgplH4t16sRl4qk113Zv8zY\n"))) + (_dafny.Seq("XfgTJvChgYkDgYYABACKN7raKlNTwzxw97HarkQB7+9cTvw1grfhwW6AkUIS8b6J\n"))) + (_dafny.Seq("7CgTTSKZ6M5XQ0leYOZMkqXgjlpUfki4G3XXa4hw0wBUw+x9qtoAlwJNYhUsYg7N\n"))) + (_dafny.Seq("bm7IF9TQSuAzWgrSfIjOJfjrHjBR0TLmtk26xxKZIw36JSl9qb9b8LqlLk8uW6eE\n"))) + (_dafny.Seq("Lw==\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))
    @_dafny.classproperty
    def ECC__P521__PUBLIC__R(instance):
        return _dafny.Seq("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAije62ipTU8M8cPex2q5EAe/vXE78NYK34cFugJFCEvG+iewoE00imejOV0NJXmDmTJKl4I5aVH5IuBt112uIcNMAVMPsfaraAJcCTWIVLGIOzW5uyBfU0ErgM1oK0nyIziX46x4wUdEy5rZNuscSmSMN+iUpfam/W/C6pS5PLlunhC8=")

class SmallEncryptionContextVariation:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [SmallEncryptionContextVariation_Empty(), SmallEncryptionContextVariation_A(), SmallEncryptionContextVariation_AB(), SmallEncryptionContextVariation_BA()]
    @classmethod
    def default(cls, ):
        return lambda: SmallEncryptionContextVariation_Empty()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Empty(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_Empty)
    @property
    def is_A(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_A)
    @property
    def is_AB(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_AB)
    @property
    def is_BA(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_BA)

class SmallEncryptionContextVariation_Empty(SmallEncryptionContextVariation, NamedTuple('Empty', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_A(SmallEncryptionContextVariation, NamedTuple('A', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.A'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_A)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_AB(SmallEncryptionContextVariation, NamedTuple('AB', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.AB'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_AB)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_BA(SmallEncryptionContextVariation, NamedTuple('BA', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.BA'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_BA)
    def __hash__(self) -> int:
        return super().__hash__()

