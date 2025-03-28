// Class AwsKmsIdentifier_AwsKmsArnIdentifier
// Dafny class AwsKmsIdentifier_AwsKmsArnIdentifier compiled into Java
package AwsArnParsing_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsIdentifier_AwsKmsArnIdentifier extends AwsKmsIdentifier {
  public AwsArn _a;
  public AwsKmsIdentifier_AwsKmsArnIdentifier (AwsArn a) {
    super();
    this._a = a;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AwsKmsIdentifier_AwsKmsArnIdentifier o = (AwsKmsIdentifier_AwsKmsArnIdentifier)other;
    return true && java.util.Objects.equals(this._a, o._a);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._a);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsArnParsing.AwsKmsIdentifier.AwsKmsArnIdentifier");
    s.append("(");
    s.append(dafny.Helpers.toString(this._a));
    s.append(")");
    return s.toString();
  }
}
