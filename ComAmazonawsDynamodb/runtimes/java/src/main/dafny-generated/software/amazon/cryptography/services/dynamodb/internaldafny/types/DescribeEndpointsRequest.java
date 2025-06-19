// Class DescribeEndpointsRequest
// Dafny class DescribeEndpointsRequest compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeEndpointsRequest {
  public DescribeEndpointsRequest () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeEndpointsRequest o = (DescribeEndpointsRequest)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeEndpointsRequest.DescribeEndpointsRequest");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeEndpointsRequest> _TYPE = dafny.TypeDescriptor.<DescribeEndpointsRequest>referenceWithInitializer(DescribeEndpointsRequest.class, () -> DescribeEndpointsRequest.Default());
  public static dafny.TypeDescriptor<DescribeEndpointsRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeEndpointsRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeEndpointsRequest theDefault = DescribeEndpointsRequest.create();
  public static DescribeEndpointsRequest Default() {
    return theDefault;
  }
  public static DescribeEndpointsRequest create() {
    return new DescribeEndpointsRequest();
  }
  public static DescribeEndpointsRequest create_DescribeEndpointsRequest() {
    return create();
  }
  public boolean is_DescribeEndpointsRequest() { return true; }
  public static java.util.ArrayList<DescribeEndpointsRequest> AllSingletonConstructors() {
    java.util.ArrayList<DescribeEndpointsRequest> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DescribeEndpointsRequest());
    return singleton_iterator;
  }
}
