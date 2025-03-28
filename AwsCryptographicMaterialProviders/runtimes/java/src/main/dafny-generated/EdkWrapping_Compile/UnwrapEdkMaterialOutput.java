// Class UnwrapEdkMaterialOutput<T>
// Dafny class UnwrapEdkMaterialOutput<T> compiled into Java
package EdkWrapping_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class UnwrapEdkMaterialOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _plaintextDataKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _symmetricSigningKey;
  public T _unwrapInfo;
  protected dafny.TypeDescriptor<T> _td_T;
  public UnwrapEdkMaterialOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T unwrapInfo) {
    this._td_T = _td_T;
    this._plaintextDataKey = plaintextDataKey;
    this._symmetricSigningKey = symmetricSigningKey;
    this._unwrapInfo = unwrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UnwrapEdkMaterialOutput<T> o = (UnwrapEdkMaterialOutput<T>)other;
    return true && java.util.Objects.equals(this._plaintextDataKey, o._plaintextDataKey) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey) && java.util.Objects.equals(this._unwrapInfo, o._unwrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextDataKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._unwrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("EdkWrapping.UnwrapEdkMaterialOutput.UnwrapEdkMaterialOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._unwrapInfo));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<UnwrapEdkMaterialOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<UnwrapEdkMaterialOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<UnwrapEdkMaterialOutput<T>>referenceWithInitializer(UnwrapEdkMaterialOutput.class, () -> UnwrapEdkMaterialOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> UnwrapEdkMaterialOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return EdkWrapping_Compile.UnwrapEdkMaterialOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), _default_T);
  }
  @Deprecated()
  public static <T> UnwrapEdkMaterialOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return EdkWrapping_Compile.UnwrapEdkMaterialOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), _default_T);
  }
  public static <T> UnwrapEdkMaterialOutput<T> create(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T unwrapInfo) {
    return new UnwrapEdkMaterialOutput<T>(_td_T, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  @Deprecated()
  public static <T> UnwrapEdkMaterialOutput<T> create(dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T unwrapInfo) {
    return new UnwrapEdkMaterialOutput<T>(null, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  public static <T> UnwrapEdkMaterialOutput<T> create_UnwrapEdkMaterialOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T unwrapInfo) {
    return create(_td_T, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  @Deprecated()
  public static <T> UnwrapEdkMaterialOutput<T> create_UnwrapEdkMaterialOutput(dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T unwrapInfo) {
    return create(null, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  public boolean is_UnwrapEdkMaterialOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_plaintextDataKey() {
    return this._plaintextDataKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_symmetricSigningKey() {
    return this._symmetricSigningKey;
  }
  public T dtor_unwrapInfo() {
    return this._unwrapInfo;
  }
}
