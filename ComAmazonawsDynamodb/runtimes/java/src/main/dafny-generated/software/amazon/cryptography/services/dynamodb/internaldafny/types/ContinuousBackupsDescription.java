// Class ContinuousBackupsDescription
// Dafny class ContinuousBackupsDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ContinuousBackupsDescription {
  public ContinuousBackupsStatus _ContinuousBackupsStatus;
  public Wrappers_Compile.Option<PointInTimeRecoveryDescription> _PointInTimeRecoveryDescription;
  public ContinuousBackupsDescription (ContinuousBackupsStatus ContinuousBackupsStatus, Wrappers_Compile.Option<PointInTimeRecoveryDescription> PointInTimeRecoveryDescription) {
    this._ContinuousBackupsStatus = ContinuousBackupsStatus;
    this._PointInTimeRecoveryDescription = PointInTimeRecoveryDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContinuousBackupsDescription o = (ContinuousBackupsDescription)other;
    return true && java.util.Objects.equals(this._ContinuousBackupsStatus, o._ContinuousBackupsStatus) && java.util.Objects.equals(this._PointInTimeRecoveryDescription, o._PointInTimeRecoveryDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContinuousBackupsStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PointInTimeRecoveryDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ContinuousBackupsDescription.ContinuousBackupsDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ContinuousBackupsStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PointInTimeRecoveryDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ContinuousBackupsDescription> _TYPE = dafny.TypeDescriptor.<ContinuousBackupsDescription>referenceWithInitializer(ContinuousBackupsDescription.class, () -> ContinuousBackupsDescription.Default());
  public static dafny.TypeDescriptor<ContinuousBackupsDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ContinuousBackupsDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ContinuousBackupsDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ContinuousBackupsDescription.create(ContinuousBackupsStatus.Default(), Wrappers_Compile.Option.<PointInTimeRecoveryDescription>Default(PointInTimeRecoveryDescription._typeDescriptor()));
  public static ContinuousBackupsDescription Default() {
    return theDefault;
  }
  public static ContinuousBackupsDescription create(ContinuousBackupsStatus ContinuousBackupsStatus, Wrappers_Compile.Option<PointInTimeRecoveryDescription> PointInTimeRecoveryDescription) {
    return new ContinuousBackupsDescription(ContinuousBackupsStatus, PointInTimeRecoveryDescription);
  }
  public static ContinuousBackupsDescription create_ContinuousBackupsDescription(ContinuousBackupsStatus ContinuousBackupsStatus, Wrappers_Compile.Option<PointInTimeRecoveryDescription> PointInTimeRecoveryDescription) {
    return create(ContinuousBackupsStatus, PointInTimeRecoveryDescription);
  }
  public boolean is_ContinuousBackupsDescription() { return true; }
  public ContinuousBackupsStatus dtor_ContinuousBackupsStatus() {
    return this._ContinuousBackupsStatus;
  }
  public Wrappers_Compile.Option<PointInTimeRecoveryDescription> dtor_PointInTimeRecoveryDescription() {
    return this._PointInTimeRecoveryDescription;
  }
}
