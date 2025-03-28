// Class ApproximateCreationDateTimePrecision_MICROSECOND
// Dafny class ApproximateCreationDateTimePrecision_MICROSECOND compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ApproximateCreationDateTimePrecision_MICROSECOND extends ApproximateCreationDateTimePrecision {
  public ApproximateCreationDateTimePrecision_MICROSECOND () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ApproximateCreationDateTimePrecision_MICROSECOND o = (ApproximateCreationDateTimePrecision_MICROSECOND)other;
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
    s.append("ComAmazonawsDynamodbTypes.ApproximateCreationDateTimePrecision.MICROSECOND");
    return s.toString();
  }
}
