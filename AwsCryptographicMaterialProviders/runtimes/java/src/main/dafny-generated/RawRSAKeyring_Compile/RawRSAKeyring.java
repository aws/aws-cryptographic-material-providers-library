// Class RawRSAKeyring
// Dafny class RawRSAKeyring compiled into Java
package RawRSAKeyring_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;
import MrkAwareStrictMultiKeyring_Compile.*;
import LocalCMC_Compile.*;
import StormTracker_Compile.*;
import software.amazon.cryptography.internaldafny.StormTrackingCMC.*;
import CacheConstants_Compile.*;
import AwsKmsHierarchicalKeyring_Compile.*;
import AwsKmsRsaKeyring_Compile.*;
import EcdhEdkWrapping_Compile.*;
import RawECDHKeyring_Compile.*;
import AwsKmsEcdhKeyring_Compile.*;
import RawAESKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawRSAKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public RawRSAKeyring() {
    this._cryptoPrimitives = null;
    this._keyNamespace = UTF8.ValidUTF8Bytes.defaultValue();
    this._keyName = UTF8.ValidUTF8Bytes.defaultValue();
    this._paddingScheme = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.Default();
    this._publicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    this._privateKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out11;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out11;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> namespace, dafny.DafnySequence<? extends java.lang.Byte> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> privateKey, software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._keyNamespace = namespace;
    (this)._keyName = name;
    (this)._paddingScheme = paddingScheme;
    (this)._publicKey = publicKey;
    (this)._privateKey = privateKey;
    (this)._cryptoPrimitives = cryptoPrimitives;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((this).publicKey()).is_Some()) && ((java.math.BigInteger.valueOf((((this).publicKey()).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))).length())).signum() == 1), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("A RawRSAKeyring without a public key cannot provide OnEncrypt")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _1_materials;
      _1_materials = (input).dtor_materials();
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_suite;
      _2_suite = (_1_materials).dtor_algorithmSuite();
      RsaWrapKeyMaterial _3_wrap;
      RsaWrapKeyMaterial _nw0 = new RsaWrapKeyMaterial();
      _nw0.__ctor(((this).publicKey()).dtor_value(), (this).paddingScheme(), (this).cryptoPrimitives());
      _3_wrap = _nw0;
      RsaGenerateAndWrapKeyMaterial _4_generateAndWrap;
      RsaGenerateAndWrapKeyMaterial _nw1 = new RsaGenerateAndWrapKeyMaterial();
      _nw1.__ctor(((this).publicKey()).dtor_value(), (this).paddingScheme(), (this).cryptoPrimitives());
      _4_generateAndWrap = _nw1;
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>Default(RsaWrapInfo._typeDescriptor(), RsaWrapInfo.Default()));
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = EdkWrapping_Compile.__default.<RsaWrapInfo>WrapEdkMaterial(RsaWrapInfo._typeDescriptor(), _1_materials, _3_wrap, _4_generateAndWrap);
      _5_valueOrError1 = _out0;
      if ((_5_valueOrError1).IsFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return output;
      }
      EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo> _6_wrapOutput;
      _6_wrapOutput = (_5_valueOrError1).Extract(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _7_symmetricSigningKeyList;
      if (((_6_wrapOutput).dtor_symmetricSigningKey()).is_Some()) {
        _7_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_6_wrapOutput).dtor_symmetricSigningKey()).dtor_value()));
      } else {
        _7_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _8_edk;
      _8_edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create((this).keyNamespace(), (this).keyName(), (_6_wrapOutput).dtor_wrappedMaterial());
      if ((_6_wrapOutput).is_GenerateAndWrapEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _9_valueOrError2 = Materials_Compile.__default.EncryptionMaterialAddDataKey(_1_materials, (_6_wrapOutput).dtor_plaintextDataKey(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _8_edk), _7_symmetricSigningKeyList);
        if ((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_9_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return output;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_result;
        _10_result = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_10_result));
        return output;
      } else if ((_6_wrapOutput).is_WrapOnlyEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _11_valueOrError3 = Materials_Compile.__default.EncryptionMaterialAddEncryptedDataKeys(_1_materials, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _8_edk), _7_symmetricSigningKeyList);
        if ((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_11_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return output;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _12_result;
        _12_result = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_12_result));
        return output;
      }
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((this).privateKey()).is_Some()) && ((java.math.BigInteger.valueOf((((this).privateKey()).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))).length())).signum() == 1), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("A RawRSAKeyring without a private key cannot provide OnEncrypt")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _1_materials;
    _1_materials = (input).dtor_materials();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_1_materials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_errors;
    _3_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> empty(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf(((input).dtor_encryptedDataKeys()).length());
    for (java.math.BigInteger _4_i = java.math.BigInteger.ZERO; _4_i.compareTo(_hi0) < 0; _4_i = _4_i.add(java.math.BigInteger.ONE)) {
      if ((this).ShouldDecryptEDK(((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((_4_i))))))) {
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _5_edk;
        _5_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((_4_i)))));
        RsaUnwrapKeyMaterial _6_unwrap;
        RsaUnwrapKeyMaterial _nw0 = new RsaUnwrapKeyMaterial();
        _nw0.__ctor(((this).privateKey()).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), (this).paddingScheme(), (this).cryptoPrimitives());
        _6_unwrap = _nw0;
        Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_unwrapOutput;
        Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = EdkWrapping_Compile.__default.<RsaUnwrapInfo>UnwrapEdkMaterial(RsaUnwrapInfo._typeDescriptor(), (_5_edk).dtor_ciphertext(), _1_materials, _6_unwrap);
        _7_unwrapOutput = _out0;
        if ((_7_unwrapOutput).is_Success()) {
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
          _8_valueOrError2 = Materials_Compile.__default.DecryptionMaterialsAddDataKey(_1_materials, ((_7_unwrapOutput).dtor_value()).dtor_plaintextDataKey(), ((_7_unwrapOutput).dtor_value()).dtor_symmetricSigningKey());
          if ((_8_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_8_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
            return output;
          }
          software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _9_returnMaterials;
          _9_returnMaterials = (_8_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_9_returnMaterials));
          return output;
        } else {
          _3_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>concatenate(_3_errors, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> of(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_7_unwrapOutput).dtor_error()));
        }
      } else {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
        _10_valueOrError3 = (UTF8.__default.Decode((((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((_4_i)))))).dtor_keyProviderId())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_11_e_boxed0) -> {
          dafny.DafnySequence<? extends Character> _11_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_11_e_boxed0));
          return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_11_e);
        }));
        if ((_10_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_10_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
          return output;
        }
        dafny.DafnySequence<? extends Character> _12_extractedKeyProviderId;
        _12_extractedKeyProviderId = (_10_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _3_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>concatenate(_3_errors, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> of(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(ErrorMessages_Compile.__default.IncorrectRawDataKeys(StandardLibrary_mString_Compile.__default.Base10Int2String(_4_i), dafny.DafnySequence.asString("RSAKeyring"), _12_extractedKeyProviderId))));
      }
    }
    output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_3_errors, dafny.DafnySequence.asString("Raw RSA Key was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")));
    return output;
  }
  public boolean ShouldDecryptEDK(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk) {
    return (((UTF8.__default.ValidUTF8Seq((edk).dtor_keyProviderInfo())) && (((edk).dtor_keyProviderInfo()).equals((this).keyName()))) && (((edk).dtor_keyProviderId()).equals((this).keyNamespace()))) && ((java.math.BigInteger.valueOf(((edk).dtor_ciphertext()).length())).signum() == 1);
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _keyNamespace;
  public dafny.DafnySequence<? extends java.lang.Byte> keyNamespace()
  {
    return this._keyNamespace;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _keyName;
  public dafny.DafnySequence<? extends java.lang.Byte> keyName()
  {
    return this._keyName;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode _paddingScheme;
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme()
  {
    return this._paddingScheme;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _publicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey()
  {
    return this._publicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _privateKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> privateKey()
  {
    return this._privateKey;
  }
  private static final dafny.TypeDescriptor<RawRSAKeyring> _TYPE = dafny.TypeDescriptor.<RawRSAKeyring>referenceWithInitializer(RawRSAKeyring.class, () -> (RawRSAKeyring) null);
  public static dafny.TypeDescriptor<RawRSAKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawRSAKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawRSAKeyring.RawRSAKeyring";
  }
}
