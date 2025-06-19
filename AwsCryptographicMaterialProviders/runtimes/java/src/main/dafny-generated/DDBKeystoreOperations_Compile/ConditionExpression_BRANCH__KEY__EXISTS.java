// Class ConditionExpression_BRANCH__KEY__EXISTS
// Dafny class ConditionExpression_BRANCH__KEY__EXISTS compiled into Java
package DDBKeystoreOperations_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConditionExpression_BRANCH__KEY__EXISTS extends ConditionExpression {
  public ConditionExpression_BRANCH__KEY__EXISTS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConditionExpression_BRANCH__KEY__EXISTS o = (ConditionExpression_BRANCH__KEY__EXISTS)other;
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
    s.append("DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_EXISTS");
    return s.toString();
  }
}
