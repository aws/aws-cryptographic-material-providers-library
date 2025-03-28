// Class ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT
// Dafny class ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT extends ESDKCommitmentPolicy {
  public ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT o = (ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT");
    return s.toString();
  }
}
