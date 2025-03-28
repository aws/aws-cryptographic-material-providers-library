// Class ContributorInsightsSummary
// Dafny class ContributorInsightsSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ContributorInsightsSummary {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<ContributorInsightsStatus> _ContributorInsightsStatus;
  public ContributorInsightsSummary (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<ContributorInsightsStatus> ContributorInsightsStatus) {
    this._TableName = TableName;
    this._IndexName = IndexName;
    this._ContributorInsightsStatus = ContributorInsightsStatus;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContributorInsightsSummary o = (ContributorInsightsSummary)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ContributorInsightsStatus, o._ContributorInsightsStatus);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContributorInsightsStatus);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ContributorInsightsSummary.ContributorInsightsSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ContributorInsightsStatus));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ContributorInsightsSummary> _TYPE = dafny.TypeDescriptor.<ContributorInsightsSummary>referenceWithInitializer(ContributorInsightsSummary.class, () -> ContributorInsightsSummary.Default());
  public static dafny.TypeDescriptor<ContributorInsightsSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<ContributorInsightsSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ContributorInsightsSummary theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ContributorInsightsSummary.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<ContributorInsightsStatus>Default(ContributorInsightsStatus._typeDescriptor()));
  public static ContributorInsightsSummary Default() {
    return theDefault;
  }
  public static ContributorInsightsSummary create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<ContributorInsightsStatus> ContributorInsightsStatus) {
    return new ContributorInsightsSummary(TableName, IndexName, ContributorInsightsStatus);
  }
  public static ContributorInsightsSummary create_ContributorInsightsSummary(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<ContributorInsightsStatus> ContributorInsightsStatus) {
    return create(TableName, IndexName, ContributorInsightsStatus);
  }
  public boolean is_ContributorInsightsSummary() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<ContributorInsightsStatus> dtor_ContributorInsightsStatus() {
    return this._ContributorInsightsStatus;
  }
}
