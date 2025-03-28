// Class Error_ComAmazonawsKms
// Dafny class Error_ComAmazonawsKms compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class Error_ComAmazonawsKms extends Error {
  public software.amazon.cryptography.services.kms.internaldafny.types.Error _ComAmazonawsKms;
  public Error_ComAmazonawsKms (software.amazon.cryptography.services.kms.internaldafny.types.Error ComAmazonawsKms) {
    super();
    this._ComAmazonawsKms = ComAmazonawsKms;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Error_ComAmazonawsKms o = (Error_ComAmazonawsKms)other;
    return true && java.util.Objects.equals(this._ComAmazonawsKms, o._ComAmazonawsKms);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 14;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ComAmazonawsKms);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.Error.ComAmazonawsKms");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ComAmazonawsKms));
    s.append(")");
    return s.toString();
  }
}
