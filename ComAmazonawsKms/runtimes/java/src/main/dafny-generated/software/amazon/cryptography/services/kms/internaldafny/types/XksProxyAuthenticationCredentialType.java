// Class XksProxyAuthenticationCredentialType
// Dafny class XksProxyAuthenticationCredentialType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class XksProxyAuthenticationCredentialType {
  public dafny.DafnySequence<? extends Character> _AccessKeyId;
  public dafny.DafnySequence<? extends Character> _RawSecretAccessKey;
  public XksProxyAuthenticationCredentialType (dafny.DafnySequence<? extends Character> AccessKeyId, dafny.DafnySequence<? extends Character> RawSecretAccessKey) {
    this._AccessKeyId = AccessKeyId;
    this._RawSecretAccessKey = RawSecretAccessKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    XksProxyAuthenticationCredentialType o = (XksProxyAuthenticationCredentialType)other;
    return true && java.util.Objects.equals(this._AccessKeyId, o._AccessKeyId) && java.util.Objects.equals(this._RawSecretAccessKey, o._RawSecretAccessKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AccessKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RawSecretAccessKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.XksProxyAuthenticationCredentialType.XksProxyAuthenticationCredentialType");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AccessKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RawSecretAccessKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<XksProxyAuthenticationCredentialType> _TYPE = dafny.TypeDescriptor.<XksProxyAuthenticationCredentialType>referenceWithInitializer(XksProxyAuthenticationCredentialType.class, () -> XksProxyAuthenticationCredentialType.Default());
  public static dafny.TypeDescriptor<XksProxyAuthenticationCredentialType> _typeDescriptor() {
    return (dafny.TypeDescriptor<XksProxyAuthenticationCredentialType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final XksProxyAuthenticationCredentialType theDefault = XksProxyAuthenticationCredentialType.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static XksProxyAuthenticationCredentialType Default() {
    return theDefault;
  }
  public static XksProxyAuthenticationCredentialType create(dafny.DafnySequence<? extends Character> AccessKeyId, dafny.DafnySequence<? extends Character> RawSecretAccessKey) {
    return new XksProxyAuthenticationCredentialType(AccessKeyId, RawSecretAccessKey);
  }
  public static XksProxyAuthenticationCredentialType create_XksProxyAuthenticationCredentialType(dafny.DafnySequence<? extends Character> AccessKeyId, dafny.DafnySequence<? extends Character> RawSecretAccessKey) {
    return create(AccessKeyId, RawSecretAccessKey);
  }
  public boolean is_XksProxyAuthenticationCredentialType() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_AccessKeyId() {
    return this._AccessKeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_RawSecretAccessKey() {
    return this._RawSecretAccessKey;
  }
}
