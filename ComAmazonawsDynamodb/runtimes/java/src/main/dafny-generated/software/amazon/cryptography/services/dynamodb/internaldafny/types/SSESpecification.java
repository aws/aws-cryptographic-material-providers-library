// Class SSESpecification
// Dafny class SSESpecification compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SSESpecification {
  public Wrappers_Compile.Option<Boolean> _Enabled;
  public Wrappers_Compile.Option<SSEType> _SSEType;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KMSMasterKeyId;
  public SSESpecification (Wrappers_Compile.Option<Boolean> Enabled, Wrappers_Compile.Option<SSEType> SSEType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId) {
    this._Enabled = Enabled;
    this._SSEType = SSEType;
    this._KMSMasterKeyId = KMSMasterKeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SSESpecification o = (SSESpecification)other;
    return true && java.util.Objects.equals(this._Enabled, o._Enabled) && java.util.Objects.equals(this._SSEType, o._SSEType) && java.util.Objects.equals(this._KMSMasterKeyId, o._KMSMasterKeyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Enabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSEType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KMSMasterKeyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.SSESpecification.SSESpecification");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Enabled));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSEType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KMSMasterKeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SSESpecification> _TYPE = dafny.TypeDescriptor.<SSESpecification>referenceWithInitializer(SSESpecification.class, () -> SSESpecification.Default());
  public static dafny.TypeDescriptor<SSESpecification> _typeDescriptor() {
    return (dafny.TypeDescriptor<SSESpecification>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SSESpecification theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.SSESpecification.create(Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<SSEType>Default(SSEType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static SSESpecification Default() {
    return theDefault;
  }
  public static SSESpecification create(Wrappers_Compile.Option<Boolean> Enabled, Wrappers_Compile.Option<SSEType> SSEType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId) {
    return new SSESpecification(Enabled, SSEType, KMSMasterKeyId);
  }
  public static SSESpecification create_SSESpecification(Wrappers_Compile.Option<Boolean> Enabled, Wrappers_Compile.Option<SSEType> SSEType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId) {
    return create(Enabled, SSEType, KMSMasterKeyId);
  }
  public boolean is_SSESpecification() { return true; }
  public Wrappers_Compile.Option<Boolean> dtor_Enabled() {
    return this._Enabled;
  }
  public Wrappers_Compile.Option<SSEType> dtor_SSEType() {
    return this._SSEType;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KMSMasterKeyId() {
    return this._KMSMasterKeyId;
  }
}
