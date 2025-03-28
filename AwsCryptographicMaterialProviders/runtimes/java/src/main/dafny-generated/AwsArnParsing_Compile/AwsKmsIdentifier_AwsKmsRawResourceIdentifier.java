// Class AwsKmsIdentifier_AwsKmsRawResourceIdentifier
// Dafny class AwsKmsIdentifier_AwsKmsRawResourceIdentifier compiled into Java
package AwsArnParsing_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsIdentifier_AwsKmsRawResourceIdentifier extends AwsKmsIdentifier {
  public AwsResource _r;
  public AwsKmsIdentifier_AwsKmsRawResourceIdentifier (AwsResource r) {
    super();
    this._r = r;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AwsKmsIdentifier_AwsKmsRawResourceIdentifier o = (AwsKmsIdentifier_AwsKmsRawResourceIdentifier)other;
    return true && java.util.Objects.equals(this._r, o._r);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._r);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsArnParsing.AwsKmsIdentifier.AwsKmsRawResourceIdentifier");
    s.append("(");
    s.append(dafny.Helpers.toString(this._r));
    s.append(")");
    return s.toString();
  }
}
