// Class DescribeKeyResponse
// Dafny class DescribeKeyResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeKeyResponse {
  public Wrappers_Compile.Option<KeyMetadata> _KeyMetadata;
  public DescribeKeyResponse (Wrappers_Compile.Option<KeyMetadata> KeyMetadata) {
    this._KeyMetadata = KeyMetadata;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeKeyResponse o = (DescribeKeyResponse)other;
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
    s.append("ComAmazonawsKmsTypes.DescribeKeyResponse.DescribeKeyResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyMetadata));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeKeyResponse> _TYPE = dafny.TypeDescriptor.<DescribeKeyResponse>referenceWithInitializer(DescribeKeyResponse.class, () -> DescribeKeyResponse.Default());
  public static dafny.TypeDescriptor<DescribeKeyResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeKeyResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeKeyResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DescribeKeyResponse.create(Wrappers_Compile.Option.<KeyMetadata>Default(KeyMetadata._typeDescriptor()));
  public static DescribeKeyResponse Default() {
    return theDefault;
  }
  public static DescribeKeyResponse create(Wrappers_Compile.Option<KeyMetadata> KeyMetadata) {
    return new DescribeKeyResponse(KeyMetadata);
  }
  public static DescribeKeyResponse create_DescribeKeyResponse(Wrappers_Compile.Option<KeyMetadata> KeyMetadata) {
    return create(KeyMetadata);
  }
  public boolean is_DescribeKeyResponse() { return true; }
  public Wrappers_Compile.Option<KeyMetadata> dtor_KeyMetadata() {
    return this._KeyMetadata;
  }
}
