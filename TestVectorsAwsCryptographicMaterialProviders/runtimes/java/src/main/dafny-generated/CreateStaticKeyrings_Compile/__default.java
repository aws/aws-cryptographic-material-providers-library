// Class __default
// Dafny class __default compiled into Java
package CreateStaticKeyrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring CreateStaticMaterialsKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials decryptMaterial)
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring keyring = null;
    StaticMaterialsKeyring _nw0 = new StaticMaterialsKeyring();
    _nw0.__ctor(encryptMaterial, decryptMaterial);
    keyring = _nw0;
    return keyring;
  }
  @Override
  public java.lang.String toString() {
    return "CreateStaticKeyrings._default";
  }
}
