// Class CommitmentPolicy_DBE
// Dafny class CommitmentPolicy_DBE compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CommitmentPolicy_DBE extends CommitmentPolicy {
  public DBECommitmentPolicy _DBE;
  public CommitmentPolicy_DBE (DBECommitmentPolicy DBE) {
    super();
    this._DBE = DBE;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CommitmentPolicy_DBE o = (CommitmentPolicy_DBE)other;
    return true && java.util.Objects.equals(this._DBE, o._DBE);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DBE);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.DBE");
    s.append("(");
    s.append(dafny.Helpers.toString(this._DBE));
    s.append(")");
    return s.toString();
  }
}
