// Class CommitmentPolicy_ESDK
// Dafny class CommitmentPolicy_ESDK compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CommitmentPolicy_ESDK extends CommitmentPolicy {
  public ESDKCommitmentPolicy _ESDK;
  public CommitmentPolicy_ESDK (ESDKCommitmentPolicy ESDK) {
    super();
    this._ESDK = ESDK;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CommitmentPolicy_ESDK o = (CommitmentPolicy_ESDK)other;
    return true && java.util.Objects.equals(this._ESDK, o._ESDK);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ESDK);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.ESDK");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ESDK));
    s.append(")");
    return s.toString();
  }
}
