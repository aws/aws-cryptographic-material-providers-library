// Class DescribeCustomKeyStoresRequest
// Dafny class DescribeCustomKeyStoresRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeCustomKeyStoresRequest {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreName;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Marker;
  public DescribeCustomKeyStoresRequest (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker) {
    this._CustomKeyStoreId = CustomKeyStoreId;
    this._CustomKeyStoreName = CustomKeyStoreName;
    this._Limit = Limit;
    this._Marker = Marker;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeCustomKeyStoresRequest o = (DescribeCustomKeyStoresRequest)other;
    return true && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId) && java.util.Objects.equals(this._CustomKeyStoreName, o._CustomKeyStoreName) && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._Marker, o._Marker);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Marker);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DescribeCustomKeyStoresRequest.DescribeCustomKeyStoresRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Marker));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeCustomKeyStoresRequest> _TYPE = dafny.TypeDescriptor.<DescribeCustomKeyStoresRequest>referenceWithInitializer(DescribeCustomKeyStoresRequest.class, () -> DescribeCustomKeyStoresRequest.Default());
  public static dafny.TypeDescriptor<DescribeCustomKeyStoresRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeCustomKeyStoresRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeCustomKeyStoresRequest theDefault = DescribeCustomKeyStoresRequest.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreNameType._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(LimitType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()));
  public static DescribeCustomKeyStoresRequest Default() {
    return theDefault;
  }
  public static DescribeCustomKeyStoresRequest create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker) {
    return new DescribeCustomKeyStoresRequest(CustomKeyStoreId, CustomKeyStoreName, Limit, Marker);
  }
  public static DescribeCustomKeyStoresRequest create_DescribeCustomKeyStoresRequest(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker) {
    return create(CustomKeyStoreId, CustomKeyStoreName, Limit, Marker);
  }
  public boolean is_DescribeCustomKeyStoresRequest() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreName() {
    return this._CustomKeyStoreName;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Marker() {
    return this._Marker;
  }
}
