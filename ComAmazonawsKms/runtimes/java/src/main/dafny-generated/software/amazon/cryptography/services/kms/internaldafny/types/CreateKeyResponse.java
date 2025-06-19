// Class CreateKeyResponse
// Dafny class CreateKeyResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateKeyResponse {
  public Wrappers_Compile.Option<KeyMetadata> _KeyMetadata;
  public CreateKeyResponse (Wrappers_Compile.Option<KeyMetadata> KeyMetadata) {
    this._KeyMetadata = KeyMetadata;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateKeyResponse o = (CreateKeyResponse)other;
    return true && java.util.Objects.equals(this._KeyMetadata, o._KeyMetadata);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyMetadata);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CreateKeyResponse.CreateKeyResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyMetadata));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateKeyResponse> _TYPE = dafny.TypeDescriptor.<CreateKeyResponse>referenceWithInitializer(CreateKeyResponse.class, () -> CreateKeyResponse.Default());
  public static dafny.TypeDescriptor<CreateKeyResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateKeyResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateKeyResponse theDefault = CreateKeyResponse.create(Wrappers_Compile.Option.<KeyMetadata>Default(KeyMetadata._typeDescriptor()));
  public static CreateKeyResponse Default() {
    return theDefault;
  }
  public static CreateKeyResponse create(Wrappers_Compile.Option<KeyMetadata> KeyMetadata) {
    return new CreateKeyResponse(KeyMetadata);
  }
  public static CreateKeyResponse create_CreateKeyResponse(Wrappers_Compile.Option<KeyMetadata> KeyMetadata) {
    return create(KeyMetadata);
  }
  public boolean is_CreateKeyResponse() { return true; }
  public Wrappers_Compile.Option<KeyMetadata> dtor_KeyMetadata() {
    return this._KeyMetadata;
  }
}
