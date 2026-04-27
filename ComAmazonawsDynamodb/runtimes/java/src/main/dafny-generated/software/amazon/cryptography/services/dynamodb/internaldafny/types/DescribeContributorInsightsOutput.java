// Class DescribeContributorInsightsOutput
// Dafny class DescribeContributorInsightsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeContributorInsightsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _ContributorInsightsRuleList;
  public Wrappers_Compile.Option<ContributorInsightsStatus> _ContributorInsightsStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastUpdateDateTime;
  public Wrappers_Compile.Option<FailureException> _FailureException;
  public DescribeContributorInsightsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> ContributorInsightsRuleList, Wrappers_Compile.Option<ContributorInsightsStatus> ContributorInsightsStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateDateTime, Wrappers_Compile.Option<FailureException> FailureException) {
    this._TableName = TableName;
    this._IndexName = IndexName;
    this._ContributorInsightsRuleList = ContributorInsightsRuleList;
    this._ContributorInsightsStatus = ContributorInsightsStatus;
    this._LastUpdateDateTime = LastUpdateDateTime;
    this._FailureException = FailureException;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeContributorInsightsOutput o = (DescribeContributorInsightsOutput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ContributorInsightsRuleList, o._ContributorInsightsRuleList) && java.util.Objects.equals(this._ContributorInsightsStatus, o._ContributorInsightsStatus) && java.util.Objects.equals(this._LastUpdateDateTime, o._LastUpdateDateTime) && java.util.Objects.equals(this._FailureException, o._FailureException);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContributorInsightsRuleList);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContributorInsightsStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastUpdateDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._FailureException);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeContributorInsightsOutput.DescribeContributorInsightsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ContributorInsightsRuleList));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ContributorInsightsStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastUpdateDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._FailureException));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeContributorInsightsOutput> _TYPE = dafny.TypeDescriptor.<DescribeContributorInsightsOutput>referenceWithInitializer(DescribeContributorInsightsOutput.class, () -> DescribeContributorInsightsOutput.Default());
  public static dafny.TypeDescriptor<DescribeContributorInsightsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeContributorInsightsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeContributorInsightsOutput theDefault = DescribeContributorInsightsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<ContributorInsightsStatus>Default(ContributorInsightsStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<FailureException>Default(FailureException._typeDescriptor()));
  public static DescribeContributorInsightsOutput Default() {
    return theDefault;
  }
  public static DescribeContributorInsightsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> ContributorInsightsRuleList, Wrappers_Compile.Option<ContributorInsightsStatus> ContributorInsightsStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateDateTime, Wrappers_Compile.Option<FailureException> FailureException) {
    return new DescribeContributorInsightsOutput(TableName, IndexName, ContributorInsightsRuleList, ContributorInsightsStatus, LastUpdateDateTime, FailureException);
  }
  public static DescribeContributorInsightsOutput create_DescribeContributorInsightsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> ContributorInsightsRuleList, Wrappers_Compile.Option<ContributorInsightsStatus> ContributorInsightsStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateDateTime, Wrappers_Compile.Option<FailureException> FailureException) {
    return create(TableName, IndexName, ContributorInsightsRuleList, ContributorInsightsStatus, LastUpdateDateTime, FailureException);
  }
  public boolean is_DescribeContributorInsightsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_ContributorInsightsRuleList() {
    return this._ContributorInsightsRuleList;
  }
  public Wrappers_Compile.Option<ContributorInsightsStatus> dtor_ContributorInsightsStatus() {
    return this._ContributorInsightsStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastUpdateDateTime() {
    return this._LastUpdateDateTime;
  }
  public Wrappers_Compile.Option<FailureException> dtor_FailureException() {
    return this._FailureException;
  }
}
