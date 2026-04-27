// Class ListExportsOutput
// Dafny class ListExportsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListExportsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ExportSummary>> _ExportSummaries;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public ListExportsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends ExportSummary>> ExportSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    this._ExportSummaries = ExportSummaries;
    this._NextToken = NextToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListExportsOutput o = (ListExportsOutput)other;
    return true && java.util.Objects.equals(this._ExportSummaries, o._ExportSummaries) && java.util.Objects.equals(this._NextToken, o._NextToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportSummaries);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListExportsOutput.ListExportsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExportSummaries));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListExportsOutput> _TYPE = dafny.TypeDescriptor.<ListExportsOutput>referenceWithInitializer(ListExportsOutput.class, () -> ListExportsOutput.Default());
  public static dafny.TypeDescriptor<ListExportsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListExportsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListExportsOutput theDefault = ListExportsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends ExportSummary>>Default(dafny.DafnySequence.<ExportSummary>_typeDescriptor(ExportSummary._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ListExportsOutput Default() {
    return theDefault;
  }
  public static ListExportsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends ExportSummary>> ExportSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return new ListExportsOutput(ExportSummaries, NextToken);
  }
  public static ListExportsOutput create_ListExportsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends ExportSummary>> ExportSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return create(ExportSummaries, NextToken);
  }
  public boolean is_ListExportsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ExportSummary>> dtor_ExportSummaries() {
    return this._ExportSummaries;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
}
