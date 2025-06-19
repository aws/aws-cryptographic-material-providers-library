// Class DescribeContributorInsightsInput
// Dafny class DescribeContributorInsightsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeContributorInsightsInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public DescribeContributorInsightsInput (dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName) {
    this._TableName = TableName;
    this._IndexName = IndexName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeContributorInsightsInput o = (DescribeContributorInsightsInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._IndexName, o._IndexName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeContributorInsightsInput.DescribeContributorInsightsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeContributorInsightsInput> _TYPE = dafny.TypeDescriptor.<DescribeContributorInsightsInput>referenceWithInitializer(DescribeContributorInsightsInput.class, () -> DescribeContributorInsightsInput.Default());
  public static dafny.TypeDescriptor<DescribeContributorInsightsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeContributorInsightsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeContributorInsightsInput theDefault = DescribeContributorInsightsInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()));
  public static DescribeContributorInsightsInput Default() {
    return theDefault;
  }
  public static DescribeContributorInsightsInput create(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName) {
    return new DescribeContributorInsightsInput(TableName, IndexName);
  }
  public static DescribeContributorInsightsInput create_DescribeContributorInsightsInput(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName) {
    return create(TableName, IndexName);
  }
  public boolean is_DescribeContributorInsightsInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
}
