// Class OnDecryptInput
// Dafny class OnDecryptInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class OnDecryptInput {
  public DecryptionMaterials _materials;
  public dafny.DafnySequence<? extends EncryptedDataKey> _encryptedDataKeys;
  public OnDecryptInput (DecryptionMaterials materials, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys) {
    this._materials = materials;
    this._encryptedDataKeys = encryptedDataKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OnDecryptInput o = (OnDecryptInput)other;
    return true && java.util.Objects.equals(this._materials, o._materials) && java.util.Objects.equals(this._encryptedDataKeys, o._encryptedDataKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._materials);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptedDataKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.OnDecryptInput.OnDecryptInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._materials));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptedDataKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<OnDecryptInput> _TYPE = dafny.TypeDescriptor.<OnDecryptInput>referenceWithInitializer(OnDecryptInput.class, () -> OnDecryptInput.Default());
  public static dafny.TypeDescriptor<OnDecryptInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDecryptInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OnDecryptInput theDefault = OnDecryptInput.create(DecryptionMaterials.Default(), dafny.DafnySequence.<EncryptedDataKey> empty(EncryptedDataKey._typeDescriptor()));
  public static OnDecryptInput Default() {
    return theDefault;
  }
  public static OnDecryptInput create(DecryptionMaterials materials, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys) {
    return new OnDecryptInput(materials, encryptedDataKeys);
  }
  public static OnDecryptInput create_OnDecryptInput(DecryptionMaterials materials, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys) {
    return create(materials, encryptedDataKeys);
  }
  public boolean is_OnDecryptInput() { return true; }
  public DecryptionMaterials dtor_materials() {
    return this._materials;
  }
  public dafny.DafnySequence<? extends EncryptedDataKey> dtor_encryptedDataKeys() {
    return this._encryptedDataKeys;
  }
}
