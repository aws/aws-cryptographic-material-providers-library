// Class CacheType_No
// Dafny class CacheType_No compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheType_No extends CacheType {
  public NoCache _No;
  public CacheType_No (NoCache No) {
    super();
    this._No = No;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheType_No o = (CacheType_No)other;
    return true && java.util.Objects.equals(this._No, o._No);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._No);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CacheType.No");
    s.append("(");
    s.append(dafny.Helpers.toString(this._No));
    s.append(")");
    return s.toString();
  }
}
