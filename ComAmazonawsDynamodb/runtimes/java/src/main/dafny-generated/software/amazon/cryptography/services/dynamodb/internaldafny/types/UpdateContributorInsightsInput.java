// Class UpdateContributorInsightsInput
// Dafny class UpdateContributorInsightsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateContributorInsightsInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public ContributorInsightsAction _ContributorInsightsAction;
  public UpdateContributorInsightsInput (dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, ContributorInsightsAction ContributorInsightsAction) {
    this._TableName = TableName;
    this._IndexName = IndexName;
    this._ContributorInsightsAction = ContributorInsightsAction;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateContributorInsightsInput o = (UpdateContributorInsightsInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ContributorInsightsAction, o._ContributorInsightsAction);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContributorInsightsAction);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateContributorInsightsInput.UpdateContributorInsightsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ContributorInsightsAction));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateContributorInsightsInput> _TYPE = dafny.TypeDescriptor.<UpdateContributorInsightsInput>referenceWithInitializer(UpdateContributorInsightsInput.class, () -> UpdateContributorInsightsInput.Default());
  public static dafny.TypeDescriptor<UpdateContributorInsightsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateContributorInsightsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateContributorInsightsInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateContributorInsightsInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), ContributorInsightsAction.Default());
  public static UpdateContributorInsightsInput Default() {
    return theDefault;
  }
  public static UpdateContributorInsightsInput create(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, ContributorInsightsAction ContributorInsightsAction) {
    return new UpdateContributorInsightsInput(TableName, IndexName, ContributorInsightsAction);
  }
  public static UpdateContributorInsightsInput create_UpdateContributorInsightsInput(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, ContributorInsightsAction ContributorInsightsAction) {
    return create(TableName, IndexName, ContributorInsightsAction);
  }
  public boolean is_UpdateContributorInsightsInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public ContributorInsightsAction dtor_ContributorInsightsAction() {
    return this._ContributorInsightsAction;
  }
}
