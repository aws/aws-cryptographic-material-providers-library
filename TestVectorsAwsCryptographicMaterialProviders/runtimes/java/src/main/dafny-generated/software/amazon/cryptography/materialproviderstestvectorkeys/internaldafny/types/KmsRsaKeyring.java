// Class KmsRsaKeyring
// Dafny class KmsRsaKeyring compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsRsaKeyring {
  public dafny.DafnySequence<? extends Character> _keyId;
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _encryptionAlgorithm;
  public KmsRsaKeyring (dafny.DafnySequence<? extends Character> keyId, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec encryptionAlgorithm) {
    this._keyId = keyId;
    this._encryptionAlgorithm = encryptionAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsRsaKeyring o = (KmsRsaKeyring)other;
    return true && java.util.Objects.equals(this._keyId, o._keyId) && java.util.Objects.equals(this._encryptionAlgorithm, o._encryptionAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring.KmsRsaKeyring");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsRsaKeyring> _TYPE = dafny.TypeDescriptor.<KmsRsaKeyring>referenceWithInitializer(KmsRsaKeyring.class, () -> KmsRsaKeyring.Default());
  public static dafny.TypeDescriptor<KmsRsaKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsRsaKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsRsaKeyring theDefault = KmsRsaKeyring.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.Default());
  public static KmsRsaKeyring Default() {
    return theDefault;
  }
  public static KmsRsaKeyring create(dafny.DafnySequence<? extends Character> keyId, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec encryptionAlgorithm) {
    return new KmsRsaKeyring(keyId, encryptionAlgorithm);
  }
  public static KmsRsaKeyring create_KmsRsaKeyring(dafny.DafnySequence<? extends Character> keyId, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec encryptionAlgorithm) {
    return create(keyId, encryptionAlgorithm);
  }
  public boolean is_KmsRsaKeyring() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec dtor_encryptionAlgorithm() {
    return this._encryptionAlgorithm;
  }
}
