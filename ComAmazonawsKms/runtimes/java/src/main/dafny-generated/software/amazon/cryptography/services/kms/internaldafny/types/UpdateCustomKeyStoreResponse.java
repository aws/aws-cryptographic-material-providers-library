// Class UpdateCustomKeyStoreResponse
// Dafny class UpdateCustomKeyStoreResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateCustomKeyStoreResponse {
  public UpdateCustomKeyStoreResponse () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateCustomKeyStoreResponse o = (UpdateCustomKeyStoreResponse)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.UpdateCustomKeyStoreResponse.UpdateCustomKeyStoreResponse");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateCustomKeyStoreResponse> _TYPE = dafny.TypeDescriptor.<UpdateCustomKeyStoreResponse>referenceWithInitializer(UpdateCustomKeyStoreResponse.class, () -> UpdateCustomKeyStoreResponse.Default());
  public static dafny.TypeDescriptor<UpdateCustomKeyStoreResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateCustomKeyStoreResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateCustomKeyStoreResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.UpdateCustomKeyStoreResponse.create();
  public static UpdateCustomKeyStoreResponse Default() {
    return theDefault;
  }
  public static UpdateCustomKeyStoreResponse create() {
    return new UpdateCustomKeyStoreResponse();
  }
  public static UpdateCustomKeyStoreResponse create_UpdateCustomKeyStoreResponse() {
    return create();
  }
  public boolean is_UpdateCustomKeyStoreResponse() { return true; }
  public static java.util.ArrayList<UpdateCustomKeyStoreResponse> AllSingletonConstructors() {
    java.util.ArrayList<UpdateCustomKeyStoreResponse> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new UpdateCustomKeyStoreResponse());
    return singleton_iterator;
  }
}
