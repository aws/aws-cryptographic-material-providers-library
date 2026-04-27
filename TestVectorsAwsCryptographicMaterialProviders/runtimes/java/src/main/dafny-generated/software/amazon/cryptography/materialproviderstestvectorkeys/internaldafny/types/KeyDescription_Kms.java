// Class KeyDescription_Kms
// Dafny class KeyDescription_Kms compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_Kms extends KeyDescription {
  public KMSInfo _Kms;
  public KeyDescription_Kms (KMSInfo Kms) {
    super();
    this._Kms = Kms;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_Kms o = (KeyDescription_Kms)other;
    return true && java.util.Objects.equals(this._Kms, o._Kms);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Kms);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Kms");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Kms));
    s.append(")");
    return s.toString();
  }
}
