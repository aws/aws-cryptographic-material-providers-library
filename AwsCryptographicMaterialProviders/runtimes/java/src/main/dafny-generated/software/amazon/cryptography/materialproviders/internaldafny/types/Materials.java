// Class Materials
// Dafny class Materials compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Materials {
  public Materials() {
  }
  private static final dafny.TypeDescriptor<Materials> _TYPE = dafny.TypeDescriptor.<Materials>referenceWithInitializer(Materials.class, () -> Materials.Default());
  public static dafny.TypeDescriptor<Materials> _typeDescriptor() {
    return (dafny.TypeDescriptor<Materials>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Materials theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_Encryption(EncryptionMaterials.Default());
  public static Materials Default() {
    return theDefault;
  }
  public static Materials create_Encryption(EncryptionMaterials Encryption) {
    return new Materials_Encryption(Encryption);
  }
  public static Materials create_Decryption(DecryptionMaterials Decryption) {
    return new Materials_Decryption(Decryption);
  }
  public static Materials create_BranchKey(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials BranchKey) {
    return new Materials_BranchKey(BranchKey);
  }
  public static Materials create_BeaconKey(software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials BeaconKey) {
    return new Materials_BeaconKey(BeaconKey);
  }
  public boolean is_Encryption() { return this instanceof Materials_Encryption; }
  public boolean is_Decryption() { return this instanceof Materials_Decryption; }
  public boolean is_BranchKey() { return this instanceof Materials_BranchKey; }
  public boolean is_BeaconKey() { return this instanceof Materials_BeaconKey; }
  public EncryptionMaterials dtor_Encryption() {
    Materials d = this;
    return ((Materials_Encryption)d)._Encryption;
  }
  public DecryptionMaterials dtor_Decryption() {
    Materials d = this;
    return ((Materials_Decryption)d)._Decryption;
  }
  public software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials dtor_BranchKey() {
    Materials d = this;
    return ((Materials_BranchKey)d)._BranchKey;
  }
  public software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials dtor_BeaconKey() {
    Materials d = this;
    return ((Materials_BeaconKey)d)._BeaconKey;
  }
}
