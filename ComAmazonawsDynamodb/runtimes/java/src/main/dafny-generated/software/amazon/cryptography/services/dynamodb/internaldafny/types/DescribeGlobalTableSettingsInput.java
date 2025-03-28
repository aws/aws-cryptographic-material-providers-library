// Class DescribeGlobalTableSettingsInput
// Dafny class DescribeGlobalTableSettingsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeGlobalTableSettingsInput {
  public dafny.DafnySequence<? extends Character> _GlobalTableName;
  public DescribeGlobalTableSettingsInput (dafny.DafnySequence<? extends Character> GlobalTableName) {
    this._GlobalTableName = GlobalTableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeGlobalTableSettingsInput o = (DescribeGlobalTableSettingsInput)other;
    return true && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeGlobalTableSettingsInput.DescribeGlobalTableSettingsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeGlobalTableSettingsInput> _TYPE = dafny.TypeDescriptor.<DescribeGlobalTableSettingsInput>referenceWithInitializer(DescribeGlobalTableSettingsInput.class, () -> DescribeGlobalTableSettingsInput.Default());
  public static dafny.TypeDescriptor<DescribeGlobalTableSettingsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeGlobalTableSettingsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeGlobalTableSettingsInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeGlobalTableSettingsInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeGlobalTableSettingsInput Default() {
    return theDefault;
  }
  public static DescribeGlobalTableSettingsInput create(dafny.DafnySequence<? extends Character> GlobalTableName) {
    return new DescribeGlobalTableSettingsInput(GlobalTableName);
  }
  public static DescribeGlobalTableSettingsInput create_DescribeGlobalTableSettingsInput(dafny.DafnySequence<? extends Character> GlobalTableName) {
    return create(GlobalTableName);
  }
  public boolean is_DescribeGlobalTableSettingsInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
}
