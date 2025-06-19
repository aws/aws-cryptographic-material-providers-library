// Class WrapEdkMaterialOutput<T>
// Dafny class WrapEdkMaterialOutput<T> compiled into Java
package EdkWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class WrapEdkMaterialOutput<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public WrapEdkMaterialOutput(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
  }
  public static <T> dafny.TypeDescriptor<WrapEdkMaterialOutput<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<WrapEdkMaterialOutput<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<WrapEdkMaterialOutput<T>>referenceWithInitializer(WrapEdkMaterialOutput.class, () -> WrapEdkMaterialOutput.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> WrapEdkMaterialOutput<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return WrapEdkMaterialOutput.<T>create_WrapOnlyEdkMaterialOutput(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), _default_T);
  }
  @Deprecated()
  public static <T> WrapEdkMaterialOutput<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return WrapEdkMaterialOutput.<T>create_WrapOnlyEdkMaterialOutput(_td_T, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), _default_T);
  }
  public static <T> WrapEdkMaterialOutput<T> create_WrapOnlyEdkMaterialOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T wrapInfo) {
    return new WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T>(_td_T, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  @Deprecated()
  public static <T> WrapEdkMaterialOutput<T> create_WrapOnlyEdkMaterialOutput(dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T wrapInfo) {
    return new WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T>(null, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  public static <T> WrapEdkMaterialOutput<T> create_GenerateAndWrapEdkMaterialOutput(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T wrapInfo) {
    return new WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>(_td_T, plaintextDataKey, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  @Deprecated()
  public static <T> WrapEdkMaterialOutput<T> create_GenerateAndWrapEdkMaterialOutput(dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T wrapInfo) {
    return new WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>(null, plaintextDataKey, wrappedMaterial, symmetricSigningKey, wrapInfo);
  }
  public boolean is_WrapOnlyEdkMaterialOutput() { return this instanceof WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput; }
  public boolean is_GenerateAndWrapEdkMaterialOutput() { return this instanceof WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_wrappedMaterial() {
    WrapEdkMaterialOutput<T> d = this;
    if (d instanceof WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput) { return ((WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T>)d)._wrappedMaterial; }
    return ((WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>)d)._wrappedMaterial;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_symmetricSigningKey() {
    WrapEdkMaterialOutput<T> d = this;
    if (d instanceof WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput) { return ((WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T>)d)._symmetricSigningKey; }
    return ((WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>)d)._symmetricSigningKey;
  }
  public T dtor_wrapInfo() {
    WrapEdkMaterialOutput<T> d = this;
    if (d instanceof WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput) { return ((WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T>)d)._wrapInfo; }
    return ((WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>)d)._wrapInfo;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_plaintextDataKey() {
    WrapEdkMaterialOutput<T> d = this;
    return ((WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>)d)._plaintextDataKey;
  }
}
