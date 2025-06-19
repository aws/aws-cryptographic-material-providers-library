// Class Materials_BranchKey
// Dafny class Materials_BranchKey compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Materials_BranchKey extends Materials {
  public software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _BranchKey;
  public Materials_BranchKey (software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials BranchKey) {
    super();
    this._BranchKey = BranchKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Materials_BranchKey o = (Materials_BranchKey)other;
    return true && java.util.Objects.equals(this._BranchKey, o._BranchKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BranchKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.Materials.BranchKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BranchKey));
    s.append(")");
    return s.toString();
  }
}
