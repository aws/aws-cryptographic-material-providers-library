// Class KeyMaterial_StaticKeyStoreInformation
// Dafny class KeyMaterial_StaticKeyStoreInformation compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyMaterial_StaticKeyStoreInformation extends KeyMaterial {
  public dafny.DafnySequence<? extends Character> _keyIdentifier;
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKeyVersion;
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _beaconKey;
  public KeyMaterial_StaticKeyStoreInformation (dafny.DafnySequence<? extends Character> keyIdentifier, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersion, dafny.DafnySequence<? extends java.lang.Byte> branchKey, dafny.DafnySequence<? extends java.lang.Byte> beaconKey) {
    super();
    this._keyIdentifier = keyIdentifier;
    this._branchKeyVersion = branchKeyVersion;
    this._branchKey = branchKey;
    this._beaconKey = beaconKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyMaterial_StaticKeyStoreInformation o = (KeyMaterial_StaticKeyStoreInformation)other;
    return true && java.util.Objects.equals(this._keyIdentifier, o._keyIdentifier) && java.util.Objects.equals(this._branchKeyVersion, o._branchKeyVersion) && java.util.Objects.equals(this._branchKey, o._branchKey) && java.util.Objects.equals(this._beaconKey, o._beaconKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyVersion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._beaconKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeyMaterial.KeyMaterial.StaticKeyStoreInformation");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._branchKeyVersion));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._branchKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._beaconKey));
    s.append(")");
    return s.toString();
  }
}
