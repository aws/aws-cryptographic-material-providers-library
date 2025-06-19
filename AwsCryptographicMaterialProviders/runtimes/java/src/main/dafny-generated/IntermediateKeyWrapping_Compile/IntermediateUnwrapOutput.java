// Class IntermediateUnwrapOutput<T>
// Dafny class IntermediateUnwrapOutput<T> compiled into Java
package IntermediateKeyWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class IntermediateUnwrapOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _plaintextDataKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _symmetricSigningKey;
  public T _unwrapInfo;
  protected dafny.TypeDescriptor<T> _td_T;
  public IntermediateUnwrapOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T unwrapInfo) {
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
    IntermediateUnwrapOutput<T> o = (IntermediateUnwrapOutput<T>)other;
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
    s.append("IntermediateKeyWrapping.IntermediateUnwrapOutput.IntermediateUnwrapOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._unwrapInfo));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<IntermediateUnwrapOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<IntermediateUnwrapOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<IntermediateUnwrapOutput<T>>referenceWithInitializer(IntermediateUnwrapOutput.class, () -> IntermediateUnwrapOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> IntermediateUnwrapOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return IntermediateUnwrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  @Deprecated()
  public static <T> IntermediateUnwrapOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return IntermediateUnwrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  public static <T> IntermediateUnwrapOutput<T> create(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T unwrapInfo) {
    return new IntermediateUnwrapOutput<T>(_td_T, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  @Deprecated()
  public static <T> IntermediateUnwrapOutput<T> create(dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T unwrapInfo) {
    return new IntermediateUnwrapOutput<T>(null, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  public static <T> IntermediateUnwrapOutput<T> create_IntermediateUnwrapOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T unwrapInfo) {
    return create(_td_T, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  @Deprecated()
  public static <T> IntermediateUnwrapOutput<T> create_IntermediateUnwrapOutput(dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey, T unwrapInfo) {
    return create(null, plaintextDataKey, symmetricSigningKey, unwrapInfo);
  }
  public boolean is_IntermediateUnwrapOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_plaintextDataKey() {
    return this._plaintextDataKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_symmetricSigningKey() {
    return this._symmetricSigningKey;
  }
  public T dtor_unwrapInfo() {
    return this._unwrapInfo;
  }
}
