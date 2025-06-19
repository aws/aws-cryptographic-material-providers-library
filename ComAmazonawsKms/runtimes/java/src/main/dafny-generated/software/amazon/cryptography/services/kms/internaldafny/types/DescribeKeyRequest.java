// Class DescribeKeyRequest
// Dafny class DescribeKeyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeKeyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public DescribeKeyRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens) {
    this._KeyId = KeyId;
    this._GrantTokens = GrantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeKeyRequest o = (DescribeKeyRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DescribeKeyRequest.DescribeKeyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeKeyRequest> _TYPE = dafny.TypeDescriptor.<DescribeKeyRequest>referenceWithInitializer(DescribeKeyRequest.class, () -> DescribeKeyRequest.Default());
  public static dafny.TypeDescriptor<DescribeKeyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeKeyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeKeyRequest theDefault = DescribeKeyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()));
  public static DescribeKeyRequest Default() {
    return theDefault;
  }
  public static DescribeKeyRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens) {
    return new DescribeKeyRequest(KeyId, GrantTokens);
  }
  public static DescribeKeyRequest create_DescribeKeyRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens) {
    return create(KeyId, GrantTokens);
  }
  public boolean is_DescribeKeyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
}
