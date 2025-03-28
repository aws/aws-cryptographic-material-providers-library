// Class UnwrapOutput<T>
// Dafny class UnwrapOutput<T> compiled into Java
package MaterialWrapping_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class UnwrapOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _unwrappedMaterial;
  public T _unwrapInfo;
  protected dafny.TypeDescriptor<T> _td_T;
  public UnwrapOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> unwrappedMaterial, T unwrapInfo) {
    this._td_T = _td_T;
    this._unwrappedMaterial = unwrappedMaterial;
    this._unwrapInfo = unwrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UnwrapOutput<T> o = (UnwrapOutput<T>)other;
    return true && java.util.Objects.equals(this._unwrappedMaterial, o._unwrappedMaterial) && java.util.Objects.equals(this._unwrapInfo, o._unwrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._unwrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._unwrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("MaterialWrapping.UnwrapOutput.UnwrapOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._unwrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._unwrapInfo));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<UnwrapOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<UnwrapOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<UnwrapOutput<T>>referenceWithInitializer(UnwrapOutput.class, () -> UnwrapOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> UnwrapOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return MaterialWrapping_Compile.UnwrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  @Deprecated()
  public static <T> UnwrapOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return MaterialWrapping_Compile.UnwrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  public static <T> UnwrapOutput<T> create(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> unwrappedMaterial, T unwrapInfo) {
    return new UnwrapOutput<T>(_td_T, unwrappedMaterial, unwrapInfo);
  }
  @Deprecated()
  public static <T> UnwrapOutput<T> create(dafny.DafnySequence<? extends java.lang.Byte> unwrappedMaterial, T unwrapInfo) {
    return new UnwrapOutput<T>(null, unwrappedMaterial, unwrapInfo);
  }
  public static <T> UnwrapOutput<T> create_UnwrapOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> unwrappedMaterial, T unwrapInfo) {
    return create(_td_T, unwrappedMaterial, unwrapInfo);
  }
  @Deprecated()
  public static <T> UnwrapOutput<T> create_UnwrapOutput(dafny.DafnySequence<? extends java.lang.Byte> unwrappedMaterial, T unwrapInfo) {
    return create(null, unwrappedMaterial, unwrapInfo);
  }
  public boolean is_UnwrapOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_unwrappedMaterial() {
    return this._unwrappedMaterial;
  }
  public T dtor_unwrapInfo() {
    return this._unwrapInfo;
  }
}
