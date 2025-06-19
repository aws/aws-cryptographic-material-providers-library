// Class ConnectCustomKeyStoreResponse
// Dafny class ConnectCustomKeyStoreResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectCustomKeyStoreResponse {
  public ConnectCustomKeyStoreResponse () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectCustomKeyStoreResponse o = (ConnectCustomKeyStoreResponse)other;
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
    s.append("ComAmazonawsKmsTypes.ConnectCustomKeyStoreResponse.ConnectCustomKeyStoreResponse");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ConnectCustomKeyStoreResponse> _TYPE = dafny.TypeDescriptor.<ConnectCustomKeyStoreResponse>referenceWithInitializer(ConnectCustomKeyStoreResponse.class, () -> ConnectCustomKeyStoreResponse.Default());
  public static dafny.TypeDescriptor<ConnectCustomKeyStoreResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ConnectCustomKeyStoreResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ConnectCustomKeyStoreResponse theDefault = ConnectCustomKeyStoreResponse.create();
  public static ConnectCustomKeyStoreResponse Default() {
    return theDefault;
  }
  public static ConnectCustomKeyStoreResponse create() {
    return new ConnectCustomKeyStoreResponse();
  }
  public static ConnectCustomKeyStoreResponse create_ConnectCustomKeyStoreResponse() {
    return create();
  }
  public boolean is_ConnectCustomKeyStoreResponse() { return true; }
  public static java.util.ArrayList<ConnectCustomKeyStoreResponse> AllSingletonConstructors() {
    java.util.ArrayList<ConnectCustomKeyStoreResponse> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ConnectCustomKeyStoreResponse());
    return singleton_iterator;
  }
}
