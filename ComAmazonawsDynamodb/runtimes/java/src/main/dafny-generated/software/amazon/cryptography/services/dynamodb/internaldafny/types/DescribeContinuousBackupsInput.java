// Class DescribeContinuousBackupsInput
// Dafny class DescribeContinuousBackupsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeContinuousBackupsInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public DescribeContinuousBackupsInput (dafny.DafnySequence<? extends Character> TableName) {
    this._TableName = TableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeContinuousBackupsInput o = (DescribeContinuousBackupsInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeContinuousBackupsInput.DescribeContinuousBackupsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeContinuousBackupsInput> _TYPE = dafny.TypeDescriptor.<DescribeContinuousBackupsInput>referenceWithInitializer(DescribeContinuousBackupsInput.class, () -> DescribeContinuousBackupsInput.Default());
  public static dafny.TypeDescriptor<DescribeContinuousBackupsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeContinuousBackupsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeContinuousBackupsInput theDefault = DescribeContinuousBackupsInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeContinuousBackupsInput Default() {
    return theDefault;
  }
  public static DescribeContinuousBackupsInput create(dafny.DafnySequence<? extends Character> TableName) {
    return new DescribeContinuousBackupsInput(TableName);
  }
  public static DescribeContinuousBackupsInput create_DescribeContinuousBackupsInput(dafny.DafnySequence<? extends Character> TableName) {
    return create(TableName);
  }
  public boolean is_DescribeContinuousBackupsInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
}
