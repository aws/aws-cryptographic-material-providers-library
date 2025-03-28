// Class EcdhWrapKeyMaterial
// Dafny class EcdhWrapKeyMaterial compiled into Java
package EcdhEdkWrapping_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class EcdhWrapKeyMaterial implements MaterialWrapping_Compile.WrapMaterial<EcdhWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.WrapInput, MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.WrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public EcdhWrapKeyMaterial() {
    this._crypto = null;
    this._fixedInfo = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._sharedSecret = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> sharedSecret, dafny.DafnySequence<? extends java.lang.Byte> fixedInfo, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    (this)._sharedSecret = sharedSecret;
    (this)._fixedInfo = fixedInfo;
    (this)._crypto = crypto;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.WrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>Default(EcdhWrapInfo._typeDescriptor(), EcdhWrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _1_valueOrError0 = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD((input).dtor_encryptionContext());
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _2_canonicalizedEC;
    _2_canonicalizedEC = (_1_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _3_maybeSalt;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).crypto()).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create(Constants_Compile.__default.KDF__SALT__LEN()));
    _3_maybeSalt = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _4_valueOrError1 = (_3_maybeSalt).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _5_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_5_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_5_e);
    }));
    if ((_4_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError1).<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _6_salt;
    _6_salt = (_4_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = __default.DeriveSharedKeyingMaterial((this).sharedSecret(), (this).fixedInfo(), _6_salt, (this).crypto());
    _7_valueOrError2 = _out1;
    if ((_7_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError2).<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _8_derivedKeyingMaterial;
    _8_derivedKeyingMaterial = (_7_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _9_commitmentKey;
    _9_commitmentKey = (_8_derivedKeyingMaterial).subsequence(dafny.Helpers.toInt((java.math.BigInteger.ZERO)), dafny.Helpers.toInt((java.math.BigInteger.valueOf(32L))));
    dafny.DafnySequence<? extends java.lang.Byte> _10_sharedKeyingMaterial;
    _10_sharedKeyingMaterial = (_8_derivedKeyingMaterial).drop(java.math.BigInteger.valueOf(32L));
    dafny.DafnySequence<? extends java.lang.Byte> _11_iv;
    _11_iv = dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf((Constants_Compile.__default.ECDH__AES__256__ENC__ALG()).dtor_ivLength()), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_12___v3_boxed0) -> {
      java.math.BigInteger _12___v3 = ((java.math.BigInteger)(java.lang.Object)(_12___v3_boxed0));
      return (byte) 0;
    }));
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _13_maybeWrappedPdk;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = ((this).crypto()).AESEncrypt(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput.create(Constants_Compile.__default.ECDH__AES__256__ENC__ALG(), _11_iv, _10_sharedKeyingMaterial, (input).dtor_plaintextMaterial(), (this).fixedInfo()));
    _13_maybeWrappedPdk = _out2;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.Default());
    _14_valueOrError3 = (_13_maybeWrappedPdk).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_15_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _15_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_15_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_15_e);
    }));
    if ((_14_valueOrError3).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_14_valueOrError3).<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput _16_wrappedPdk;
    _16_wrappedPdk = (_14_valueOrError3).Extract(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo> _17_output;
    _17_output = MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>create(EcdhWrapInfo._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_6_salt, _9_commitmentKey), (_16_wrappedPdk).dtor_cipherText()), (_16_wrappedPdk).dtor_authTag()), EcdhEdkWrapping_Compile.EcdhWrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _17_output);
    return res;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _crypto;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto()
  {
    return this._crypto;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _fixedInfo;
  public dafny.DafnySequence<? extends java.lang.Byte> fixedInfo()
  {
    return this._fixedInfo;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _sharedSecret;
  public dafny.DafnySequence<? extends java.lang.Byte> sharedSecret()
  {
    return this._sharedSecret;
  }
  private static final dafny.TypeDescriptor<EcdhWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<EcdhWrapKeyMaterial>referenceWithInitializer(EcdhWrapKeyMaterial.class, () -> (EcdhWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<EcdhWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<EcdhWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "EcdhEdkWrapping.EcdhWrapKeyMaterial";
  }
}
