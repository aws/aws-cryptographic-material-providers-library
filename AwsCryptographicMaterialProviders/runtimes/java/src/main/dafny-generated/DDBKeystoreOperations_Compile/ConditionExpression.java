// Class ConditionExpression
// Dafny class ConditionExpression compiled into Java
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
public abstract class ConditionExpression {
  public ConditionExpression() {
  }
  private static final dafny.TypeDescriptor<ConditionExpression> _TYPE = dafny.TypeDescriptor.<ConditionExpression>referenceWithInitializer(ConditionExpression.class, () -> ConditionExpression.Default());
  public static dafny.TypeDescriptor<ConditionExpression> _typeDescriptor() {
    return (dafny.TypeDescriptor<ConditionExpression>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ConditionExpression theDefault = DDBKeystoreOperations_Compile.ConditionExpression.create_BRANCH__KEY__NOT__EXIST();
  public static ConditionExpression Default() {
    return theDefault;
  }
  public static ConditionExpression create_BRANCH__KEY__NOT__EXIST() {
    return new ConditionExpression_BRANCH__KEY__NOT__EXIST();
  }
  public static ConditionExpression create_BRANCH__KEY__EXISTS() {
    return new ConditionExpression_BRANCH__KEY__EXISTS();
  }
  public boolean is_BRANCH__KEY__NOT__EXIST() { return this instanceof ConditionExpression_BRANCH__KEY__NOT__EXIST; }
  public boolean is_BRANCH__KEY__EXISTS() { return this instanceof ConditionExpression_BRANCH__KEY__EXISTS; }
  public static java.util.ArrayList<ConditionExpression> AllSingletonConstructors() {
    java.util.ArrayList<ConditionExpression> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ConditionExpression_BRANCH__KEY__NOT__EXIST());
    singleton_iterator.add(new ConditionExpression_BRANCH__KEY__EXISTS());
    return singleton_iterator;
  }
}
