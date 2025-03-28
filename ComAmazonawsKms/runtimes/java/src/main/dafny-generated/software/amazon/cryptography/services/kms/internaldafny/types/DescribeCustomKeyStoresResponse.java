// Class DescribeCustomKeyStoresResponse
// Dafny class DescribeCustomKeyStoresResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeCustomKeyStoresResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends CustomKeyStoresListEntry>> _CustomKeyStores;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextMarker;
  public Wrappers_Compile.Option<Boolean> _Truncated;
  public DescribeCustomKeyStoresResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends CustomKeyStoresListEntry>> CustomKeyStores, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    this._CustomKeyStores = CustomKeyStores;
    this._NextMarker = NextMarker;
    this._Truncated = Truncated;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeCustomKeyStoresResponse o = (DescribeCustomKeyStoresResponse)other;
    return true && java.util.Objects.equals(this._CustomKeyStores, o._CustomKeyStores) && java.util.Objects.equals(this._NextMarker, o._NextMarker) && java.util.Objects.equals(this._Truncated, o._Truncated);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStores);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextMarker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Truncated);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DescribeCustomKeyStoresResponse.DescribeCustomKeyStoresResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStores));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextMarker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Truncated));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeCustomKeyStoresResponse> _TYPE = dafny.TypeDescriptor.<DescribeCustomKeyStoresResponse>referenceWithInitializer(DescribeCustomKeyStoresResponse.class, () -> DescribeCustomKeyStoresResponse.Default());
  public static dafny.TypeDescriptor<DescribeCustomKeyStoresResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeCustomKeyStoresResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeCustomKeyStoresResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DescribeCustomKeyStoresResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends CustomKeyStoresListEntry>>Default(dafny.DafnySequence.<CustomKeyStoresListEntry>_typeDescriptor(CustomKeyStoresListEntry._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static DescribeCustomKeyStoresResponse Default() {
    return theDefault;
  }
  public static DescribeCustomKeyStoresResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends CustomKeyStoresListEntry>> CustomKeyStores, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return new DescribeCustomKeyStoresResponse(CustomKeyStores, NextMarker, Truncated);
  }
  public static DescribeCustomKeyStoresResponse create_DescribeCustomKeyStoresResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends CustomKeyStoresListEntry>> CustomKeyStores, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return create(CustomKeyStores, NextMarker, Truncated);
  }
  public boolean is_DescribeCustomKeyStoresResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends CustomKeyStoresListEntry>> dtor_CustomKeyStores() {
    return this._CustomKeyStores;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextMarker() {
    return this._NextMarker;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Truncated() {
    return this._Truncated;
  }
}
