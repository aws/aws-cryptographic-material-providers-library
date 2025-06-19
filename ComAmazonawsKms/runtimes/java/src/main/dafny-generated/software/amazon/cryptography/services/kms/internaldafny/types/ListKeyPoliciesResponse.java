// Class ListKeyPoliciesResponse
// Dafny class ListKeyPoliciesResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListKeyPoliciesResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _PolicyNames;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextMarker;
  public Wrappers_Compile.Option<Boolean> _Truncated;
  public ListKeyPoliciesResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> PolicyNames, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    this._PolicyNames = PolicyNames;
    this._NextMarker = NextMarker;
    this._Truncated = Truncated;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListKeyPoliciesResponse o = (ListKeyPoliciesResponse)other;
    return true && java.util.Objects.equals(this._PolicyNames, o._PolicyNames) && java.util.Objects.equals(this._NextMarker, o._NextMarker) && java.util.Objects.equals(this._Truncated, o._Truncated);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PolicyNames);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextMarker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Truncated);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListKeyPoliciesResponse.ListKeyPoliciesResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PolicyNames));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextMarker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Truncated));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListKeyPoliciesResponse> _TYPE = dafny.TypeDescriptor.<ListKeyPoliciesResponse>referenceWithInitializer(ListKeyPoliciesResponse.class, () -> ListKeyPoliciesResponse.Default());
  public static dafny.TypeDescriptor<ListKeyPoliciesResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListKeyPoliciesResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListKeyPoliciesResponse theDefault = ListKeyPoliciesResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(PolicyNameType._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ListKeyPoliciesResponse Default() {
    return theDefault;
  }
  public static ListKeyPoliciesResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> PolicyNames, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return new ListKeyPoliciesResponse(PolicyNames, NextMarker, Truncated);
  }
  public static ListKeyPoliciesResponse create_ListKeyPoliciesResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> PolicyNames, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return create(PolicyNames, NextMarker, Truncated);
  }
  public boolean is_ListKeyPoliciesResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_PolicyNames() {
    return this._PolicyNames;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextMarker() {
    return this._NextMarker;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Truncated() {
    return this._Truncated;
  }
}
