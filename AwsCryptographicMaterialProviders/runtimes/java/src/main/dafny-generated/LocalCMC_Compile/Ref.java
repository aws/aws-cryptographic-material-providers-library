// Class Ref<T>
// Dafny class Ref<T> compiled into Java
package LocalCMC_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Ref<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public Ref(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
  }
  public static <T> dafny.TypeDescriptor<Ref<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Ref<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Ref<T>>referenceWithInitializer(Ref.class, () -> Ref.<T>Default(_td_T));
  }

  public static <T> Ref<T> Default(dafny.TypeDescriptor<T> _td_T) {
    return LocalCMC_Compile.Ref.<T>create_Null(_td_T);
  }
  @Deprecated()
  public static <T> Ref<T> Default() {
    dafny.TypeDescriptor<T> _td_T = null;
    return LocalCMC_Compile.Ref.<T>create_Null(_td_T);
  }
  public static <T> Ref<T> create_Ptr(dafny.TypeDescriptor<T> _td_T, T deref) {
    return new Ref_Ptr<T>(_td_T, deref);
  }
  @Deprecated()
  public static <T> Ref<T> create_Ptr(T deref) {
    return new Ref_Ptr<T>(null, deref);
  }
  public static <T> Ref<T> create_Null(dafny.TypeDescriptor<T> _td_T) {
    return new Ref_Null<T>(_td_T);
  }
  @Deprecated()
  public static <T> Ref<T> create_Null() {
    return new Ref_Null<T>(null);
  }
  public boolean is_Ptr() { return this instanceof Ref_Ptr; }
  public boolean is_Null() { return this instanceof Ref_Null; }
  public T dtor_deref() {
    Ref<T> d = this;
    return ((Ref_Ptr<T>)d)._deref;
  }
}
