// Class RestoreTableToPointInTimeOutput
// Dafny class RestoreTableToPointInTimeOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RestoreTableToPointInTimeOutput {
  public Wrappers_Compile.Option<TableDescription> _TableDescription;
  public RestoreTableToPointInTimeOutput (Wrappers_Compile.Option<TableDescription> TableDescription) {
    this._TableDescription = TableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RestoreTableToPointInTimeOutput o = (RestoreTableToPointInTimeOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.RestoreTableToPointInTimeOutput.RestoreTableToPointInTimeOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RestoreTableToPointInTimeOutput> _TYPE = dafny.TypeDescriptor.<RestoreTableToPointInTimeOutput>referenceWithInitializer(RestoreTableToPointInTimeOutput.class, () -> RestoreTableToPointInTimeOutput.Default());
  public static dafny.TypeDescriptor<RestoreTableToPointInTimeOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<RestoreTableToPointInTimeOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RestoreTableToPointInTimeOutput theDefault = RestoreTableToPointInTimeOutput.create(Wrappers_Compile.Option.<TableDescription>Default(TableDescription._typeDescriptor()));
  public static RestoreTableToPointInTimeOutput Default() {
    return theDefault;
  }
  public static RestoreTableToPointInTimeOutput create(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return new RestoreTableToPointInTimeOutput(TableDescription);
  }
  public static RestoreTableToPointInTimeOutput create_RestoreTableToPointInTimeOutput(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return create(TableDescription);
  }
  public boolean is_RestoreTableToPointInTimeOutput() { return true; }
  public Wrappers_Compile.Option<TableDescription> dtor_TableDescription() {
    return this._TableDescription;
  }
}
