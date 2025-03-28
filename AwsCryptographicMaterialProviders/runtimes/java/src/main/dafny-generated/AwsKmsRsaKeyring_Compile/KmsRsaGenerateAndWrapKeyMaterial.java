// Class KmsRsaGenerateAndWrapKeyMaterial
// Dafny class KmsRsaGenerateAndWrapKeyMaterial compiled into Java
package AwsKmsRsaKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsRsaGenerateAndWrapKeyMaterial implements MaterialWrapping_Compile.GenerateAndWrapMaterial<KmsRsaWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.GenerateAndWrapInput, MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.GenerateAndWrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsRsaGenerateAndWrapKeyMaterial() {
    this._publicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._cryptoPrimitives = null;
    this._paddingScheme = software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.Default();
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> publicKey, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._publicKey = publicKey;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._paddingScheme = paddingScheme;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.GenerateAndWrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsRsaWrapInfo>Default(KmsRsaWrapInfo._typeDescriptor(), KmsRsaWrapInfo.Default()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_generateBytesResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).cryptoPrimitives()).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create(AlgorithmSuites_Compile.__default.GetEncryptKeyLength((input).dtor_algorithmSuite())));
    _0_generateBytesResult = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _1_valueOrError0 = (_0_generateBytesResult).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_plaintextMaterial;
    _3_plaintextMaterial = (_1_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    KmsRsaWrapKeyMaterial _4_wrap;
    KmsRsaWrapKeyMaterial _nw0 = new KmsRsaWrapKeyMaterial();
    _nw0.__ctor((this).publicKey(), (this).paddingScheme(), (this).cryptoPrimitives());
    _4_wrap = _nw0;
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>Default(KmsRsaWrapInfo._typeDescriptor(), KmsRsaWrapInfo.Default()));
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_4_wrap).Invoke(MaterialWrapping_Compile.WrapInput.create(_3_plaintextMaterial, (input).dtor_algorithmSuite(), (input).dtor_encryptionContext()));
    _5_valueOrError1 = _out1;
    if ((_5_valueOrError1).IsFailure(MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>>PropagateFailure(MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo> _6_wrapOutput;
    _6_wrapOutput = (_5_valueOrError1).Extract(MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo> _7_output;
    _7_output = MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsRsaWrapInfo>create(KmsRsaWrapInfo._typeDescriptor(), _3_plaintextMaterial, (_6_wrapOutput).dtor_wrappedMaterial(), AwsKmsRsaKeyring_Compile.KmsRsaWrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _7_output);
    return res;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> publicKey()
  {
    return this._publicKey;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _paddingScheme;
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme()
  {
    return this._paddingScheme;
  }
  private static final dafny.TypeDescriptor<KmsRsaGenerateAndWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsRsaGenerateAndWrapKeyMaterial>referenceWithInitializer(KmsRsaGenerateAndWrapKeyMaterial.class, () -> (KmsRsaGenerateAndWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsRsaGenerateAndWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsRsaGenerateAndWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsRsaKeyring.KmsRsaGenerateAndWrapKeyMaterial";
  }
}
