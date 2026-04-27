// Class CreateCustomKeyStoreRequest
// Dafny class CreateCustomKeyStoreRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateCustomKeyStoreRequest {
  public dafny.DafnySequence<? extends Character> _CustomKeyStoreName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CloudHsmClusterId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TrustAnchorCertificate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyStorePassword;
  public Wrappers_Compile.Option<CustomKeyStoreType> _CustomKeyStoreType;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _XksProxyUriEndpoint;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _XksProxyUriPath;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _XksProxyVpcEndpointServiceName;
  public Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> _XksProxyAuthenticationCredential;
  public Wrappers_Compile.Option<XksProxyConnectivityType> _XksProxyConnectivity;
  public CreateCustomKeyStoreRequest (dafny.DafnySequence<? extends Character> CustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TrustAnchorCertificate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyStorePassword, Wrappers_Compile.Option<CustomKeyStoreType> CustomKeyStoreType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyVpcEndpointServiceName, Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> XksProxyAuthenticationCredential, Wrappers_Compile.Option<XksProxyConnectivityType> XksProxyConnectivity) {
    this._CustomKeyStoreName = CustomKeyStoreName;
    this._CloudHsmClusterId = CloudHsmClusterId;
    this._TrustAnchorCertificate = TrustAnchorCertificate;
    this._KeyStorePassword = KeyStorePassword;
    this._CustomKeyStoreType = CustomKeyStoreType;
    this._XksProxyUriEndpoint = XksProxyUriEndpoint;
    this._XksProxyUriPath = XksProxyUriPath;
    this._XksProxyVpcEndpointServiceName = XksProxyVpcEndpointServiceName;
    this._XksProxyAuthenticationCredential = XksProxyAuthenticationCredential;
    this._XksProxyConnectivity = XksProxyConnectivity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateCustomKeyStoreRequest o = (CreateCustomKeyStoreRequest)other;
    return true && java.util.Objects.equals(this._CustomKeyStoreName, o._CustomKeyStoreName) && java.util.Objects.equals(this._CloudHsmClusterId, o._CloudHsmClusterId) && java.util.Objects.equals(this._TrustAnchorCertificate, o._TrustAnchorCertificate) && java.util.Objects.equals(this._KeyStorePassword, o._KeyStorePassword) && java.util.Objects.equals(this._CustomKeyStoreType, o._CustomKeyStoreType) && java.util.Objects.equals(this._XksProxyUriEndpoint, o._XksProxyUriEndpoint) && java.util.Objects.equals(this._XksProxyUriPath, o._XksProxyUriPath) && java.util.Objects.equals(this._XksProxyVpcEndpointServiceName, o._XksProxyVpcEndpointServiceName) && java.util.Objects.equals(this._XksProxyAuthenticationCredential, o._XksProxyAuthenticationCredential) && java.util.Objects.equals(this._XksProxyConnectivity, o._XksProxyConnectivity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CloudHsmClusterId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TrustAnchorCertificate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyStorePassword);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksProxyUriEndpoint);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksProxyUriPath);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksProxyVpcEndpointServiceName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksProxyAuthenticationCredential);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksProxyConnectivity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CreateCustomKeyStoreRequest.CreateCustomKeyStoreRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CloudHsmClusterId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TrustAnchorCertificate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyStorePassword));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksProxyUriEndpoint));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksProxyUriPath));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksProxyVpcEndpointServiceName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksProxyAuthenticationCredential));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksProxyConnectivity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateCustomKeyStoreRequest> _TYPE = dafny.TypeDescriptor.<CreateCustomKeyStoreRequest>referenceWithInitializer(CreateCustomKeyStoreRequest.class, () -> CreateCustomKeyStoreRequest.Default());
  public static dafny.TypeDescriptor<CreateCustomKeyStoreRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateCustomKeyStoreRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateCustomKeyStoreRequest theDefault = CreateCustomKeyStoreRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CloudHsmClusterIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TrustAnchorCertificateType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyStorePasswordType._typeDescriptor()), Wrappers_Compile.Option.<CustomKeyStoreType>Default(CustomKeyStoreType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyUriEndpointType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyUriPathType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyVpcEndpointServiceNameType._typeDescriptor()), Wrappers_Compile.Option.<XksProxyAuthenticationCredentialType>Default(XksProxyAuthenticationCredentialType._typeDescriptor()), Wrappers_Compile.Option.<XksProxyConnectivityType>Default(XksProxyConnectivityType._typeDescriptor()));
  public static CreateCustomKeyStoreRequest Default() {
    return theDefault;
  }
  public static CreateCustomKeyStoreRequest create(dafny.DafnySequence<? extends Character> CustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TrustAnchorCertificate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyStorePassword, Wrappers_Compile.Option<CustomKeyStoreType> CustomKeyStoreType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyVpcEndpointServiceName, Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> XksProxyAuthenticationCredential, Wrappers_Compile.Option<XksProxyConnectivityType> XksProxyConnectivity) {
    return new CreateCustomKeyStoreRequest(CustomKeyStoreName, CloudHsmClusterId, TrustAnchorCertificate, KeyStorePassword, CustomKeyStoreType, XksProxyUriEndpoint, XksProxyUriPath, XksProxyVpcEndpointServiceName, XksProxyAuthenticationCredential, XksProxyConnectivity);
  }
  public static CreateCustomKeyStoreRequest create_CreateCustomKeyStoreRequest(dafny.DafnySequence<? extends Character> CustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TrustAnchorCertificate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyStorePassword, Wrappers_Compile.Option<CustomKeyStoreType> CustomKeyStoreType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyVpcEndpointServiceName, Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> XksProxyAuthenticationCredential, Wrappers_Compile.Option<XksProxyConnectivityType> XksProxyConnectivity) {
    return create(CustomKeyStoreName, CloudHsmClusterId, TrustAnchorCertificate, KeyStorePassword, CustomKeyStoreType, XksProxyUriEndpoint, XksProxyUriPath, XksProxyVpcEndpointServiceName, XksProxyAuthenticationCredential, XksProxyConnectivity);
  }
  public boolean is_CreateCustomKeyStoreRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_CustomKeyStoreName() {
    return this._CustomKeyStoreName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CloudHsmClusterId() {
    return this._CloudHsmClusterId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TrustAnchorCertificate() {
    return this._TrustAnchorCertificate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyStorePassword() {
    return this._KeyStorePassword;
  }
  public Wrappers_Compile.Option<CustomKeyStoreType> dtor_CustomKeyStoreType() {
    return this._CustomKeyStoreType;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_XksProxyUriEndpoint() {
    return this._XksProxyUriEndpoint;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_XksProxyUriPath() {
    return this._XksProxyUriPath;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_XksProxyVpcEndpointServiceName() {
    return this._XksProxyVpcEndpointServiceName;
  }
  public Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> dtor_XksProxyAuthenticationCredential() {
    return this._XksProxyAuthenticationCredential;
  }
  public Wrappers_Compile.Option<XksProxyConnectivityType> dtor_XksProxyConnectivity() {
    return this._XksProxyConnectivity;
  }
}
