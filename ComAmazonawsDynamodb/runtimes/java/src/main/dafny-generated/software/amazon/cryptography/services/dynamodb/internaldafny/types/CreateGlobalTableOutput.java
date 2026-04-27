// Class CreateGlobalTableOutput
// Dafny class CreateGlobalTableOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateGlobalTableOutput {
  public Wrappers_Compile.Option<GlobalTableDescription> _GlobalTableDescription;
  public CreateGlobalTableOutput (Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    this._GlobalTableDescription = GlobalTableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateGlobalTableOutput o = (CreateGlobalTableOutput)other;
    return true && java.util.Objects.equals(this._GlobalTableDescription, o._GlobalTableDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CreateGlobalTableOutput.CreateGlobalTableOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateGlobalTableOutput> _TYPE = dafny.TypeDescriptor.<CreateGlobalTableOutput>referenceWithInitializer(CreateGlobalTableOutput.class, () -> CreateGlobalTableOutput.Default());
  public static dafny.TypeDescriptor<CreateGlobalTableOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateGlobalTableOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateGlobalTableOutput theDefault = CreateGlobalTableOutput.create(Wrappers_Compile.Option.<GlobalTableDescription>Default(GlobalTableDescription._typeDescriptor()));
  public static CreateGlobalTableOutput Default() {
    return theDefault;
  }
  public static CreateGlobalTableOutput create(Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    return new CreateGlobalTableOutput(GlobalTableDescription);
  }
  public static CreateGlobalTableOutput create_CreateGlobalTableOutput(Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    return create(GlobalTableDescription);
  }
  public boolean is_CreateGlobalTableOutput() { return true; }
  public Wrappers_Compile.Option<GlobalTableDescription> dtor_GlobalTableDescription() {
    return this._GlobalTableDescription;
  }
}
