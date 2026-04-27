// Class CreateMultiKeyringInput
// Dafny class CreateMultiKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateMultiKeyringInput {
  public Wrappers_Compile.Option<IKeyring> _generator;
  public dafny.DafnySequence<? extends IKeyring> _childKeyrings;
  public CreateMultiKeyringInput (Wrappers_Compile.Option<IKeyring> generator, dafny.DafnySequence<? extends IKeyring> childKeyrings) {
    this._generator = generator;
    this._childKeyrings = childKeyrings;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateMultiKeyringInput o = (CreateMultiKeyringInput)other;
    return true && java.util.Objects.equals(this._generator, o._generator) && java.util.Objects.equals(this._childKeyrings, o._childKeyrings);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._generator);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._childKeyrings);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput.CreateMultiKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._generator));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._childKeyrings));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateMultiKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateMultiKeyringInput>referenceWithInitializer(CreateMultiKeyringInput.class, () -> CreateMultiKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateMultiKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateMultiKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateMultiKeyringInput theDefault = CreateMultiKeyringInput.create(Wrappers_Compile.Option.<IKeyring>Default(((dafny.TypeDescriptor<IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(IKeyring.class))), dafny.DafnySequence.<IKeyring> empty(((dafny.TypeDescriptor<IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(IKeyring.class))));
  public static CreateMultiKeyringInput Default() {
    return theDefault;
  }
  public static CreateMultiKeyringInput create(Wrappers_Compile.Option<IKeyring> generator, dafny.DafnySequence<? extends IKeyring> childKeyrings) {
    return new CreateMultiKeyringInput(generator, childKeyrings);
  }
  public static CreateMultiKeyringInput create_CreateMultiKeyringInput(Wrappers_Compile.Option<IKeyring> generator, dafny.DafnySequence<? extends IKeyring> childKeyrings) {
    return create(generator, childKeyrings);
  }
  public boolean is_CreateMultiKeyringInput() { return true; }
  public Wrappers_Compile.Option<IKeyring> dtor_generator() {
    return this._generator;
  }
  public dafny.DafnySequence<? extends IKeyring> dtor_childKeyrings() {
    return this._childKeyrings;
  }
}
