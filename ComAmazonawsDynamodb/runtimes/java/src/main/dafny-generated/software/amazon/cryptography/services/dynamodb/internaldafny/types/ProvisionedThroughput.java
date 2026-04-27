// Class ProvisionedThroughput
// Dafny class ProvisionedThroughput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ProvisionedThroughput {
  public long _ReadCapacityUnits;
  public long _WriteCapacityUnits;
  public ProvisionedThroughput (long ReadCapacityUnits, long WriteCapacityUnits) {
    this._ReadCapacityUnits = ReadCapacityUnits;
    this._WriteCapacityUnits = WriteCapacityUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ProvisionedThroughput o = (ProvisionedThroughput)other;
    return true && this._ReadCapacityUnits == o._ReadCapacityUnits && this._WriteCapacityUnits == o._WriteCapacityUnits;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._ReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._WriteCapacityUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ProvisionedThroughput.ProvisionedThroughput");
    s.append("(");
    s.append(this._ReadCapacityUnits);
    s.append(", ");
    s.append(this._WriteCapacityUnits);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ProvisionedThroughput> _TYPE = dafny.TypeDescriptor.<ProvisionedThroughput>referenceWithInitializer(ProvisionedThroughput.class, () -> ProvisionedThroughput.Default());
  public static dafny.TypeDescriptor<ProvisionedThroughput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ProvisionedThroughput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ProvisionedThroughput theDefault = ProvisionedThroughput.create(0L, 0L);
  public static ProvisionedThroughput Default() {
    return theDefault;
  }
  public static ProvisionedThroughput create(long ReadCapacityUnits, long WriteCapacityUnits) {
    return new ProvisionedThroughput(ReadCapacityUnits, WriteCapacityUnits);
  }
  public static ProvisionedThroughput create_ProvisionedThroughput(long ReadCapacityUnits, long WriteCapacityUnits) {
    return create(ReadCapacityUnits, WriteCapacityUnits);
  }
  public boolean is_ProvisionedThroughput() { return true; }
  public long dtor_ReadCapacityUnits() {
    return this._ReadCapacityUnits;
  }
  public long dtor_WriteCapacityUnits() {
    return this._WriteCapacityUnits;
  }
}
