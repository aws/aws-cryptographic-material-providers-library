// Class Materials_Encryption
// Dafny class Materials_Encryption compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class Materials_Encryption extends Materials {
  public EncryptionMaterials _Encryption;
  public Materials_Encryption (EncryptionMaterials Encryption) {
    super();
    this._Encryption = Encryption;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Materials_Encryption o = (Materials_Encryption)other;
    return true && java.util.Objects.equals(this._Encryption, o._Encryption);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Encryption);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.Materials.Encryption");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Encryption));
    s.append(")");
    return s.toString();
  }
}
