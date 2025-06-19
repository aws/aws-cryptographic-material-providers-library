// Class UpdateCustomKeyStoreRequest
// Dafny class UpdateCustomKeyStoreRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateCustomKeyStoreRequest {
  public dafny.DafnySequence<? extends Character> _CustomKeyStoreId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NewCustomKeyStoreName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyStorePassword;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CloudHsmClusterId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _XksProxyUriEndpoint;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _XksProxyUriPath;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _XksProxyVpcEndpointServiceName;
  public Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> _XksProxyAuthenticationCredential;
  public Wrappers_Compile.Option<XksProxyConnectivityType> _XksProxyConnectivity;
  public UpdateCustomKeyStoreRequest (dafny.DafnySequence<? extends Character> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NewCustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyStorePassword, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyVpcEndpointServiceName, Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> XksProxyAuthenticationCredential, Wrappers_Compile.Option<XksProxyConnectivityType> XksProxyConnectivity) {
    this._CustomKeyStoreId = CustomKeyStoreId;
    this._NewCustomKeyStoreName = NewCustomKeyStoreName;
    this._KeyStorePassword = KeyStorePassword;
    this._CloudHsmClusterId = CloudHsmClusterId;
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
    UpdateCustomKeyStoreRequest o = (UpdateCustomKeyStoreRequest)other;
    return true && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId) && java.util.Objects.equals(this._NewCustomKeyStoreName, o._NewCustomKeyStoreName) && java.util.Objects.equals(this._KeyStorePassword, o._KeyStorePassword) && java.util.Objects.equals(this._CloudHsmClusterId, o._CloudHsmClusterId) && java.util.Objects.equals(this._XksProxyUriEndpoint, o._XksProxyUriEndpoint) && java.util.Objects.equals(this._XksProxyUriPath, o._XksProxyUriPath) && java.util.Objects.equals(this._XksProxyVpcEndpointServiceName, o._XksProxyVpcEndpointServiceName) && java.util.Objects.equals(this._XksProxyAuthenticationCredential, o._XksProxyAuthenticationCredential) && java.util.Objects.equals(this._XksProxyConnectivity, o._XksProxyConnectivity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NewCustomKeyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyStorePassword);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CloudHsmClusterId);
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
    s.append("ComAmazonawsKmsTypes.UpdateCustomKeyStoreRequest.UpdateCustomKeyStoreRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NewCustomKeyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyStorePassword));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CloudHsmClusterId));
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
  private static final dafny.TypeDescriptor<UpdateCustomKeyStoreRequest> _TYPE = dafny.TypeDescriptor.<UpdateCustomKeyStoreRequest>referenceWithInitializer(UpdateCustomKeyStoreRequest.class, () -> UpdateCustomKeyStoreRequest.Default());
  public static dafny.TypeDescriptor<UpdateCustomKeyStoreRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateCustomKeyStoreRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateCustomKeyStoreRequest theDefault = UpdateCustomKeyStoreRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreNameType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyStorePasswordType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CloudHsmClusterIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyUriEndpointType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyUriPathType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksProxyVpcEndpointServiceNameType._typeDescriptor()), Wrappers_Compile.Option.<XksProxyAuthenticationCredentialType>Default(XksProxyAuthenticationCredentialType._typeDescriptor()), Wrappers_Compile.Option.<XksProxyConnectivityType>Default(XksProxyConnectivityType._typeDescriptor()));
  public static UpdateCustomKeyStoreRequest Default() {
    return theDefault;
  }
  public static UpdateCustomKeyStoreRequest create(dafny.DafnySequence<? extends Character> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NewCustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyStorePassword, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyVpcEndpointServiceName, Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> XksProxyAuthenticationCredential, Wrappers_Compile.Option<XksProxyConnectivityType> XksProxyConnectivity) {
    return new UpdateCustomKeyStoreRequest(CustomKeyStoreId, NewCustomKeyStoreName, KeyStorePassword, CloudHsmClusterId, XksProxyUriEndpoint, XksProxyUriPath, XksProxyVpcEndpointServiceName, XksProxyAuthenticationCredential, XksProxyConnectivity);
  }
  public static UpdateCustomKeyStoreRequest create_UpdateCustomKeyStoreRequest(dafny.DafnySequence<? extends Character> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NewCustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyStorePassword, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriEndpoint, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyUriPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksProxyVpcEndpointServiceName, Wrappers_Compile.Option<XksProxyAuthenticationCredentialType> XksProxyAuthenticationCredential, Wrappers_Compile.Option<XksProxyConnectivityType> XksProxyConnectivity) {
    return create(CustomKeyStoreId, NewCustomKeyStoreName, KeyStorePassword, CloudHsmClusterId, XksProxyUriEndpoint, XksProxyUriPath, XksProxyVpcEndpointServiceName, XksProxyAuthenticationCredential, XksProxyConnectivity);
  }
  public boolean is_UpdateCustomKeyStoreRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NewCustomKeyStoreName() {
    return this._NewCustomKeyStoreName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyStorePassword() {
    return this._KeyStorePassword;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CloudHsmClusterId() {
    return this._CloudHsmClusterId;
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
