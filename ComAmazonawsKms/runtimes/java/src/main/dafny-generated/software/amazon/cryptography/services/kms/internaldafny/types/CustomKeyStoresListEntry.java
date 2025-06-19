// Class CustomKeyStoresListEntry
// Dafny class CustomKeyStoresListEntry compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CustomKeyStoresListEntry {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CloudHsmClusterId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TrustAnchorCertificate;
  public Wrappers_Compile.Option<ConnectionStateType> _ConnectionState;
  public Wrappers_Compile.Option<ConnectionErrorCodeType> _ConnectionErrorCode;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CreationDate;
  public Wrappers_Compile.Option<CustomKeyStoreType> _CustomKeyStoreType;
  public Wrappers_Compile.Option<XksProxyConfigurationType> _XksProxyConfiguration;
  public CustomKeyStoresListEntry (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TrustAnchorCertificate, Wrappers_Compile.Option<ConnectionStateType> ConnectionState, Wrappers_Compile.Option<ConnectionErrorCodeType> ConnectionErrorCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<CustomKeyStoreType> CustomKeyStoreType, Wrappers_Compile.Option<XksProxyConfigurationType> XksProxyConfiguration) {
    this._CustomKeyStoreId = CustomKeyStoreId;
    this._CustomKeyStoreName = CustomKeyStoreName;
    this._CloudHsmClusterId = CloudHsmClusterId;
    this._TrustAnchorCertificate = TrustAnchorCertificate;
    this._ConnectionState = ConnectionState;
    this._ConnectionErrorCode = ConnectionErrorCode;
    this._CreationDate = CreationDate;
    this._CustomKeyStoreType = CustomKeyStoreType;
    this._XksProxyConfiguration = XksProxyConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomKeyStoresListEntry o = (CustomKeyStoresListEntry)other;
    return true && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId) && java.util.Objects.equals(this._CustomKeyStoreName, o._CustomKeyStoreName) && java.util.Objects.equals(this._CloudHsmClusterId, o._CloudHsmClusterId) && java.util.Objects.equals(this._TrustAnchorCertificate, o._TrustAnchorCertificate) && java.util.Objects.equals(this._ConnectionState, o._ConnectionState) && java.util.Objects.equals(this._ConnectionErrorCode, o._ConnectionErrorCode) && java.util.Objects.equals(this._CreationDate, o._CreationDate) && java.util.Objects.equals(this._CustomKeyStoreType, o._CustomKeyStoreType) && java.util.Objects.equals(this._XksProxyConfiguration, o._XksProxyConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CloudHsmClusterId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TrustAnchorCertificate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConnectionState);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConnectionErrorCode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CreationDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksProxyConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CustomKeyStoresListEntry.CustomKeyStoresListEntry");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CloudHsmClusterId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TrustAnchorCertificate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConnectionState));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConnectionErrorCode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CreationDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksProxyConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CustomKeyStoresListEntry> _TYPE = dafny.TypeDescriptor.<CustomKeyStoresListEntry>referenceWithInitializer(CustomKeyStoresListEntry.class, () -> CustomKeyStoresListEntry.Default());
  public static dafny.TypeDescriptor<CustomKeyStoresListEntry> _typeDescriptor() {
    return (dafny.TypeDescriptor<CustomKeyStoresListEntry>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CustomKeyStoresListEntry theDefault = CustomKeyStoresListEntry.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreNameType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CloudHsmClusterIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TrustAnchorCertificateType._typeDescriptor()), Wrappers_Compile.Option.<ConnectionStateType>Default(ConnectionStateType._typeDescriptor()), Wrappers_Compile.Option.<ConnectionErrorCodeType>Default(ConnectionErrorCodeType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<CustomKeyStoreType>Default(CustomKeyStoreType._typeDescriptor()), Wrappers_Compile.Option.<XksProxyConfigurationType>Default(XksProxyConfigurationType._typeDescriptor()));
  public static CustomKeyStoresListEntry Default() {
    return theDefault;
  }
  public static CustomKeyStoresListEntry create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TrustAnchorCertificate, Wrappers_Compile.Option<ConnectionStateType> ConnectionState, Wrappers_Compile.Option<ConnectionErrorCodeType> ConnectionErrorCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<CustomKeyStoreType> CustomKeyStoreType, Wrappers_Compile.Option<XksProxyConfigurationType> XksProxyConfiguration) {
    return new CustomKeyStoresListEntry(CustomKeyStoreId, CustomKeyStoreName, CloudHsmClusterId, TrustAnchorCertificate, ConnectionState, ConnectionErrorCode, CreationDate, CustomKeyStoreType, XksProxyConfiguration);
  }
  public static CustomKeyStoresListEntry create_CustomKeyStoresListEntry(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TrustAnchorCertificate, Wrappers_Compile.Option<ConnectionStateType> ConnectionState, Wrappers_Compile.Option<ConnectionErrorCodeType> ConnectionErrorCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<CustomKeyStoreType> CustomKeyStoreType, Wrappers_Compile.Option<XksProxyConfigurationType> XksProxyConfiguration) {
    return create(CustomKeyStoreId, CustomKeyStoreName, CloudHsmClusterId, TrustAnchorCertificate, ConnectionState, ConnectionErrorCode, CreationDate, CustomKeyStoreType, XksProxyConfiguration);
  }
  public boolean is_CustomKeyStoresListEntry() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreName() {
    return this._CustomKeyStoreName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CloudHsmClusterId() {
    return this._CloudHsmClusterId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TrustAnchorCertificate() {
    return this._TrustAnchorCertificate;
  }
  public Wrappers_Compile.Option<ConnectionStateType> dtor_ConnectionState() {
    return this._ConnectionState;
  }
  public Wrappers_Compile.Option<ConnectionErrorCodeType> dtor_ConnectionErrorCode() {
    return this._ConnectionErrorCode;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CreationDate() {
    return this._CreationDate;
  }
  public Wrappers_Compile.Option<CustomKeyStoreType> dtor_CustomKeyStoreType() {
    return this._CustomKeyStoreType;
  }
  public Wrappers_Compile.Option<XksProxyConfigurationType> dtor_XksProxyConfiguration() {
    return this._XksProxyConfiguration;
  }
}
