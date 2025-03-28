// Class EcdhGenerateAndWrapKeyMaterial
// Dafny class EcdhGenerateAndWrapKeyMaterial compiled into Java
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
public class EcdhGenerateAndWrapKeyMaterial implements MaterialWrapping_Compile.GenerateAndWrapMaterial<EcdhWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.GenerateAndWrapInput, MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.GenerateAndWrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public EcdhGenerateAndWrapKeyMaterial() {
    this._crypto = null;
    this._sharedSecret = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._fixedInfo = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> sharedSecret, dafny.DafnySequence<? extends java.lang.Byte> fixedInfo, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    (this)._sharedSecret = sharedSecret;
    (this)._fixedInfo = fixedInfo;
    (this)._crypto = crypto;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.GenerateAndWrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.GenerateAndWrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<EcdhWrapInfo>Default(EcdhWrapInfo._typeDescriptor(), EcdhWrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _1_pdkResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).crypto()).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create(AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_0_suite)));
    _1_pdkResult = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _2_valueOrError0 = (_1_pdkResult).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_3_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _3_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_3_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_3_e);
    }));
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _4_pdk;
    _4_pdk = (_2_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    EcdhWrapKeyMaterial _5_wrap;
    EcdhWrapKeyMaterial _nw0 = new EcdhWrapKeyMaterial();
    _nw0.__ctor((this).sharedSecret(), (this).fixedInfo(), (this).crypto());
    _5_wrap = _nw0;
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>Default(EcdhWrapInfo._typeDescriptor(), EcdhWrapInfo.Default()));
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_5_wrap).Invoke(MaterialWrapping_Compile.WrapInput.create(_4_pdk, (input).dtor_algorithmSuite(), (input).dtor_encryptionContext()));
    _6_valueOrError1 = _out1;
    if ((_6_valueOrError1).IsFailure(MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError1).<MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>>PropagateFailure(MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.WrapOutput<EcdhWrapInfo> _7_wrapOutput;
    _7_wrapOutput = (_6_valueOrError1).Extract(MaterialWrapping_Compile.WrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo> _8_output;
    _8_output = MaterialWrapping_Compile.GenerateAndWrapOutput.<EcdhWrapInfo>create(EcdhWrapInfo._typeDescriptor(), _4_pdk, (_7_wrapOutput).dtor_wrappedMaterial(), (_7_wrapOutput).dtor_wrapInfo());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.GenerateAndWrapOutput.<EcdhWrapInfo>_typeDescriptor(EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _8_output);
    return res;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _crypto;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto()
  {
    return this._crypto;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _sharedSecret;
  public dafny.DafnySequence<? extends java.lang.Byte> sharedSecret()
  {
    return this._sharedSecret;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _fixedInfo;
  public dafny.DafnySequence<? extends java.lang.Byte> fixedInfo()
  {
    return this._fixedInfo;
  }
  private static final dafny.TypeDescriptor<EcdhGenerateAndWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<EcdhGenerateAndWrapKeyMaterial>referenceWithInitializer(EcdhGenerateAndWrapKeyMaterial.class, () -> (EcdhGenerateAndWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<EcdhGenerateAndWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<EcdhGenerateAndWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial";
  }
}
