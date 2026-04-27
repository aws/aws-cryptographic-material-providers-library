// Class PdkEncryptionAndSymmetricSigningKeys
// Dafny class PdkEncryptionAndSymmetricSigningKeys compiled into Java
package IntermediateKeyWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class PdkEncryptionAndSymmetricSigningKeys {
  public dafny.DafnySequence<? extends java.lang.Byte> _pdkEncryptionKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _symmetricSigningKey;
  public PdkEncryptionAndSymmetricSigningKeys (dafny.DafnySequence<? extends java.lang.Byte> pdkEncryptionKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey) {
    this._pdkEncryptionKey = pdkEncryptionKey;
    this._symmetricSigningKey = symmetricSigningKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PdkEncryptionAndSymmetricSigningKeys o = (PdkEncryptionAndSymmetricSigningKeys)other;
    return true && java.util.Objects.equals(this._pdkEncryptionKey, o._pdkEncryptionKey) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._pdkEncryptionKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.PdkEncryptionAndSymmetricSigningKeys");
    s.append("(");
    s.append(dafny.Helpers.toString(this._pdkEncryptionKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PdkEncryptionAndSymmetricSigningKeys> _TYPE = dafny.TypeDescriptor.<PdkEncryptionAndSymmetricSigningKeys>referenceWithInitializer(PdkEncryptionAndSymmetricSigningKeys.class, () -> PdkEncryptionAndSymmetricSigningKeys.Default());
  public static dafny.TypeDescriptor<PdkEncryptionAndSymmetricSigningKeys> _typeDescriptor() {
    return (dafny.TypeDescriptor<PdkEncryptionAndSymmetricSigningKeys>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PdkEncryptionAndSymmetricSigningKeys theDefault = PdkEncryptionAndSymmetricSigningKeys.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static PdkEncryptionAndSymmetricSigningKeys Default() {
    return theDefault;
  }
  public static PdkEncryptionAndSymmetricSigningKeys create(dafny.DafnySequence<? extends java.lang.Byte> pdkEncryptionKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey) {
    return new PdkEncryptionAndSymmetricSigningKeys(pdkEncryptionKey, symmetricSigningKey);
  }
  public static PdkEncryptionAndSymmetricSigningKeys create_PdkEncryptionAndSymmetricSigningKeys(dafny.DafnySequence<? extends java.lang.Byte> pdkEncryptionKey, dafny.DafnySequence<? extends java.lang.Byte> symmetricSigningKey) {
    return create(pdkEncryptionKey, symmetricSigningKey);
  }
  public boolean is_PdkEncryptionAndSymmetricSigningKeys() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_pdkEncryptionKey() {
    return this._pdkEncryptionKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_symmetricSigningKey() {
    return this._symmetricSigningKey;
  }
}
