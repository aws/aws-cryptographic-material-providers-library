// Class XksProxyConfigurationType
// Dafny class XksProxyConfigurationType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class XksProxyConfigurationType {
  public Wrappers_Compile.Option<XksProxyConnectivityType> _Connectivity;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _AccessKeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _UriEndpoint;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _UriPath;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _VpcEndpointServiceName;
  public XksProxyConfigurationType (Wrappers_Compile.Option<XksProxyConnectivityType> Connectivity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AccessKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> UriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> UriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> VpcEndpointServiceName) {
    this._Connectivity = Connectivity;
    this._AccessKeyId = AccessKeyId;
    this._UriEndpoint = UriEndpoint;
    this._UriPath = UriPath;
    this._VpcEndpointServiceName = VpcEndpointServiceName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    XksProxyConfigurationType o = (XksProxyConfigurationType)other;
    return true && java.util.Objects.equals(this._Connectivity, o._Connectivity) && java.util.Objects.equals(this._AccessKeyId, o._AccessKeyId) && java.util.Objects.equals(this._UriEndpoint, o._UriEndpoint) && java.util.Objects.equals(this._UriPath, o._UriPath) && java.util.Objects.equals(this._VpcEndpointServiceName, o._VpcEndpointServiceName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Connectivity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AccessKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._UriEndpoint);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._UriPath);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._VpcEndpointServiceName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.XksProxyConfigurationType.XksProxyConfigurationType");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Connectivity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AccessKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._UriEndpoint));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._UriPath));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._VpcEndpointServiceName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<XksProxyConfigurationType> _TYPE = dafny.TypeDescriptor.<XksProxyConfigurationType>referenceWithInitializer(XksProxyConfigurationType.class, () -> XksProxyConfigurationType.Default());
  public static dafny.TypeDescriptor<XksProxyConfigurationType> _typeDescriptor() {
    return (dafny.TypeDescriptor<XksProxyConfigurationType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final XksProxyConfigurationType theDefault = software.amazon.cryptography.services.kms.internaldafny.types.XksProxyConfigurationType.create(Wrappers_Compile.Option.<XksProxyConnectivityType>Default(XksProxyConnectivityType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyAuthenticationAccessKeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyUriEndpointType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyUriPathType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyVpcEndpointServiceNameType._typeDescriptor()));
  public static XksProxyConfigurationType Default() {
    return theDefault;
  }
  public static XksProxyConfigurationType create(Wrappers_Compile.Option<XksProxyConnectivityType> Connectivity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AccessKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> UriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> UriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> VpcEndpointServiceName) {
    return new XksProxyConfigurationType(Connectivity, AccessKeyId, UriEndpoint, UriPath, VpcEndpointServiceName);
  }
  public static XksProxyConfigurationType create_XksProxyConfigurationType(Wrappers_Compile.Option<XksProxyConnectivityType> Connectivity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AccessKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> UriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> UriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> VpcEndpointServiceName) {
    return create(Connectivity, AccessKeyId, UriEndpoint, UriPath, VpcEndpointServiceName);
  }
  public boolean is_XksProxyConfigurationType() { return true; }
  public Wrappers_Compile.Option<XksProxyConnectivityType> dtor_Connectivity() {
    return this._Connectivity;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_AccessKeyId() {
    return this._AccessKeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_UriEndpoint() {
    return this._UriEndpoint;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_UriPath() {
    return this._UriPath;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_VpcEndpointServiceName() {
    return this._VpcEndpointServiceName;
  }
}
