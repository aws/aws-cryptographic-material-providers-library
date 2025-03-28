// Class DescribeEndpointsResponse
// Dafny class DescribeEndpointsResponse compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeEndpointsResponse {
  public dafny.DafnySequence<? extends Endpoint> _Endpoints;
  public DescribeEndpointsResponse (dafny.DafnySequence<? extends Endpoint> Endpoints) {
    this._Endpoints = Endpoints;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeEndpointsResponse o = (DescribeEndpointsResponse)other;
    return true && java.util.Objects.equals(this._Endpoints, o._Endpoints);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Endpoints);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeEndpointsResponse.DescribeEndpointsResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Endpoints));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeEndpointsResponse> _TYPE = dafny.TypeDescriptor.<DescribeEndpointsResponse>referenceWithInitializer(DescribeEndpointsResponse.class, () -> DescribeEndpointsResponse.Default());
  public static dafny.TypeDescriptor<DescribeEndpointsResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeEndpointsResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeEndpointsResponse theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeEndpointsResponse.create(dafny.DafnySequence.<Endpoint> empty(Endpoint._typeDescriptor()));
  public static DescribeEndpointsResponse Default() {
    return theDefault;
  }
  public static DescribeEndpointsResponse create(dafny.DafnySequence<? extends Endpoint> Endpoints) {
    return new DescribeEndpointsResponse(Endpoints);
  }
  public static DescribeEndpointsResponse create_DescribeEndpointsResponse(dafny.DafnySequence<? extends Endpoint> Endpoints) {
    return create(Endpoints);
  }
  public boolean is_DescribeEndpointsResponse() { return true; }
  public dafny.DafnySequence<? extends Endpoint> dtor_Endpoints() {
    return this._Endpoints;
  }
}
