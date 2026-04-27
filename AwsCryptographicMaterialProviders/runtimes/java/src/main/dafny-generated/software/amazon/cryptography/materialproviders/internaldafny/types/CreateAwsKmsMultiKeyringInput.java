// Class CreateAwsKmsMultiKeyringInput
// Dafny class CreateAwsKmsMultiKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsMultiKeyringInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _generator;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _kmsKeyIds;
  public Wrappers_Compile.Option<IClientSupplier> _clientSupplier;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public CreateAwsKmsMultiKeyringInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> generator, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> kmsKeyIds, Wrappers_Compile.Option<IClientSupplier> clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    this._generator = generator;
    this._kmsKeyIds = kmsKeyIds;
    this._clientSupplier = clientSupplier;
    this._grantTokens = grantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsMultiKeyringInput o = (CreateAwsKmsMultiKeyringInput)other;
    return true && java.util.Objects.equals(this._generator, o._generator) && java.util.Objects.equals(this._kmsKeyIds, o._kmsKeyIds) && java.util.Objects.equals(this._clientSupplier, o._clientSupplier) && java.util.Objects.equals(this._grantTokens, o._grantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._generator);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsKeyIds);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._clientSupplier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMultiKeyringInput.CreateAwsKmsMultiKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._generator));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsKeyIds));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._clientSupplier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsMultiKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsMultiKeyringInput>referenceWithInitializer(CreateAwsKmsMultiKeyringInput.class, () -> CreateAwsKmsMultiKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsMultiKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsMultiKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsMultiKeyringInput theDefault = CreateAwsKmsMultiKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<IClientSupplier>Default(((dafny.TypeDescriptor<IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(IClientSupplier.class))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
  public static CreateAwsKmsMultiKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsMultiKeyringInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> generator, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> kmsKeyIds, Wrappers_Compile.Option<IClientSupplier> clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return new CreateAwsKmsMultiKeyringInput(generator, kmsKeyIds, clientSupplier, grantTokens);
  }
  public static CreateAwsKmsMultiKeyringInput create_CreateAwsKmsMultiKeyringInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> generator, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> kmsKeyIds, Wrappers_Compile.Option<IClientSupplier> clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return create(generator, kmsKeyIds, clientSupplier, grantTokens);
  }
  public boolean is_CreateAwsKmsMultiKeyringInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_generator() {
    return this._generator;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_kmsKeyIds() {
    return this._kmsKeyIds;
  }
  public Wrappers_Compile.Option<IClientSupplier> dtor_clientSupplier() {
    return this._clientSupplier;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
}
