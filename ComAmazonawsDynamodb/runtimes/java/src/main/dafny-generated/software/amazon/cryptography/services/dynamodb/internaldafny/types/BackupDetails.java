// Class BackupDetails
// Dafny class BackupDetails compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BackupDetails {
  public dafny.DafnySequence<? extends Character> _BackupArn;
  public dafny.DafnySequence<? extends Character> _BackupName;
  public Wrappers_Compile.Option<java.lang.Long> _BackupSizeBytes;
  public BackupStatus _BackupStatus;
  public BackupType _BackupType;
  public dafny.DafnySequence<? extends Character> _BackupCreationDateTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _BackupExpiryDateTime;
  public BackupDetails (dafny.DafnySequence<? extends Character> BackupArn, dafny.DafnySequence<? extends Character> BackupName, Wrappers_Compile.Option<java.lang.Long> BackupSizeBytes, BackupStatus BackupStatus, BackupType BackupType, dafny.DafnySequence<? extends Character> BackupCreationDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupExpiryDateTime) {
    this._BackupArn = BackupArn;
    this._BackupName = BackupName;
    this._BackupSizeBytes = BackupSizeBytes;
    this._BackupStatus = BackupStatus;
    this._BackupType = BackupType;
    this._BackupCreationDateTime = BackupCreationDateTime;
    this._BackupExpiryDateTime = BackupExpiryDateTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupDetails o = (BackupDetails)other;
    return true && java.util.Objects.equals(this._BackupArn, o._BackupArn) && java.util.Objects.equals(this._BackupName, o._BackupName) && java.util.Objects.equals(this._BackupSizeBytes, o._BackupSizeBytes) && java.util.Objects.equals(this._BackupStatus, o._BackupStatus) && java.util.Objects.equals(this._BackupType, o._BackupType) && java.util.Objects.equals(this._BackupCreationDateTime, o._BackupCreationDateTime) && java.util.Objects.equals(this._BackupExpiryDateTime, o._BackupExpiryDateTime);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupSizeBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupCreationDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupExpiryDateTime);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BackupDetails.BackupDetails");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupSizeBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupCreationDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupExpiryDateTime));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BackupDetails> _TYPE = dafny.TypeDescriptor.<BackupDetails>referenceWithInitializer(BackupDetails.class, () -> BackupDetails.Default());
  public static dafny.TypeDescriptor<BackupDetails> _typeDescriptor() {
    return (dafny.TypeDescriptor<BackupDetails>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BackupDetails theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupDetails.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>Default(BackupSizeBytes._typeDescriptor()), BackupStatus.Default(), BackupType.Default(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static BackupDetails Default() {
    return theDefault;
  }
  public static BackupDetails create(dafny.DafnySequence<? extends Character> BackupArn, dafny.DafnySequence<? extends Character> BackupName, Wrappers_Compile.Option<java.lang.Long> BackupSizeBytes, BackupStatus BackupStatus, BackupType BackupType, dafny.DafnySequence<? extends Character> BackupCreationDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupExpiryDateTime) {
    return new BackupDetails(BackupArn, BackupName, BackupSizeBytes, BackupStatus, BackupType, BackupCreationDateTime, BackupExpiryDateTime);
  }
  public static BackupDetails create_BackupDetails(dafny.DafnySequence<? extends Character> BackupArn, dafny.DafnySequence<? extends Character> BackupName, Wrappers_Compile.Option<java.lang.Long> BackupSizeBytes, BackupStatus BackupStatus, BackupType BackupType, dafny.DafnySequence<? extends Character> BackupCreationDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupExpiryDateTime) {
    return create(BackupArn, BackupName, BackupSizeBytes, BackupStatus, BackupType, BackupCreationDateTime, BackupExpiryDateTime);
  }
  public boolean is_BackupDetails() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_BackupArn() {
    return this._BackupArn;
  }
  public dafny.DafnySequence<? extends Character> dtor_BackupName() {
    return this._BackupName;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_BackupSizeBytes() {
    return this._BackupSizeBytes;
  }
  public BackupStatus dtor_BackupStatus() {
    return this._BackupStatus;
  }
  public BackupType dtor_BackupType() {
    return this._BackupType;
  }
  public dafny.DafnySequence<? extends Character> dtor_BackupCreationDateTime() {
    return this._BackupCreationDateTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_BackupExpiryDateTime() {
    return this._BackupExpiryDateTime;
  }
}
