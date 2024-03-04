import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries

# Module: software_amazon_cryptography_primitives_internaldafny_types

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


class PositiveInteger:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

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

class RSAModulusLengthBitsToGenerate:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

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

class Uint8Bits:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class Uint8Bytes:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_AwsCryptographicPrimitivesError(_dafny.Seq({}))
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

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesTypes.Error.Opaque({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Error.default()()
