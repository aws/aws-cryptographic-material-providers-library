// Class Materials_BeaconKey
// Dafny class Materials_BeaconKey compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class Materials_BeaconKey extends Materials {
  public software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials _BeaconKey;
  public Materials_BeaconKey (software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials BeaconKey) {
    super();
    this._BeaconKey = BeaconKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Materials_BeaconKey o = (Materials_BeaconKey)other;
    return true && java.util.Objects.equals(this._BeaconKey, o._BeaconKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BeaconKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.Materials.BeaconKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BeaconKey));
    s.append(")");
    return s.toString();
  }
}
