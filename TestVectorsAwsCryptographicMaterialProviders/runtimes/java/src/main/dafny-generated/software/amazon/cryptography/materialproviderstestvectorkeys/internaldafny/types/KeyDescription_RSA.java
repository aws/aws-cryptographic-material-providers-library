// Class KeyDescription_RSA
// Dafny class KeyDescription_RSA compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_RSA extends KeyDescription {
  public RawRSA _RSA;
  public KeyDescription_RSA (RawRSA RSA) {
    super();
    this._RSA = RSA;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_RSA o = (KeyDescription_RSA)other;
    return true && java.util.Objects.equals(this._RSA, o._RSA);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RSA);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RSA");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RSA));
    s.append(")");
    return s.toString();
  }
}
