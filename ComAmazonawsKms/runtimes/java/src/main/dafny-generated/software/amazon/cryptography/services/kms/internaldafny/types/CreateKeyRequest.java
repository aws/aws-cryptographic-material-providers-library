// Class CreateKeyRequest
// Dafny class CreateKeyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateKeyRequest {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Policy;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Description;
  public Wrappers_Compile.Option<KeyUsageType> _KeyUsage;
  public Wrappers_Compile.Option<CustomerMasterKeySpec> _CustomerMasterKeySpec;
  public Wrappers_Compile.Option<KeySpec> _KeySpec;
  public Wrappers_Compile.Option<OriginType> _Origin;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreId;
  public Wrappers_Compile.Option<Boolean> _BypassPolicyLockoutSafetyCheck;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> _Tags;
  public Wrappers_Compile.Option<Boolean> _MultiRegion;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _XksKeyId;
  public CreateKeyRequest (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<OriginType> Origin, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<Boolean> MultiRegion, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksKeyId) {
    this._Policy = Policy;
    this._Description = Description;
    this._KeyUsage = KeyUsage;
    this._CustomerMasterKeySpec = CustomerMasterKeySpec;
    this._KeySpec = KeySpec;
    this._Origin = Origin;
    this._CustomKeyStoreId = CustomKeyStoreId;
    this._BypassPolicyLockoutSafetyCheck = BypassPolicyLockoutSafetyCheck;
    this._Tags = Tags;
    this._MultiRegion = MultiRegion;
    this._XksKeyId = XksKeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateKeyRequest o = (CreateKeyRequest)other;
    return true && java.util.Objects.equals(this._Policy, o._Policy) && java.util.Objects.equals(this._Description, o._Description) && java.util.Objects.equals(this._KeyUsage, o._KeyUsage) && java.util.Objects.equals(this._CustomerMasterKeySpec, o._CustomerMasterKeySpec) && java.util.Objects.equals(this._KeySpec, o._KeySpec) && java.util.Objects.equals(this._Origin, o._Origin) && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId) && java.util.Objects.equals(this._BypassPolicyLockoutSafetyCheck, o._BypassPolicyLockoutSafetyCheck) && java.util.Objects.equals(this._Tags, o._Tags) && java.util.Objects.equals(this._MultiRegion, o._MultiRegion) && java.util.Objects.equals(this._XksKeyId, o._XksKeyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Policy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyUsage);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomerMasterKeySpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Origin);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BypassPolicyLockoutSafetyCheck);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Tags);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MultiRegion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksKeyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CreateKeyRequest.CreateKeyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Policy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyUsage));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomerMasterKeySpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Origin));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BypassPolicyLockoutSafetyCheck));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Tags));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MultiRegion));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksKeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateKeyRequest> _TYPE = dafny.TypeDescriptor.<CreateKeyRequest>referenceWithInitializer(CreateKeyRequest.class, () -> CreateKeyRequest.Default());
  public static dafny.TypeDescriptor<CreateKeyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateKeyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateKeyRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.CreateKeyRequest.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(DescriptionType._typeDescriptor()), Wrappers_Compile.Option.<KeyUsageType>Default(KeyUsageType._typeDescriptor()), Wrappers_Compile.Option.<CustomerMasterKeySpec>Default(CustomerMasterKeySpec._typeDescriptor()), Wrappers_Compile.Option.<KeySpec>Default(KeySpec._typeDescriptor()), Wrappers_Compile.Option.<OriginType>Default(OriginType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreIdType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Tag>>Default(dafny.DafnySequence.<Tag>_typeDescriptor(Tag._typeDescriptor())), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksKeyIdType._typeDescriptor()));
  public static CreateKeyRequest Default() {
    return theDefault;
  }
  public static CreateKeyRequest create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<OriginType> Origin, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<Boolean> MultiRegion, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksKeyId) {
    return new CreateKeyRequest(Policy, Description, KeyUsage, CustomerMasterKeySpec, KeySpec, Origin, CustomKeyStoreId, BypassPolicyLockoutSafetyCheck, Tags, MultiRegion, XksKeyId);
  }
  public static CreateKeyRequest create_CreateKeyRequest(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<OriginType> Origin, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<Boolean> MultiRegion, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> XksKeyId) {
    return create(Policy, Description, KeyUsage, CustomerMasterKeySpec, KeySpec, Origin, CustomKeyStoreId, BypassPolicyLockoutSafetyCheck, Tags, MultiRegion, XksKeyId);
  }
  public boolean is_CreateKeyRequest() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Policy() {
    return this._Policy;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Description() {
    return this._Description;
  }
  public Wrappers_Compile.Option<KeyUsageType> dtor_KeyUsage() {
    return this._KeyUsage;
  }
  public Wrappers_Compile.Option<CustomerMasterKeySpec> dtor_CustomerMasterKeySpec() {
    return this._CustomerMasterKeySpec;
  }
  public Wrappers_Compile.Option<KeySpec> dtor_KeySpec() {
    return this._KeySpec;
  }
  public Wrappers_Compile.Option<OriginType> dtor_Origin() {
    return this._Origin;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
  public Wrappers_Compile.Option<Boolean> dtor_BypassPolicyLockoutSafetyCheck() {
    return this._BypassPolicyLockoutSafetyCheck;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> dtor_Tags() {
    return this._Tags;
  }
  public Wrappers_Compile.Option<Boolean> dtor_MultiRegion() {
    return this._MultiRegion;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_XksKeyId() {
    return this._XksKeyId;
  }
}
