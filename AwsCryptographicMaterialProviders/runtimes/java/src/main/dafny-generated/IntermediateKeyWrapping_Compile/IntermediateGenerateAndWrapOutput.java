// Class IntermediateGenerateAndWrapOutput<T>
// Dafny class IntermediateGenerateAndWrapOutput<T> compiled into Java
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
public class IntermediateGenerateAndWrapOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _plaintextDataKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappedMaterial;
  public dafny.DafnySequence<? extends java.lang.Byte> _symmetricSigningKey;
  public T _wrapInfo;
  protected dafny.TypeDescriptor<T> _td_T;
  public IntermediateGenerateAndWrapOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    this._td_T = _td_T;
    this._plaintextDataKey = plaintextDataKey;
    this._wrappedMaterial = wrappedMaterial;
    this._symmetricSigningKey = symmetricSigningKey;
    this._wrapInfo = wrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IntermediateGenerateAndWrapOutput<T> o = (IntermediateGenerateAndWrapOutput<T>)other;
    return true && java.util.Objects.equals(this._plaintextDataKey, o._plaintextDataKey) && java.util.Objects.equals(this._wrappedMaterial, o._wrappedMaterial) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey) && java.util.Objects.equals(this._wrapInfo, o._wrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextDataKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput.IntermediateGenerateAndWrapOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrapInfo));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<IntermediateGenerateAndWrapOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<IntermediateGenerateAndWrapOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<IntermediateGenerateAndWrapOutput<T>>referenceWithInitializer(IntermediateGenerateAndWrapOutput.class, () -> IntermediateGenerateAndWrapOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> IntermediateGenerateAndWrapOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  @Deprecated()
  public static <T> IntermediateGenerateAndWrapOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  public static <T> IntermediateGenerateAndWrapOutput<T> create(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return new IntermediateGenerateAndWrapOutput<T>(_td_T, plaintextDataKey, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  @Deprecated()
  public static <T> IntermediateGenerateAndWrapOutput<T> create(dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return new IntermediateGenerateAndWrapOutput<T>(null, plaintextDataKey, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  public static <T> IntermediateGenerateAndWrapOutput<T> create_IntermediateGenerateAndWrapOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return create(_td_T, plaintextDataKey, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  @Deprecated()
  public static <T> IntermediateGenerateAndWrapOutput<T> create_IntermediateGenerateAndWrapOutput(dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T wrapInfo) {
    return create(null, plaintextDataKey, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  public boolean is_IntermediateGenerateAndWrapOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_plaintextDataKey() {
    return this._plaintextDataKey;
  }
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
