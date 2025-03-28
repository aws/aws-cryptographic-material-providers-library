// Class CreateGrantResponse
// Dafny class CreateGrantResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateGrantResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GrantToken;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GrantId;
  public CreateGrantResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId) {
    this._GrantToken = GrantToken;
    this._GrantId = GrantId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateGrantResponse o = (CreateGrantResponse)other;
    return true && java.util.Objects.equals(this._GrantToken, o._GrantToken) && java.util.Objects.equals(this._GrantId, o._GrantId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CreateGrantResponse.CreateGrantResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GrantToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateGrantResponse> _TYPE = dafny.TypeDescriptor.<CreateGrantResponse>referenceWithInitializer(CreateGrantResponse.class, () -> CreateGrantResponse.Default());
  public static dafny.TypeDescriptor<CreateGrantResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateGrantResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateGrantResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.CreateGrantResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantTokenType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantIdType._typeDescriptor()));
  public static CreateGrantResponse Default() {
    return theDefault;
  }
  public static CreateGrantResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId) {
    return new CreateGrantResponse(GrantToken, GrantId);
  }
  public static CreateGrantResponse create_CreateGrantResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId) {
    return create(GrantToken, GrantId);
  }
  public boolean is_CreateGrantResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GrantToken() {
    return this._GrantToken;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GrantId() {
    return this._GrantId;
  }
}
