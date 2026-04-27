// Class RecipientInfo
// Dafny class RecipientInfo compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RecipientInfo {
  public Wrappers_Compile.Option<KeyEncryptionMechanism> _KeyEncryptionAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _AttestationDocument;
  public RecipientInfo (Wrappers_Compile.Option<KeyEncryptionMechanism> KeyEncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> AttestationDocument) {
    this._KeyEncryptionAlgorithm = KeyEncryptionAlgorithm;
    this._AttestationDocument = AttestationDocument;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RecipientInfo o = (RecipientInfo)other;
    return true && java.util.Objects.equals(this._KeyEncryptionAlgorithm, o._KeyEncryptionAlgorithm) && java.util.Objects.equals(this._AttestationDocument, o._AttestationDocument);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyEncryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttestationDocument);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.RecipientInfo.RecipientInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyEncryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttestationDocument));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RecipientInfo> _TYPE = dafny.TypeDescriptor.<RecipientInfo>referenceWithInitializer(RecipientInfo.class, () -> RecipientInfo.Default());
  public static dafny.TypeDescriptor<RecipientInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<RecipientInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RecipientInfo theDefault = RecipientInfo.create(Wrappers_Compile.Option.<KeyEncryptionMechanism>Default(KeyEncryptionMechanism._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(AttestationDocumentType._typeDescriptor()));
  public static RecipientInfo Default() {
    return theDefault;
  }
  public static RecipientInfo create(Wrappers_Compile.Option<KeyEncryptionMechanism> KeyEncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> AttestationDocument) {
    return new RecipientInfo(KeyEncryptionAlgorithm, AttestationDocument);
  }
  public static RecipientInfo create_RecipientInfo(Wrappers_Compile.Option<KeyEncryptionMechanism> KeyEncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> AttestationDocument) {
    return create(KeyEncryptionAlgorithm, AttestationDocument);
  }
  public boolean is_RecipientInfo() { return true; }
  public Wrappers_Compile.Option<KeyEncryptionMechanism> dtor_KeyEncryptionAlgorithm() {
    return this._KeyEncryptionAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_AttestationDocument() {
    return this._AttestationDocument;
  }
}
