// Class ApproximateCreationDateTimePrecision_MILLISECOND
// Dafny class ApproximateCreationDateTimePrecision_MILLISECOND compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ApproximateCreationDateTimePrecision_MILLISECOND extends ApproximateCreationDateTimePrecision {
  public ApproximateCreationDateTimePrecision_MILLISECOND () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ApproximateCreationDateTimePrecision_MILLISECOND o = (ApproximateCreationDateTimePrecision_MILLISECOND)other;
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
    s.append("ComAmazonawsDynamodbTypes.ApproximateCreationDateTimePrecision.MILLISECOND");
    return s.toString();
  }
}
