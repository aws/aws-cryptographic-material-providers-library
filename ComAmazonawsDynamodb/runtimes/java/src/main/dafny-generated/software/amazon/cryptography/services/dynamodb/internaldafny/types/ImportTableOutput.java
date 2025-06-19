// Class ImportTableOutput
// Dafny class ImportTableOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ImportTableOutput {
  public ImportTableDescription _ImportTableDescription;
  public ImportTableOutput (ImportTableDescription ImportTableDescription) {
    this._ImportTableDescription = ImportTableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportTableOutput o = (ImportTableOutput)other;
    return true && java.util.Objects.equals(this._ImportTableDescription, o._ImportTableDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportTableDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ImportTableOutput.ImportTableOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ImportTableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ImportTableOutput> _TYPE = dafny.TypeDescriptor.<ImportTableOutput>referenceWithInitializer(ImportTableOutput.class, () -> ImportTableOutput.Default());
  public static dafny.TypeDescriptor<ImportTableOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ImportTableOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ImportTableOutput theDefault = ImportTableOutput.create(ImportTableDescription.Default());
  public static ImportTableOutput Default() {
    return theDefault;
  }
  public static ImportTableOutput create(ImportTableDescription ImportTableDescription) {
    return new ImportTableOutput(ImportTableDescription);
  }
  public static ImportTableOutput create_ImportTableOutput(ImportTableDescription ImportTableDescription) {
    return create(ImportTableDescription);
  }
  public boolean is_ImportTableOutput() { return true; }
  public ImportTableDescription dtor_ImportTableDescription() {
    return this._ImportTableDescription;
  }
}
