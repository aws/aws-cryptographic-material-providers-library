// Class SSEDescription
// Dafny class SSEDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SSEDescription {
  public Wrappers_Compile.Option<SSEStatus> _Status;
  public Wrappers_Compile.Option<SSEType> _SSEType;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KMSMasterKeyArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _InaccessibleEncryptionDateTime;
  public SSEDescription (Wrappers_Compile.Option<SSEStatus> Status, Wrappers_Compile.Option<SSEType> SSEType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> InaccessibleEncryptionDateTime) {
    this._Status = Status;
    this._SSEType = SSEType;
    this._KMSMasterKeyArn = KMSMasterKeyArn;
    this._InaccessibleEncryptionDateTime = InaccessibleEncryptionDateTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SSEDescription o = (SSEDescription)other;
    return true && java.util.Objects.equals(this._Status, o._Status) && java.util.Objects.equals(this._SSEType, o._SSEType) && java.util.Objects.equals(this._KMSMasterKeyArn, o._KMSMasterKeyArn) && java.util.Objects.equals(this._InaccessibleEncryptionDateTime, o._InaccessibleEncryptionDateTime);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Status);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSEType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KMSMasterKeyArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InaccessibleEncryptionDateTime);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.SSEDescription.SSEDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Status));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSEType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KMSMasterKeyArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InaccessibleEncryptionDateTime));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SSEDescription> _TYPE = dafny.TypeDescriptor.<SSEDescription>referenceWithInitializer(SSEDescription.class, () -> SSEDescription.Default());
  public static dafny.TypeDescriptor<SSEDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<SSEDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SSEDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.SSEDescription.create(Wrappers_Compile.Option.<SSEStatus>Default(SSEStatus._typeDescriptor()), Wrappers_Compile.Option.<SSEType>Default(SSEType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static SSEDescription Default() {
    return theDefault;
  }
  public static SSEDescription create(Wrappers_Compile.Option<SSEStatus> Status, Wrappers_Compile.Option<SSEType> SSEType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> InaccessibleEncryptionDateTime) {
    return new SSEDescription(Status, SSEType, KMSMasterKeyArn, InaccessibleEncryptionDateTime);
  }
  public static SSEDescription create_SSEDescription(Wrappers_Compile.Option<SSEStatus> Status, Wrappers_Compile.Option<SSEType> SSEType, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> InaccessibleEncryptionDateTime) {
    return create(Status, SSEType, KMSMasterKeyArn, InaccessibleEncryptionDateTime);
  }
  public boolean is_SSEDescription() { return true; }
  public Wrappers_Compile.Option<SSEStatus> dtor_Status() {
    return this._Status;
  }
  public Wrappers_Compile.Option<SSEType> dtor_SSEType() {
    return this._SSEType;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KMSMasterKeyArn() {
    return this._KMSMasterKeyArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_InaccessibleEncryptionDateTime() {
    return this._InaccessibleEncryptionDateTime;
  }
}
