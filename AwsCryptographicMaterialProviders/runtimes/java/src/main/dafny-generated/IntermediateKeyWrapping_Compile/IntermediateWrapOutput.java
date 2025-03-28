// Class IntermediateWrapOutput<T>
// Dafny class IntermediateWrapOutput<T> compiled into Java
package IntermediateKeyWrapping_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class IntermediateWrapOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappedMaterial;
  public dafny.DafnySequence<? extends java.lang.Byte> _symmetricSigningKey;
  public T _wrapInfo;
  protected dafny.TypeDescriptor<T> _td_T;
  public IntermediateWrapOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    this._td_T = _td_T;
    this._wrappedMaterial = wrappedMaterial;
    this._symmetricSigningKey = symmetricSigningKey;
    this._wrapInfo = wrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IntermediateWrapOutput<T> o = (IntermediateWrapOutput<T>)other;
    return true && java.util.Objects.equals(this._wrappedMaterial, o._wrappedMaterial) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey) && java.util.Objects.equals(this._wrapInfo, o._wrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("IntermediateKeyWrapping.IntermediateWrapOutput.IntermediateWrapOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._wrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrapInfo));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<IntermediateWrapOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<IntermediateWrapOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<IntermediateWrapOutput<T>>referenceWithInitializer(IntermediateWrapOutput.class, () -> IntermediateWrapOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> IntermediateWrapOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return IntermediateKeyWrapping_Compile.IntermediateWrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  @Deprecated()
  public static <T> IntermediateWrapOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return IntermediateKeyWrapping_Compile.IntermediateWrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  public static <T> IntermediateWrapOutput<T> create(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return new IntermediateWrapOutput<T>(_td_T, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  @Deprecated()
  public static <T> IntermediateWrapOutput<T> create(dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return new IntermediateWrapOutput<T>(null, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  public static <T> IntermediateWrapOutput<T> create_IntermediateWrapOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return create(_td_T, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  @Deprecated()
  public static <T> IntermediateWrapOutput<T> create_IntermediateWrapOutput(dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return create(null, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  public boolean is_IntermediateWrapOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_wrappedMaterial() {
    return this._wrappedMaterial;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_symmetricSigningKey() {
    return this._symmetricSigningKey;
  }
  public T dtor_wrapInfo() {
    return this._wrapInfo;
  }
}
