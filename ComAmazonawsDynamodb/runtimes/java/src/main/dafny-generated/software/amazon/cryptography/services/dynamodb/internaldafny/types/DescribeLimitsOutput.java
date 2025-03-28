// Class DescribeLimitsOutput
// Dafny class DescribeLimitsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeLimitsOutput {
  public Wrappers_Compile.Option<java.lang.Long> _AccountMaxReadCapacityUnits;
  public Wrappers_Compile.Option<java.lang.Long> _AccountMaxWriteCapacityUnits;
  public Wrappers_Compile.Option<java.lang.Long> _TableMaxReadCapacityUnits;
  public Wrappers_Compile.Option<java.lang.Long> _TableMaxWriteCapacityUnits;
  public DescribeLimitsOutput (Wrappers_Compile.Option<java.lang.Long> AccountMaxReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> AccountMaxWriteCapacityUnits, Wrappers_Compile.Option<java.lang.Long> TableMaxReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> TableMaxWriteCapacityUnits) {
    this._AccountMaxReadCapacityUnits = AccountMaxReadCapacityUnits;
    this._AccountMaxWriteCapacityUnits = AccountMaxWriteCapacityUnits;
    this._TableMaxReadCapacityUnits = TableMaxReadCapacityUnits;
    this._TableMaxWriteCapacityUnits = TableMaxWriteCapacityUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeLimitsOutput o = (DescribeLimitsOutput)other;
    return true && java.util.Objects.equals(this._AccountMaxReadCapacityUnits, o._AccountMaxReadCapacityUnits) && java.util.Objects.equals(this._AccountMaxWriteCapacityUnits, o._AccountMaxWriteCapacityUnits) && java.util.Objects.equals(this._TableMaxReadCapacityUnits, o._TableMaxReadCapacityUnits) && java.util.Objects.equals(this._TableMaxWriteCapacityUnits, o._TableMaxWriteCapacityUnits);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AccountMaxReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AccountMaxWriteCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableMaxReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableMaxWriteCapacityUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeLimitsOutput.DescribeLimitsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AccountMaxReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AccountMaxWriteCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableMaxReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableMaxWriteCapacityUnits));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeLimitsOutput> _TYPE = dafny.TypeDescriptor.<DescribeLimitsOutput>referenceWithInitializer(DescribeLimitsOutput.class, () -> DescribeLimitsOutput.Default());
  public static dafny.TypeDescriptor<DescribeLimitsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeLimitsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeLimitsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeLimitsOutput.create(Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()));
  public static DescribeLimitsOutput Default() {
    return theDefault;
  }
  public static DescribeLimitsOutput create(Wrappers_Compile.Option<java.lang.Long> AccountMaxReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> AccountMaxWriteCapacityUnits, Wrappers_Compile.Option<java.lang.Long> TableMaxReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> TableMaxWriteCapacityUnits) {
    return new DescribeLimitsOutput(AccountMaxReadCapacityUnits, AccountMaxWriteCapacityUnits, TableMaxReadCapacityUnits, TableMaxWriteCapacityUnits);
  }
  public static DescribeLimitsOutput create_DescribeLimitsOutput(Wrappers_Compile.Option<java.lang.Long> AccountMaxReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> AccountMaxWriteCapacityUnits, Wrappers_Compile.Option<java.lang.Long> TableMaxReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> TableMaxWriteCapacityUnits) {
    return create(AccountMaxReadCapacityUnits, AccountMaxWriteCapacityUnits, TableMaxReadCapacityUnits, TableMaxWriteCapacityUnits);
  }
  public boolean is_DescribeLimitsOutput() { return true; }
  public Wrappers_Compile.Option<java.lang.Long> dtor_AccountMaxReadCapacityUnits() {
    return this._AccountMaxReadCapacityUnits;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_AccountMaxWriteCapacityUnits() {
    return this._AccountMaxWriteCapacityUnits;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_TableMaxReadCapacityUnits() {
    return this._TableMaxReadCapacityUnits;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_TableMaxWriteCapacityUnits() {
    return this._TableMaxWriteCapacityUnits;
  }
}
