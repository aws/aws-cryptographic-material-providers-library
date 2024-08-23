import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
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
import TestSignature as TestSignature
import TestAwsCryptographyPrimitivesHKDF as TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes as TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime as ConstantTime
import ConstantTimeTest as ConstantTimeTest
import TestHKDF__Rfc5869TestVectors as TestHKDF__Rfc5869TestVectors
import TestKDF as TestKDF
import TestKDFK__TestVectors as TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesRSA as TestAwsCryptographyPrimitivesRSA
import TestAwsCryptographyPrimitivesAES as TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesHMAC as TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesDigest as TestAwsCryptographyPrimitivesDigest
import TestAwsCryptographyPrimitivesHMacDigest as TestAwsCryptographyPrimitivesHMacDigest

# Module: TestECDH

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestKeyGen():
        d_144_supportedCurves_: _dafny.Seq
        d_144_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi3_ = len(d_144_supportedCurves_)
        for d_145_i_ in range(0, hi3_):
            d_146_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_146_curve_ = (d_144_supportedCurves_)[d_145_i_]
            d_147_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_148_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out29_: Wrappers.Result
            out29_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_146_curve_))
            d_148_valueOrError0_ = out29_
            if not(not((d_148_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(145,21): " + _dafny.string_of(d_148_valueOrError0_))
            d_147_keypair_ = (d_148_valueOrError0_).Extract()

    @staticmethod
    def TestGetPublicKeyFromPrivatePem():
        d_149_pemPrivateKeys_: _dafny.Seq
        d_149_pemPrivateKeys_ = _dafny.Seq([default__.ECC__P256__PRIVATE, default__.ECC__P384__PRIVATE, default__.ECC__P521__PRIVATE])
        d_150_derPublicKeys_: _dafny.Seq
        d_150_derPublicKeys_ = _dafny.Seq([default__.ECC__P256__PUBLIC, default__.ECC__384__PUBLIC, default__.ECC__P521__PUBLIC])
        d_151_supportedCurves_: _dafny.Seq
        d_151_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi4_ = len(d_151_supportedCurves_)
        for d_152_i_ in range(0, hi4_):
            d_153_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_153_curve_ = (d_151_supportedCurves_)[d_152_i_]
            d_154_privateKey_: _dafny.Seq
            d_155_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
            d_155_valueOrError0_ = UTF8.default__.Encode((d_149_pemPrivateKeys_)[d_152_i_])
            if not(not((d_155_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(162,24): " + _dafny.string_of(d_155_valueOrError0_))
            d_154_privateKey_ = (d_155_valueOrError0_).Extract()
            d_156_looseHexPublicKey_: _dafny.Seq
            out30_: _dafny.Seq
            out30_ = default__.expectLooseHexString((d_150_derPublicKeys_)[d_152_i_])
            d_156_looseHexPublicKey_ = out30_
            d_157_publicKeyBytes_: _dafny.Seq
            d_157_publicKeyBytes_ = HexStrings.default__.FromHexString(d_156_looseHexPublicKey_)
            d_158_expectedPublicKey_: AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput
            d_159_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.default())()
            out31_: Wrappers.Result
            out31_ = ECDH.default__.ParsePublicKey(AwsCryptographyPrimitivesTypes.ParsePublicKeyInput_ParsePublicKeyInput(d_157_publicKeyBytes_))
            d_159_valueOrError1_ = out31_
            if not(not((d_159_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(166,31): " + _dafny.string_of(d_159_valueOrError1_))
            d_158_expectedPublicKey_ = (d_159_valueOrError1_).Extract()
            d_160_publicKey_: AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput
            d_161_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput.default())()
            out32_: Wrappers.Result
            out32_ = ECDH.default__.GetPublicKeyFromPrivate(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput(d_153_curve_, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_154_privateKey_)))
            d_161_valueOrError2_ = out32_
            if not(not((d_161_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(171,23): " + _dafny.string_of(d_161_valueOrError2_))
            d_160_publicKey_ = (d_161_valueOrError2_).Extract()
            if not(((d_160_publicKey_).publicKey) == (((d_158_expectedPublicKey_).publicKey).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(178,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetPublicKeyFromPrivateIncorrectCruve():
        d_162_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
        d_162_curve_ = default__.P384
        d_163_privateKey_: _dafny.Seq
        d_164_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_164_valueOrError0_ = UTF8.default__.Encode(default__.ECC__P256__PRIVATE)
        if not(not((d_164_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestECDH.dfy(185,22): " + _dafny.string_of(d_164_valueOrError0_))
        d_163_privateKey_ = (d_164_valueOrError0_).Extract()
        d_165_looseHexPublicKey_: _dafny.Seq
        out33_: _dafny.Seq
        out33_ = default__.expectLooseHexString(default__.ECC__P256__PUBLIC)
        d_165_looseHexPublicKey_ = out33_
        d_166_publicKeyBytes_: _dafny.Seq
        d_166_publicKeyBytes_ = HexStrings.default__.FromHexString(d_165_looseHexPublicKey_)
        d_167_expectedPublicKey_: AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput
        d_168_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.default())()
        out34_: Wrappers.Result
        out34_ = ECDH.default__.ParsePublicKey(AwsCryptographyPrimitivesTypes.ParsePublicKeyInput_ParsePublicKeyInput(d_166_publicKeyBytes_))
        d_168_valueOrError1_ = out34_
        if not(not((d_168_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestECDH.dfy(189,29): " + _dafny.string_of(d_168_valueOrError1_))
        d_167_expectedPublicKey_ = (d_168_valueOrError1_).Extract()
        d_169_publicKey_: Wrappers.Result
        out35_: Wrappers.Result
        out35_ = ECDH.default__.GetPublicKeyFromPrivate(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput(d_162_curve_, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_163_privateKey_)))
        d_169_publicKey_ = out35_
        if not((d_169_publicKey_).is_Failure):
            raise _dafny.HaltException("test/TestECDH.dfy(201,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def expectLooseHexString(s):
        s2: _dafny.Seq = _dafny.Seq("")
        if not(HexStrings.default__.IsLooseHexString(s)):
            raise _dafny.HaltException("test/TestECDH.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        s2 = s
        return s2
        return s2

    @staticmethod
    def TestValidatePublicKeySuccess():
        d_170_supportedCurves_: _dafny.Seq
        d_170_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi5_ = len(d_170_supportedCurves_)
        for d_171_i_ in range(0, hi5_):
            d_172_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_172_curve_ = (d_170_supportedCurves_)[d_171_i_]
            d_173_keypairA_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_174_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out36_: Wrappers.Result
            out36_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_172_curve_))
            d_174_valueOrError0_ = out36_
            if not(not((d_174_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(218,22): " + _dafny.string_of(d_174_valueOrError0_))
            d_173_keypairA_ = (d_174_valueOrError0_).Extract()
            d_175_keypairB_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_176_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out37_: Wrappers.Result
            out37_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_172_curve_))
            d_176_valueOrError1_ = out37_
            if not(not((d_176_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(223,22): " + _dafny.string_of(d_176_valueOrError1_))
            d_175_keypairB_ = (d_176_valueOrError1_).Extract()
            d_177_validPublicKeyB_: AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
            d_178_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
            out38_: Wrappers.Result
            out38_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(d_172_curve_, ((d_175_keypairB_).publicKey).der))
            d_178_valueOrError2_ = out38_
            if not(not((d_178_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(229,29): " + _dafny.string_of(d_178_valueOrError2_))
            d_177_validPublicKeyB_ = (d_178_valueOrError2_).Extract()

    @staticmethod
    def TestValidatePublicKeyFailure():
        d_179_supportedCurves_: _dafny.Seq
        d_179_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi6_ = len(d_179_supportedCurves_)
        for d_180_i_ in range(0, hi6_):
            hi7_ = len(d_179_supportedCurves_)
            for d_181_j_ in range(0, hi7_):
                d_182_curve__i_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                d_182_curve__i_ = (d_179_supportedCurves_)[d_180_i_]
                d_183_curve__j_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                d_183_curve__j_ = (d_179_supportedCurves_)[d_181_j_]
                d_184_keypairA_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
                d_185_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
                out39_: Wrappers.Result
                out39_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_182_curve__i_))
                d_185_valueOrError0_ = out39_
                if not(not((d_185_valueOrError0_).IsFailure())):
                    raise _dafny.HaltException("test/TestECDH.dfy(249,24): " + _dafny.string_of(d_185_valueOrError0_))
                d_184_keypairA_ = (d_185_valueOrError0_).Extract()
                d_186_keypairB_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
                d_187_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
                out40_: Wrappers.Result
                out40_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_183_curve__j_))
                d_187_valueOrError1_ = out40_
                if not(not((d_187_valueOrError1_).IsFailure())):
                    raise _dafny.HaltException("test/TestECDH.dfy(254,24): " + _dafny.string_of(d_187_valueOrError1_))
                d_186_keypairB_ = (d_187_valueOrError1_).Extract()
                d_188_validPublicKeyB_: Wrappers.Result
                out41_: Wrappers.Result
                out41_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(d_182_curve__i_, ((d_186_keypairB_).publicKey).der))
                d_188_validPublicKeyB_ = out41_
                if (d_182_curve__i_) != (d_183_curve__j_):
                    if not((d_188_validPublicKeyB_).is_Failure):
                        raise _dafny.HaltException("test/TestECDH.dfy(268,10): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                elif True:
                    if not((d_188_validPublicKeyB_).is_Success):
                        raise _dafny.HaltException("test/TestECDH.dfy(270,10): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointAtINFFailOnLoad():
        d_189_publicKeysWithPointsAtINF_: _dafny.Seq
        d_189_publicKeysWithPointsAtINF_ = _dafny.Seq([default__.ECC__256__PUBLIC__INF__FAIL__ON__LOAD, default__.ECC__384__PUBLIC__INF__FAIL__ON__LOAD, default__.ECC__521__PUBLIC__INF__FAIL__ON__LOAD])
        d_190_supportedCurves_: _dafny.Seq
        d_190_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi8_ = len(d_190_supportedCurves_)
        for d_191_i_ in range(0, hi8_):
            d_192_looseHexPublicKey_: _dafny.Seq
            out42_: _dafny.Seq
            out42_ = default__.expectLooseHexString((d_189_publicKeysWithPointsAtINF_)[d_191_i_])
            d_192_looseHexPublicKey_ = out42_
            d_193_publicKeyBytes_: _dafny.Seq
            d_193_publicKeyBytes_ = HexStrings.default__.FromHexString(d_192_looseHexPublicKey_)
            d_194_validPublicKey_: Wrappers.Result
            out43_: Wrappers.Result
            out43_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_190_supportedCurves_)[d_191_i_], d_193_publicKeyBytes_))
            d_194_validPublicKey_ = out43_
            if not((d_194_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(294,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_194_validPublicKey_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(296,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_195_errMsg_: _dafny.Seq
            d_195_errMsg_ = ((d_194_validPublicKey_).error).message
            if not(((((d_195_errMsg_) == (default__.BAD__X509__KEY__ERR__MSG__RUST)) or ((d_195_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__JAVA))) or ((d_195_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET6))) or ((d_195_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET48))):
                raise _dafny.HaltException("test/TestECDH.dfy(299,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointAtINF():
        d_196_publicKeysWithPointsAtINF_: _dafny.Seq
        d_196_publicKeysWithPointsAtINF_ = _dafny.Seq([default__.ECC__256__PUBLIC__INF, default__.ECC__384__PUBLIC__INF, default__.ECC__521__PUBLIC__INF])
        d_197_supportedCurves_: _dafny.Seq
        d_197_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi9_ = len(d_197_supportedCurves_)
        for d_198_i_ in range(0, hi9_):
            d_199_looseHexPublicKey_: _dafny.Seq
            out44_: _dafny.Seq
            out44_ = default__.expectLooseHexString((d_196_publicKeysWithPointsAtINF_)[d_198_i_])
            d_199_looseHexPublicKey_ = out44_
            d_200_publicKeyBytes_: _dafny.Seq
            d_200_publicKeyBytes_ = HexStrings.default__.FromHexString(d_199_looseHexPublicKey_)
            d_201_validPublicKey_: Wrappers.Result
            out45_: Wrappers.Result
            out45_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_197_supportedCurves_)[d_198_i_], d_200_publicKeyBytes_))
            d_201_validPublicKey_ = out45_
            if not((d_201_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(323,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad():
        d_202_publicKeysWithPointsGreaterThanP_: _dafny.Seq
        d_202_publicKeysWithPointsGreaterThanP_ = _dafny.Seq([default__.ECC__P256__PUBLIC__GP__FAIL__ON__LOAD, default__.ECC__P384__PUBLIC__GP__FAIL__ON__LOAD, default__.ECC__P521__PUBLIC__GP__FAIL__ON__LOAD])
        d_203_supportedCurves_: _dafny.Seq
        d_203_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi10_ = len(d_203_supportedCurves_)
        for d_204_i_ in range(0, hi10_):
            d_205_looseHexPublicKey_: _dafny.Seq
            out46_: _dafny.Seq
            out46_ = default__.expectLooseHexString((d_202_publicKeysWithPointsGreaterThanP_)[d_204_i_])
            d_205_looseHexPublicKey_ = out46_
            d_206_publicKeyBytes_: _dafny.Seq
            d_206_publicKeyBytes_ = HexStrings.default__.FromHexString(d_205_looseHexPublicKey_)
            d_207_validPublicKey_: Wrappers.Result
            out47_: Wrappers.Result
            out47_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_203_supportedCurves_)[d_204_i_], d_206_publicKeyBytes_))
            d_207_validPublicKey_ = out47_
            if not((d_207_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(344,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_207_validPublicKey_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(346,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_208_errMsg_: _dafny.Seq
            d_208_errMsg_ = ((d_207_validPublicKey_).error).message
            if not((((default__.seq__contains(d_208_errMsg_, default__.OUT__OF__BOUNDS__ERR__MSG__JAVA)) or ((d_208_errMsg_) == (default__.BAD__X509__KEY__ERR__MSG__RUST))) or ((d_208_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NET6))) or ((d_208_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NE48))):
                raise _dafny.HaltException("test/TestECDH.dfy(348,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointGreaterThanP():
        d_209_publicKeysWithPointsGreaterThanP_: _dafny.Seq
        d_209_publicKeysWithPointsGreaterThanP_ = _dafny.Seq([default__.ECC__P256__PUBLIC__GP, default__.ECC__P384__PUBLIC__GP, default__.ECC__P521__PUBLIC__GP])
        d_210_supportedCurves_: _dafny.Seq
        d_210_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi11_ = len(d_210_supportedCurves_)
        for d_211_i_ in range(0, hi11_):
            d_212_looseHexPublicKey_: _dafny.Seq
            out48_: _dafny.Seq
            out48_ = default__.expectLooseHexString((d_209_publicKeysWithPointsGreaterThanP_)[d_211_i_])
            d_212_looseHexPublicKey_ = out48_
            d_213_publicKeyBytes_: _dafny.Seq
            d_213_publicKeyBytes_ = HexStrings.default__.FromHexString(d_212_looseHexPublicKey_)
            d_214_validPublicKey_: Wrappers.Result
            out49_: Wrappers.Result
            out49_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_210_supportedCurves_)[d_211_i_], d_213_publicKeyBytes_))
            d_214_validPublicKey_ = out49_
            if not((d_214_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(372,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGenerateSharedSecret():
        d_215_supportedCurves_: _dafny.Seq
        d_215_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi12_ = len(d_215_supportedCurves_)
        for d_216_i_ in range(0, hi12_):
            d_217_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_217_curve_ = (d_215_supportedCurves_)[d_216_i_]
            d_218_keypairA_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_219_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out50_: Wrappers.Result
            out50_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_217_curve_))
            d_219_valueOrError0_ = out50_
            if not(not((d_219_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(382,22): " + _dafny.string_of(d_219_valueOrError0_))
            d_218_keypairA_ = (d_219_valueOrError0_).Extract()
            d_220_keypairB_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_221_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out51_: Wrappers.Result
            out51_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_217_curve_))
            d_221_valueOrError1_ = out51_
            if not(not((d_221_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(387,22): " + _dafny.string_of(d_221_valueOrError1_))
            d_220_keypairB_ = (d_221_valueOrError1_).Extract()
            if not((((d_218_keypairA_).privateKey) != ((d_220_keypairB_).privateKey)) and (((d_218_keypairA_).publicKey) != ((d_220_keypairB_).publicKey))):
                raise _dafny.HaltException("test/TestECDH.dfy(393,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_222_validPublicKeyB_: AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
            d_223_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
            out52_: Wrappers.Result
            out52_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(d_217_curve_, ((d_220_keypairB_).publicKey).der))
            d_223_valueOrError2_ = out52_
            if not(not((d_223_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(398,29): " + _dafny.string_of(d_223_valueOrError2_))
            d_222_validPublicKeyB_ = (d_223_valueOrError2_).Extract()
            d_224_sharedSecretA_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_225_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out53_: Wrappers.Result
            out53_ = ECDH.default__.DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(d_217_curve_, (d_218_keypairA_).privateKey, (d_220_keypairB_).publicKey))
            d_225_valueOrError3_ = out53_
            if not(not((d_225_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(405,27): " + _dafny.string_of(d_225_valueOrError3_))
            d_224_sharedSecretA_ = (d_225_valueOrError3_).Extract()
            d_226_sharedSecretB_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_227_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out54_: Wrappers.Result
            out54_ = ECDH.default__.DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(d_217_curve_, (d_220_keypairB_).privateKey, (d_218_keypairA_).publicKey))
            d_227_valueOrError4_ = out54_
            if not(not((d_227_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(413,27): " + _dafny.string_of(d_227_valueOrError4_))
            d_226_sharedSecretB_ = (d_227_valueOrError4_).Extract()
            if not((d_224_sharedSecretA_) == (d_226_sharedSecretB_)):
                raise _dafny.HaltException("test/TestECDH.dfy(421,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCompressDecompressPublicKey():
        d_228_supportedCurves_: _dafny.Seq
        d_228_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi13_ = len(d_228_supportedCurves_)
        for d_229_i_ in range(0, hi13_):
            d_230_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_230_curve_ = (d_228_supportedCurves_)[d_229_i_]
            d_231_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_232_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out55_: Wrappers.Result
            out55_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_230_curve_))
            d_232_valueOrError0_ = out55_
            if not(not((d_232_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(430,21): " + _dafny.string_of(d_232_valueOrError0_))
            d_231_keypair_ = (d_232_valueOrError0_).Extract()
            d_233_originalPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey
            d_233_originalPublicKey_ = (d_231_keypair_).publicKey
            d_234_compressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
            d_235_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
            out56_: Wrappers.Result
            out56_ = ECDH.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.CompressPublicKeyInput_CompressPublicKeyInput(d_233_originalPublicKey_, d_230_curve_))
            d_235_valueOrError1_ = out56_
            if not(not((d_235_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(437,39): " + _dafny.string_of(d_235_valueOrError1_))
            d_234_compressedPublicKeyResult_ = (d_235_valueOrError1_).Extract()
            if not(((d_234_compressedPublicKeyResult_).compressedPublicKey) != ((d_233_originalPublicKey_).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(444,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_236_compressedPublicKey_: _dafny.Seq
            d_236_compressedPublicKey_ = (d_234_compressedPublicKeyResult_).compressedPublicKey
            d_237_decompressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
            d_238_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
            out57_: Wrappers.Result
            out57_ = ECDH.default__.DecompressPublicKey(AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput_DecompressPublicKeyInput(d_236_compressedPublicKey_, d_230_curve_))
            d_238_valueOrError2_ = out57_
            if not(not((d_238_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(448,41): " + _dafny.string_of(d_238_valueOrError2_))
            d_237_decompressedPublicKeyResult_ = (d_238_valueOrError2_).Extract()
            d_239_decompressedPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey
            d_239_decompressedPublicKey_ = (d_237_decompressedPublicKeyResult_).publicKey
            if not(((d_233_originalPublicKey_).der) == ((d_239_decompressedPublicKey_).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(457,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCompressDecompressConstantPublicKeys():
        d_240_derX509PublicKeys_: _dafny.Seq
        d_240_derX509PublicKeys_ = _dafny.Seq([default__.ECC__P256__PUBLIC, default__.ECC__384__PUBLIC, default__.ECC__P521__PUBLIC])
        d_241_compressedKeys_: _dafny.Seq
        d_241_compressedKeys_ = _dafny.Seq([default__.ECC__P256__PUBLIC__COMPRESSED, default__.ECC__384__PUBLIC__COMPRESSED, default__.ECC__P521__PUBLIC__COMPRESSED])
        d_242_curves_: _dafny.Seq
        d_242_curves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi14_ = len(d_242_curves_)
        for d_243_i_ in range(0, hi14_):
            d_244_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_244_curve_ = (d_242_curves_)[d_243_i_]
            d_245_originalPublicKey_: _dafny.Seq
            d_245_originalPublicKey_ = (d_240_derX509PublicKeys_)[d_243_i_]
            d_246_publicKeyBytes_: _dafny.Seq
            d_246_publicKeyBytes_ = HexStrings.default__.FromHexString(d_245_originalPublicKey_)
            d_247_compressedKey_: _dafny.Seq
            out58_: _dafny.Seq
            out58_ = default__.expectLooseHexString((d_241_compressedKeys_)[d_243_i_])
            d_247_compressedKey_ = out58_
            d_248_compressedKeyBytes_: _dafny.Seq
            d_248_compressedKeyBytes_ = HexStrings.default__.FromHexString(d_247_compressedKey_)
            d_249_compressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
            d_250_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
            out59_: Wrappers.Result
            out59_ = ECDH.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.CompressPublicKeyInput_CompressPublicKeyInput(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_246_publicKeyBytes_), d_244_curve_))
            d_250_valueOrError0_ = out59_
            if not(not((d_250_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(474,39): " + _dafny.string_of(d_250_valueOrError0_))
            d_249_compressedPublicKeyResult_ = (d_250_valueOrError0_).Extract()
            if not(((d_249_compressedPublicKeyResult_).compressedPublicKey) == (d_248_compressedKeyBytes_)):
                raise _dafny.HaltException("test/TestECDH.dfy(481,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_251_compressedPublicKey_: _dafny.Seq
            d_251_compressedPublicKey_ = (d_249_compressedPublicKeyResult_).compressedPublicKey
            d_252_decompressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
            d_253_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
            out60_: Wrappers.Result
            out60_ = ECDH.default__.DecompressPublicKey(AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput_DecompressPublicKeyInput(d_251_compressedPublicKey_, d_244_curve_))
            d_253_valueOrError1_ = out60_
            if not(not((d_253_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(485,41): " + _dafny.string_of(d_253_valueOrError1_))
            d_252_decompressedPublicKeyResult_ = (d_253_valueOrError1_).Extract()
            d_254_decompressedPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey
            d_254_decompressedPublicKey_ = (d_252_decompressedPublicKeyResult_).publicKey
            if not((d_246_publicKeyBytes_) == ((d_254_decompressedPublicKey_).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(494,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPublicKeyValidationTestVectorsInfinity():
        d_255_curves_: _dafny.Seq
        d_255_curves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi15_ = len(d_255_curves_)
        for d_256_i_ in range(0, hi15_):
            d_257_der__ecc__inf_: _dafny.Seq
            d_258_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out61_: Wrappers.Result
            out61_ = ECDH.ECCUtils.GetInfinityPublicKey((d_255_curves_)[d_256_i_])
            d_258_valueOrError0_ = out61_
            if not(not((d_258_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(504,25): " + _dafny.string_of(d_258_valueOrError0_))
            d_257_der__ecc__inf_ = (d_258_valueOrError0_).Extract()
            d_259_validPublicKeyB_: Wrappers.Result
            out62_: Wrappers.Result
            out62_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_255_curves_)[d_256_i_], d_257_der__ecc__inf_))
            d_259_validPublicKeyB_ = out62_
            if not((d_259_validPublicKeyB_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(512,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_259_validPublicKeyB_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(513,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_260_errMsg_: _dafny.Seq
            d_260_errMsg_ = ((d_259_validPublicKeyB_).error).message
            if not(((((d_260_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__JAVA)) or ((d_260_errMsg_) == (default__.BAD__X509__KEY__ERR__MSG__RUST))) or ((d_260_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET6))) or ((d_260_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET48))):
                raise _dafny.HaltException("test/TestECDH.dfy(516,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPublicKeyValidationTestVectorsOutOfBounds():
        d_261_curves_: _dafny.Seq
        d_261_curves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi16_ = len(d_261_curves_)
        for d_262_i_ in range(0, hi16_):
            d_263_der__ecc__inf_: _dafny.Seq
            d_264_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out63_: Wrappers.Result
            out63_ = ECDH.ECCUtils.GetOutOfBoundsPublicKey((d_261_curves_)[d_262_i_])
            d_264_valueOrError0_ = out63_
            if not(not((d_264_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(531,25): " + _dafny.string_of(d_264_valueOrError0_))
            d_263_der__ecc__inf_ = (d_264_valueOrError0_).Extract()
            d_265_validPublicKeyB_: Wrappers.Result
            out64_: Wrappers.Result
            out64_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_261_curves_)[d_262_i_], d_263_der__ecc__inf_))
            d_265_validPublicKeyB_ = out64_
            if not((d_265_validPublicKeyB_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(539,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_265_validPublicKeyB_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(540,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_266_errMsg_: _dafny.Seq
            d_266_errMsg_ = ((d_265_validPublicKeyB_).error).message
            if not((((default__.seq__contains(d_266_errMsg_, default__.OUT__OF__BOUNDS__ERR__MSG__JAVA)) or ((d_266_errMsg_) == (default__.BAD__X509__KEY__ERR__MSG__RUST))) or ((d_266_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NET6))) or ((d_266_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NE48))):
                raise _dafny.HaltException("test/TestECDH.dfy(543,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def seq__contains(haystack, needle):
        while True:
            with _dafny.label():
                if (len(needle)) == (0):
                    return True
                elif (len(haystack)) == (0):
                    return False
                elif (len(haystack)) < (len(needle)):
                    return False
                elif (((needle)[0]) == ((haystack)[0])) and ((_dafny.Seq((needle)[1::])) <= (_dafny.Seq((haystack)[1::]))):
                    return True
                elif True:
                    in3_ = _dafny.Seq((haystack)[1::])
                    in4_ = needle
                    haystack = in3_
                    needle = in4_
                    raise _dafny.TailCall()
                break

    @_dafny.classproperty
    def P256(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()
    @_dafny.classproperty
    def P384(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384()
    @_dafny.classproperty
    def P521(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()
    @_dafny.classproperty
    def ECC__P256__PRIVATE(instance):
        return ((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n"))) + (_dafny.Seq("22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n"))) + (_dafny.Seq("7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))
    @_dafny.classproperty
    def ECC__P384__PRIVATE(instance):
        return (((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n"))) + (_dafny.Seq("6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n"))) + (_dafny.Seq("GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n"))) + (_dafny.Seq("b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))
    @_dafny.classproperty
    def ECC__P521__PRIVATE(instance):
        return (((((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n"))) + (_dafny.Seq("xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n"))) + (_dafny.Seq("oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n"))) + (_dafny.Seq("I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n"))) + (_dafny.Seq("C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n"))) + (_dafny.Seq("Qg==\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))
    @_dafny.classproperty
    def ECC__P256__PUBLIC(instance):
        return ((_dafny.Seq("3059301306072a8648ce3d020106082a8648ce3d03010703420004a7520c7b4ab9478")) + (_dafny.Seq("4f227dcc7197dcddc108b3cf9715fec9be172e575c1610b199f008eec272a313489"))) + (_dafny.Seq("e944c126391d8cd6085efbdc5bc96961981981a149b6bc"))
    @_dafny.classproperty
    def ECC__384__PUBLIC(instance):
        return (((_dafny.Seq("3076301006072a8648ce3d020106052b81040022036200041ac8f5ba07769518a58505")) + (_dafny.Seq("b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c"))) + (_dafny.Seq("905998c89f20e4daea5e6f54e2bcfd1461acbe7484bc32b04533ba0b06c248ab11a2"))) + (_dafny.Seq("450d443c522904bbf89a6b5e3a66b9aadf"))
    @_dafny.classproperty
    def ECC__P521__PUBLIC(instance):
        return ((((_dafny.Seq("30819b301006072a8648ce3d020106052b81040023038186000401de32732469d8769e")) + (_dafny.Seq("47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb2"))) + (_dafny.Seq("1d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39017df878ad9db941c8bd6e"))) + (_dafny.Seq("dcdea45a151f0b7babcb5d53f1d90d5be2db564997f01dfeb3a55a11058a6be49805"))) + (_dafny.Seq("e98f574e5a261534c5a685fcc86c2c6c0a2e93e942"))
    @_dafny.classproperty
    def ECC__256__PUBLIC__INF__FAIL__ON__LOAD(instance):
        return _dafny.Seq("3019301306072a8648ce3d020106082a8648ce3d03010703020000")
    @_dafny.classproperty
    def ECC__384__PUBLIC__INF__FAIL__ON__LOAD(instance):
        return _dafny.Seq("3016301006072a8648ce3d020106052b8104002203020000")
    @_dafny.classproperty
    def ECC__521__PUBLIC__INF__FAIL__ON__LOAD(instance):
        return _dafny.Seq("3016301006072a8648ce3d020106052b8104002303020000")
    @_dafny.classproperty
    def BAD__X509__KEY__ERR__MSG__RUST(instance):
        return _dafny.Seq("Invalid X509 Public Key.")
    @_dafny.classproperty
    def INFINITY__POINT__ERR__MSG__JAVA(instance):
        return _dafny.Seq("encoded key spec not recognized: Point at infinity")
    @_dafny.classproperty
    def INFINITY__POINT__ERR__MSG__NET6(instance):
        return _dafny.Seq("Point at infinity (Parameter 'q')")
    @_dafny.classproperty
    def INFINITY__POINT__ERR__MSG__NET48(instance):
        return _dafny.Seq("Point at infinity\r\nParameter name: q")
    @_dafny.classproperty
    def ECC__256__PUBLIC__INF(instance):
        return ((_dafny.Seq("3059301306072a864886f70d0106082a864886f70d03010703420004000000000000")) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000"))
    @_dafny.classproperty
    def ECC__384__PUBLIC__INF(instance):
        return (((_dafny.Seq("3076301006072a864886f70d0106052b810400220362000400000000000000000000")) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000"))
    @_dafny.classproperty
    def ECC__521__PUBLIC__INF(instance):
        return (((((_dafny.Seq("3081ee3010060772a8648ce3d02106052b81040023038186000400000000000000000")) + (_dafny.Seq("000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("0000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000"))
    @_dafny.classproperty
    def ECC__P256__PUBLIC__GP__FAIL__ON__LOAD(instance):
        return ((_dafny.Seq("3059301306072a8648ce3d020106082a8648ce3d03010703420004fffffffffffffffff")) + (_dafny.Seq("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"))) + (_dafny.Seq("ffffffffffffffffffffffffffffffffffffffffff"))
    @_dafny.classproperty
    def ECC__P384__PUBLIC__GP__FAIL__ON__LOAD(instance):
        return (((_dafny.Seq("3076301006072a8648ce3d020106052b8104002203620004fffffffffffffffffffffff")) + (_dafny.Seq("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"))) + (_dafny.Seq("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"))) + (_dafny.Seq("fffffffffffffffffffffffffffff"))
    @_dafny.classproperty
    def ECC__P521__PUBLIC__GP__FAIL__ON__LOAD(instance):
        return ((((_dafny.Seq("30819b301006072a8648ce3d020106052b810400230381860004ffffffffffffffffffff")) + (_dafny.Seq("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"))) + (_dafny.Seq("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"))) + (_dafny.Seq("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"))) + (_dafny.Seq("ffffffffffffffffffffffffffffffffff"))
    @_dafny.classproperty
    def OUT__OF__BOUNDS__ERR__MSG__JAVA(instance):
        return _dafny.Seq("encoded key spec not recognized: x value invalid for")
    @_dafny.classproperty
    def OUT__OF__BOUNDS__ERR__MSG__NET6(instance):
        return _dafny.Seq("value invalid for Fp field element (Parameter 'x')")
    @_dafny.classproperty
    def OUT__OF__BOUNDS__ERR__MSG__NE48(instance):
        return _dafny.Seq("value invalid for Fp field element\r\nParameter name: x")
    @_dafny.classproperty
    def ECC__P256__PUBLIC__GP(instance):
        return (((_dafny.Seq("3059301306072a864886f70d0106082a864886f70d03010703420004000000000000000")) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("000000001"))
    @_dafny.classproperty
    def ECC__P384__PUBLIC__GP(instance):
        return (((((_dafny.Seq("3076301006072a864886f70d0106052b810400220362000400000000000000000000000")) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("0000000000000000000000000000001"))
    @_dafny.classproperty
    def ECC__P521__PUBLIC__GP(instance):
        return (((((_dafny.Seq("3081ee3010060772a8648ce3d02106052b8104002303818600040000000000000000000")) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000000000000000000000000000000000000000000"))) + (_dafny.Seq("00000000000000000000000000000000001"))
    @_dafny.classproperty
    def ECC__P256__PUBLIC__COMPRESSED(instance):
        return _dafny.Seq("02a7520c7b4ab94784f227dcc7197dcddc108b3cf9715fec9be172e575c1610b19")
    @_dafny.classproperty
    def ECC__384__PUBLIC__COMPRESSED(instance):
        return _dafny.Seq("031ac8f5ba07769518a58505b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c905998")
    @_dafny.classproperty
    def ECC__P521__PUBLIC__COMPRESSED(instance):
        return _dafny.Seq("0201de32732469d8769e47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb21d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39")
