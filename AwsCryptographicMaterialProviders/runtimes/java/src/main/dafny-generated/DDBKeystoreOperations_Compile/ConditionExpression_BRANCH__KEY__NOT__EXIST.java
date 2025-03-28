// Class ConditionExpression_BRANCH__KEY__NOT__EXIST
// Dafny class ConditionExpression_BRANCH__KEY__NOT__EXIST compiled into Java
package DDBKeystoreOperations_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConditionExpression_BRANCH__KEY__NOT__EXIST extends ConditionExpression {
  public ConditionExpression_BRANCH__KEY__NOT__EXIST () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConditionExpression_BRANCH__KEY__NOT__EXIST o = (ConditionExpression_BRANCH__KEY__NOT__EXIST)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_NOT_EXIST");
    return s.toString();
  }
}
