// Class EdkWrappingAlgorithm
// Dafny class EdkWrappingAlgorithm compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class EdkWrappingAlgorithm {
  public EdkWrappingAlgorithm() {
  }
  private static final dafny.TypeDescriptor<EdkWrappingAlgorithm> _TYPE = dafny.TypeDescriptor.<EdkWrappingAlgorithm>referenceWithInitializer(EdkWrappingAlgorithm.class, () -> EdkWrappingAlgorithm.Default());
  public static dafny.TypeDescriptor<EdkWrappingAlgorithm> _typeDescriptor() {
    return (dafny.TypeDescriptor<EdkWrappingAlgorithm>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EdkWrappingAlgorithm theDefault = EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(DIRECT__KEY__WRAPPING.Default());
  public static EdkWrappingAlgorithm Default() {
    return theDefault;
  }
  public static EdkWrappingAlgorithm create_DIRECT__KEY__WRAPPING(DIRECT__KEY__WRAPPING DIRECT__KEY__WRAPPING) {
    return new EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(DIRECT__KEY__WRAPPING);
  }
  public static EdkWrappingAlgorithm create_IntermediateKeyWrapping(IntermediateKeyWrapping IntermediateKeyWrapping) {
    return new EdkWrappingAlgorithm_IntermediateKeyWrapping(IntermediateKeyWrapping);
  }
  public boolean is_DIRECT__KEY__WRAPPING() { return this instanceof EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING; }
  public boolean is_IntermediateKeyWrapping() { return this instanceof EdkWrappingAlgorithm_IntermediateKeyWrapping; }
  public DIRECT__KEY__WRAPPING dtor_DIRECT__KEY__WRAPPING() {
    EdkWrappingAlgorithm d = this;
    return ((EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING)d)._DIRECT__KEY__WRAPPING;
  }
  public IntermediateKeyWrapping dtor_IntermediateKeyWrapping() {
    EdkWrappingAlgorithm d = this;
    return ((EdkWrappingAlgorithm_IntermediateKeyWrapping)d)._IntermediateKeyWrapping;
  }
}
