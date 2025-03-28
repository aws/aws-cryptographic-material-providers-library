// Class AesUnwrapKeyMaterial
// Dafny class AesUnwrapKeyMaterial compiled into Java
package RawAESKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class AesUnwrapKeyMaterial implements MaterialWrapping_Compile.UnwrapMaterial<AesUnwrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.UnwrapInput, MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.UnwrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public AesUnwrapKeyMaterial() {
    this._wrappingKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._iv = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._wrappingAlgorithm = (software.amazon.cryptography.primitives.internaldafny.types.AES__GCM)null;
    this._cryptoPrimitives = null;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> wrappingKey, software.amazon.cryptography.primitives.internaldafny.types.AES__GCM wrappingAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> iv, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._wrappingKey = wrappingKey;
    (this)._iv = iv;
    (this)._wrappingAlgorithm = wrappingAlgorithm;
    (this)._cryptoPrimitives = cryptoPrimitives;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.UnwrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>_typeDescriptor(AesUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>Default(AesUnwrapInfo._typeDescriptor(), AesUnwrapInfo.Default()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _0_valueOrError0 = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD((input).dtor_encryptionContext());
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>_typeDescriptor(AesUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_aad;
    _1_aad = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf(((this).wrappingAlgorithm()).dtor_tagLength())).compareTo(java.math.BigInteger.valueOf(((input).dtor_wrappedMaterial()).length())) <= 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Insufficient data to decrypt.")));
    if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError1).<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>_typeDescriptor(AesUnwrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput _3_encryptionOutput;
    _3_encryptionOutput = __default.DeserializeEDKCiphertext((input).dtor_wrappedMaterial(), java.math.BigInteger.valueOf(((this).wrappingAlgorithm()).dtor_tagLength()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _4_maybePtKey;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).cryptoPrimitives()).AESDecrypt(software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput.create((this).wrappingAlgorithm(), (this).wrappingKey(), (_3_encryptionOutput).dtor_cipherText(), (_3_encryptionOutput).dtor_authTag(), (this).iv(), _1_aad));
    _4_maybePtKey = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _5_valueOrError2 = (_4_maybePtKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_6_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _6_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_6_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_6_e);
    }));
    if ((_5_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError2).<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>_typeDescriptor(AesUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _7_ptKey;
    _7_ptKey = (_5_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _8_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.util.Objects.equals(java.math.BigInteger.valueOf(AlgorithmSuites_Compile.__default.GetEncryptKeyLength((input).dtor_algorithmSuite())), java.math.BigInteger.valueOf((_7_ptKey).length())), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Plaintext Data Key is not the expected length")));
    if ((_8_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError3).<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>_typeDescriptor(AesUnwrapInfo._typeDescriptor()));
      return res;
    }
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>_typeDescriptor(AesUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<AesUnwrapInfo>create(AesUnwrapInfo._typeDescriptor(), _7_ptKey, RawAESKeyring_Compile.AesUnwrapInfo.create()));
    return res;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappingKey;
  public dafny.DafnySequence<? extends java.lang.Byte> wrappingKey()
  {
    return this._wrappingKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _iv;
  public dafny.DafnySequence<? extends java.lang.Byte> iv()
  {
    return this._iv;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _wrappingAlgorithm;
  public software.amazon.cryptography.primitives.internaldafny.types.AES__GCM wrappingAlgorithm()
  {
    return this._wrappingAlgorithm;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  private static final dafny.TypeDescriptor<AesUnwrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<AesUnwrapKeyMaterial>referenceWithInitializer(AesUnwrapKeyMaterial.class, () -> (AesUnwrapKeyMaterial) null);
  public static dafny.TypeDescriptor<AesUnwrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesUnwrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawAESKeyring.AesUnwrapKeyMaterial";
  }
}
