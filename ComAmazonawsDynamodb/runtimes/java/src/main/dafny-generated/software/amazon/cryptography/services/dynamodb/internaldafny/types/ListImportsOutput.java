// Class ListImportsOutput
// Dafny class ListImportsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListImportsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ImportSummary>> _ImportSummaryList;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public ListImportsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends ImportSummary>> ImportSummaryList, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    this._ImportSummaryList = ImportSummaryList;
    this._NextToken = NextToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListImportsOutput o = (ListImportsOutput)other;
    return true && java.util.Objects.equals(this._ImportSummaryList, o._ImportSummaryList) && java.util.Objects.equals(this._NextToken, o._NextToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportSummaryList);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListImportsOutput.ListImportsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ImportSummaryList));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListImportsOutput> _TYPE = dafny.TypeDescriptor.<ListImportsOutput>referenceWithInitializer(ListImportsOutput.class, () -> ListImportsOutput.Default());
  public static dafny.TypeDescriptor<ListImportsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListImportsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListImportsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ListImportsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends ImportSummary>>Default(dafny.DafnySequence.<ImportSummary>_typeDescriptor(ImportSummary._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ImportNextToken._typeDescriptor()));
  public static ListImportsOutput Default() {
    return theDefault;
  }
  public static ListImportsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends ImportSummary>> ImportSummaryList, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return new ListImportsOutput(ImportSummaryList, NextToken);
  }
  public static ListImportsOutput create_ListImportsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends ImportSummary>> ImportSummaryList, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return create(ImportSummaryList, NextToken);
  }
  public boolean is_ListImportsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ImportSummary>> dtor_ImportSummaryList() {
    return this._ImportSummaryList;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
}
