// Class WrapOutput<T>
// Dafny class WrapOutput<T> compiled into Java
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
public class WrapOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappedMaterial;
  public T _wrapInfo;
  protected dafny.TypeDescriptor<T> _td_T;
  public WrapOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    this._td_T = _td_T;
    this._wrappedMaterial = wrappedMaterial;
    this._wrapInfo = wrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    WrapOutput<T> o = (WrapOutput<T>)other;
    return true && java.util.Objects.equals(this._wrappedMaterial, o._wrappedMaterial) && java.util.Objects.equals(this._wrapInfo, o._wrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("MaterialWrapping.WrapOutput.WrapOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._wrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrapInfo));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<WrapOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<WrapOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<WrapOutput<T>>referenceWithInitializer(WrapOutput.class, () -> WrapOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> WrapOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return MaterialWrapping_Compile.WrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  @Deprecated()
  public static <T> WrapOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return MaterialWrapping_Compile.WrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  public static <T> WrapOutput<T> create(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return new WrapOutput<T>(_td_T, wrappedMaterial, wrapInfo);
  }
  @Deprecated()
  public static <T> WrapOutput<T> create(dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return new WrapOutput<T>(null, wrappedMaterial, wrapInfo);
  }
  public static <T> WrapOutput<T> create_WrapOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return create(_td_T, wrappedMaterial, wrapInfo);
  }
  @Deprecated()
  public static <T> WrapOutput<T> create_WrapOutput(dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return create(null, wrappedMaterial, wrapInfo);
  }
  public boolean is_WrapOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_wrappedMaterial() {
    return this._wrappedMaterial;
  }
  public T dtor_wrapInfo() {
    return this._wrapInfo;
  }
}
