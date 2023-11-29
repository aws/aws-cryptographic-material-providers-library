import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants
import JSON_mZeroCopy_mDeserializer_mValues
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy
import JSON_mAPI
import JSON
import JSONHelpers
import KeyDescription

# Module: KeyMaterial

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildKeyMaterials(mpl, obj):
        if (len(obj)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            d_1448_name_ = ((obj)[0])[0]
            d_1449_valueOrError0_ = default__.ToKeyMaterial(mpl, d_1448_name_, ((obj)[0])[1])
            if (d_1449_valueOrError0_).IsFailure():
                return (d_1449_valueOrError0_).PropagateFailure()
            elif True:
                d_1450_keyMaterial_ = (d_1449_valueOrError0_).Extract()
                d_1451_valueOrError1_ = default__.BuildKeyMaterials(mpl, _dafny.Seq((obj)[1::]))
                if (d_1451_valueOrError1_).IsFailure():
                    return (d_1451_valueOrError1_).PropagateFailure()
                elif True:
                    d_1452_tail_ = (d_1451_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Map({d_1448_name_: d_1450_keyMaterial_})) | (d_1452_tail_))

    @staticmethod
    def ToKeyMaterial(mpl, name, obj):
        d_1453_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("KeyDescription not an object"))
        if (d_1453_valueOrError0_).IsFailure():
            return (d_1453_valueOrError0_).PropagateFailure()
        elif True:
            d_1454_obj_ = (obj).obj
            d_1455_typString_ = _dafny.Seq("type")
            d_1456_valueOrError1_ = JSONHelpers.default__.GetString(d_1455_typString_, d_1454_obj_)
            if (d_1456_valueOrError1_).IsFailure():
                return (d_1456_valueOrError1_).PropagateFailure()
            elif True:
                d_1457_typ_ = (d_1456_valueOrError1_).Extract()
                d_1458_valueOrError2_ = Wrappers.default__.Need(default__.KeyMaterialString_q(d_1457_typ_), (_dafny.Seq("Unsupported KeyMaterial type:")) + (d_1457_typ_))
                if (d_1458_valueOrError2_).IsFailure():
                    return (d_1458_valueOrError2_).PropagateFailure()
                elif True:
                    if (d_1457_typ_) == (_dafny.Seq("static-material")):
                        d_1459_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), d_1454_obj_)
                        if (d_1459_valueOrError3_).IsFailure():
                            return (d_1459_valueOrError3_).PropagateFailure()
                        elif True:
                            d_1460_algorithmSuiteHex_ = (d_1459_valueOrError3_).Extract()
                            d_1461_valueOrError4_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_1460_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binnary"))
                            if (d_1461_valueOrError4_).IsFailure():
                                return (d_1461_valueOrError4_).PropagateFailure()
                            elif True:
                                d_1462_binaryId_ = HexStrings.default__.FromHexString(d_1460_algorithmSuiteHex_)
                                def lambda90_(d_1464_algorithmSuiteHex_):
                                    def lambda91_(d_1465_e_):
                                        return (_dafny.Seq("Invalid Suite:")) + (d_1464_algorithmSuiteHex_)

                                    return lambda91_

                                d_1463_valueOrError5_ = ((mpl).GetAlgorithmSuiteInfo(d_1462_binaryId_)).MapFailure(lambda90_(d_1460_algorithmSuiteHex_))
                                if (d_1463_valueOrError5_).IsFailure():
                                    return (d_1463_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_1466_algorithmSuite_ = (d_1463_valueOrError5_).Extract()
                                    d_1467_valueOrError6_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_1454_obj_)
                                    if (d_1467_valueOrError6_).IsFailure():
                                        return (d_1467_valueOrError6_).PropagateFailure()
                                    elif True:
                                        d_1468_encryptionContextStrings_ = (d_1467_valueOrError6_).Extract()
                                        d_1469_valueOrError7_ = JSONHelpers.default__.utf8EncodeMap(d_1468_encryptionContextStrings_)
                                        if (d_1469_valueOrError7_).IsFailure():
                                            return (d_1469_valueOrError7_).PropagateFailure()
                                        elif True:
                                            d_1470_encryptionContext_ = (d_1469_valueOrError7_).Extract()
                                            d_1471_valueOrError8_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_1454_obj_)
                                            if (d_1471_valueOrError8_).IsFailure():
                                                return (d_1471_valueOrError8_).PropagateFailure()
                                            elif True:
                                                d_1472_keysAsStrings_ = (d_1471_valueOrError8_).Extract()
                                                d_1473_valueOrError9_ = JSONHelpers.default__.utf8EncodeSeq(d_1472_keysAsStrings_)
                                                if (d_1473_valueOrError9_).IsFailure():
                                                    return (d_1473_valueOrError9_).PropagateFailure()
                                                elif True:
                                                    d_1474_requiredEncryptionContextKeys_ = (d_1473_valueOrError9_).Extract()
                                                    d_1475_valueOrError10_ = JSONHelpers.default__.GetArrayObject(_dafny.Seq("encryptedDataKeys"), d_1454_obj_)
                                                    if (d_1475_valueOrError10_).IsFailure():
                                                        return (d_1475_valueOrError10_).PropagateFailure()
                                                    elif True:
                                                        d_1476_encryptedDataKeysJSON_ = (d_1475_valueOrError10_).Extract()
                                                        d_1477_valueOrError11_ = Seq.default__.MapWithResult(default__.ToEncryptedDataKey, d_1476_encryptedDataKeysJSON_)
                                                        if (d_1477_valueOrError11_).IsFailure():
                                                            return (d_1477_valueOrError11_).PropagateFailure()
                                                        elif True:
                                                            d_1478_encryptedDataKeys_ = (d_1477_valueOrError11_).Extract()
                                                            d_1479_valueOrError12_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), d_1454_obj_)
                                                            if (d_1479_valueOrError12_).IsFailure():
                                                                return (d_1479_valueOrError12_).PropagateFailure()
                                                            elif True:
                                                                d_1480_plaintextDataKeyEncoded_ = (d_1479_valueOrError12_).Extract()
                                                                def iife61_(_pat_let26_0):
                                                                    def iife62_(d_1482_result_):
                                                                        return (Wrappers.Result_Success(Wrappers.Option_Some((d_1482_result_).value)) if (d_1482_result_).is_Success else Wrappers.Result_Failure((d_1482_result_).error))
                                                                    return iife62_(_pat_let26_0)
                                                                d_1481_valueOrError13_ = (iife61_(Base64.default__.Decode((d_1480_plaintextDataKeyEncoded_).value)) if (d_1480_plaintextDataKeyEncoded_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                                                                if (d_1481_valueOrError13_).IsFailure():
                                                                    return (d_1481_valueOrError13_).PropagateFailure()
                                                                elif True:
                                                                    d_1483_plaintextDataKey_ = (d_1481_valueOrError13_).Extract()
                                                                    d_1484_valueOrError14_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("signingKey"), d_1454_obj_)
                                                                    if (d_1484_valueOrError14_).IsFailure():
                                                                        return (d_1484_valueOrError14_).PropagateFailure()
                                                                    elif True:
                                                                        d_1485_signingKey_ = (d_1484_valueOrError14_).Extract()
                                                                        d_1486_valueOrError15_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("verificationKey"), d_1454_obj_)
                                                                        if (d_1486_valueOrError15_).IsFailure():
                                                                            return (d_1486_valueOrError15_).PropagateFailure()
                                                                        elif True:
                                                                            d_1487_verificationKey_ = (d_1486_valueOrError15_).Extract()
                                                                            d_1488_symmetricSigningKeys_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("symmetricSigningKeys"), d_1454_obj_)).ToOption()
                                                                            return Wrappers.Result_Success(KeyMaterial_StaticMaterial(name, d_1466_algorithmSuite_, d_1470_encryptionContext_, d_1478_encryptedDataKeys_, d_1474_requiredEncryptionContextKeys_, d_1483_plaintextDataKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
                    elif (d_1457_typ_) == (_dafny.Seq("static-branch-key")):
                        d_1489_valueOrError16_ = JSONHelpers.default__.GetString(_dafny.Seq("key-id"), d_1454_obj_)
                        if (d_1489_valueOrError16_).IsFailure():
                            return (d_1489_valueOrError16_).PropagateFailure()
                        elif True:
                            d_1490_keyIdentifier_ = (d_1489_valueOrError16_).Extract()
                            d_1491_valueOrError17_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKeyVersion"), d_1454_obj_)
                            if (d_1491_valueOrError17_).IsFailure():
                                return (d_1491_valueOrError17_).PropagateFailure()
                            elif True:
                                d_1492_branchKeyVersionEncoded_ = (d_1491_valueOrError17_).Extract()
                                d_1493_valueOrError18_ = UTF8.default__.Encode(d_1492_branchKeyVersionEncoded_)
                                if (d_1493_valueOrError18_).IsFailure():
                                    return (d_1493_valueOrError18_).PropagateFailure()
                                elif True:
                                    d_1494_branchKeyVersion_ = (d_1493_valueOrError18_).Extract()
                                    d_1495_valueOrError19_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKey"), d_1454_obj_)
                                    if (d_1495_valueOrError19_).IsFailure():
                                        return (d_1495_valueOrError19_).PropagateFailure()
                                    elif True:
                                        d_1496_branchKeyEncoded_ = (d_1495_valueOrError19_).Extract()
                                        d_1497_valueOrError20_ = Base64.default__.Decode(d_1496_branchKeyEncoded_)
                                        if (d_1497_valueOrError20_).IsFailure():
                                            return (d_1497_valueOrError20_).PropagateFailure()
                                        elif True:
                                            d_1498_branchKey_ = (d_1497_valueOrError20_).Extract()
                                            d_1499_valueOrError21_ = JSONHelpers.default__.GetString(_dafny.Seq("beaconKey"), d_1454_obj_)
                                            if (d_1499_valueOrError21_).IsFailure():
                                                return (d_1499_valueOrError21_).PropagateFailure()
                                            elif True:
                                                d_1500_beaconKeyEncoded_ = (d_1499_valueOrError21_).Extract()
                                                d_1501_valueOrError22_ = Base64.default__.Decode(d_1500_beaconKeyEncoded_)
                                                if (d_1501_valueOrError22_).IsFailure():
                                                    return (d_1501_valueOrError22_).PropagateFailure()
                                                elif True:
                                                    d_1502_beaconKey_ = (d_1501_valueOrError22_).Extract()
                                                    return Wrappers.Result_Success(KeyMaterial_StaticKeyStoreInformation(d_1490_keyIdentifier_, d_1494_branchKeyVersion_, d_1498_branchKey_, d_1502_beaconKey_))
                    elif True:
                        d_1503_valueOrError23_ = JSONHelpers.default__.GetBool(_dafny.Seq("encrypt"), d_1454_obj_)
                        if (d_1503_valueOrError23_).IsFailure():
                            return (d_1503_valueOrError23_).PropagateFailure()
                        elif True:
                            d_1504_encrypt_ = (d_1503_valueOrError23_).Extract()
                            d_1505_valueOrError24_ = JSONHelpers.default__.GetBool(_dafny.Seq("decrypt"), d_1454_obj_)
                            if (d_1505_valueOrError24_).IsFailure():
                                return (d_1505_valueOrError24_).PropagateFailure()
                            elif True:
                                d_1506_decrypt_ = (d_1505_valueOrError24_).Extract()
                                d_1507_valueOrError25_ = JSONHelpers.default__.GetString(_dafny.Seq("key-id"), d_1454_obj_)
                                if (d_1507_valueOrError25_).IsFailure():
                                    return (d_1507_valueOrError25_).PropagateFailure()
                                elif True:
                                    d_1508_keyIdentifier_ = (d_1507_valueOrError25_).Extract()
                                    if (d_1457_typ_) == (_dafny.Seq("aws-kms")):
                                        return Wrappers.Result_Success(KeyMaterial_KMS(name, d_1504_encrypt_, d_1506_decrypt_, d_1508_keyIdentifier_))
                                    elif True:
                                        d_1509_valueOrError26_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_1454_obj_)
                                        if (d_1509_valueOrError26_).IsFailure():
                                            return (d_1509_valueOrError26_).PropagateFailure()
                                        elif True:
                                            d_1510_algorithm_ = (d_1509_valueOrError26_).Extract()
                                            d_1511_valueOrError27_ = JSONHelpers.default__.GetNat(_dafny.Seq("bits"), d_1454_obj_)
                                            if (d_1511_valueOrError27_).IsFailure():
                                                return (d_1511_valueOrError27_).PropagateFailure()
                                            elif True:
                                                d_1512_bits_ = (d_1511_valueOrError27_).Extract()
                                                d_1513_valueOrError28_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_1454_obj_)
                                                if (d_1513_valueOrError28_).IsFailure():
                                                    return (d_1513_valueOrError28_).PropagateFailure()
                                                elif True:
                                                    d_1514_encoding_ = (d_1513_valueOrError28_).Extract()
                                                    d_1515_valueOrError29_ = JSONHelpers.default__.GetString(_dafny.Seq("material"), d_1454_obj_)
                                                    if (d_1515_valueOrError29_).IsFailure():
                                                        return (d_1515_valueOrError29_).PropagateFailure()
                                                    elif True:
                                                        d_1516_material_ = (d_1515_valueOrError29_).Extract()
                                                        if (d_1457_typ_) == (_dafny.Seq("symmetric")):
                                                            d_1517_valueOrError30_ = Base64.default__.Decode(d_1516_material_)
                                                            if (d_1517_valueOrError30_).IsFailure():
                                                                return (d_1517_valueOrError30_).PropagateFailure()
                                                            elif True:
                                                                d_1518_materialBytes_ = (d_1517_valueOrError30_).Extract()
                                                                return Wrappers.Result_Success(KeyMaterial_Symetric(name, d_1504_encrypt_, d_1506_decrypt_, d_1510_algorithm_, d_1512_bits_, d_1514_encoding_, d_1518_materialBytes_, d_1508_keyIdentifier_))
                                                        elif (d_1457_typ_) == (_dafny.Seq("private")):
                                                            return Wrappers.Result_Success(KeyMaterial_PrivateRSA(name, d_1504_encrypt_, d_1506_decrypt_, d_1510_algorithm_, d_1512_bits_, d_1514_encoding_, d_1516_material_, d_1508_keyIdentifier_))
                                                        elif (d_1457_typ_) == (_dafny.Seq("public")):
                                                            return Wrappers.Result_Success(KeyMaterial_PublicRSA(name, d_1504_encrypt_, d_1506_decrypt_, d_1512_bits_, d_1510_algorithm_, d_1514_encoding_, d_1516_material_, d_1508_keyIdentifier_))
                                                        elif True:
                                                            d_1519_valueOrError31_ = UTF8.default__.Encode(d_1516_material_)
                                                            if (d_1519_valueOrError31_).IsFailure():
                                                                return (d_1519_valueOrError31_).PropagateFailure()
                                                            elif True:
                                                                d_1520_publicKey_ = (d_1519_valueOrError31_).Extract()
                                                                return Wrappers.Result_Success(KeyMaterial_KMSAsymetric(name, d_1504_encrypt_, d_1506_decrypt_, d_1508_keyIdentifier_, d_1512_bits_, d_1510_algorithm_, d_1514_encoding_, d_1520_publicKey_))

    @staticmethod
    def ToEncryptedDataKey(obj):
        d_1521_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), obj)
        if (d_1521_valueOrError0_).IsFailure():
            return (d_1521_valueOrError0_).PropagateFailure()
        elif True:
            d_1522_keyProviderIdJSON_ = (d_1521_valueOrError0_).Extract()
            d_1523_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), obj)
            if (d_1523_valueOrError1_).IsFailure():
                return (d_1523_valueOrError1_).PropagateFailure()
            elif True:
                d_1524_keyProviderInfoJSON_ = (d_1523_valueOrError1_).Extract()
                d_1525_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), obj)
                if (d_1525_valueOrError2_).IsFailure():
                    return (d_1525_valueOrError2_).PropagateFailure()
                elif True:
                    d_1526_ciphertextJSON_ = (d_1525_valueOrError2_).Extract()
                    d_1527_valueOrError3_ = UTF8.default__.Encode(d_1522_keyProviderIdJSON_)
                    if (d_1527_valueOrError3_).IsFailure():
                        return (d_1527_valueOrError3_).PropagateFailure()
                    elif True:
                        d_1528_keyProviderId_ = (d_1527_valueOrError3_).Extract()
                        d_1529_valueOrError4_ = Base64.default__.Decode(d_1524_keyProviderInfoJSON_)
                        if (d_1529_valueOrError4_).IsFailure():
                            return (d_1529_valueOrError4_).PropagateFailure()
                        elif True:
                            d_1530_keyProviderInfo_ = (d_1529_valueOrError4_).Extract()
                            d_1531_valueOrError5_ = Base64.default__.Decode(d_1526_ciphertextJSON_)
                            if (d_1531_valueOrError5_).IsFailure():
                                return (d_1531_valueOrError5_).PropagateFailure()
                            elif True:
                                d_1532_ciphertext_ = (d_1531_valueOrError5_).Extract()
                                return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(d_1528_keyProviderId_, d_1530_keyProviderInfo_, d_1532_ciphertext_))

    @staticmethod
    def KeyMaterialString_q(s):
        return (((((((s) == (_dafny.Seq("static-material"))) or ((s) == (_dafny.Seq("aws-kms")))) or ((s) == (_dafny.Seq("symmetric")))) or ((s) == (_dafny.Seq("private")))) or ((s) == (_dafny.Seq("public")))) or ((s) == (_dafny.Seq("static-branch-key")))) or ((s) == (_dafny.Seq("aws-kms-rsa")))


