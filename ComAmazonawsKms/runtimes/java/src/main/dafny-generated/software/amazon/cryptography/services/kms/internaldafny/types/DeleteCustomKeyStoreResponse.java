// Class DeleteCustomKeyStoreResponse
// Dafny class DeleteCustomKeyStoreResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteCustomKeyStoreResponse {
  public DeleteCustomKeyStoreResponse () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteCustomKeyStoreResponse o = (DeleteCustomKeyStoreResponse)other;
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
    s.append("ComAmazonawsKmsTypes.DeleteCustomKeyStoreResponse.DeleteCustomKeyStoreResponse");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteCustomKeyStoreResponse> _TYPE = dafny.TypeDescriptor.<DeleteCustomKeyStoreResponse>referenceWithInitializer(DeleteCustomKeyStoreResponse.class, () -> DeleteCustomKeyStoreResponse.Default());
  public static dafny.TypeDescriptor<DeleteCustomKeyStoreResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteCustomKeyStoreResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteCustomKeyStoreResponse theDefault = DeleteCustomKeyStoreResponse.create();
  public static DeleteCustomKeyStoreResponse Default() {
    return theDefault;
  }
  public static DeleteCustomKeyStoreResponse create() {
    return new DeleteCustomKeyStoreResponse();
  }
  public static DeleteCustomKeyStoreResponse create_DeleteCustomKeyStoreResponse() {
    return create();
  }
  public boolean is_DeleteCustomKeyStoreResponse() { return true; }
  public static java.util.ArrayList<DeleteCustomKeyStoreResponse> AllSingletonConstructors() {
    java.util.ArrayList<DeleteCustomKeyStoreResponse> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DeleteCustomKeyStoreResponse());
    return singleton_iterator;
  }
}
