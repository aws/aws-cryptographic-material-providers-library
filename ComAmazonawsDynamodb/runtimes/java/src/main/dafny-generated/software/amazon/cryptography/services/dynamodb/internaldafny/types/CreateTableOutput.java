// Class CreateTableOutput
// Dafny class CreateTableOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateTableOutput {
  public Wrappers_Compile.Option<TableDescription> _TableDescription;
  public CreateTableOutput (Wrappers_Compile.Option<TableDescription> TableDescription) {
    this._TableDescription = TableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateTableOutput o = (CreateTableOutput)other;
    return true && java.util.Objects.equals(this._TableDescription, o._TableDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CreateTableOutput.CreateTableOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateTableOutput> _TYPE = dafny.TypeDescriptor.<CreateTableOutput>referenceWithInitializer(CreateTableOutput.class, () -> CreateTableOutput.Default());
  public static dafny.TypeDescriptor<CreateTableOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateTableOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateTableOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateTableOutput.create(Wrappers_Compile.Option.<TableDescription>Default(TableDescription._typeDescriptor()));
  public static CreateTableOutput Default() {
    return theDefault;
  }
  public static CreateTableOutput create(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return new CreateTableOutput(TableDescription);
  }
  public static CreateTableOutput create_CreateTableOutput(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return create(TableDescription);
  }
  public boolean is_CreateTableOutput() { return true; }
  public Wrappers_Compile.Option<TableDescription> dtor_TableDescription() {
    return this._TableDescription;
  }
}
