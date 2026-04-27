// Class UpdateTableOutput
// Dafny class UpdateTableOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateTableOutput {
  public Wrappers_Compile.Option<TableDescription> _TableDescription;
  public UpdateTableOutput (Wrappers_Compile.Option<TableDescription> TableDescription) {
    this._TableDescription = TableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateTableOutput o = (UpdateTableOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.UpdateTableOutput.UpdateTableOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateTableOutput> _TYPE = dafny.TypeDescriptor.<UpdateTableOutput>referenceWithInitializer(UpdateTableOutput.class, () -> UpdateTableOutput.Default());
  public static dafny.TypeDescriptor<UpdateTableOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateTableOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateTableOutput theDefault = UpdateTableOutput.create(Wrappers_Compile.Option.<TableDescription>Default(TableDescription._typeDescriptor()));
  public static UpdateTableOutput Default() {
    return theDefault;
  }
  public static UpdateTableOutput create(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return new UpdateTableOutput(TableDescription);
  }
  public static UpdateTableOutput create_UpdateTableOutput(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return create(TableDescription);
  }
  public boolean is_UpdateTableOutput() { return true; }
  public Wrappers_Compile.Option<TableDescription> dtor_TableDescription() {
    return this._TableDescription;
  }
}
