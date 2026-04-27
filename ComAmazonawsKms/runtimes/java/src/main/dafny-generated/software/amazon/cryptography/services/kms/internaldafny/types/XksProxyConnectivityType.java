// Class XksProxyConnectivityType
// Dafny class XksProxyConnectivityType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class XksProxyConnectivityType {
  public XksProxyConnectivityType() {
  }
  private static final dafny.TypeDescriptor<XksProxyConnectivityType> _TYPE = dafny.TypeDescriptor.<XksProxyConnectivityType>referenceWithInitializer(XksProxyConnectivityType.class, () -> XksProxyConnectivityType.Default());
  public static dafny.TypeDescriptor<XksProxyConnectivityType> _typeDescriptor() {
    return (dafny.TypeDescriptor<XksProxyConnectivityType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final XksProxyConnectivityType theDefault = XksProxyConnectivityType.create_PUBLIC__ENDPOINT();
  public static XksProxyConnectivityType Default() {
    return theDefault;
  }
  public static XksProxyConnectivityType create_PUBLIC__ENDPOINT() {
    return new XksProxyConnectivityType_PUBLIC__ENDPOINT();
  }
  public static XksProxyConnectivityType create_VPC__ENDPOINT__SERVICE() {
    return new XksProxyConnectivityType_VPC__ENDPOINT__SERVICE();
  }
  public boolean is_PUBLIC__ENDPOINT() { return this instanceof XksProxyConnectivityType_PUBLIC__ENDPOINT; }
  public boolean is_VPC__ENDPOINT__SERVICE() { return this instanceof XksProxyConnectivityType_VPC__ENDPOINT__SERVICE; }
  public static java.util.ArrayList<XksProxyConnectivityType> AllSingletonConstructors() {
    java.util.ArrayList<XksProxyConnectivityType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new XksProxyConnectivityType_PUBLIC__ENDPOINT());
    singleton_iterator.add(new XksProxyConnectivityType_VPC__ENDPOINT__SERVICE());
    return singleton_iterator;
  }
}
