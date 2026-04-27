// Class Materials_Decryption
// Dafny class Materials_Decryption compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Materials_Decryption extends Materials {
  public DecryptionMaterials _Decryption;
  public Materials_Decryption (DecryptionMaterials Decryption) {
    super();
    this._Decryption = Decryption;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Materials_Decryption o = (Materials_Decryption)other;
    return true && java.util.Objects.equals(this._Decryption, o._Decryption);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Decryption);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.Materials.Decryption");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Decryption));
    s.append(")");
    return s.toString();
  }
}
