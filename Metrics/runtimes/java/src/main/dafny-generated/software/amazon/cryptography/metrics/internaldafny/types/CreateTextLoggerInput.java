// Class CreateTextLoggerInput
// Dafny class CreateTextLoggerInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateTextLoggerInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _fileName;
  public CreateTextLoggerInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> fileName) {
    this._fileName = fileName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateTextLoggerInput o = (CreateTextLoggerInput)other;
    return true && java.util.Objects.equals(this._fileName, o._fileName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._fileName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.CreateTextLoggerInput.CreateTextLoggerInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._fileName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateTextLoggerInput> _TYPE = dafny.TypeDescriptor.<CreateTextLoggerInput>referenceWithInitializer(CreateTextLoggerInput.class, () -> CreateTextLoggerInput.Default());
  public static dafny.TypeDescriptor<CreateTextLoggerInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateTextLoggerInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateTextLoggerInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.CreateTextLoggerInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static CreateTextLoggerInput Default() {
    return theDefault;
  }
  public static CreateTextLoggerInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> fileName) {
    return new CreateTextLoggerInput(fileName);
  }
  public static CreateTextLoggerInput create_CreateTextLoggerInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> fileName) {
    return create(fileName);
  }
  public boolean is_CreateTextLoggerInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_fileName() {
    return this._fileName;
  }
}
