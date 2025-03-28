// Class CreateKeyInput
// Dafny class CreateKeyInput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateKeyInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _branchKeyIdentifier;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _encryptionContext;
  public CreateKeyInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyIdentifier, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContext) {
    this._branchKeyIdentifier = branchKeyIdentifier;
    this._encryptionContext = encryptionContext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateKeyInput o = (CreateKeyInput)other;
    return true && java.util.Objects.equals(this._branchKeyIdentifier, o._branchKeyIdentifier) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.CreateKeyInput.CreateKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateKeyInput> _TYPE = dafny.TypeDescriptor.<CreateKeyInput>referenceWithInitializer(CreateKeyInput.class, () -> CreateKeyInput.Default());
  public static dafny.TypeDescriptor<CreateKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateKeyInput theDefault = software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor())));
  public static CreateKeyInput Default() {
    return theDefault;
  }
  public static CreateKeyInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyIdentifier, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContext) {
    return new CreateKeyInput(branchKeyIdentifier, encryptionContext);
  }
  public static CreateKeyInput create_CreateKeyInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyIdentifier, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContext) {
    return create(branchKeyIdentifier, encryptionContext);
  }
  public boolean is_CreateKeyInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_branchKeyIdentifier() {
    return this._branchKeyIdentifier;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
}
