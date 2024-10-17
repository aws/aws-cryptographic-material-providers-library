import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_primitives.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
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
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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

# Module: AwsCryptographyPrimitivesTypes

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsValid__PositiveInteger(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__RSAModulusLengthBits(x):
        return (81) <= (x)

    @staticmethod
    def IsValid__RSAModulusLengthBitsToGenerate(x):
        return ((81) <= (x)) and ((x) <= (4096))

    @staticmethod
    def IsValid__SymmetricKeyLength(x):
        return ((1) <= (x)) and ((x) <= (32))

    @staticmethod
    def IsValid__Uint8Bits(x):
        return ((0) <= (x)) and ((x) <= (255))

    @staticmethod
    def IsValid__Uint8Bytes(x):
        return ((0) <= (x)) and ((x) <= (32))


class DafnyCallEvent:
    @classmethod
    def default(cls, default_I, default_O):
        return lambda: DafnyCallEvent_DafnyCallEvent(default_I(), default_O())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DafnyCallEvent(self) -> bool:
        return isinstance(self, DafnyCallEvent_DafnyCallEvent)

class DafnyCallEvent_DafnyCallEvent(DafnyCallEvent, NamedTuple('DafnyCallEvent', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class AES__CTR:
    @classmethod
    def default(cls, ):
        return lambda: AES__CTR_AES__CTR(int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AES__CTR(self) -> bool:
        return isinstance(self, AES__CTR_AES__CTR)

class AES__CTR_AES__CTR(AES__CTR, NamedTuple('AES__CTR', [('keyLength', Any), ('nonceLength', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.AES_CTR.AES_CTR({_dafny.string_of(self.keyLength)}, {_dafny.string_of(self.nonceLength)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AES__CTR_AES__CTR) and self.keyLength == __o.keyLength and self.nonceLength == __o.nonceLength
    def __hash__(self) -> int:
        return super().__hash__()


class AES__GCM:
    @classmethod
    def default(cls, ):
        return lambda: AES__GCM_AES__GCM(int(0), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AES__GCM(self) -> bool:
        return isinstance(self, AES__GCM_AES__GCM)

class AES__GCM_AES__GCM(AES__GCM, NamedTuple('AES__GCM', [('keyLength', Any), ('tagLength', Any), ('ivLength', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.AES_GCM.AES_GCM({_dafny.string_of(self.keyLength)}, {_dafny.string_of(self.tagLength)}, {_dafny.string_of(self.ivLength)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AES__GCM_AES__GCM) and self.keyLength == __o.keyLength and self.tagLength == __o.tagLength and self.ivLength == __o.ivLength
    def __hash__(self) -> int:
        return super().__hash__()


class AESDecryptInput:
    @classmethod
    def default(cls, ):
        return lambda: AESDecryptInput_AESDecryptInput(AES__GCM.default()(), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AESDecryptInput(self) -> bool:
        return isinstance(self, AESDecryptInput_AESDecryptInput)

class AESDecryptInput_AESDecryptInput(AESDecryptInput, NamedTuple('AESDecryptInput', [('encAlg', Any), ('key', Any), ('cipherTxt', Any), ('authTag', Any), ('iv', Any), ('aad', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.AESDecryptInput.AESDecryptInput({_dafny.string_of(self.encAlg)}, {_dafny.string_of(self.key)}, {_dafny.string_of(self.cipherTxt)}, {_dafny.string_of(self.authTag)}, {_dafny.string_of(self.iv)}, {_dafny.string_of(self.aad)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AESDecryptInput_AESDecryptInput) and self.encAlg == __o.encAlg and self.key == __o.key and self.cipherTxt == __o.cipherTxt and self.authTag == __o.authTag and self.iv == __o.iv and self.aad == __o.aad
    def __hash__(self) -> int:
        return super().__hash__()


class AESEncryptInput:
    @classmethod
    def default(cls, ):
        return lambda: AESEncryptInput_AESEncryptInput(AES__GCM.default()(), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AESEncryptInput(self) -> bool:
        return isinstance(self, AESEncryptInput_AESEncryptInput)

class AESEncryptInput_AESEncryptInput(AESEncryptInput, NamedTuple('AESEncryptInput', [('encAlg', Any), ('iv', Any), ('key', Any), ('msg', Any), ('aad', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.AESEncryptInput.AESEncryptInput({_dafny.string_of(self.encAlg)}, {_dafny.string_of(self.iv)}, {_dafny.string_of(self.key)}, {_dafny.string_of(self.msg)}, {_dafny.string_of(self.aad)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AESEncryptInput_AESEncryptInput) and self.encAlg == __o.encAlg and self.iv == __o.iv and self.key == __o.key and self.msg == __o.msg and self.aad == __o.aad
    def __hash__(self) -> int:
        return super().__hash__()


class AESEncryptOutput:
    @classmethod
    def default(cls, ):
        return lambda: AESEncryptOutput_AESEncryptOutput(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AESEncryptOutput(self) -> bool:
        return isinstance(self, AESEncryptOutput_AESEncryptOutput)

class AESEncryptOutput_AESEncryptOutput(AESEncryptOutput, NamedTuple('AESEncryptOutput', [('cipherText', Any), ('authTag', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.AESEncryptOutput.AESEncryptOutput({_dafny.string_of(self.cipherText)}, {_dafny.string_of(self.authTag)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AESEncryptOutput_AESEncryptOutput) and self.cipherText == __o.cipherText and self.authTag == __o.authTag
    def __hash__(self) -> int:
        return super().__hash__()


class AesKdfCtrInput:
    @classmethod
    def default(cls, ):
        return lambda: AesKdfCtrInput_AesKdfCtrInput(_dafny.Seq({}), int(0), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AesKdfCtrInput(self) -> bool:
        return isinstance(self, AesKdfCtrInput_AesKdfCtrInput)

class AesKdfCtrInput_AesKdfCtrInput(AesKdfCtrInput, NamedTuple('AesKdfCtrInput', [('ikm', Any), ('expectedLength', Any), ('nonce', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.AesKdfCtrInput.AesKdfCtrInput({_dafny.string_of(self.ikm)}, {_dafny.string_of(self.expectedLength)}, {_dafny.string_of(self.nonce)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesKdfCtrInput_AesKdfCtrInput) and self.ikm == __o.ikm and self.expectedLength == __o.expectedLength and self.nonce == __o.nonce
    def __hash__(self) -> int:
        return super().__hash__()


class IAwsCryptographicPrimitivesClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClientCallHistory"

class IAwsCryptographicPrimitivesClient:
    pass
    def GenerateRandomBytes(self, input):
        pass

    def Digest(self, input):
        pass

    def HkdfExtract(self, input):
        pass

    def HkdfExpand(self, input):
        pass

    def Hkdf(self, input):
        pass

    def KdfCounterMode(self, input):
        pass

    def AesKdfCounterMode(self, input):
        pass

    def AESEncrypt(self, input):
        pass

    def AESDecrypt(self, input):
        pass

    def GenerateRSAKeyPair(self, input):
        pass

    def RSADecrypt(self, input):
        pass

    def RSAEncrypt(self, input):
        pass

    def GenerateECDSASignatureKey(self, input):
        pass

    def ECDSASign(self, input):
        pass

    def ECDSAVerify(self, input):
        pass

    def GenerateECCKeyPair(self, input):
        pass

    def GetPublicKeyFromPrivateKey(self, input):
        pass

    def ValidatePublicKey(self, input):
        pass

    def DeriveSharedSecret(self, input):
        pass

    def CompressPublicKey(self, input):
        pass

    def DecompressPublicKey(self, input):
        pass

    def ParsePublicKey(self, input):
        pass


class CompressPublicKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: CompressPublicKeyInput_CompressPublicKeyInput(ECCPublicKey.default()(), ECDHCurveSpec.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CompressPublicKeyInput(self) -> bool:
        return isinstance(self, CompressPublicKeyInput_CompressPublicKeyInput)

class CompressPublicKeyInput_CompressPublicKeyInput(CompressPublicKeyInput, NamedTuple('CompressPublicKeyInput', [('publicKey', Any), ('eccCurve', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.CompressPublicKeyInput.CompressPublicKeyInput({_dafny.string_of(self.publicKey)}, {_dafny.string_of(self.eccCurve)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CompressPublicKeyInput_CompressPublicKeyInput) and self.publicKey == __o.publicKey and self.eccCurve == __o.eccCurve
    def __hash__(self) -> int:
        return super().__hash__()


class CompressPublicKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: CompressPublicKeyOutput_CompressPublicKeyOutput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CompressPublicKeyOutput(self) -> bool:
        return isinstance(self, CompressPublicKeyOutput_CompressPublicKeyOutput)

class CompressPublicKeyOutput_CompressPublicKeyOutput(CompressPublicKeyOutput, NamedTuple('CompressPublicKeyOutput', [('compressedPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.CompressPublicKeyOutput({_dafny.string_of(self.compressedPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CompressPublicKeyOutput_CompressPublicKeyOutput) and self.compressedPublicKey == __o.compressedPublicKey
    def __hash__(self) -> int:
        return super().__hash__()


class CryptoConfig:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CryptoConfig_CryptoConfig()]
    @classmethod
    def default(cls, ):
        return lambda: CryptoConfig_CryptoConfig()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CryptoConfig(self) -> bool:
        return isinstance(self, CryptoConfig_CryptoConfig)

class CryptoConfig_CryptoConfig(CryptoConfig, NamedTuple('CryptoConfig', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.CryptoConfig.CryptoConfig'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CryptoConfig_CryptoConfig)
    def __hash__(self) -> int:
        return super().__hash__()


class DecompressPublicKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: DecompressPublicKeyInput_DecompressPublicKeyInput(_dafny.Seq({}), ECDHCurveSpec.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecompressPublicKeyInput(self) -> bool:
        return isinstance(self, DecompressPublicKeyInput_DecompressPublicKeyInput)

class DecompressPublicKeyInput_DecompressPublicKeyInput(DecompressPublicKeyInput, NamedTuple('DecompressPublicKeyInput', [('compressedPublicKey', Any), ('eccCurve', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput.DecompressPublicKeyInput({_dafny.string_of(self.compressedPublicKey)}, {_dafny.string_of(self.eccCurve)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecompressPublicKeyInput_DecompressPublicKeyInput) and self.compressedPublicKey == __o.compressedPublicKey and self.eccCurve == __o.eccCurve
    def __hash__(self) -> int:
        return super().__hash__()


class DecompressPublicKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: DecompressPublicKeyOutput_DecompressPublicKeyOutput(ECCPublicKey.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecompressPublicKeyOutput(self) -> bool:
        return isinstance(self, DecompressPublicKeyOutput_DecompressPublicKeyOutput)

class DecompressPublicKeyOutput_DecompressPublicKeyOutput(DecompressPublicKeyOutput, NamedTuple('DecompressPublicKeyOutput', [('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.DecompressPublicKeyOutput({_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecompressPublicKeyOutput_DecompressPublicKeyOutput) and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class DeriveSharedSecretInput:
    @classmethod
    def default(cls, ):
        return lambda: DeriveSharedSecretInput_DeriveSharedSecretInput(ECDHCurveSpec.default()(), ECCPrivateKey.default()(), ECCPublicKey.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeriveSharedSecretInput(self) -> bool:
        return isinstance(self, DeriveSharedSecretInput_DeriveSharedSecretInput)

class DeriveSharedSecretInput_DeriveSharedSecretInput(DeriveSharedSecretInput, NamedTuple('DeriveSharedSecretInput', [('eccCurve', Any), ('privateKey', Any), ('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput.DeriveSharedSecretInput({_dafny.string_of(self.eccCurve)}, {_dafny.string_of(self.privateKey)}, {_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeriveSharedSecretInput_DeriveSharedSecretInput) and self.eccCurve == __o.eccCurve and self.privateKey == __o.privateKey and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class DeriveSharedSecretOutput:
    @classmethod
    def default(cls, ):
        return lambda: DeriveSharedSecretOutput_DeriveSharedSecretOutput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeriveSharedSecretOutput(self) -> bool:
        return isinstance(self, DeriveSharedSecretOutput_DeriveSharedSecretOutput)

class DeriveSharedSecretOutput_DeriveSharedSecretOutput(DeriveSharedSecretOutput, NamedTuple('DeriveSharedSecretOutput', [('sharedSecret', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.DeriveSharedSecretOutput({_dafny.string_of(self.sharedSecret)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeriveSharedSecretOutput_DeriveSharedSecretOutput) and self.sharedSecret == __o.sharedSecret
    def __hash__(self) -> int:
        return super().__hash__()


class DigestAlgorithm:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DigestAlgorithm_SHA__512(), DigestAlgorithm_SHA__384(), DigestAlgorithm_SHA__256()]
    @classmethod
    def default(cls, ):
        return lambda: DigestAlgorithm_SHA__512()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SHA__512(self) -> bool:
        return isinstance(self, DigestAlgorithm_SHA__512)
    @property
    def is_SHA__384(self) -> bool:
        return isinstance(self, DigestAlgorithm_SHA__384)
    @property
    def is_SHA__256(self) -> bool:
        return isinstance(self, DigestAlgorithm_SHA__256)

class DigestAlgorithm_SHA__512(DigestAlgorithm, NamedTuple('SHA__512', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DigestAlgorithm.SHA_512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DigestAlgorithm_SHA__512)
    def __hash__(self) -> int:
        return super().__hash__()

class DigestAlgorithm_SHA__384(DigestAlgorithm, NamedTuple('SHA__384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DigestAlgorithm.SHA_384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DigestAlgorithm_SHA__384)
    def __hash__(self) -> int:
        return super().__hash__()

class DigestAlgorithm_SHA__256(DigestAlgorithm, NamedTuple('SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DigestAlgorithm.SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DigestAlgorithm_SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()


class DigestInput:
    @classmethod
    def default(cls, ):
        return lambda: DigestInput_DigestInput(DigestAlgorithm.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DigestInput(self) -> bool:
        return isinstance(self, DigestInput_DigestInput)

class DigestInput_DigestInput(DigestInput, NamedTuple('DigestInput', [('digestAlgorithm', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.DigestInput.DigestInput({_dafny.string_of(self.digestAlgorithm)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DigestInput_DigestInput) and self.digestAlgorithm == __o.digestAlgorithm and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()


class ECCPrivateKey:
    @classmethod
    def default(cls, ):
        return lambda: ECCPrivateKey_ECCPrivateKey(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECCPrivateKey(self) -> bool:
        return isinstance(self, ECCPrivateKey_ECCPrivateKey)

class ECCPrivateKey_ECCPrivateKey(ECCPrivateKey, NamedTuple('ECCPrivateKey', [('pem', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECCPrivateKey.ECCPrivateKey({_dafny.string_of(self.pem)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECCPrivateKey_ECCPrivateKey) and self.pem == __o.pem
    def __hash__(self) -> int:
        return super().__hash__()


class ECCPublicKey:
    @classmethod
    def default(cls, ):
        return lambda: ECCPublicKey_ECCPublicKey(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECCPublicKey(self) -> bool:
        return isinstance(self, ECCPublicKey_ECCPublicKey)

class ECCPublicKey_ECCPublicKey(ECCPublicKey, NamedTuple('ECCPublicKey', [('der', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECCPublicKey.ECCPublicKey({_dafny.string_of(self.der)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECCPublicKey_ECCPublicKey) and self.der == __o.der
    def __hash__(self) -> int:
        return super().__hash__()


class ECDHCurveSpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ECDHCurveSpec_ECC__NIST__P256(), ECDHCurveSpec_ECC__NIST__P384(), ECDHCurveSpec_ECC__NIST__P521(), ECDHCurveSpec_SM2()]
    @classmethod
    def default(cls, ):
        return lambda: ECDHCurveSpec_ECC__NIST__P256()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECC__NIST__P256(self) -> bool:
        return isinstance(self, ECDHCurveSpec_ECC__NIST__P256)
    @property
    def is_ECC__NIST__P384(self) -> bool:
        return isinstance(self, ECDHCurveSpec_ECC__NIST__P384)
    @property
    def is_ECC__NIST__P521(self) -> bool:
        return isinstance(self, ECDHCurveSpec_ECC__NIST__P521)
    @property
    def is_SM2(self) -> bool:
        return isinstance(self, ECDHCurveSpec_SM2)

class ECDHCurveSpec_ECC__NIST__P256(ECDHCurveSpec, NamedTuple('ECC__NIST__P256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDHCurveSpec.ECC_NIST_P256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDHCurveSpec_ECC__NIST__P256)
    def __hash__(self) -> int:
        return super().__hash__()

class ECDHCurveSpec_ECC__NIST__P384(ECDHCurveSpec, NamedTuple('ECC__NIST__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDHCurveSpec.ECC_NIST_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDHCurveSpec_ECC__NIST__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class ECDHCurveSpec_ECC__NIST__P521(ECDHCurveSpec, NamedTuple('ECC__NIST__P521', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDHCurveSpec.ECC_NIST_P521'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDHCurveSpec_ECC__NIST__P521)
    def __hash__(self) -> int:
        return super().__hash__()

class ECDHCurveSpec_SM2(ECDHCurveSpec, NamedTuple('SM2', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDHCurveSpec.SM2'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDHCurveSpec_SM2)
    def __hash__(self) -> int:
        return super().__hash__()


class ECDSASignatureAlgorithm:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ECDSASignatureAlgorithm_ECDSA__P384(), ECDSASignatureAlgorithm_ECDSA__P256()]
    @classmethod
    def default(cls, ):
        return lambda: ECDSASignatureAlgorithm_ECDSA__P384()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDSA__P384(self) -> bool:
        return isinstance(self, ECDSASignatureAlgorithm_ECDSA__P384)
    @property
    def is_ECDSA__P256(self) -> bool:
        return isinstance(self, ECDSASignatureAlgorithm_ECDSA__P256)

class ECDSASignatureAlgorithm_ECDSA__P384(ECDSASignatureAlgorithm, NamedTuple('ECDSA__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm.ECDSA_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDSASignatureAlgorithm_ECDSA__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class ECDSASignatureAlgorithm_ECDSA__P256(ECDSASignatureAlgorithm, NamedTuple('ECDSA__P256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm.ECDSA_P256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDSASignatureAlgorithm_ECDSA__P256)
    def __hash__(self) -> int:
        return super().__hash__()


class ECDSASignInput:
    @classmethod
    def default(cls, ):
        return lambda: ECDSASignInput_ECDSASignInput(ECDSASignatureAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDSASignInput(self) -> bool:
        return isinstance(self, ECDSASignInput_ECDSASignInput)

class ECDSASignInput_ECDSASignInput(ECDSASignInput, NamedTuple('ECDSASignInput', [('signatureAlgorithm', Any), ('signingKey', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDSASignInput.ECDSASignInput({_dafny.string_of(self.signatureAlgorithm)}, {_dafny.string_of(self.signingKey)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDSASignInput_ECDSASignInput) and self.signatureAlgorithm == __o.signatureAlgorithm and self.signingKey == __o.signingKey and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()


class ECDSAVerifyInput:
    @classmethod
    def default(cls, ):
        return lambda: ECDSAVerifyInput_ECDSAVerifyInput(ECDSASignatureAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDSAVerifyInput(self) -> bool:
        return isinstance(self, ECDSAVerifyInput_ECDSAVerifyInput)

class ECDSAVerifyInput_ECDSAVerifyInput(ECDSAVerifyInput, NamedTuple('ECDSAVerifyInput', [('signatureAlgorithm', Any), ('verificationKey', Any), ('message', Any), ('signature', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ECDSAVerifyInput.ECDSAVerifyInput({_dafny.string_of(self.signatureAlgorithm)}, {_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.message)}, {_dafny.string_of(self.signature)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDSAVerifyInput_ECDSAVerifyInput) and self.signatureAlgorithm == __o.signatureAlgorithm and self.verificationKey == __o.verificationKey and self.message == __o.message and self.signature == __o.signature
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateECCKeyPairInput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateECCKeyPairInput_GenerateECCKeyPairInput(ECDHCurveSpec.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateECCKeyPairInput(self) -> bool:
        return isinstance(self, GenerateECCKeyPairInput_GenerateECCKeyPairInput)

class GenerateECCKeyPairInput_GenerateECCKeyPairInput(GenerateECCKeyPairInput, NamedTuple('GenerateECCKeyPairInput', [('eccCurve', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput.GenerateECCKeyPairInput({_dafny.string_of(self.eccCurve)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateECCKeyPairInput_GenerateECCKeyPairInput) and self.eccCurve == __o.eccCurve
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateECCKeyPairOutput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateECCKeyPairOutput_GenerateECCKeyPairOutput(ECDHCurveSpec.default()(), ECCPrivateKey.default()(), ECCPublicKey.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateECCKeyPairOutput(self) -> bool:
        return isinstance(self, GenerateECCKeyPairOutput_GenerateECCKeyPairOutput)

class GenerateECCKeyPairOutput_GenerateECCKeyPairOutput(GenerateECCKeyPairOutput, NamedTuple('GenerateECCKeyPairOutput', [('eccCurve', Any), ('privateKey', Any), ('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.GenerateECCKeyPairOutput({_dafny.string_of(self.eccCurve)}, {_dafny.string_of(self.privateKey)}, {_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateECCKeyPairOutput_GenerateECCKeyPairOutput) and self.eccCurve == __o.eccCurve and self.privateKey == __o.privateKey and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateECDSASignatureKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput(ECDSASignatureAlgorithm.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateECDSASignatureKeyInput(self) -> bool:
        return isinstance(self, GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput)

class GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput(GenerateECDSASignatureKeyInput, NamedTuple('GenerateECDSASignatureKeyInput', [('signatureAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput.GenerateECDSASignatureKeyInput({_dafny.string_of(self.signatureAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput) and self.signatureAlgorithm == __o.signatureAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateECDSASignatureKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput(ECDSASignatureAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateECDSASignatureKeyOutput(self) -> bool:
        return isinstance(self, GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput)

class GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput(GenerateECDSASignatureKeyOutput, NamedTuple('GenerateECDSASignatureKeyOutput', [('signatureAlgorithm', Any), ('verificationKey', Any), ('signingKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput.GenerateECDSASignatureKeyOutput({_dafny.string_of(self.signatureAlgorithm)}, {_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.signingKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput) and self.signatureAlgorithm == __o.signatureAlgorithm and self.verificationKey == __o.verificationKey and self.signingKey == __o.signingKey
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateRandomBytesInput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateRandomBytesInput_GenerateRandomBytesInput(int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateRandomBytesInput(self) -> bool:
        return isinstance(self, GenerateRandomBytesInput_GenerateRandomBytesInput)

class GenerateRandomBytesInput_GenerateRandomBytesInput(GenerateRandomBytesInput, NamedTuple('GenerateRandomBytesInput', [('length', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput.GenerateRandomBytesInput({_dafny.string_of(self.length)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateRandomBytesInput_GenerateRandomBytesInput) and self.length == __o.length
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateRSAKeyPairInput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateRSAKeyPairInput(self) -> bool:
        return isinstance(self, GenerateRSAKeyPairInput_GenerateRSAKeyPairInput)

class GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(GenerateRSAKeyPairInput, NamedTuple('GenerateRSAKeyPairInput', [('lengthBits', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairInput.GenerateRSAKeyPairInput({_dafny.string_of(self.lengthBits)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateRSAKeyPairInput_GenerateRSAKeyPairInput) and self.lengthBits == __o.lengthBits
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateRSAKeyPairOutput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(RSAPublicKey.default()(), RSAPrivateKey.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateRSAKeyPairOutput(self) -> bool:
        return isinstance(self, GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput)

class GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(GenerateRSAKeyPairOutput, NamedTuple('GenerateRSAKeyPairOutput', [('publicKey', Any), ('privateKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput.GenerateRSAKeyPairOutput({_dafny.string_of(self.publicKey)}, {_dafny.string_of(self.privateKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput) and self.publicKey == __o.publicKey and self.privateKey == __o.privateKey
    def __hash__(self) -> int:
        return super().__hash__()


class GetPublicKeyFromPrivateKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput(ECDHCurveSpec.default()(), ECCPrivateKey.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetPublicKeyFromPrivateKeyInput(self) -> bool:
        return isinstance(self, GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput)

class GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput(GetPublicKeyFromPrivateKeyInput, NamedTuple('GetPublicKeyFromPrivateKeyInput', [('eccCurve', Any), ('privateKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyInput.GetPublicKeyFromPrivateKeyInput({_dafny.string_of(self.eccCurve)}, {_dafny.string_of(self.privateKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput) and self.eccCurve == __o.eccCurve and self.privateKey == __o.privateKey
    def __hash__(self) -> int:
        return super().__hash__()


class GetPublicKeyFromPrivateKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetPublicKeyFromPrivateKeyOutput_GetPublicKeyFromPrivateKeyOutput(ECDHCurveSpec.default()(), ECCPrivateKey.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetPublicKeyFromPrivateKeyOutput(self) -> bool:
        return isinstance(self, GetPublicKeyFromPrivateKeyOutput_GetPublicKeyFromPrivateKeyOutput)

class GetPublicKeyFromPrivateKeyOutput_GetPublicKeyFromPrivateKeyOutput(GetPublicKeyFromPrivateKeyOutput, NamedTuple('GetPublicKeyFromPrivateKeyOutput', [('eccCurve', Any), ('privateKey', Any), ('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput.GetPublicKeyFromPrivateKeyOutput({_dafny.string_of(self.eccCurve)}, {_dafny.string_of(self.privateKey)}, {_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetPublicKeyFromPrivateKeyOutput_GetPublicKeyFromPrivateKeyOutput) and self.eccCurve == __o.eccCurve and self.privateKey == __o.privateKey and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class GetRSAKeyModulusLengthInput:
    @classmethod
    def default(cls, ):
        return lambda: GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetRSAKeyModulusLengthInput(self) -> bool:
        return isinstance(self, GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput)

class GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(GetRSAKeyModulusLengthInput, NamedTuple('GetRSAKeyModulusLengthInput', [('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthInput.GetRSAKeyModulusLengthInput({_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput) and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class GetRSAKeyModulusLengthOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput(int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetRSAKeyModulusLengthOutput(self) -> bool:
        return isinstance(self, GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput)

class GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput(GetRSAKeyModulusLengthOutput, NamedTuple('GetRSAKeyModulusLengthOutput', [('length', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput.GetRSAKeyModulusLengthOutput({_dafny.string_of(self.length)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput) and self.length == __o.length
    def __hash__(self) -> int:
        return super().__hash__()


class HkdfExpandInput:
    @classmethod
    def default(cls, ):
        return lambda: HkdfExpandInput_HkdfExpandInput(DigestAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HkdfExpandInput(self) -> bool:
        return isinstance(self, HkdfExpandInput_HkdfExpandInput)

class HkdfExpandInput_HkdfExpandInput(HkdfExpandInput, NamedTuple('HkdfExpandInput', [('digestAlgorithm', Any), ('prk', Any), ('info', Any), ('expectedLength', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.HkdfExpandInput.HkdfExpandInput({_dafny.string_of(self.digestAlgorithm)}, {_dafny.string_of(self.prk)}, {_dafny.string_of(self.info)}, {_dafny.string_of(self.expectedLength)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HkdfExpandInput_HkdfExpandInput) and self.digestAlgorithm == __o.digestAlgorithm and self.prk == __o.prk and self.info == __o.info and self.expectedLength == __o.expectedLength
    def __hash__(self) -> int:
        return super().__hash__()


class HkdfExtractInput:
    @classmethod
    def default(cls, ):
        return lambda: HkdfExtractInput_HkdfExtractInput(DigestAlgorithm.default()(), Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HkdfExtractInput(self) -> bool:
        return isinstance(self, HkdfExtractInput_HkdfExtractInput)

class HkdfExtractInput_HkdfExtractInput(HkdfExtractInput, NamedTuple('HkdfExtractInput', [('digestAlgorithm', Any), ('salt', Any), ('ikm', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.HkdfExtractInput.HkdfExtractInput({_dafny.string_of(self.digestAlgorithm)}, {_dafny.string_of(self.salt)}, {_dafny.string_of(self.ikm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HkdfExtractInput_HkdfExtractInput) and self.digestAlgorithm == __o.digestAlgorithm and self.salt == __o.salt and self.ikm == __o.ikm
    def __hash__(self) -> int:
        return super().__hash__()


class HkdfInput:
    @classmethod
    def default(cls, ):
        return lambda: HkdfInput_HkdfInput(DigestAlgorithm.default()(), Wrappers.Option.default()(), _dafny.Seq({}), _dafny.Seq({}), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HkdfInput(self) -> bool:
        return isinstance(self, HkdfInput_HkdfInput)

class HkdfInput_HkdfInput(HkdfInput, NamedTuple('HkdfInput', [('digestAlgorithm', Any), ('salt', Any), ('ikm', Any), ('info', Any), ('expectedLength', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.HkdfInput.HkdfInput({_dafny.string_of(self.digestAlgorithm)}, {_dafny.string_of(self.salt)}, {_dafny.string_of(self.ikm)}, {_dafny.string_of(self.info)}, {_dafny.string_of(self.expectedLength)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HkdfInput_HkdfInput) and self.digestAlgorithm == __o.digestAlgorithm and self.salt == __o.salt and self.ikm == __o.ikm and self.info == __o.info and self.expectedLength == __o.expectedLength
    def __hash__(self) -> int:
        return super().__hash__()


class HMacInput:
    @classmethod
    def default(cls, ):
        return lambda: HMacInput_HMacInput(DigestAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HMacInput(self) -> bool:
        return isinstance(self, HMacInput_HMacInput)

class HMacInput_HMacInput(HMacInput, NamedTuple('HMacInput', [('digestAlgorithm', Any), ('key', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.HMacInput.HMacInput({_dafny.string_of(self.digestAlgorithm)}, {_dafny.string_of(self.key)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HMacInput_HMacInput) and self.digestAlgorithm == __o.digestAlgorithm and self.key == __o.key and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()


class KdfCtrInput:
    @classmethod
    def default(cls, ):
        return lambda: KdfCtrInput_KdfCtrInput(DigestAlgorithm.default()(), _dafny.Seq({}), int(0), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KdfCtrInput(self) -> bool:
        return isinstance(self, KdfCtrInput_KdfCtrInput)

class KdfCtrInput_KdfCtrInput(KdfCtrInput, NamedTuple('KdfCtrInput', [('digestAlgorithm', Any), ('ikm', Any), ('expectedLength', Any), ('purpose', Any), ('nonce', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.KdfCtrInput.KdfCtrInput({_dafny.string_of(self.digestAlgorithm)}, {_dafny.string_of(self.ikm)}, {_dafny.string_of(self.expectedLength)}, {_dafny.string_of(self.purpose)}, {_dafny.string_of(self.nonce)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KdfCtrInput_KdfCtrInput) and self.digestAlgorithm == __o.digestAlgorithm and self.ikm == __o.ikm and self.expectedLength == __o.expectedLength and self.purpose == __o.purpose and self.nonce == __o.nonce
    def __hash__(self) -> int:
        return super().__hash__()


class ParsePublicKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: ParsePublicKeyInput_ParsePublicKeyInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ParsePublicKeyInput(self) -> bool:
        return isinstance(self, ParsePublicKeyInput_ParsePublicKeyInput)

class ParsePublicKeyInput_ParsePublicKeyInput(ParsePublicKeyInput, NamedTuple('ParsePublicKeyInput', [('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ParsePublicKeyInput.ParsePublicKeyInput({_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ParsePublicKeyInput_ParsePublicKeyInput) and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class ParsePublicKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: ParsePublicKeyOutput_ParsePublicKeyOutput(ECCPublicKey.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ParsePublicKeyOutput(self) -> bool:
        return isinstance(self, ParsePublicKeyOutput_ParsePublicKeyOutput)

class ParsePublicKeyOutput_ParsePublicKeyOutput(ParsePublicKeyOutput, NamedTuple('ParsePublicKeyOutput', [('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.ParsePublicKeyOutput({_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ParsePublicKeyOutput_ParsePublicKeyOutput) and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class PositiveInteger:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_0_x_: int = source__
        if True:
            return default__.IsValid__PositiveInteger(d_0_x_)
        return False

class RSADecryptInput:
    @classmethod
    def default(cls, ):
        return lambda: RSADecryptInput_RSADecryptInput(RSAPaddingMode.default()(), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSADecryptInput(self) -> bool:
        return isinstance(self, RSADecryptInput_RSADecryptInput)

class RSADecryptInput_RSADecryptInput(RSADecryptInput, NamedTuple('RSADecryptInput', [('padding', Any), ('privateKey', Any), ('cipherText', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSADecryptInput.RSADecryptInput({_dafny.string_of(self.padding)}, {_dafny.string_of(self.privateKey)}, {_dafny.string_of(self.cipherText)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSADecryptInput_RSADecryptInput) and self.padding == __o.padding and self.privateKey == __o.privateKey and self.cipherText == __o.cipherText
    def __hash__(self) -> int:
        return super().__hash__()


class RSAEncryptInput:
    @classmethod
    def default(cls, ):
        return lambda: RSAEncryptInput_RSAEncryptInput(RSAPaddingMode.default()(), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSAEncryptInput(self) -> bool:
        return isinstance(self, RSAEncryptInput_RSAEncryptInput)

class RSAEncryptInput_RSAEncryptInput(RSAEncryptInput, NamedTuple('RSAEncryptInput', [('padding', Any), ('publicKey', Any), ('plaintext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAEncryptInput.RSAEncryptInput({_dafny.string_of(self.padding)}, {_dafny.string_of(self.publicKey)}, {_dafny.string_of(self.plaintext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAEncryptInput_RSAEncryptInput) and self.padding == __o.padding and self.publicKey == __o.publicKey and self.plaintext == __o.plaintext
    def __hash__(self) -> int:
        return super().__hash__()


class RSAModulusLengthBits:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_1_x_: int = source__
        if True:
            return default__.IsValid__RSAModulusLengthBits(d_1_x_)
        return False

class RSAModulusLengthBitsToGenerate:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_2_x_: int = source__
        if True:
            return default__.IsValid__RSAModulusLengthBitsToGenerate(d_2_x_)
        return False

class RSAPaddingMode:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [RSAPaddingMode_PKCS1(), RSAPaddingMode_OAEP__SHA1(), RSAPaddingMode_OAEP__SHA256(), RSAPaddingMode_OAEP__SHA384(), RSAPaddingMode_OAEP__SHA512()]
    @classmethod
    def default(cls, ):
        return lambda: RSAPaddingMode_PKCS1()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PKCS1(self) -> bool:
        return isinstance(self, RSAPaddingMode_PKCS1)
    @property
    def is_OAEP__SHA1(self) -> bool:
        return isinstance(self, RSAPaddingMode_OAEP__SHA1)
    @property
    def is_OAEP__SHA256(self) -> bool:
        return isinstance(self, RSAPaddingMode_OAEP__SHA256)
    @property
    def is_OAEP__SHA384(self) -> bool:
        return isinstance(self, RSAPaddingMode_OAEP__SHA384)
    @property
    def is_OAEP__SHA512(self) -> bool:
        return isinstance(self, RSAPaddingMode_OAEP__SHA512)

class RSAPaddingMode_PKCS1(RSAPaddingMode, NamedTuple('PKCS1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAPaddingMode.PKCS1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAPaddingMode_PKCS1)
    def __hash__(self) -> int:
        return super().__hash__()

class RSAPaddingMode_OAEP__SHA1(RSAPaddingMode, NamedTuple('OAEP__SHA1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAPaddingMode.OAEP_SHA1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAPaddingMode_OAEP__SHA1)
    def __hash__(self) -> int:
        return super().__hash__()

class RSAPaddingMode_OAEP__SHA256(RSAPaddingMode, NamedTuple('OAEP__SHA256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAPaddingMode.OAEP_SHA256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAPaddingMode_OAEP__SHA256)
    def __hash__(self) -> int:
        return super().__hash__()

class RSAPaddingMode_OAEP__SHA384(RSAPaddingMode, NamedTuple('OAEP__SHA384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAPaddingMode.OAEP_SHA384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAPaddingMode_OAEP__SHA384)
    def __hash__(self) -> int:
        return super().__hash__()

class RSAPaddingMode_OAEP__SHA512(RSAPaddingMode, NamedTuple('OAEP__SHA512', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAPaddingMode.OAEP_SHA512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAPaddingMode_OAEP__SHA512)
    def __hash__(self) -> int:
        return super().__hash__()


class RSAPrivateKey:
    @classmethod
    def default(cls, ):
        return lambda: RSAPrivateKey_RSAPrivateKey(int(0), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSAPrivateKey(self) -> bool:
        return isinstance(self, RSAPrivateKey_RSAPrivateKey)

class RSAPrivateKey_RSAPrivateKey(RSAPrivateKey, NamedTuple('RSAPrivateKey', [('lengthBits', Any), ('pem', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAPrivateKey.RSAPrivateKey({_dafny.string_of(self.lengthBits)}, {_dafny.string_of(self.pem)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAPrivateKey_RSAPrivateKey) and self.lengthBits == __o.lengthBits and self.pem == __o.pem
    def __hash__(self) -> int:
        return super().__hash__()


class RSAPublicKey:
    @classmethod
    def default(cls, ):
        return lambda: RSAPublicKey_RSAPublicKey(int(0), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSAPublicKey(self) -> bool:
        return isinstance(self, RSAPublicKey_RSAPublicKey)

class RSAPublicKey_RSAPublicKey(RSAPublicKey, NamedTuple('RSAPublicKey', [('lengthBits', Any), ('pem', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.RSAPublicKey.RSAPublicKey({_dafny.string_of(self.lengthBits)}, {_dafny.string_of(self.pem)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RSAPublicKey_RSAPublicKey) and self.lengthBits == __o.lengthBits and self.pem == __o.pem
    def __hash__(self) -> int:
        return super().__hash__()


class SymmetricKeyLength:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_3_x_: int = source__
        if True:
            return default__.IsValid__SymmetricKeyLength(d_3_x_)
        return False

class Uint8Bits:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_4_x_: int = source__
        if True:
            return default__.IsValid__Uint8Bits(d_4_x_)
        return False

class Uint8Bytes:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_5_x_: int = source__
        if True:
            return default__.IsValid__Uint8Bytes(d_5_x_)
        return False

class ValidatePublicKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidatePublicKeyInput_ValidatePublicKeyInput(ECDHCurveSpec.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidatePublicKeyInput(self) -> bool:
        return isinstance(self, ValidatePublicKeyInput_ValidatePublicKeyInput)

class ValidatePublicKeyInput_ValidatePublicKeyInput(ValidatePublicKeyInput, NamedTuple('ValidatePublicKeyInput', [('eccCurve', Any), ('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput.ValidatePublicKeyInput({_dafny.string_of(self.eccCurve)}, {_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ValidatePublicKeyInput_ValidatePublicKeyInput) and self.eccCurve == __o.eccCurve and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()


class ValidatePublicKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: ValidatePublicKeyOutput_ValidatePublicKeyOutput(False)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidatePublicKeyOutput(self) -> bool:
        return isinstance(self, ValidatePublicKeyOutput_ValidatePublicKeyOutput)

class ValidatePublicKeyOutput_ValidatePublicKeyOutput(ValidatePublicKeyOutput, NamedTuple('ValidatePublicKeyOutput', [('success', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.ValidatePublicKeyOutput({_dafny.string_of(self.success)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ValidatePublicKeyOutput_ValidatePublicKeyOutput) and self.success == __o.success
    def __hash__(self) -> int:
        return super().__hash__()


class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_AwsCryptographicPrimitivesError(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsCryptographicPrimitivesError(self) -> bool:
        return isinstance(self, Error_AwsCryptographicPrimitivesError)
    @property
    def is_CollectionOfErrors(self) -> bool:
        return isinstance(self, Error_CollectionOfErrors)
    @property
    def is_Opaque(self) -> bool:
        return isinstance(self, Error_Opaque)

class Error_AwsCryptographicPrimitivesError(Error, NamedTuple('AwsCryptographicPrimitivesError', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.Error.AwsCryptographicPrimitivesError({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_AwsCryptographicPrimitivesError) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CollectionOfErrors(Error, NamedTuple('CollectionOfErrors', [('list', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.Error.CollectionOfErrors({_dafny.string_of(self.list)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CollectionOfErrors) and self.list == __o.list and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any), ('alt__text', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.Error.Opaque({_dafny.string_of(self.obj)}, {_dafny.string_of(self.alt__text)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj and self.alt__text == __o.alt__text
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Error.default()()
    def _Is(source__):
        d_6_e_: Error = source__
        return (d_6_e_).is_Opaque
