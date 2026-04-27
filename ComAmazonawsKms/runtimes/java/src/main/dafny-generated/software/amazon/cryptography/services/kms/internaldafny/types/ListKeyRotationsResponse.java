// Class ListKeyRotationsResponse
// Dafny class ListKeyRotationsResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListKeyRotationsResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends RotationsListEntry>> _Rotations;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextMarker;
  public Wrappers_Compile.Option<Boolean> _Truncated;
  public ListKeyRotationsResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends RotationsListEntry>> Rotations, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    this._Rotations = Rotations;
    this._NextMarker = NextMarker;
    this._Truncated = Truncated;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListKeyRotationsResponse o = (ListKeyRotationsResponse)other;
    return true && java.util.Objects.equals(this._Rotations, o._Rotations) && java.util.Objects.equals(this._NextMarker, o._NextMarker) && java.util.Objects.equals(this._Truncated, o._Truncated);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Rotations);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextMarker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Truncated);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListKeyRotationsResponse.ListKeyRotationsResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Rotations));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextMarker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Truncated));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListKeyRotationsResponse> _TYPE = dafny.TypeDescriptor.<ListKeyRotationsResponse>referenceWithInitializer(ListKeyRotationsResponse.class, () -> ListKeyRotationsResponse.Default());
  public static dafny.TypeDescriptor<ListKeyRotationsResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListKeyRotationsResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListKeyRotationsResponse theDefault = ListKeyRotationsResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends RotationsListEntry>>Default(dafny.DafnySequence.<RotationsListEntry>_typeDescriptor(RotationsListEntry._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ListKeyRotationsResponse Default() {
    return theDefault;
  }
  public static ListKeyRotationsResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends RotationsListEntry>> Rotations, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return new ListKeyRotationsResponse(Rotations, NextMarker, Truncated);
  }
  public static ListKeyRotationsResponse create_ListKeyRotationsResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends RotationsListEntry>> Rotations, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return create(Rotations, NextMarker, Truncated);
  }
  public boolean is_ListKeyRotationsResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends RotationsListEntry>> dtor_Rotations() {
    return this._Rotations;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextMarker() {
    return this._NextMarker;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Truncated() {
    return this._Truncated;
  }
}