class KeyMaterial:
    @classmethod
    def default(cls, ):
        return lambda: KeyMaterial_Symetric(_dafny.Seq({}), False, False, _dafny.Seq({}), int(0), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Symetric(self) -> bool:
        return isinstance(self, KeyMaterial_Symetric)
    @property
    def is_PrivateRSA(self) -> bool:
        return isinstance(self, KeyMaterial_PrivateRSA)
    @property
    def is_PublicRSA(self) -> bool:
        return isinstance(self, KeyMaterial_PublicRSA)
    @property
    def is_KMS(self) -> bool:
        return isinstance(self, KeyMaterial_KMS)
    @property
    def is_KMSAsymetric(self) -> bool:
        return isinstance(self, KeyMaterial_KMSAsymetric)
    @property
    def is_StaticMaterial(self) -> bool:
        return isinstance(self, KeyMaterial_StaticMaterial)
    @property
    def is_StaticKeyStoreInformation(self) -> bool:
        return isinstance(self, KeyMaterial_StaticKeyStoreInformation)

class KeyMaterial_Symetric(KeyMaterial, NamedTuple('Symetric', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('algorithm', Any), ('bits', Any), ('encoding', Any), ('wrappingKey', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.Symetric({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.wrappingKey)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_Symetric) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.algorithm == __o.algorithm and self.bits == __o.bits and self.encoding == __o.encoding and self.wrappingKey == __o.wrappingKey and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_PrivateRSA(KeyMaterial, NamedTuple('PrivateRSA', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('algorithm', Any), ('bits', Any), ('encoding', Any), ('material', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.PrivateRSA({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.material)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_PrivateRSA) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.algorithm == __o.algorithm and self.bits == __o.bits and self.encoding == __o.encoding and self.material == __o.material and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_PublicRSA(KeyMaterial, NamedTuple('PublicRSA', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('bits', Any), ('algorithm', Any), ('encoding', Any), ('material', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.PublicRSA({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.material)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_PublicRSA) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.bits == __o.bits and self.algorithm == __o.algorithm and self.encoding == __o.encoding and self.material == __o.material and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_KMS(KeyMaterial, NamedTuple('KMS', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.KMS({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_KMS) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_KMSAsymetric(KeyMaterial, NamedTuple('KMSAsymetric', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('keyIdentifier', Any), ('bits', Any), ('algorithm', Any), ('encoding', Any), ('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.KMSAsymetric({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.keyIdentifier)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_KMSAsymetric) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.keyIdentifier == __o.keyIdentifier and self.bits == __o.bits and self.algorithm == __o.algorithm and self.encoding == __o.encoding and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_StaticMaterial(KeyMaterial, NamedTuple('StaticMaterial', [('name', Any), ('algorithmSuite', Any), ('encryptionContext', Any), ('encryptedDataKeys', Any), ('requiredEncryptionContextKeys', Any), ('plaintextDataKey', Any), ('signingKey', Any), ('verificationKey', Any), ('symmetricSigningKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.StaticMaterial({_dafny.string_of(self.name)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.signingKey)}, {_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.symmetricSigningKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_StaticMaterial) and self.name == __o.name and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext and self.encryptedDataKeys == __o.encryptedDataKeys and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.plaintextDataKey == __o.plaintextDataKey and self.signingKey == __o.signingKey and self.verificationKey == __o.verificationKey and self.symmetricSigningKeys == __o.symmetricSigningKeys
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_StaticKeyStoreInformation(KeyMaterial, NamedTuple('StaticKeyStoreInformation', [('keyIdentifier', Any), ('branchKeyVersion', Any), ('branchKey', Any), ('beaconKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.StaticKeyStoreInformation({_dafny.string_of(self.keyIdentifier)}, {_dafny.string_of(self.branchKeyVersion)}, {_dafny.string_of(self.branchKey)}, {_dafny.string_of(self.beaconKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_StaticKeyStoreInformation) and self.keyIdentifier == __o.keyIdentifier and self.branchKeyVersion == __o.branchKeyVersion and self.branchKey == __o.branchKey and self.beaconKey == __o.beaconKey
    def __hash__(self) -> int:
        return super().__hash__()

