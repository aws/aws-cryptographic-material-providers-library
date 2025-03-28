// Class BackupDescription
// Dafny class BackupDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BackupDescription {
  public Wrappers_Compile.Option<BackupDetails> _BackupDetails;
  public Wrappers_Compile.Option<SourceTableDetails> _SourceTableDetails;
  public Wrappers_Compile.Option<SourceTableFeatureDetails> _SourceTableFeatureDetails;
  public BackupDescription (Wrappers_Compile.Option<BackupDetails> BackupDetails, Wrappers_Compile.Option<SourceTableDetails> SourceTableDetails, Wrappers_Compile.Option<SourceTableFeatureDetails> SourceTableFeatureDetails) {
    this._BackupDetails = BackupDetails;
    this._SourceTableDetails = SourceTableDetails;
    this._SourceTableFeatureDetails = SourceTableFeatureDetails;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupDescription o = (BackupDescription)other;
    return true && java.util.Objects.equals(this._BackupDetails, o._BackupDetails) && java.util.Objects.equals(this._SourceTableDetails, o._SourceTableDetails) && java.util.Objects.equals(this._SourceTableFeatureDetails, o._SourceTableFeatureDetails);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupDetails);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceTableDetails);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceTableFeatureDetails);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BackupDescription.BackupDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupDetails));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceTableDetails));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceTableFeatureDetails));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BackupDescription> _TYPE = dafny.TypeDescriptor.<BackupDescription>referenceWithInitializer(BackupDescription.class, () -> BackupDescription.Default());
  public static dafny.TypeDescriptor<BackupDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<BackupDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BackupDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupDescription.create(Wrappers_Compile.Option.<BackupDetails>Default(BackupDetails._typeDescriptor()), Wrappers_Compile.Option.<SourceTableDetails>Default(SourceTableDetails._typeDescriptor()), Wrappers_Compile.Option.<SourceTableFeatureDetails>Default(SourceTableFeatureDetails._typeDescriptor()));
  public static BackupDescription Default() {
    return theDefault;
  }
  public static BackupDescription create(Wrappers_Compile.Option<BackupDetails> BackupDetails, Wrappers_Compile.Option<SourceTableDetails> SourceTableDetails, Wrappers_Compile.Option<SourceTableFeatureDetails> SourceTableFeatureDetails) {
    return new BackupDescription(BackupDetails, SourceTableDetails, SourceTableFeatureDetails);
  }
  public static BackupDescription create_BackupDescription(Wrappers_Compile.Option<BackupDetails> BackupDetails, Wrappers_Compile.Option<SourceTableDetails> SourceTableDetails, Wrappers_Compile.Option<SourceTableFeatureDetails> SourceTableFeatureDetails) {
    return create(BackupDetails, SourceTableDetails, SourceTableFeatureDetails);
  }
  public boolean is_BackupDescription() { return true; }
  public Wrappers_Compile.Option<BackupDetails> dtor_BackupDetails() {
    return this._BackupDetails;
  }
  public Wrappers_Compile.Option<SourceTableDetails> dtor_SourceTableDetails() {
    return this._SourceTableDetails;
  }
  public Wrappers_Compile.Option<SourceTableFeatureDetails> dtor_SourceTableFeatureDetails() {
    return this._SourceTableFeatureDetails;
  }
}
