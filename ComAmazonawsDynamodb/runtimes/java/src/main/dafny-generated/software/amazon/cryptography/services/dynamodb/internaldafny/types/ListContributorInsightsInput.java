// Class ListContributorInsightsInput
// Dafny class ListContributorInsightsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListContributorInsightsInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public Wrappers_Compile.Option<java.lang.Integer> _MaxResults;
  public ListContributorInsightsInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<java.lang.Integer> MaxResults) {
    this._TableName = TableName;
    this._NextToken = NextToken;
    this._MaxResults = MaxResults;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListContributorInsightsInput o = (ListContributorInsightsInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._NextToken, o._NextToken) && java.util.Objects.equals(this._MaxResults, o._MaxResults);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MaxResults);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListContributorInsightsInput.ListContributorInsightsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MaxResults));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListContributorInsightsInput> _TYPE = dafny.TypeDescriptor.<ListContributorInsightsInput>referenceWithInitializer(ListContributorInsightsInput.class, () -> ListContributorInsightsInput.Default());
  public static dafny.TypeDescriptor<ListContributorInsightsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListContributorInsightsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListContributorInsightsInput theDefault = ListContributorInsightsInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<java.lang.Integer>Default(ListContributorInsightsLimit._typeDescriptor()));
  public static ListContributorInsightsInput Default() {
    return theDefault;
  }
  public static ListContributorInsightsInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<java.lang.Integer> MaxResults) {
    return new ListContributorInsightsInput(TableName, NextToken, MaxResults);
  }
  public static ListContributorInsightsInput create_ListContributorInsightsInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<java.lang.Integer> MaxResults) {
    return create(TableName, NextToken, MaxResults);
  }
  public boolean is_ListContributorInsightsInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_MaxResults() {
    return this._MaxResults;
  }
}
