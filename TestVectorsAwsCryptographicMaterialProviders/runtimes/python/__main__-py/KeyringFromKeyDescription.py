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
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
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
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores

# Module: KeyringFromKeyDescription

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ToKeyring(mpl, info):
        output: Wrappers.Result = None
        let_tmp_rhs17_ = info
        d_1533_description_ = let_tmp_rhs17_.description
        d_1534_material_ = let_tmp_rhs17_.material
        source40_ = d_1533_description_
        if source40_.is_Kms:
            d_1535___mcc_h0_ = source40_.Kms
            source41_ = d_1535___mcc_h0_
            d_1536___mcc_h1_ = source41_.keyId
            d_1537_key_ = d_1536___mcc_h1_
            if True:
                d_1538_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1538_valueOrError1_ = Wrappers.default__.Need(((d_1534_material_).is_Some) and (((d_1534_material_).value).is_KMS), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_1538_valueOrError1_).IsFailure():
                    output = (d_1538_valueOrError1_).PropagateFailure()
                    return output
                d_1539_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_1540_valueOrError2_: Wrappers.Result = None
                out303_: Wrappers.Result
                out303_ = default__.getKmsClient(mpl, ((d_1534_material_).value).keyIdentifier)
                d_1540_valueOrError2_ = out303_
                if (d_1540_valueOrError2_).IsFailure():
                    output = (d_1540_valueOrError2_).PropagateFailure()
                    return output
                d_1539_kmsClient_ = (d_1540_valueOrError2_).Extract()
                d_1541_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput
                d_1541_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_1534_material_).value).keyIdentifier, d_1539_kmsClient_, Wrappers.Option_None())
                d_1542_keyring_: Wrappers.Result
                out304_: Wrappers.Result
                out304_ = (mpl).CreateAwsKmsKeyring(d_1541_input_)
                d_1542_keyring_ = out304_
                def lambda92_(d_1543_e_):
                    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1543_e_)

                output = (d_1542_keyring_).MapFailure(lambda92_)
                return output
        elif source40_.is_KmsMrk:
            d_1544___mcc_h2_ = source40_.KmsMrk
            source42_ = d_1544___mcc_h2_
            d_1545___mcc_h3_ = source42_.keyId
            d_1546_key_ = d_1545___mcc_h3_
            if True:
                d_1547_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1547_valueOrError3_ = Wrappers.default__.Need(((d_1534_material_).is_Some) and (((d_1534_material_).value).is_KMS), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_1547_valueOrError3_).IsFailure():
                    output = (d_1547_valueOrError3_).PropagateFailure()
                    return output
                d_1548_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_1549_valueOrError4_: Wrappers.Result = None
                out305_: Wrappers.Result
                out305_ = default__.getKmsClient(mpl, ((d_1534_material_).value).keyIdentifier)
                d_1549_valueOrError4_ = out305_
                if (d_1549_valueOrError4_).IsFailure():
                    output = (d_1549_valueOrError4_).PropagateFailure()
                    return output
                d_1548_kmsClient_ = (d_1549_valueOrError4_).Extract()
                d_1550_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput
                d_1550_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_1534_material_).value).keyIdentifier, d_1548_kmsClient_, Wrappers.Option_None())
                d_1551_keyring_: Wrappers.Result
                out306_: Wrappers.Result
                out306_ = (mpl).CreateAwsKmsMrkKeyring(d_1550_input_)
                d_1551_keyring_ = out306_
                def lambda93_(d_1552_e_):
                    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1552_e_)

                output = (d_1551_keyring_).MapFailure(lambda93_)
                return output
        elif source40_.is_KmsMrkDiscovery:
            d_1553___mcc_h4_ = source40_.KmsMrkDiscovery
            source43_ = d_1553___mcc_h4_
            d_1554___mcc_h5_ = source43_.keyId
            d_1555___mcc_h6_ = source43_.defaultMrkRegion
            d_1556___mcc_h7_ = source43_.awsKmsDiscoveryFilter
            d_1557_awsKmsDiscoveryFilter_ = d_1556___mcc_h7_
            d_1558_defaultMrkRegion_ = d_1555___mcc_h6_
            if True:
                d_1559_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1559_valueOrError8_ = Wrappers.default__.Need((d_1534_material_).is_None, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                if (d_1559_valueOrError8_).IsFailure():
                    output = (d_1559_valueOrError8_).PropagateFailure()
                    return output
                d_1560_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                d_1560_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_1558_defaultMrkRegion_]), d_1557_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                d_1561_keyring_: Wrappers.Result
                out307_: Wrappers.Result
                out307_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_1560_input_)
                d_1561_keyring_ = out307_
                def lambda94_(d_1562_e_):
                    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1562_e_)

                output = (d_1561_keyring_).MapFailure(lambda94_)
                return output
        elif source40_.is_RSA:
            d_1563___mcc_h8_ = source40_.RSA
            source44_ = d_1563___mcc_h8_
            d_1564___mcc_h9_ = source44_.keyId
            d_1565___mcc_h10_ = source44_.providerId
            d_1566___mcc_h11_ = source44_.padding
            d_1567_padding_ = d_1566___mcc_h11_
            d_1568_providerId_ = d_1565___mcc_h10_
            d_1569_key_ = d_1564___mcc_h9_
            if True:
                d_1570_valueOrError11_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1570_valueOrError11_ = Wrappers.default__.Need(((d_1534_material_).is_Some) and ((((d_1534_material_).value).is_PrivateRSA) or (((d_1534_material_).value).is_PublicRSA)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
                if (d_1570_valueOrError11_).IsFailure():
                    output = (d_1570_valueOrError11_).PropagateFailure()
                    return output
                source45_ = d_1534_material_
                d_1571___mcc_h22_ = source45_.value
                source46_ = d_1571___mcc_h22_
                if source46_.is_PrivateRSA:
                    d_1572___mcc_h31_ = source46_.name
                    d_1573___mcc_h32_ = source46_.encrypt
                    d_1574___mcc_h33_ = source46_.decrypt
                    d_1575___mcc_h34_ = source46_.algorithm
                    d_1576___mcc_h35_ = source46_.bits
                    d_1577___mcc_h36_ = source46_.encoding
                    d_1578___mcc_h37_ = source46_.material
                    d_1579___mcc_h38_ = source46_.keyIdentifier
                    d_1580_keyIdentifier_ = d_1579___mcc_h38_
                    d_1581_material_ = d_1578___mcc_h37_
                    d_1582_decrypt_ = d_1574___mcc_h33_
                    if True:
                        d_1583_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_1583_valueOrError12_ = Wrappers.default__.Need(d_1582_decrypt_, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                        if (d_1583_valueOrError12_).IsFailure():
                            output = (d_1583_valueOrError12_).PropagateFailure()
                            return output
                        d_1584_privateKeyPemBytes_: _dafny.Seq
                        d_1585_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda95_(d_1586_e_):
                            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(d_1586_e_)

                        d_1585_valueOrError13_ = (UTF8.default__.Encode(d_1581_material_)).MapFailure(lambda95_)
                        if (d_1585_valueOrError13_).IsFailure():
                            output = (d_1585_valueOrError13_).PropagateFailure()
                            return output
                        d_1584_privateKeyPemBytes_ = (d_1585_valueOrError13_).Extract()
                        d_1587_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_1587_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1568_providerId_, d_1580_keyIdentifier_, d_1567_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_1584_privateKeyPemBytes_))
                        d_1588_keyring_: Wrappers.Result
                        out308_: Wrappers.Result
                        out308_ = (mpl).CreateRawRsaKeyring(d_1587_input_)
                        d_1588_keyring_ = out308_
                        def lambda96_(d_1589_e_):
                            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1589_e_)

                        output = (d_1588_keyring_).MapFailure(lambda96_)
                        return output
                elif True:
                    d_1590___mcc_h39_ = source46_.name
                    d_1591___mcc_h40_ = source46_.encrypt
                    d_1592___mcc_h41_ = source46_.decrypt
                    d_1593___mcc_h42_ = source46_.bits
                    d_1594___mcc_h43_ = source46_.algorithm
                    d_1595___mcc_h44_ = source46_.encoding
                    d_1596___mcc_h45_ = source46_.material
                    d_1597___mcc_h46_ = source46_.keyIdentifier
                    d_1598_keyIdentifier_ = d_1597___mcc_h46_
                    d_1599_material_ = d_1596___mcc_h45_
                    d_1600_encrypt_ = d_1591___mcc_h40_
                    if True:
                        d_1601_valueOrError14_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_1601_valueOrError14_ = Wrappers.default__.Need(d_1600_encrypt_, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                        if (d_1601_valueOrError14_).IsFailure():
                            output = (d_1601_valueOrError14_).PropagateFailure()
                            return output
                        d_1602_publicKeyPemBytes_: _dafny.Seq
                        d_1603_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda97_(d_1604_e_):
                            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(d_1604_e_)

                        d_1603_valueOrError15_ = (UTF8.default__.Encode(d_1599_material_)).MapFailure(lambda97_)
                        if (d_1603_valueOrError15_).IsFailure():
                            output = (d_1603_valueOrError15_).PropagateFailure()
                            return output
                        d_1602_publicKeyPemBytes_ = (d_1603_valueOrError15_).Extract()
                        d_1605_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_1605_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1568_providerId_, d_1598_keyIdentifier_, d_1567_padding_, Wrappers.Option_Some(d_1602_publicKeyPemBytes_), Wrappers.Option_None())
                        d_1606_keyring_: Wrappers.Result
                        out309_: Wrappers.Result
                        out309_ = (mpl).CreateRawRsaKeyring(d_1605_input_)
                        d_1606_keyring_ = out309_
                        def lambda98_(d_1607_e_):
                            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1607_e_)

                        output = (d_1606_keyring_).MapFailure(lambda98_)
                        return output
        elif source40_.is_AES:
            d_1608___mcc_h12_ = source40_.AES
            source47_ = d_1608___mcc_h12_
            d_1609___mcc_h13_ = source47_.keyId
            d_1610___mcc_h14_ = source47_.providerId
            d_1611_providerId_ = d_1610___mcc_h14_
            d_1612_key_ = d_1609___mcc_h13_
            if True:
                d_1613_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1613_valueOrError9_ = Wrappers.default__.Need(((d_1534_material_).is_Some) and (((d_1534_material_).value).is_Symetric), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not type: Symetric")))
                if (d_1613_valueOrError9_).IsFailure():
                    output = (d_1613_valueOrError9_).PropagateFailure()
                    return output
                d_1614_wrappingAlg_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
                d_1615_valueOrError10_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg.default())()
                d_1615_valueOrError10_ = (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()) if (((d_1534_material_).value).bits) == (128) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16()) if (((d_1534_material_).value).bits) == (192) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()) if (((d_1534_material_).value).bits) == (256) else Wrappers.Result_Failure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not a supported bit length"))))))
                if (d_1615_valueOrError10_).IsFailure():
                    output = (d_1615_valueOrError10_).PropagateFailure()
                    return output
                d_1614_wrappingAlg_ = (d_1615_valueOrError10_).Extract()
                d_1616_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput
                d_1616_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1611_providerId_, ((d_1534_material_).value).keyIdentifier, ((d_1534_material_).value).wrappingKey, d_1614_wrappingAlg_)
                d_1617_keyring_: Wrappers.Result
                out310_: Wrappers.Result
                out310_ = (mpl).CreateRawAesKeyring(d_1616_input_)
                d_1617_keyring_ = out310_
                def lambda99_(d_1618_e_):
                    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1618_e_)

                output = (d_1617_keyring_).MapFailure(lambda99_)
                return output
        elif source40_.is_Static:
            d_1619___mcc_h15_ = source40_.Static
            source48_ = d_1619___mcc_h15_
            d_1620___mcc_h16_ = source48_.keyId
            d_1621_key_ = d_1620___mcc_h16_
            if True:
                d_1622_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1622_valueOrError0_ = Wrappers.default__.Need(((d_1534_material_).is_Some) and (((d_1534_material_).value).is_StaticMaterial), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                if (d_1622_valueOrError0_).IsFailure():
                    output = (d_1622_valueOrError0_).PropagateFailure()
                    return output
                d_1623_encrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
                d_1623_encrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials(((d_1534_material_).value).algorithmSuite, ((d_1534_material_).value).encryptionContext, ((d_1534_material_).value).encryptedDataKeys, ((d_1534_material_).value).requiredEncryptionContextKeys, ((d_1534_material_).value).plaintextDataKey, ((d_1534_material_).value).signingKey, ((d_1534_material_).value).symmetricSigningKeys)
                d_1624_decrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                d_1624_decrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials(((d_1534_material_).value).algorithmSuite, ((d_1534_material_).value).encryptionContext, ((d_1534_material_).value).requiredEncryptionContextKeys, ((d_1534_material_).value).plaintextDataKey, ((d_1534_material_).value).verificationKey, Wrappers.Option_None())
                d_1625_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out311_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out311_ = CreateStaticKeyrings.default__.CreateStaticMaterialsKeyring(d_1623_encrypt_, d_1624_decrypt_)
                d_1625_keyring_ = out311_
                output = Wrappers.Result_Success(d_1625_keyring_)
                return output
        elif source40_.is_KmsRsa:
            d_1626___mcc_h17_ = source40_.KmsRsa
            source49_ = d_1626___mcc_h17_
            d_1627___mcc_h18_ = source49_.keyId
            d_1628___mcc_h19_ = source49_.encryptionAlgorithm
            d_1629_encryptionAlgorithm_ = d_1628___mcc_h19_
            d_1630_key_ = d_1627___mcc_h18_
            if True:
                d_1631_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1631_valueOrError5_ = Wrappers.default__.Need(((d_1534_material_).is_Some) and (((d_1534_material_).value).is_KMSAsymetric), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                if (d_1631_valueOrError5_).IsFailure():
                    output = (d_1631_valueOrError5_).PropagateFailure()
                    return output
                d_1632_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_1633_valueOrError6_: Wrappers.Result = None
                out312_: Wrappers.Result
                out312_ = default__.getKmsClient(mpl, ((d_1534_material_).value).keyIdentifier)
                d_1633_valueOrError6_ = out312_
                if (d_1633_valueOrError6_).IsFailure():
                    output = (d_1633_valueOrError6_).PropagateFailure()
                    return output
                d_1632_kmsClient_ = (d_1633_valueOrError6_).Extract()
                d_1634_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput
                d_1634_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_1534_material_).value).publicKey), ((d_1534_material_).value).keyIdentifier, d_1629_encryptionAlgorithm_, Wrappers.Option_Some(d_1632_kmsClient_), Wrappers.Option_None())
                d_1635_keyring_: Wrappers.Result
                out313_: Wrappers.Result
                out313_ = (mpl).CreateAwsKmsRsaKeyring(d_1634_input_)
                d_1635_keyring_ = out313_
                def lambda100_(d_1636_e_):
                    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1636_e_)

                output = (d_1635_keyring_).MapFailure(lambda100_)
                return output
        elif True:
            d_1637___mcc_h20_ = source40_.Hierarchy
            source50_ = d_1637___mcc_h20_
            d_1638___mcc_h21_ = source50_.keyId
            d_1639_key_ = d_1638___mcc_h21_
            if True:
                d_1640_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1640_valueOrError7_ = Wrappers.default__.Need(((d_1534_material_).is_Some) and (((d_1534_material_).value).is_StaticKeyStoreInformation), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                if (d_1640_valueOrError7_).IsFailure():
                    output = (d_1640_valueOrError7_).PropagateFailure()
                    return output
                d_1641_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out314_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out314_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_1534_material_).value)
                d_1641_keyStore_ = out314_
                d_1642_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput
                d_1642_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_1534_material_).value).keyIdentifier), Wrappers.Option_None(), d_1641_keyStore_, 0, Wrappers.Option_None())
                d_1643_keyring_: Wrappers.Result
                out315_: Wrappers.Result
                out315_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_1642_input_)
                d_1643_keyring_ = out315_
                def lambda101_(d_1644_e_):
                    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1644_e_)

                output = (d_1643_keyring_).MapFailure(lambda101_)
                return output
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_1645_maybeClientSupplier_: Wrappers.Result
        out316_: Wrappers.Result
        out316_ = (mpl).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_1645_maybeClientSupplier_ = out316_
        d_1646_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_1647_valueOrError0_: Wrappers.Result = None
        def lambda102_(d_1648_e_):
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1648_e_)

        d_1647_valueOrError0_ = (d_1645_maybeClientSupplier_).MapFailure(lambda102_)
        if (d_1647_valueOrError0_).IsFailure():
            output = (d_1647_valueOrError0_).PropagateFailure()
            return output
        d_1646_clientSupplier_ = (d_1647_valueOrError0_).Extract()
        d_1649_arn_: AwsArnParsing.AwsArn
        d_1650_valueOrError1_: Wrappers.Result = None
        def lambda103_(d_1651_e_):
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(d_1651_e_)

        d_1650_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(maybeKmsArn)).MapFailure(lambda103_)
        if (d_1650_valueOrError1_).IsFailure():
            output = (d_1650_valueOrError1_).PropagateFailure()
            return output
        d_1649_arn_ = (d_1650_valueOrError1_).Extract()
        d_1652_tmp_: Wrappers.Result
        out317_: Wrappers.Result
        out317_ = (d_1646_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_1649_arn_).region))
        d_1652_tmp_ = out317_
        def lambda104_(d_1653_e_):
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_1653_e_)

        output = (d_1652_tmp_).MapFailure(lambda104_)
        return output


class KeyringInfo:
    @classmethod
    def default(cls, ):
        return lambda: KeyringInfo_KeyringInfo(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyringInfo(self) -> bool:
        return isinstance(self, KeyringInfo_KeyringInfo)

class KeyringInfo_KeyringInfo(KeyringInfo, NamedTuple('KeyringInfo', [('description', Any), ('material', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyringFromKeyDescription.KeyringInfo.KeyringInfo({_dafny.string_of(self.description)}, {_dafny.string_of(self.material)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyringInfo_KeyringInfo) and self.description == __o.description and self.material == __o.material
    def __hash__(self) -> int:
        return super().__hash__()

