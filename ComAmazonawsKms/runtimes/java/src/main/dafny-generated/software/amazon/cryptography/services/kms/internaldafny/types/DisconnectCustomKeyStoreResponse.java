// Class DisconnectCustomKeyStoreResponse
// Dafny class DisconnectCustomKeyStoreResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DisconnectCustomKeyStoreResponse {
  public DisconnectCustomKeyStoreResponse () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DisconnectCustomKeyStoreResponse o = (DisconnectCustomKeyStoreResponse)other;
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
    s.append("ComAmazonawsKmsTypes.DisconnectCustomKeyStoreResponse.DisconnectCustomKeyStoreResponse");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DisconnectCustomKeyStoreResponse> _TYPE = dafny.TypeDescriptor.<DisconnectCustomKeyStoreResponse>referenceWithInitializer(DisconnectCustomKeyStoreResponse.class, () -> DisconnectCustomKeyStoreResponse.Default());
  public static dafny.TypeDescriptor<DisconnectCustomKeyStoreResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<DisconnectCustomKeyStoreResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DisconnectCustomKeyStoreResponse theDefault = DisconnectCustomKeyStoreResponse.create();
  public static DisconnectCustomKeyStoreResponse Default() {
    return theDefault;
  }
  public static DisconnectCustomKeyStoreResponse create() {
    return new DisconnectCustomKeyStoreResponse();
  }
  public static DisconnectCustomKeyStoreResponse create_DisconnectCustomKeyStoreResponse() {
    return create();
  }
  public boolean is_DisconnectCustomKeyStoreResponse() { return true; }
  public static java.util.ArrayList<DisconnectCustomKeyStoreResponse> AllSingletonConstructors() {
    java.util.ArrayList<DisconnectCustomKeyStoreResponse> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DisconnectCustomKeyStoreResponse());
    return singleton_iterator;
  }
}
