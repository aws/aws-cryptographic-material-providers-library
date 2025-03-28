// Class CreateCustomKeyStoreResponse
// Dafny class CreateCustomKeyStoreResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateCustomKeyStoreResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreId;
  public CreateCustomKeyStoreResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId) {
    this._CustomKeyStoreId = CustomKeyStoreId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateCustomKeyStoreResponse o = (CreateCustomKeyStoreResponse)other;
    return true && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CreateCustomKeyStoreResponse.CreateCustomKeyStoreResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateCustomKeyStoreResponse> _TYPE = dafny.TypeDescriptor.<CreateCustomKeyStoreResponse>referenceWithInitializer(CreateCustomKeyStoreResponse.class, () -> CreateCustomKeyStoreResponse.Default());
  public static dafny.TypeDescriptor<CreateCustomKeyStoreResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateCustomKeyStoreResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateCustomKeyStoreResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.CreateCustomKeyStoreResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreIdType._typeDescriptor()));
  public static CreateCustomKeyStoreResponse Default() {
    return theDefault;
  }
  public static CreateCustomKeyStoreResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId) {
    return new CreateCustomKeyStoreResponse(CustomKeyStoreId);
  }
  public static CreateCustomKeyStoreResponse create_CreateCustomKeyStoreResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId) {
    return create(CustomKeyStoreId);
  }
  public boolean is_CreateCustomKeyStoreResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
}
