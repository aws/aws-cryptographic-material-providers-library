// Class RestoreTableFromBackupOutput
// Dafny class RestoreTableFromBackupOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RestoreTableFromBackupOutput {
  public Wrappers_Compile.Option<TableDescription> _TableDescription;
  public RestoreTableFromBackupOutput (Wrappers_Compile.Option<TableDescription> TableDescription) {
    this._TableDescription = TableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RestoreTableFromBackupOutput o = (RestoreTableFromBackupOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.RestoreTableFromBackupOutput.RestoreTableFromBackupOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RestoreTableFromBackupOutput> _TYPE = dafny.TypeDescriptor.<RestoreTableFromBackupOutput>referenceWithInitializer(RestoreTableFromBackupOutput.class, () -> RestoreTableFromBackupOutput.Default());
  public static dafny.TypeDescriptor<RestoreTableFromBackupOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<RestoreTableFromBackupOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RestoreTableFromBackupOutput theDefault = RestoreTableFromBackupOutput.create(Wrappers_Compile.Option.<TableDescription>Default(TableDescription._typeDescriptor()));
  public static RestoreTableFromBackupOutput Default() {
    return theDefault;
  }
  public static RestoreTableFromBackupOutput create(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return new RestoreTableFromBackupOutput(TableDescription);
  }
  public static RestoreTableFromBackupOutput create_RestoreTableFromBackupOutput(Wrappers_Compile.Option<TableDescription> TableDescription) {
    return create(TableDescription);
  }
  public boolean is_RestoreTableFromBackupOutput() { return true; }
  public Wrappers_Compile.Option<TableDescription> dtor_TableDescription() {
    return this._TableDescription;
  }
}
