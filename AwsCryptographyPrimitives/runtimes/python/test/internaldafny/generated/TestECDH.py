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
        d_0_supportedCurves_: _dafny.Seq
        d_0_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_0_supportedCurves_)
        for d_1_i_ in range(0, hi0_):
            d_2_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_2_curve_ = (d_0_supportedCurves_)[d_1_i_]
            d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out0_: Wrappers.Result
            out0_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_2_curve_))
            d_3_valueOrError0_ = out0_
            if not(not((d_3_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(144,21): " + _dafny.string_of(d_3_valueOrError0_))
            d_4_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_4_keypair_ = (d_3_valueOrError0_).Extract()

    @staticmethod
    def TestGetPublicKeyFromPrivatePem():
        d_0_pemPrivateKeys_: _dafny.Seq
        d_0_pemPrivateKeys_ = _dafny.Seq([default__.ECC__P256__PRIVATE, default__.ECC__P384__PRIVATE, default__.ECC__P521__PRIVATE])
        d_1_derPublicKeys_: _dafny.Seq
        d_1_derPublicKeys_ = _dafny.Seq([default__.ECC__P256__PUBLIC, default__.ECC__384__PUBLIC, default__.ECC__P521__PUBLIC])
        d_2_supportedCurves_: _dafny.Seq
        d_2_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_2_supportedCurves_)
        for d_3_i_ in range(0, hi0_):
            d_4_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_4_curve_ = (d_2_supportedCurves_)[d_3_i_]
            d_5_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
            d_5_valueOrError0_ = UTF8.default__.Encode((d_0_pemPrivateKeys_)[d_3_i_])
            if not(not((d_5_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(161,24): " + _dafny.string_of(d_5_valueOrError0_))
            d_6_privateKey_: _dafny.Seq
            d_6_privateKey_ = (d_5_valueOrError0_).Extract()
            d_7_looseHexPublicKey_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.expectLooseHexString((d_1_derPublicKeys_)[d_3_i_])
            d_7_looseHexPublicKey_ = out0_
            d_8_publicKeyBytes_: _dafny.Seq
            d_8_publicKeyBytes_ = HexStrings.default__.FromHexString(d_7_looseHexPublicKey_)
            d_9_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.default())()
            out1_: Wrappers.Result
            out1_ = ECDH.default__.ParsePublicKey(AwsCryptographyPrimitivesTypes.ParsePublicKeyInput_ParsePublicKeyInput(d_8_publicKeyBytes_))
            d_9_valueOrError1_ = out1_
            if not(not((d_9_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(165,31): " + _dafny.string_of(d_9_valueOrError1_))
            d_10_expectedPublicKey_: AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput
            d_10_expectedPublicKey_ = (d_9_valueOrError1_).Extract()
            d_11_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput.default())()
            out2_: Wrappers.Result
            out2_ = ECDH.default__.GetPublicKeyFromPrivate(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput(d_4_curve_, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_6_privateKey_)))
            d_11_valueOrError2_ = out2_
            if not(not((d_11_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(170,23): " + _dafny.string_of(d_11_valueOrError2_))
            d_12_publicKey_: AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput
            d_12_publicKey_ = (d_11_valueOrError2_).Extract()
            if not(((d_12_publicKey_).publicKey) == (((d_10_expectedPublicKey_).publicKey).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(177,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetPublicKeyFromPrivateIncorrectCruve():
        d_0_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
        d_0_curve_ = default__.P384
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1_valueOrError0_ = UTF8.default__.Encode(default__.ECC__P256__PRIVATE)
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestECDH.dfy(184,22): " + _dafny.string_of(d_1_valueOrError0_))
        d_2_privateKey_: _dafny.Seq
        d_2_privateKey_ = (d_1_valueOrError0_).Extract()
        d_3_looseHexPublicKey_: _dafny.Seq
        out0_: _dafny.Seq
        out0_ = default__.expectLooseHexString(default__.ECC__P256__PUBLIC)
        d_3_looseHexPublicKey_ = out0_
        d_4_publicKeyBytes_: _dafny.Seq
        d_4_publicKeyBytes_ = HexStrings.default__.FromHexString(d_3_looseHexPublicKey_)
        d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.default())()
        out1_: Wrappers.Result
        out1_ = ECDH.default__.ParsePublicKey(AwsCryptographyPrimitivesTypes.ParsePublicKeyInput_ParsePublicKeyInput(d_4_publicKeyBytes_))
        d_5_valueOrError1_ = out1_
        if not(not((d_5_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestECDH.dfy(188,29): " + _dafny.string_of(d_5_valueOrError1_))
        d_6_expectedPublicKey_: AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput
        d_6_expectedPublicKey_ = (d_5_valueOrError1_).Extract()
        d_7_publicKey_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = ECDH.default__.GetPublicKeyFromPrivate(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput(d_0_curve_, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_2_privateKey_)))
        d_7_publicKey_ = out2_
        if not((d_7_publicKey_).is_Failure):
            raise _dafny.HaltException("test/TestECDH.dfy(200,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def expectLooseHexString(s):
        s2: _dafny.Seq = _dafny.Seq("")
        if not(HexStrings.default__.IsLooseHexString(s)):
            raise _dafny.HaltException("test/TestECDH.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        s2 = s
        return s2
        return s2

    @staticmethod
    def TestValidatePublicKeySuccess():
        d_0_supportedCurves_: _dafny.Seq
        d_0_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_0_supportedCurves_)
        for d_1_i_ in range(0, hi0_):
            d_2_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_2_curve_ = (d_0_supportedCurves_)[d_1_i_]
            d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out0_: Wrappers.Result
            out0_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_2_curve_))
            d_3_valueOrError0_ = out0_
            if not(not((d_3_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(217,22): " + _dafny.string_of(d_3_valueOrError0_))
            d_4_keypairA_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_4_keypairA_ = (d_3_valueOrError0_).Extract()
            d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out1_: Wrappers.Result
            out1_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_2_curve_))
            d_5_valueOrError1_ = out1_
            if not(not((d_5_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(222,22): " + _dafny.string_of(d_5_valueOrError1_))
            d_6_keypairB_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_6_keypairB_ = (d_5_valueOrError1_).Extract()
            d_7_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
            out2_: Wrappers.Result
            out2_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(d_2_curve_, ((d_6_keypairB_).publicKey).der))
            d_7_valueOrError2_ = out2_
            if not(not((d_7_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(228,29): " + _dafny.string_of(d_7_valueOrError2_))
            d_8_validPublicKeyB_: AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
            d_8_validPublicKeyB_ = (d_7_valueOrError2_).Extract()

    @staticmethod
    def TestValidatePublicKeyFailure():
        d_0_supportedCurves_: _dafny.Seq
        d_0_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_0_supportedCurves_)
        for d_1_i_ in range(0, hi0_):
            hi1_ = len(d_0_supportedCurves_)
            for d_2_j_ in range(0, hi1_):
                d_3_curve__i_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                d_3_curve__i_ = (d_0_supportedCurves_)[d_1_i_]
                d_4_curve__j_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                d_4_curve__j_ = (d_0_supportedCurves_)[d_2_j_]
                d_5_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
                out0_: Wrappers.Result
                out0_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_3_curve__i_))
                d_5_valueOrError0_ = out0_
                if not(not((d_5_valueOrError0_).IsFailure())):
                    raise _dafny.HaltException("test/TestECDH.dfy(248,24): " + _dafny.string_of(d_5_valueOrError0_))
                d_6_keypairA_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
                d_6_keypairA_ = (d_5_valueOrError0_).Extract()
                d_7_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
                out1_: Wrappers.Result
                out1_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_4_curve__j_))
                d_7_valueOrError1_ = out1_
                if not(not((d_7_valueOrError1_).IsFailure())):
                    raise _dafny.HaltException("test/TestECDH.dfy(253,24): " + _dafny.string_of(d_7_valueOrError1_))
                d_8_keypairB_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
                d_8_keypairB_ = (d_7_valueOrError1_).Extract()
                d_9_validPublicKeyB_: Wrappers.Result
                out2_: Wrappers.Result
                out2_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(d_3_curve__i_, ((d_8_keypairB_).publicKey).der))
                d_9_validPublicKeyB_ = out2_
                if (d_3_curve__i_) != (d_4_curve__j_):
                    if not((d_9_validPublicKeyB_).is_Failure):
                        raise _dafny.HaltException("test/TestECDH.dfy(267,10): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                elif True:
                    if not((d_9_validPublicKeyB_).is_Success):
                        raise _dafny.HaltException("test/TestECDH.dfy(269,10): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointAtINFFailOnLoad():
        d_0_publicKeysWithPointsAtINF_: _dafny.Seq
        d_0_publicKeysWithPointsAtINF_ = _dafny.Seq([default__.ECC__256__PUBLIC__INF__FAIL__ON__LOAD, default__.ECC__384__PUBLIC__INF__FAIL__ON__LOAD, default__.ECC__521__PUBLIC__INF__FAIL__ON__LOAD])
        d_1_supportedCurves_: _dafny.Seq
        d_1_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_1_supportedCurves_)
        for d_2_i_ in range(0, hi0_):
            d_3_looseHexPublicKey_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.expectLooseHexString((d_0_publicKeysWithPointsAtINF_)[d_2_i_])
            d_3_looseHexPublicKey_ = out0_
            d_4_publicKeyBytes_: _dafny.Seq
            d_4_publicKeyBytes_ = HexStrings.default__.FromHexString(d_3_looseHexPublicKey_)
            d_5_validPublicKey_: Wrappers.Result
            out1_: Wrappers.Result
            out1_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_1_supportedCurves_)[d_2_i_], d_4_publicKeyBytes_))
            d_5_validPublicKey_ = out1_
            if not((d_5_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(293,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_5_validPublicKey_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(295,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_6_errMsg_: _dafny.Seq
            d_6_errMsg_ = ((d_5_validPublicKey_).error).message
            if not(((((d_6_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__JAVA)) or ((d_6_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET6))) or ((d_6_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET48))) or (default__.seq__contains(d_6_errMsg_, default__.INFINITY__POINT__ERR__MSG__PYTHON))):
                raise _dafny.HaltException("test/TestECDH.dfy(298,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointAtINF():
        d_0_publicKeysWithPointsAtINF_: _dafny.Seq
        d_0_publicKeysWithPointsAtINF_ = _dafny.Seq([default__.ECC__256__PUBLIC__INF, default__.ECC__384__PUBLIC__INF, default__.ECC__521__PUBLIC__INF])
        d_1_supportedCurves_: _dafny.Seq
        d_1_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_1_supportedCurves_)
        for d_2_i_ in range(0, hi0_):
            d_3_looseHexPublicKey_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.expectLooseHexString((d_0_publicKeysWithPointsAtINF_)[d_2_i_])
            d_3_looseHexPublicKey_ = out0_
            d_4_publicKeyBytes_: _dafny.Seq
            d_4_publicKeyBytes_ = HexStrings.default__.FromHexString(d_3_looseHexPublicKey_)
            d_5_validPublicKey_: Wrappers.Result
            out1_: Wrappers.Result
            out1_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_1_supportedCurves_)[d_2_i_], d_4_publicKeyBytes_))
            d_5_validPublicKey_ = out1_
            if not((d_5_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(322,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad():
        d_0_publicKeysWithPointsGreaterThanP_: _dafny.Seq
        d_0_publicKeysWithPointsGreaterThanP_ = _dafny.Seq([default__.ECC__P256__PUBLIC__GP__FAIL__ON__LOAD, default__.ECC__P384__PUBLIC__GP__FAIL__ON__LOAD, default__.ECC__P521__PUBLIC__GP__FAIL__ON__LOAD])
        d_1_supportedCurves_: _dafny.Seq
        d_1_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_1_supportedCurves_)
        for d_2_i_ in range(0, hi0_):
            d_3_looseHexPublicKey_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.expectLooseHexString((d_0_publicKeysWithPointsGreaterThanP_)[d_2_i_])
            d_3_looseHexPublicKey_ = out0_
            d_4_publicKeyBytes_: _dafny.Seq
            d_4_publicKeyBytes_ = HexStrings.default__.FromHexString(d_3_looseHexPublicKey_)
            d_5_validPublicKey_: Wrappers.Result
            out1_: Wrappers.Result
            out1_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_1_supportedCurves_)[d_2_i_], d_4_publicKeyBytes_))
            d_5_validPublicKey_ = out1_
            if not((d_5_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(343,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_5_validPublicKey_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(345,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_6_errMsg_: _dafny.Seq
            d_6_errMsg_ = ((d_5_validPublicKey_).error).message
            if not((((default__.seq__contains(d_6_errMsg_, default__.OUT__OF__BOUNDS__ERR__MSG__JAVA)) or ((d_6_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NET6))) or ((d_6_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NE48))) or (default__.seq__contains(d_6_errMsg_, default__.OUT__OF__BOUNDS__ERR__MSG__PYTHON))):
                raise _dafny.HaltException("test/TestECDH.dfy(347,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidatePublicKeyFailurePointGreaterThanP():
        d_0_publicKeysWithPointsGreaterThanP_: _dafny.Seq
        d_0_publicKeysWithPointsGreaterThanP_ = _dafny.Seq([default__.ECC__P256__PUBLIC__GP, default__.ECC__P384__PUBLIC__GP, default__.ECC__P521__PUBLIC__GP])
        d_1_supportedCurves_: _dafny.Seq
        d_1_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_1_supportedCurves_)
        for d_2_i_ in range(0, hi0_):
            d_3_looseHexPublicKey_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.expectLooseHexString((d_0_publicKeysWithPointsGreaterThanP_)[d_2_i_])
            d_3_looseHexPublicKey_ = out0_
            d_4_publicKeyBytes_: _dafny.Seq
            d_4_publicKeyBytes_ = HexStrings.default__.FromHexString(d_3_looseHexPublicKey_)
            d_5_validPublicKey_: Wrappers.Result
            out1_: Wrappers.Result
            out1_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_1_supportedCurves_)[d_2_i_], d_4_publicKeyBytes_))
            d_5_validPublicKey_ = out1_
            if not((d_5_validPublicKey_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(371,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGenerateSharedSecret():
        d_0_supportedCurves_: _dafny.Seq
        d_0_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_0_supportedCurves_)
        for d_1_i_ in range(0, hi0_):
            d_2_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_2_curve_ = (d_0_supportedCurves_)[d_1_i_]
            d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out0_: Wrappers.Result
            out0_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_2_curve_))
            d_3_valueOrError0_ = out0_
            if not(not((d_3_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(381,22): " + _dafny.string_of(d_3_valueOrError0_))
            d_4_keypairA_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_4_keypairA_ = (d_3_valueOrError0_).Extract()
            d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out1_: Wrappers.Result
            out1_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_2_curve_))
            d_5_valueOrError1_ = out1_
            if not(not((d_5_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(386,22): " + _dafny.string_of(d_5_valueOrError1_))
            d_6_keypairB_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_6_keypairB_ = (d_5_valueOrError1_).Extract()
            if not((((d_4_keypairA_).privateKey) != ((d_6_keypairB_).privateKey)) and (((d_4_keypairA_).publicKey) != ((d_6_keypairB_).publicKey))):
                raise _dafny.HaltException("test/TestECDH.dfy(392,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_7_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
            out2_: Wrappers.Result
            out2_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(d_2_curve_, ((d_6_keypairB_).publicKey).der))
            d_7_valueOrError2_ = out2_
            if not(not((d_7_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(397,29): " + _dafny.string_of(d_7_valueOrError2_))
            d_8_validPublicKeyB_: AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
            d_8_validPublicKeyB_ = (d_7_valueOrError2_).Extract()
            d_9_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out3_: Wrappers.Result
            out3_ = ECDH.default__.DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(d_2_curve_, (d_4_keypairA_).privateKey, (d_6_keypairB_).publicKey))
            d_9_valueOrError3_ = out3_
            if not(not((d_9_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(404,27): " + _dafny.string_of(d_9_valueOrError3_))
            d_10_sharedSecretA_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_10_sharedSecretA_ = (d_9_valueOrError3_).Extract()
            d_11_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out4_: Wrappers.Result
            out4_ = ECDH.default__.DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(d_2_curve_, (d_6_keypairB_).privateKey, (d_4_keypairA_).publicKey))
            d_11_valueOrError4_ = out4_
            if not(not((d_11_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(412,27): " + _dafny.string_of(d_11_valueOrError4_))
            d_12_sharedSecretB_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_12_sharedSecretB_ = (d_11_valueOrError4_).Extract()
            if not((d_10_sharedSecretA_) == (d_12_sharedSecretB_)):
                raise _dafny.HaltException("test/TestECDH.dfy(420,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCompressDecompressPublicKey():
        d_0_supportedCurves_: _dafny.Seq
        d_0_supportedCurves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_0_supportedCurves_)
        for d_1_i_ in range(0, hi0_):
            d_2_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_2_curve_ = (d_0_supportedCurves_)[d_1_i_]
            d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out0_: Wrappers.Result
            out0_ = ECDH.default__.GenerateEccKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(d_2_curve_))
            d_3_valueOrError0_ = out0_
            if not(not((d_3_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(429,21): " + _dafny.string_of(d_3_valueOrError0_))
            d_4_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_4_keypair_ = (d_3_valueOrError0_).Extract()
            d_5_originalPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey
            d_5_originalPublicKey_ = (d_4_keypair_).publicKey
            d_6_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
            out1_: Wrappers.Result
            out1_ = ECDH.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.CompressPublicKeyInput_CompressPublicKeyInput(d_5_originalPublicKey_, d_2_curve_))
            d_6_valueOrError1_ = out1_
            if not(not((d_6_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(436,39): " + _dafny.string_of(d_6_valueOrError1_))
            d_7_compressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
            d_7_compressedPublicKeyResult_ = (d_6_valueOrError1_).Extract()
            if not(((d_7_compressedPublicKeyResult_).compressedPublicKey) != ((d_5_originalPublicKey_).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(443,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_8_compressedPublicKey_: _dafny.Seq
            d_8_compressedPublicKey_ = (d_7_compressedPublicKeyResult_).compressedPublicKey
            d_9_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
            out2_: Wrappers.Result
            out2_ = ECDH.default__.DecompressPublicKey(AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput_DecompressPublicKeyInput(d_8_compressedPublicKey_, d_2_curve_))
            d_9_valueOrError2_ = out2_
            if not(not((d_9_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(447,41): " + _dafny.string_of(d_9_valueOrError2_))
            d_10_decompressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
            d_10_decompressedPublicKeyResult_ = (d_9_valueOrError2_).Extract()
            d_11_decompressedPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey
            d_11_decompressedPublicKey_ = (d_10_decompressedPublicKeyResult_).publicKey
            if not(((d_5_originalPublicKey_).der) == ((d_11_decompressedPublicKey_).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(456,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCompressDecompressConstantPublicKeys():
        d_0_derX509PublicKeys_: _dafny.Seq
        d_0_derX509PublicKeys_ = _dafny.Seq([default__.ECC__P256__PUBLIC, default__.ECC__384__PUBLIC, default__.ECC__P521__PUBLIC])
        d_1_compressedKeys_: _dafny.Seq
        d_1_compressedKeys_ = _dafny.Seq([default__.ECC__P256__PUBLIC__COMPRESSED, default__.ECC__384__PUBLIC__COMPRESSED, default__.ECC__P521__PUBLIC__COMPRESSED])
        d_2_curves_: _dafny.Seq
        d_2_curves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_2_curves_)
        for d_3_i_ in range(0, hi0_):
            d_4_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_4_curve_ = (d_2_curves_)[d_3_i_]
            d_5_originalPublicKey_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.expectLooseHexString((d_0_derX509PublicKeys_)[d_3_i_])
            d_5_originalPublicKey_ = out0_
            d_6_publicKeyBytes_: _dafny.Seq
            d_6_publicKeyBytes_ = HexStrings.default__.FromHexString(d_5_originalPublicKey_)
            d_7_compressedKey_: _dafny.Seq
            out1_: _dafny.Seq
            out1_ = default__.expectLooseHexString((d_1_compressedKeys_)[d_3_i_])
            d_7_compressedKey_ = out1_
            d_8_compressedKeyBytes_: _dafny.Seq
            d_8_compressedKeyBytes_ = HexStrings.default__.FromHexString(d_7_compressedKey_)
            d_9_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
            out2_: Wrappers.Result
            out2_ = ECDH.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.CompressPublicKeyInput_CompressPublicKeyInput(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_6_publicKeyBytes_), d_4_curve_))
            d_9_valueOrError0_ = out2_
            if not(not((d_9_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(473,39): " + _dafny.string_of(d_9_valueOrError0_))
            d_10_compressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
            d_10_compressedPublicKeyResult_ = (d_9_valueOrError0_).Extract()
            if not(((d_10_compressedPublicKeyResult_).compressedPublicKey) == (d_8_compressedKeyBytes_)):
                raise _dafny.HaltException("test/TestECDH.dfy(480,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_11_compressedPublicKey_: _dafny.Seq
            d_11_compressedPublicKey_ = (d_10_compressedPublicKeyResult_).compressedPublicKey
            d_12_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
            out3_: Wrappers.Result
            out3_ = ECDH.default__.DecompressPublicKey(AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput_DecompressPublicKeyInput(d_11_compressedPublicKey_, d_4_curve_))
            d_12_valueOrError1_ = out3_
            if not(not((d_12_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(484,41): " + _dafny.string_of(d_12_valueOrError1_))
            d_13_decompressedPublicKeyResult_: AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
            d_13_decompressedPublicKeyResult_ = (d_12_valueOrError1_).Extract()
            d_14_decompressedPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey
            d_14_decompressedPublicKey_ = (d_13_decompressedPublicKeyResult_).publicKey
            if not((d_6_publicKeyBytes_) == ((d_14_decompressedPublicKey_).der)):
                raise _dafny.HaltException("test/TestECDH.dfy(493,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPublicKeyValidationTestVectorsInfinity():
        d_0_curves_: _dafny.Seq
        d_0_curves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_0_curves_)
        for d_1_i_ in range(0, hi0_):
            d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out0_: Wrappers.Result
            out0_ = ECDH.ECCUtils.GetInfinityPublicKey((d_0_curves_)[d_1_i_])
            d_2_valueOrError0_ = out0_
            if not(not((d_2_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(503,25): " + _dafny.string_of(d_2_valueOrError0_))
            d_3_der__ecc__inf_: _dafny.Seq
            d_3_der__ecc__inf_ = (d_2_valueOrError0_).Extract()
            d_4_validPublicKeyB_: Wrappers.Result
            out1_: Wrappers.Result
            out1_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_0_curves_)[d_1_i_], d_3_der__ecc__inf_))
            d_4_validPublicKeyB_ = out1_
            if not((d_4_validPublicKeyB_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(511,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_4_validPublicKeyB_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(512,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_5_errMsg_: _dafny.Seq
            d_5_errMsg_ = ((d_4_validPublicKeyB_).error).message
            if not(((((d_5_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__JAVA)) or ((d_5_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET6))) or ((d_5_errMsg_) == (default__.INFINITY__POINT__ERR__MSG__NET48))) or (default__.seq__contains(d_5_errMsg_, default__.INFINITY__POINT__ERR__MSG__PYTHON))):
                raise _dafny.HaltException("test/TestECDH.dfy(515,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPublicKeyValidationTestVectorsOutOfBounds():
        d_0_curves_: _dafny.Seq
        d_0_curves_ = _dafny.Seq([default__.P256, default__.P384, default__.P521])
        hi0_ = len(d_0_curves_)
        for d_1_i_ in range(0, hi0_):
            d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out0_: Wrappers.Result
            out0_ = ECDH.ECCUtils.GetOutOfBoundsPublicKey((d_0_curves_)[d_1_i_])
            d_2_valueOrError0_ = out0_
            if not(not((d_2_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("test/TestECDH.dfy(530,25): " + _dafny.string_of(d_2_valueOrError0_))
            d_3_der__ecc__inf_: _dafny.Seq
            d_3_der__ecc__inf_ = (d_2_valueOrError0_).Extract()
            d_4_validPublicKeyB_: Wrappers.Result
            out1_: Wrappers.Result
            out1_ = ECDH.default__.ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput((d_0_curves_)[d_1_i_], d_3_der__ecc__inf_))
            d_4_validPublicKeyB_ = out1_
            if not((d_4_validPublicKeyB_).is_Failure):
                raise _dafny.HaltException("test/TestECDH.dfy(538,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_4_validPublicKeyB_).error).is_AwsCryptographicPrimitivesError):
                raise _dafny.HaltException("test/TestECDH.dfy(539,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_5_errMsg_: _dafny.Seq
            d_5_errMsg_ = ((d_4_validPublicKeyB_).error).message
            if not((((default__.seq__contains(d_5_errMsg_, default__.OUT__OF__BOUNDS__ERR__MSG__JAVA)) or ((d_5_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NET6))) or ((d_5_errMsg_) == (default__.OUT__OF__BOUNDS__ERR__MSG__NE48))) or (default__.seq__contains(d_5_errMsg_, default__.OUT__OF__BOUNDS__ERR__MSG__PYTHON))):
                raise _dafny.HaltException("test/TestECDH.dfy(542,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

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
                    in0_ = _dafny.Seq((haystack)[1::])
                    in1_ = needle
                    haystack = in0_
                    needle = in1_
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
    def INFINITY__POINT__ERR__MSG__JAVA(instance):
        return _dafny.Seq("encoded key spec not recognized: Point at infinity")
    @_dafny.classproperty
    def INFINITY__POINT__ERR__MSG__NET6(instance):
        return _dafny.Seq("Point at infinity (Parameter 'q')")
    @_dafny.classproperty
    def INFINITY__POINT__ERR__MSG__NET48(instance):
        return _dafny.Seq("Point at infinity\r\nParameter name: q")
    @_dafny.classproperty
    def INFINITY__POINT__ERR__MSG__PYTHON(instance):
        return _dafny.Seq("Unable to load EC key")
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
    def OUT__OF__BOUNDS__ERR__MSG__PYTHON(instance):
        return _dafny.Seq("Could not deserialize key data. The data may be in an incorrect format")
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
