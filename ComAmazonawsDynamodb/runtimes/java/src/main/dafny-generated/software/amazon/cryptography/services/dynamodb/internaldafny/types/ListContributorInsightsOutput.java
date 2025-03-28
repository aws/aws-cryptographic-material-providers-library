// Class ListContributorInsightsOutput
// Dafny class ListContributorInsightsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListContributorInsightsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ContributorInsightsSummary>> _ContributorInsightsSummaries;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public ListContributorInsightsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends ContributorInsightsSummary>> ContributorInsightsSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    this._ContributorInsightsSummaries = ContributorInsightsSummaries;
    this._NextToken = NextToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListContributorInsightsOutput o = (ListContributorInsightsOutput)other;
    return true && java.util.Objects.equals(this._ContributorInsightsSummaries, o._ContributorInsightsSummaries) && java.util.Objects.equals(this._NextToken, o._NextToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContributorInsightsSummaries);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListContributorInsightsOutput.ListContributorInsightsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ContributorInsightsSummaries));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListContributorInsightsOutput> _TYPE = dafny.TypeDescriptor.<ListContributorInsightsOutput>referenceWithInitializer(ListContributorInsightsOutput.class, () -> ListContributorInsightsOutput.Default());
  public static dafny.TypeDescriptor<ListContributorInsightsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListContributorInsightsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListContributorInsightsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ListContributorInsightsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends ContributorInsightsSummary>>Default(dafny.DafnySequence.<ContributorInsightsSummary>_typeDescriptor(ContributorInsightsSummary._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ListContributorInsightsOutput Default() {
    return theDefault;
  }
  public static ListContributorInsightsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends ContributorInsightsSummary>> ContributorInsightsSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return new ListContributorInsightsOutput(ContributorInsightsSummaries, NextToken);
  }
  public static ListContributorInsightsOutput create_ListContributorInsightsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends ContributorInsightsSummary>> ContributorInsightsSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return create(ContributorInsightsSummaries, NextToken);
  }
  public boolean is_ListContributorInsightsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ContributorInsightsSummary>> dtor_ContributorInsightsSummaries() {
    return this._ContributorInsightsSummaries;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
}
