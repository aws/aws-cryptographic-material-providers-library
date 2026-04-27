// Class GenerateAndWrapOutput<T>
// Dafny class GenerateAndWrapOutput<T> compiled into Java
package MaterialWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateAndWrapOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _plaintextMaterial;
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappedMaterial;
  public T _wrapInfo;
  protected dafny.TypeDescriptor<T> _td_T;
  public GenerateAndWrapOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    this._td_T = _td_T;
    this._plaintextMaterial = plaintextMaterial;
    this._wrappedMaterial = wrappedMaterial;
    this._wrapInfo = wrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateAndWrapOutput<T> o = (GenerateAndWrapOutput<T>)other;
    return true && java.util.Objects.equals(this._plaintextMaterial, o._plaintextMaterial) && java.util.Objects.equals(this._wrappedMaterial, o._wrappedMaterial) && java.util.Objects.equals(this._wrapInfo, o._wrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("MaterialWrapping.GenerateAndWrapOutput.GenerateAndWrapOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._plaintextMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrapInfo));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<GenerateAndWrapOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<GenerateAndWrapOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<GenerateAndWrapOutput<T>>referenceWithInitializer(GenerateAndWrapOutput.class, () -> GenerateAndWrapOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> GenerateAndWrapOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return GenerateAndWrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  @Deprecated()
  public static <T> GenerateAndWrapOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return GenerateAndWrapOutput.<T>create(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _default_T);
  }
  public static <T> GenerateAndWrapOutput<T> create(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return new GenerateAndWrapOutput<T>(_td_T, plaintextMaterial, wrappedMaterial, wrapInfo);
  }
  @Deprecated()
  public static <T> GenerateAndWrapOutput<T> create(dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return new GenerateAndWrapOutput<T>(null, plaintextMaterial, wrappedMaterial, wrapInfo);
  }
  public static <T> GenerateAndWrapOutput<T> create_GenerateAndWrapOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return create(_td_T, plaintextMaterial, wrappedMaterial, wrapInfo);
  }
  @Deprecated()
  public static <T> GenerateAndWrapOutput<T> create_GenerateAndWrapOutput(dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, T wrapInfo) {
    return create(null, plaintextMaterial, wrappedMaterial, wrapInfo);
  }
  public boolean is_GenerateAndWrapOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_plaintextMaterial() {
    return this._plaintextMaterial;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_wrappedMaterial() {
    return this._wrappedMaterial;
  }
  public T dtor_wrapInfo() {
    return this._wrapInfo;
  }
}
