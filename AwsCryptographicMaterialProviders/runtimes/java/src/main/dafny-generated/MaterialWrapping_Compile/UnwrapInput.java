// Class UnwrapInput
// Dafny class UnwrapInput compiled into Java
package MaterialWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class UnwrapInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappedMaterial;
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _algorithmSuite;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _serializedEC;
  public UnwrapInput (dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> serializedEC) {
    this._wrappedMaterial = wrappedMaterial;
    this._algorithmSuite = algorithmSuite;
    this._encryptionContext = encryptionContext;
    this._serializedEC = serializedEC;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UnwrapInput o = (UnwrapInput)other;
    return true && java.util.Objects.equals(this._wrappedMaterial, o._wrappedMaterial) && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._serializedEC, o._serializedEC);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._serializedEC);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("MaterialWrapping.UnwrapInput.UnwrapInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._wrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithmSuite));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._serializedEC));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UnwrapInput> _TYPE = dafny.TypeDescriptor.<UnwrapInput>referenceWithInitializer(UnwrapInput.class, () -> UnwrapInput.Default());
  public static dafny.TypeDescriptor<UnwrapInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UnwrapInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UnwrapInput theDefault = UnwrapInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.Default(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor())));
  public static UnwrapInput Default() {
    return theDefault;
  }
  public static UnwrapInput create(dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> serializedEC) {
    return new UnwrapInput(wrappedMaterial, algorithmSuite, encryptionContext, serializedEC);
  }
  public static UnwrapInput create_UnwrapInput(dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> serializedEC) {
    return create(wrappedMaterial, algorithmSuite, encryptionContext, serializedEC);
  }
  public boolean is_UnwrapInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_wrappedMaterial() {
    return this._wrappedMaterial;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo dtor_algorithmSuite() {
    return this._algorithmSuite;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> dtor_serializedEC() {
    return this._serializedEC;
  }
}
